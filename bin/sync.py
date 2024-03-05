import sys
import requests
import yaml

with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

server = "https://" + cfg['server']['host'] + "/"
api_key = cfg['server']['api_key']

url = server + "workflows/?tags=splunkaction"

headers = {'X-N8N-API-KEY': api_key}

data = requests.get(url=url, headers=headers)

print(data.json())