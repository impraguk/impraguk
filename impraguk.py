import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
players = {}

@client.event
async def on_ready():
    print ("Skah lat.")
    await client.change_presence(game=discord.Game(name="with Bloodsteel."))
                                
@client.event
async def on_message(message):
    if message.content.startswith("!ug"):
        msg = ("Nub time for blahin {0.author.mention}, get back ta' working.".format(message))
        await client.send_message(message.channel, msg)
        
@client.event
async def on_message(message):
    if message.content.startswith("!stop"):
        try:
            voice_client = client_voice_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "I'm not connected.")
        except Exception as Hugo:
            await client.send_message(message.channel, "Error1_______|type|_______".format(type=Hugo))

    if message.content.startswith("!play"):
        try:
            yt_url = message.content[6:]
            if client.is_voice_connected(message.server):
                try:
                    voice = client.voice_client_in(message.server)
                    players[message.server.id].stop()
                    player = await voice.create_ytdl_player(yt_url, before_options=" -reconnect 1 -reconnect_streamed 1"
                                                                                   " -reconnect_delay_max 5")
                    players[message.server.id] = player
                    player.start()
                except Exception as e:
                    await client.send_message(message.server, "Error2______[Error]".format(error=e))

            if not client.is_voice_connected(message.server):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await client.join_voice_channel(channel)
                    player = await voice.create_ytdl_player(yt_url, before_options=" -reconnect 1 -reconnect_streamed 1"
                                                                                   " -reconnect_delay_max 5")
                    players[message.server.id] = player
                    player.start()
                except Exception as e:       
        

client.run(os.getenv('TOKEN'))
