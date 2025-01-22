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

st.sidebar.title("About")
st.sidebar.info("""
    Medium is an online publishing platform where people (e.g. software developers or product designers) can read and write articles.            
    This website allows you to get information about Medium users, 
    including their follower count and the number of articles in which they are a top writer. 
    You can also view a chart of Tim Denning's followers over time - he is currently one of the most followed authors on Medium.
    (Website best viewed in light mode.)
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/0/0d/Medium_%28website%29_logo.svg", width=200)

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
        image_url = data.get('image_url')
        user_info = {
            'fullname': data.get('fullname'),
            'followers_count': data.get('followers_count'),
            'following_count': data.get('following_count'),
            'top_writer_in': data.get('top_writer_in')
        }
        df = pd.DataFrame(user_info, index=[0])
        st.image(image_url, width=100)
        st.write(df)
    else:
	    st.error('Response not found.')
    
with tab2:
    st.write("A chart of Tim Denning's followers over time:")
    # Query the database for follower data
    query = session.query(followers_table).all()
    dftim = pd.DataFrame(query, columns=[col.name for col in followers_table.columns])
    dftim['timestamp'] = pd.to_datetime(dftim['timestamp'])
    chart = alt.Chart(dftim).mark_line().encode(
        x='timestamp:T',
        y='followers_count:Q'
    ).properties(
        width=600,
        height=400
    )
    st.write(chart)
    st.markdown('---')
    st.write("This is the data used to create the chart:")
    st.write(dftim)

with tab3:
    st.subheader("Get Article Information")
    st.caption("This section displays the top 10 articles of the user chosen in the first tab.")
    url3 = f"https://medium2.p.rapidapi.com/user/{userid}/top_articles"
    response3 = requests.get(url3, headers=headers)
    
    if response3.status_code == 200:
        articles = response3.json()['top_articles']
        article_ids = [value for key, value in articles.items()]
    
        for article_id in article_ids:
            url4 = f"https://medium2.p.rapidapi.com/article/{article_id}"  
            response4 = requests.get(url4, headers=headers)
            article_data = response4.json()
            article_info = {
            'title': article_data.get('title'),
            'subtitle': article_data.get('subtitle'),
            'claps': article_data.get('claps'),
            }
            st.write(article_info)
    else: 
        st.error('Response not found.')
      
    
# Close the session
session.close()