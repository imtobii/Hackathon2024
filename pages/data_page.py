import streamlit as st
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

st.markdown("<h2>Data Analysis Page</h2>", unsafe_allow_html=True)

if "uploaded_file" in st.session_state and st.session_state["uploaded_file"] is not None:
    
    uploaded_file = st.session_state["uploaded_file"]

    # Step 1: Load the data
    data = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded Data:")
    # Resize the table to be compact
    st.dataframe(data.head(10), width=800, height=300)  # Limit rows and adjust dimensions

    # Step 2: Data Cleaning
    # Convert 'Time' column to datetime format
    data['Time'] = pd.to_datetime(data['Time'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
    # Drop rows with missing critical data
    data_cleaned = data.dropna(subset=['Inj Gas Meter Volume Instantaneous', 'Inj Gas Valve Percent Open'])
    # Interpolate missing Setpoint values
    data_cleaned['Inj Gas Meter Volume Setpoint'] = data_cleaned['Inj Gas Meter Volume Setpoint'].interpolate()

    # Step 3: Visualization of All Columns
    st.write("Trend Analysis:")
    # Center the chart in the middle of the app
    with st.container():
        fig, ax = plt.subplots(figsize=(12, 6))  # Adjusted size for compactness
        ax.plot(data_cleaned['Time'], data_cleaned['Inj Gas Meter Volume Instantaneous'], label='Instantaneous Volume', color='green')
        ax.plot(data_cleaned['Time'], data_cleaned['Inj Gas Meter Volume Setpoint'], label='Setpoint Volume', color='red', linestyle='dashed')
        ax.plot(data_cleaned['Time'], data_cleaned['Inj Gas Valve Percent Open'], label='Valve Percent Open (%)', color='blue')

        ax.set_title("Gas Injection Trends")
        ax.set_xlabel("Time")
        ax.set_ylabel("Values")
        ax.legend()
        ax.grid()

        st.pyplot(fig)

    # Step 4: Hydrate Detection Logic
    threshold = -50  # Example threshold for volume drop
    duration = 10    # Number of consecutive points to consider a sustained decline
    data_cleaned['Volume_Change'] = data_cleaned['Inj Gas Meter Volume Instantaneous'].diff()
    hydrate_risk = (data_cleaned['Volume_Change'] < threshold).rolling(window=duration).sum() >= duration

    if hydrate_risk.any():
        st.error("ALERT: Potential hydrate formation detected! Check the system immediately.")
    else:
        st.success("System stable: No hydrate risks detected.")
else:
    st.warning("Please upload a file to proceed.")

col1, col2, col3, col4, col5, col6 = st.columns(6)
