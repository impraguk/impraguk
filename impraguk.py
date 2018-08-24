import discord
import random
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
import asyncio
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print ("Skah lat.")
    await client.change_presence(game=discord.Game(name="with Bloodsteel."))
                                
@client.event
async def on_message(message):
    if message.content.startswith("!ug"):
        msg = ("Nub time for blahin {0.author.mention}, get back ta' working.".format(message))
        await client.send_message(message.channel, msg)
    elif message.content.startswith("!name"):
        lines = open('orknames.txt').read().splitlines()
        orkname = random.choice(lines)
        preMsg = ("{0.author.mention}, lat Raguk name iz: ".format(message))
        msg = (preMsg),(orkname)
        await client.send_message(message.channel, msg)
               
               
client.run(os.getenv('TOKEN'))
