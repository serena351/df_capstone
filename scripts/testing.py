import requests

url = "https://medium2.p.rapidapi.com/user/id_for/timdenning"

headers = {
	"x-rapidapi-key": "043c43e953msh1eb760651409ee1p1d655fjsn4067b6421bd8",
	"x-rapidapi-host": "medium2.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())