# IrishScottishShipMap
A most simple ship plotting app

# AISHub Web Application

This is a Dockerized web application that displays AIS (Automatic Identification System) data for ship tracking. It retrieves ship data from AISHub and visualizes it on a map.

## Prerequisites

Before you can run this application, ensure you have the following installed on your system:

- [Docker](https://www.docker.com/products/docker-desktop)

## Getting Started

Follow these steps to run the AISHub web application:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ais-hub-web-app.git
   cd ais-hub-web-app
   ```

   Replace `yourusername` and `ais-hub-web-app` with your actual repository information.

2. **Environment Configuration**

   Create a `.env` file in the project directory with your AISHub credentials and geographical coordinates:

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
   docker-compose up --build
   ```

4. **Access the Web Application**

   Once the container is running, you can access the web application in your browser:

   - Open your web browser.
   - Visit `http://localhost:8034` to view the AISHub web application.

5. **Using the Application**

   - The application provides a map displaying the tracked ships within the specified geographical area.
   - You can interact with the map and view ship details by clicking on ship icons.

6. **Stopping the Application**

   To stop the application and the Docker container, press `Ctrl+C` in the terminal where the container is running.

7. **Cleanup**

   If you wish to remove the Docker container and associated resources, run the following command in the project directory:

   ```bash
   docker-compose down
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This application is powered by AISHub (https://www.aishub.net/).

