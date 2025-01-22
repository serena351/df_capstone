import requests
from dotenv import load_dotenv
import os

#load_dotenv()
#API_KEY = os.getenv("API_KEY")

username = "timdenning"
url = f"https://medium2.p.rapidapi.com/user/id_for/{username}"
headers = {
	"x-rapidapi-key": "043c43e953msh1eb760651409ee1p1d655fjsn4067b6421bd8",
	"x-rapidapi-host": "medium2.p.rapidapi.com"
}
response = requests.get(url, headers=headers)
print(response.json())
print(response.status_code)
# if response.status_code == 200:
#     print(response.json())
# else:
# 	print('Response not found.')