import json
import requests
import bz2
import gzip
import os
import time

from flask import Flask, jsonify, Response, send_from_directory
from flask_cors import cross_origin
from flask_caching import Cache

app = Flask(__name__, static_url_path='')
cache = Cache(app, config={'CACHE_TYPE': 'simple', 'CACHE_DEFAULT_TIMEOUT': 120})

BASE_URL = 'https://data.aishub.net/ws.php'
FORMAT = 1
OUTPUT = 'json'
COMPRESS = 3

USERNAME = os.environ.get('AISHUB_USERNAME')

LAT_MIN = float(os.environ.get('LAT_MIN'))
LAT_MAX = float(os.environ.get('LAT_MAX'))
LON_MIN = float(os.environ.get('LON_MIN'))
LON_MAX = float(os.environ.get('LON_MAX'))

url = f'{BASE_URL}?username={USERNAME}&format={FORMAT}&output={OUTPUT}&compress={COMPRESS}&latmin={LAT_MIN}&latmax={LAT_MAX}&lonmin={LON_MIN}&lonmax={LON_MAX}'  

last_refresh_time = 0  # Initialize the last refresh time

@app.before_request
def check_cache_refresh():
    global last_refresh_time

    # Check if it's time to refresh the cache (1 minute has passed)
    current_time = time.time()
    if current_time - last_refresh_time > 60:
        cache.clear()  # Clear the cache
        last_refresh_time = current_time  # Update the last refresh time

@app.route('/api/shipmini')
@cross_origin()
@cache.cached()
def get_ships_geomini():
    response = requests.get(url)
    decompressed_data = bz2.decompress(response.content)
    data = json.loads(decompressed_data)

    # Check if data contains at least two elements
    if len(data) < 2:
        return jsonify({'error': 'Data format error'}), 500

    # Create a GeoJSON feature for each ship record
    features = []

    for row in data[1]:
        if 'LATITUDE' in row and 'LONGITUDE' in row and row['LATITUDE'] and row['LONGITUDE']:
            properties = [
                row['MMSI'],
                row['TIME'],
                row['COG'],
                row['SOG'],
                row['HEADING'],
                row['NAVSTAT'],
                row['IMO'],
                row['NAME'],
                row['CALLSIGN'],
                row['TYPE']
            ]

            coordinates = [float(row['LONGITUDE']), float(row['LATITUDE'])]

            features.append({
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': coordinates
                },
                'properties': properties
            })

    json_data = json.dumps(features)
    compressed_data = gzip.compress(json_data.encode('utf-8'))

    response = Response(compressed_data, content_type='application/json')
    response.headers['Content-Encoding'] = 'gzip'

    return response

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run()
