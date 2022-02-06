import requests

params = {
    'collection': 'hausphases',
    'limit': 1
}

r = requests.get("https://testnets-api.opensea.io/api/v1/assets", params=params)

print(r.json())
