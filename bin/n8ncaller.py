import sys 
import requests
import yaml
import json

payload = sys.stdin.readlines()

with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

server = "https://" + cfg['server']['host'] + "/"

data = json.load(payload)
webhook_id = data['param']['webhook_id']

url = server + webhook_id

requests.post(url=url,json=payload)