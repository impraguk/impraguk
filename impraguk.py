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
    await client.change_presence(game=discord.Game(name="with Bloodsteel."))
                                
@client.event
async def on_message(message):
    if message.content.startswith("!ug"):
        msg = ("Nub time for blahin {0.author.mention}, get back ta' working.".format(message))
        await client.send_message(message.channel, msg)
        
@client.command(pass_context=True)
async def yt(ctx, url):

    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)

    player = await vc.create_ytdl_player(url)
    player.start()        
        

client.run(os.getenv('TOKEN'))
