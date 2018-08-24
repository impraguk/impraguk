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
        msg = (":speech_balloon:**Nub time for blahin {0.author.mention}, get back ta' working.**".format(message))
        await client.send_message(message.channel, msg)
        
    elif message.content.startswith("!orkname"):
        lines = open('orknames.txt').read().splitlines()
        orkname = random.choice(lines)
        msg = (":speech_balloon:{0.author.mention}**, lat Raguk name iz:** ".format(message) + orkname)
        await client.send_message(message.channel, msg)
        
    elif message.content.startswith("!ologname"):
        lines = open('consonants.txt').read().splitlines()
        a = random.choice(lines)
        lines = open('vowels.txt').read().splitlines()
        b = random.choice(lines)
        lines = open('consonants2.txt').read().splitlines()
        c = random.choice(lines)
        ologname = a + b + c
        msg = (":speech_balloon:{0.author.mention}**, lat Raguk name iz:** ".format(message) + ologname)
        await client.send_message(message.channel, msg)
        
    elif message.content.startswith("!help"):
        embed = discord.Embed(title="Elder Imp'Raguk", description="A notable lore character.", color=0xcc0909)
    
        embed.add_field(name = "!ug", value = "Say Hello to Imp'Raguk.", inline=False)
        embed.add_field(name = "!orkname", value = "Generate an orkish name fit for a Raguk.", inline=False)
        embed.add_field(name = "!ologname", value = "Generate an olog name fit for a Raguk.", inline=False)
    
        await client.send_message(message.channel, embed=embed)
                          
client.run(os.getenv('TOKEN'))
