import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
from discord.voice_Client import VoiceClient

startup_extensions = ["Music"]
Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print ("Skah lat.")
    await client.change_presence(game=discord.Game(name="with Bloodsteel."))
    
Class Main_Command():
        def __init__(self,bot)
        self.bot = bot
                                 
@client.event
async def on_message(message):
    if message.content.startswith("!ug"):
        msg = ("Nub time for blahin {0.author.mention}, get back ta' working.".format(message))
        await client.send_message(message.channel, msg)
        
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = ("(): ()".format(type(e).__name__, e))
            print ("Failed to load extension ()\n()".format(extension, exc))       
        
client.run(os.getenv('TOKEN'))
