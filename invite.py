import requests
import yaml
import json
from oauth import Oauth

guild_id = ""

with open("database.json",'r+') as file:
        file_data = json.load(file)

with open('config.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

for user in file_data.get("users"):
    access_token = user.get("access_token")
    url = "{}/guilds/{}/members/{}".format(Oauth.discord_api_url, guild_id, user.get("id"))

    headers = {
        'Authorization' : 'Bot {}'.format(config['token']),
        'Content-Type': 'application/json'
    }

    data = {
        'access_token': access_token
    }

    response = requests.put(url=url, json=data, headers=headers)
    print("{} ({}) - {}".format(user.get('name'), user.get('id'), response.status_code))
