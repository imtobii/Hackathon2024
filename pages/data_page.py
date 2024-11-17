import streamlit as st
import pandas as pd
from io import StringIO

st.markdown("<h2>Data Analysis Page</h2>", unsafe_allow_html=True)

if "uploaded_file" in st.session_state and st.session_state["uploaded_file"] is not None:
    try:
        # Retrieve the uploaded file from session state
        uploaded_file = st.session_state["uploaded_file"]

        # Convert the file to a DataFrame
        string_data = StringIO(uploaded_file.getvalue().decode("utf-8"))
        chart_data = pd.read_csv(string_data)

        # Ensure the required columns exist
        required_columns = ['Time', 'Inj Gas Valve Percent Open', 'Inj Gas Meter Volume Instantaneous', 'Inj Gas Meter Volume Setpoint']
        if not all(column in chart_data.columns for column in required_columns):
            st.error("Uploaded file does not contain the required columns.")
        else:
            # Display the line chart
            st.line_chart(chart_data, x='Time', y=[
                'Inj Gas Valve Percent Open',
                'Inj Gas Meter Volume Instantaneous',
                'Inj Gas Meter Volume Setpoint'
                ],
            color=["#43a700", "#a70000", "#04f"]
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.warning("No file uploaded. Please upload a file on the main page.")
