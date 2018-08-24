import discord
import random
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
import asyncio
import os


Client = discord.Client()
client = commands.Bot(command_prefix = "!")

consonants = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','Z','W','Y']
a = random.randint(0,21)
vowels = ['A','E','I','O','U']
b = random.randint(0,5)

@client.event
async def on_ready():
    print ("Skah lat.")
    await client.change_presence(game=discord.Game(name="with Bloodsteel."))
                                
@client.event
async def on_message(message):
    if message.content.startswith("!ug"):
        msg = ("Nub time for blahin {0.author.mention}, get back ta' working.".format(message))
        await client.send_message(message.channel, msg)
    elif message.content.startswith("!orkname"):
        lines = open('orknames.txt').read().splitlines()
        orkname = random.choice(lines)
        msg = (":speech_balloon:{0.author.mention}**, lat Raguk name iz:** ".format(message) + orkname)
        await client.send_message(message.channel, msg)
     elif message.content.startswith("!ologname"):
        ologname = consonants[a] + vowels[b] + consonants[a].lower
        msg = (":speech_balloon:{0.author.mention}**, lat Raguk name iz:** ".format(message) + ologname)
        await client.send_message(message.channel, msg)
                       
client.run(os.getenv('TOKEN'))
