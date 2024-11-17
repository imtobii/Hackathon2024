import streamlit as st
import pandas as pd
from io import StringIO


st.markdown("<h1 style='text-align: center; color: Black; margin-top: 100px; font-family:Arial, Times, serif;'>EOG HYDRATE ALERT</h1>", unsafe_allow_html=True)



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Save the uploaded file in session state
    st.session_state["uploaded_file"] = uploaded_file
    st.success("File uploaded successfully! Navigate to the Data Analysis Page to visualize the data.")
else:
    st.warning("Please upload a file to proceed.")
    
with st.container():
    st.image("background.jpg")

col1, col2, col3, col4,col5,col6 = st.columns(6)


   

with col6:
    

    st.page_link("pages\data_page.py", label="Analyze")

