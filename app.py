import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import altair as alt

st.title("Medium Followers")

tab1, tab2 = st.tabs(["User Info", "Tim Dennings Followers"])

with tab1:
    st.write("Input a Medium username in lowercase with no spaces to get the user's information.")
    
with tab2:
    st.write("A chart of Tim Dennings followers over time.")

# user_input = st.text_input("Enter a username: ", "AAPL")

# response = requests.get(f"https://randomapi.co/api/{user_input.lower()}")
# if response.status_code == 200:
#     image_url = response.json()['sprites']['front_default']
#     st.image(image_url, width=200) #, use_container_width=True
# else:
#     st.error('Response not found.')