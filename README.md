# IrishScottishShipMap

This is a Dockerized web application that displays AIS (Automatic Identification System) data for ship tracking. It retrieves ship data from AISHub and visualizes it on a map.

## Prerequisites

Before you can run this application, ensure you have the following installed on your system:

- [Docker](https://www.docker.com/products/docker-desktop)

## Getting Started

Follow these steps to run the AISHub web application:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/NgTrThanh/IrishScottishShipMap.git
   cd IrishScottishShipMap
   ```


2. **Environment Configuration**

   Update environment section of the docker-compose.yml file in the project directory with your AISHub credentials and geographical coordinates:

   ```ini
   AISHUB_USERNAME=Your_AISHub_Username
   LAT_MIN=51
   LAT_MAX=58
   LON_MIN=-10
   LON_MAX=-2
   ```

   Replace `Your_AISHub_Username` with your AISHub username, and adjust the geographical coordinates as needed.

3. **Build and Run the Docker Container**

   Build the Docker container and start the application:

   ```bash
   docker compose up --build -d
   ```

4. **Access the Web Application**

   Once the container is running, you can access the web application in your browser:

   - Open your web browser.
   - Visit `http://localhost:8034` to view the web application.

5. **Using the Application**

   - The application provides a map displaying the tracked ships within the specified geographical area.
   - You can interact with the map and view ship details by clicking on ship icons.

6. **Stopping the Application**

   To stop the application and the Docker container,

   ```bash
   docker compose stop
   ```

8. **Cleanup**

   If you wish to remove the Docker container and associated resources, run the following command in the project directory:

   ```bash
   docker compose down
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This application is powered by [AISHub](https://www.aishub.net/) and makes use of the following open-source libraries and resources:

- [jQuery](https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.3/jquery.min.js)
- [Leaflet](https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.3/leaflet.js)
- [Leaflet Providers](https://cdnjs.cloudflare.com/ajax/libs/leaflet-providers/1.13.0/leaflet-providers.js)
- [Leaflet MarkerCluster](https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/leaflet.markercluster-src.min.js)

### Map Tile Providers:

- "Toner Lite" by Stamen.TonerLite
- "Watercolor" by Stamen.Watercolor
- "Terrain" by Stamen.Terrain
- "MapTiler Street" by MapTiler.Streets
- "Jawg Terrain" by Jawg.Terrain

We extend our appreciation to the creators and maintainers of these resources for their contributions to our web application.

