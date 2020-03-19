import requests
import json

url="https://corona.lmao.ninja/countries/India"
r = requests.get(url)
countries_data=r.json()
with open('countries_data.txt', 'w') as json_file:
  json.dump(countries_data, json_file)
