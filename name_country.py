import requests
import json

url = "https://api.nationalize.io/"
with open('names.txt') as source:
	names = source.readlines()
for name in names:
	name = name.replace("\n", "")
	params = {'name[]':name}
	response = requests.get(url, params)
	binary = response.content
	output = json.loads(binary)
	print(output[0]["name"], "=>", output[0]["country"][0]["country_id"])
