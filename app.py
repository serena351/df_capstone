import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import altair as alt
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

st.title("Medium Followers")

tab1, tab2 = st.tabs(["User Info", "Tim Denning Followers"])

with tab1:
    st.write("Input a Medium username in lowercase with no spaces to get the user's information.")
    username = str(st.text_input("Enter a username: ", "timdenning"))
    url = f"https://medium2.p.rapidapi.com/user/id_for/{username}"
    headers = {
	    "x-rapidapi-key": API_KEY,
	    "x-rapidapi-host": "medium2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
	    userid = response.json()['id']
	    st.write(userid)
    else:
	    st.error('Response not found.')
    
with tab2:
    st.write("A chart of Tim Dennings followers over time.")
