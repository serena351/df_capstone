import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import altair as alt
from dotenv import load_dotenv
import os

load_dotenv()

st.title("Medium Followers")

tab1, tab2 = st.tabs(["User Info", "Tim Dennings Followers"])

with tab1:
    st.write("Input a Medium username in lowercase with no spaces to get the user's information.")
    username = st.text_input("Enter a username: ", "timdennings")
    url = f"https://medium2.p.rapidapi.com/user/id_for/{username}"
    API_KEY = os.getenv("API_KEY")
    headers = {
	    "x-rapidapi-key": API_KEY,
	    "x-rapidapi-host": "medium2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        userid = response.json()
    else:
        st.error('Response not found.')
    
with tab2:
    st.write("A chart of Tim Dennings followers over time.")