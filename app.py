import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import altair as alt

st.title("App")

user_input = st.text_input("Enter: ", "AAPL")

response = requests.get(f"https://randomapi.co/api/{user_input.lower()}")
if response.status_code == 200:
    image_url = response.json()['sprites']['front_default']
    st.image(image_url, width=200) #, use_container_width=True
else:
    st.error('Response not found.')