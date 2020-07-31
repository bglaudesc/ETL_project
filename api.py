import requests

url = "https://crimescore.p.rapidapi.com/crimescore"

querystring = {"f":"json","id":"174","lon":"29.7604","lat":"95.3698"}

headers = {
    'x-rapidapi-host': "crimescore.p.rapidapi.com",
    'x-rapidapi-key': "bbfe6dd4b3msh65ebb992ab302b0p19fb10jsn7ed161c6b16e"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)