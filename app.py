import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
import matplotlib.pyplot as plt
import requests
import altair as alt
import os

# Create an engine and metadata
DATABASE_URL = st.secrets["DATABASE_URL"]
engine = create_engine(DATABASE_URL)
metadata = MetaData(schema='student')

# Reflect the existing table
followers_table = Table('serena_capstone', metadata, autoload_with=engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

st.title("Medium Followers")

tab1, tab2, tab3 = st.tabs(["User Info", "Tim Denning Followers", "Article Info"])

with tab1:
    st.subheader("Get User Information")
    st.write("Type in a Medium username (lowercase, no spaces) to get the user's information.")
    username = str(st.text_input("Enter a username: ", "timdenning"))
    url = f"https://medium2.p.rapidapi.com/user/id_for/{username}"
    headers = {
	    "x-rapidapi-key": st.secrets["API_KEY"],
	    "x-rapidapi-host": "medium2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        userid = response.json()['id']
        url2 = f"https://medium2.p.rapidapi.com/user/{userid}"
        response2 = requests.get(url2, headers=headers)
        data = response2.json()
        df = pd.DataFrame(data, index=[0])
        st.write(df)
    else:
	    st.error('Response not found.')
    
with tab2:
    st.write("A chart of Tim Denning's followers over time:")
    # Query the database for follower data
    query = session.query(followers_table).all()
    dftim = pd.DataFrame(query, columns=[col.name for col in followers_table.columns])
    st.write(dftim)

with tab3:
    st.subheader("Get Article Information")
    
# Close the session
session.close()