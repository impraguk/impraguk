import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print ("Skah lat.")
    await client.change_presence(game=discord.Game(name="Imp'Raguk"))
                                 
@client.event
async def on_message(message):
    if message.content.startswith("!ug"):
        msg = 'Nub time for blahin {0.author.mention}, get back ta' working'.format(message)
        await client.send_message(message.channel, msg)
        
client.run(os.getenv('TOKEN'))
