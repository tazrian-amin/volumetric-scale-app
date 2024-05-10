import streamlit as st
import time
import numpy as np
import pandas as pd

# Sidebar for user inputs
st.sidebar.header("Configuration")
belt_width = st.sidebar.number_input('Belt Width (m)', min_value=0.0, value=1.0)
velocity = st.sidebar.number_input('Velocity (m/s)', min_value=0.0, value=1.0)
sensor_speed = st.sidebar.number_input('Sensor Speed (fps)', min_value=0, value=100, step=1)
sensor_height = st.sidebar.number_input('Sensor Height (m)', min_value=0.0, value=1.0)
sensor_cnt = st.sidebar.number_input('Number of Sensors', min_value=0, value=100, step=1)

st.title("Volumetric Scale")

# Columns to make charts responsive and more distinct
col1, spacer, col2 = st.columns([5, 1, 5])  # Adjust the middle column width for spacing

with col1:
    st.subheader("Cumulative Rock Volume Over Time")
    volume_chart = st.empty()

    # Placeholder for latest volume display
    latest_volume_text = st.empty()
with col2:
    st.subheader("Average Rock Height Over Time")
    height_chart = st.empty()

# Button to start calculation
if st.button('Start Calculation'):
    # Setup initial parameters
    prev_heights = np.zeros(sensor_cnt)
    dx = belt_width / sensor_cnt
    dy = velocity / sensor_speed
    volume = 0
    volumes = []
    heights_data = []

    # Simulate sensor data generation
    while True:
        time.sleep(1)  # slow down the loop for visibility
        heights = sensor_height - np.random.rand(sensor_cnt)
        heights_data.append(heights.mean())  # Store mean height for visualization

        for i in range(sensor_cnt - 1):
            new_volume = dx * dy * (heights[i] + heights[i+1] + prev_heights[i] + prev_heights[i+1]) / 4
            volume += new_volume
        volumes.append(volume)
        prev_heights = heights

        # Update the DataFrames and charts
        volume_df = pd.DataFrame(volumes, columns=['Volume'])
        heights_df = pd.DataFrame(heights_data, columns=['Average Height'])
        volume_chart.line_chart(volume_df)
        height_chart.line_chart(heights_df)

        # Update the text element with the latest volume
        latest_volume_text.metric(label="Total Volume (m³)", value=volume)
