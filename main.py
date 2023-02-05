from flask import Flask, request, redirect
from oauth import Oauth
import discord
from discord.ext import commands, tasks
import yaml
import time
import json
import requests
from threading import Thread
import os

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

class Url(discord.ui.View):
    def __init__(self, url:str, label:str):
        super().__init__()
        self.add_item(discord.ui.Button(label=label, url=url))

@bot.command()
async def button(ctx, title: str, discription: str, label: str, url: str):
    embed=discord.Embed(title=title, url=url, description=discription)
    
    await ctx.send(
        embed=embed,
        view=Url(url=url,label=label)
    )

app = Flask(__name__)

@app.route("/", methods=["get"])
def index():
    return "My name is Patrick Bateman. I`m 27 years old. I believe in taking care of myself, and a balanced diet and a rigorous exercise routine. In the morning, if my face is a little puffy, I`ll put on an ice pack while doing my stomach crunches. I can do a thousand now. After I remove the ice pack I use a deep pore cleanser lotion. In the shower I use a water activated gel cleanser, then a honey almond body scrub, and on the face an exfoliating gel scrub. Then I apply an herb-mint facial masque which I leave on for 10 minutes while I prepare the rest of my routine. I always use an after shave lotion with little or no alcohol, because alcohol dries your face out and makes you look older. Then moisturizer, then an anti-aging eye balm followed by a final moisturizing protective lotion. There is an idea of a Patrick Bateman. Some kind of abstraction. But there is no real me. Only an entity. Something illusory. And though I can hide my cold gaze, and you can shake my hand and feel flesh gripping yours, and maybe you can even sense our lifestyles are probably comparable, I simply am not there."

queue = []

@app.route("/login", methods=["get"])
def login():
    access_token = Oauth.getAccessToken(request.args.get("code"))
    user_json = Oauth.getUser(access_token=access_token)

    id = user_json.get('id')
    name = "{}#{}".format(user_json['username'], user_json['discriminator'])
    avatar = user_json['avatar']
    ip = ""
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    time_stamp = time.time()

    with open('config.yml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        if (config['anti_vpn'] == True):
            api_res = requests.get(f"http://check.getipintel.net/check.php?ip={ip}&contact={config['email']}")
            if (api_res.status_code != 429):
                if (api_res.text == "1"):
                    return redirect('/failure')
            else:
                return redirect('/wait')
    
    bot.loop.create_task(add_role(id))

    data = {
        "id": id,
        "name": name,
        "avatar": avatar,
        "access_token": access_token,
        "ip_address": ip,
        "time_stamp": time_stamp
    }

    with open("database.json",'r+') as file:
        file_data = json.load(file)
        file_data['users'].append(data)
        file.seek(0)
        json.dump(file_data, file, indent = 2)

    return redirect('/success')

async def add_role(member_id):
    guild = bot.get_guild(config['guild_id'])
    member = guild.get_member(int(member_id))
    role = guild.get_role(config['role_id'])
    await member.add_roles(role)

@app.route("/success")
def success():
    return "Login is Success. Thanks."

@app.route("/failure")
def failure():
    return "Login is Failure. Please retry."

@app.route("/wait")
def wait():
    return "Try again in a little while."


def run():
    app.run()

thread = Thread(target=run)
thread.start()

with open('config.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

if config['token'] == None:
  config['token'] = os.environ('token')
    
bot.run(token=config['token'])
