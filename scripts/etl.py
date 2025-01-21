import requests
import json
from sqlalchemy import create_engine, Table, Column, String, Integer, MetaData
from sqlalchemy.orm import sessionmaker
import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Extract data from the API
url = "https://medium2.p.rapidapi.com/user/b6d641be1066"

API_KEY = os.getenv("API_KEY")
headers = {
	"x-rapidapi-key": API_KEY,
	"x-rapidapi-host": "medium2.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

# Transform the data
transformed_data = {
    "user_id": data.get("id"),
    "username": data.get("username"),
    "followers_count": data.get("followers_count")
}

# Load the data into PostgreSQL using SQLAlchemy
DATABASE_URL = os.getenv("DATABASE_URL")

# Create an engine and metadata
engine = create_engine(DATABASE_URL)
metadata = MetaData(schema='student')

# Define the users table
followers_table = Table(
    'serena_capstone', metadata,
    Column('timestamp', String, primary_key=True),
    Column('user_id', String),
    Column('username', String),
    Column('followers_count', Integer)
)

# Create the table if it doesn't already exist
metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into the table
insert_query = followers_table.insert().values(
    timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    user_id=transformed_data["user_id"],
    username=transformed_data["username"],
    followers_count=transformed_data["followers_count"]
)

# Execute the insert query
session.execute(insert_query)
session.commit()

# Close the session
session.close()

print("Data inserted successfully and table created in schema 'student'.")