# Volumetric Scale Application

This Streamlit application is designed to simulate and visualize the volumetric calculation of materials on a conveyor belt using multiple sensors. It calculates the cumulative volume of rock (or similar materials) over time and displays the average height of rock across the belt.

## Features

- **User Configurable Settings:** Configure belt width, velocity, sensor speed, sensor height, and the number of sensors through an interactive sidebar.
- **Real-time Visualization:** View cumulative rock volume and average rock height over time through responsive charts.
- **Dynamic Simulation:** The application simulates sensor data to demonstrate how the system responds to real-world operating conditions.

## How It Works

The application uses a simple model to simulate the passage of rocks under a series of sensors:
1. **Sensor Data Generation:** Random heights are generated (which can be replaced by real sensor data) to simulate the variation in rock height as they pass under the sensors.
2. **Volume Calculation:** The volume between successive sensor readings is calculated using the trapezoidal rule, and cumulative volume is updated and displayed in real-time.
3. **Visualization:** Real-time updates of cumulative volume and average rock height are displayed through interactive charts.

## Requirements

To run this application, you will need the following:
- Python 3.x
- Streamlit
- NumPy
- pandas

## Installation

1. Clone this repository: git clone <repository-url>
2. Install the required packages: pip install streamlit numpy pandas
3. Run the application: streamlit run home.py


## Usage

After starting the application, use the sidebar to adjust the configuration settings according to your needs:
- **Belt Width (m):** Width of the conveyor belt.
- **Velocity (m/s):** Speed at which the belt moves.
- **Sensor Speed (fps):** Frequency at which sensors record data.
- **Sensor Height (m):** Height of sensors from the belt.
- **Number of Sensors:** Total sensors used to measure the rock volume.

Press the 'Start Calculation' button to begin the simulation. You can view the cumulative volume and average height data on the respective charts.

## Contributing

Contributions are welcome! Please feel free to submit pull requests, suggest features, or report bugs.

