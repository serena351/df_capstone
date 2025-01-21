import requests
import json
from sqlalchemy import create_engine, Table, Column, String, Integer, MetaData
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Extract data from the API

url = "https://medium2.p.rapidapi.com/user/id_for/craftingcode"

headers = {
	"x-rapidapi-key": "043c43e953msh1eb760651409ee1p1d655fjsn4067b6421bd8",
	"x-rapidapi-host": "medium2.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

# Transform the data
transformed_data = {
    "user_id": data.get("id"),
    "username": data.get("username"),
    "followers_count": data.get("followersCount")
}

# Load the data into PostgreSQL using SQLAlchemy
DATABASE_URL = os.getenv("DATABASE_URL")

# Create an engine and metadata
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Define the users table
users_table = Table(
    'users', metadata,
    Column('user_id', String, primary_key=True),
    Column('username', String),
    Column('followers_count', Integer)
)

# Create the table if it doesn't exist
metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into the table
insert_query = users_table.insert().values(
    user_id=transformed_data["user_id"],
    username=transformed_data["username"],
    followers_count=transformed_data["followers_count"]
)

# Execute the insert query
session.execute(insert_query)
session.commit()

# Close the session
session.close()