import requests
import yaml

class Oauth(object):
    with open('config.yml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    client_id = config['client_id']
    client_secret = config['client_secret']
    redirect_uri = config['redirect_uri']
    scope = config['scope']
    discord_login_url = 'https://discord.com/api/oauth2/authorize?client_id={}&redirect_uri={}&response_type=code&scope={}'.format(client_id, redirect_uri, scope)
    discord_token_url = 'https://discord.com/api/oauth2/token'
    discord_api_url = 'https://discord.com/api'

    @staticmethod
    def getAccessToken(code):
        payload = {
            'client_id': Oauth.client_id,
            'client_secret': Oauth.client_secret,
            'grant_type': "authorization_code",
            'redirect_uri': Oauth.redirect_uri,
            "code": code,
            'scope': Oauth.scope
        }
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        access_token = requests.post(
            url=Oauth.discord_token_url, data=payload, headers=headers
            )
        json = access_token.json()
        return json.get("access_token")

    @staticmethod
    def getUser(access_token):
        url = Oauth.discord_api_url+'/users/@me'

        headres = {
            "Authorization": "Bearer {}".format(access_token)
        }

        return requests.get(url=url, headers=headres).json()
        