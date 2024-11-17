# import streamlit as st
# import pandas as pd
# from io import StringIO


# st.markdown("<h1 style='text-align: center; color: Black; margin-top: 100px; font-family:Arial, Times, serif;'>EOG HYDRATE ALERT</h1>", unsafe_allow_html=True)



# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     # Save the uploaded file in session state
#     st.session_state["uploaded_file"] = uploaded_file
#     st.success("File uploaded successfully! Navigate to the Data Analysis Page to visualize the data.")
# else:
#     st.warning("Please upload a file to proceed.")
    
# with st.container():
#     st.image("background.jpg")

# col1, col2, col3, col4,col5,col6 = st.columns(6)


   

# with col6:
    

#     st.page_link("pages\data_page.py", label="Analyze")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App title and header
background_image = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://cdn.discordapp.com/attachments/1307572297506361364/1307654666158477452/d80ab04d9fba5fc9d212276f112e04938c39444d7aab11468daab127.png?ex=673b17cf&is=6739c64f&hm=0b9024ff5a9c0a9e5791cef02c0f8278cfc7a1dfde938e0b9f4bebccf6c90e46&");
    background-size: 100vw 100vh;  
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html= True)
st.markdown(
    "<h1 style='text-align: center; color: Black; margin-top: 100px; font-family:Arial, Times, serif;'>EOG HYDRATE ALERT</h1>",
    unsafe_allow_html=True,
)

# File upload
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Save the uploaded file in session state
    st.session_state["uploaded_file"] = uploaded_file
    st.success("File uploaded successfully! Navigate to the Data Analysis Page to visualize the data.")

    # Step 1: Load the data
    data = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded Data:")
    st.dataframe(data.head())

    # Step 2: Data Cleaning
    # Convert 'Time' column to datetime format
    data['Time'] = pd.to_datetime(data['Time'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
    # Drop rows with missing critical data
    data_cleaned = data.dropna(subset=['Inj Gas Meter Volume Instantaneous', 'Inj Gas Valve Percent Open'])
    # Interpolate missing Setpoint values
    data_cleaned['Inj Gas Meter Volume Setpoint'] = data_cleaned['Inj Gas Meter Volume Setpoint'].interpolate()

    # Step 3: Visualization of All Columns
    st.write("Trend Analysis:")
    fig, ax = plt.subplots(figsize=(14, 8))

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
    

# Navigation links


col1, col2, col3, col4, col5, col6 = st.columns(6)
with col6:

    st.page_link("pages\data_page.py", label="Analyze")
