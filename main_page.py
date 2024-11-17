import streamlit as st
import pandas as pd
from io import StringIO

background_image = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://cdn.discordapp.com/attachments/1307572297506361364/1307654666158477452/d80ab04d9fba5fc9d212276f112e04938c39444d7aab11468daab127.png?ex=673b17cf&is=6739c64f&hm=0b9024ff5a9c0a9e5791cef02c0f8278cfc7a1dfde938e0b9f4bebccf6c90e46&");
    background-size: 100vw 120vh;  
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html= True)

st.markdown("<h1 style='text-align: center; color: Black; margin-top: 100px; font-family:Arial, Times, serif;'>EOG HYDRATE ALERT</h1>", unsafe_allow_html=True)



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Save the uploaded file in session state
    st.session_state["uploaded_file"] = uploaded_file
    st.success("File uploaded successfully! Navigate to the Data Analysis Page to visualize the data.")
else:
    st.warning("Please upload a file to proceed.")
    
# with st.container():
#     st.image("background.jpg")

col1, col2, col3, col4,col5,col6 = st.columns(6)

with col6:
    st.page_link("pages\data_page.py", label="Analyze")
