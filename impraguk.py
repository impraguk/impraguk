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
    if message.content.lower().startswith("!ug"):
        msg = (":speech_balloon:**Nub time for blahin {0.author.mention}, get back ta' working.**".format(message))
        await client.send_message(message.channel, msg)
        
    elif message.content.lower().startswith("!orkname"):
        lines = open('orknames.txt').read().splitlines()
        orkname = random.choice(lines)
        msg = (":speech_balloon:{0.author.mention}**, lat Raguk name iz:** ".format(message) + orkname)
        await client.send_message(message.channel, msg)
        
    elif message.content.lower().startswith("!goboname"):
        lines = open('gobonames.txt').read().splitlines()
        goboname = random.choice(lines)
        msg = (":speech_balloon:{0.author.mention}**, lat Raguk name iz:** ".format(message) + goboname)
        await client.send_message(message.channel, msg)
        
    elif message.content.lower().startswith("!ologname"):
        lines = open('consonants.txt').read().splitlines()
        a = random.choice(lines)
        lines = open('vowels.txt').read().splitlines()
        b = random.choice(lines)
        lines = open('consonants2.txt').read().splitlines()
        c = random.choice(lines)
        ologname = a + b + c
        msg = (":speech_balloon:{0.author.mention}**, lat Raguk name iz:** ".format(message) + ologname)
        await client.send_message(message.channel, msg)
        
    elif message.content.lower().startswith("!help"):
        embed = discord.Embed(title="Elder Imp'Raguk", description="A notable lore character.", color=0xcc0909)
    
        embed.add_field(name = "!ug", value = "Say Hello to Imp'Raguk.", inline=False)
        embed.add_field(name = "!orkname", value = "Generate an orkish name fit for a Raguk.", inline=False)
        embed.add_field(name = "!ologname", value = "Generate an olog name fit for a Raguk.", inline=False)
        embed.add_field(name = "!goboname", value = "Generate a goblin name fit for a Raguk.", inline=False)
        embed.add_field(name = "!skin", value = "Gives you a skin based on your Rank.", inline=False)
        embed.add_field(name = "!ppoint", value = "Displays your current prestige points. (TBA)", inline=False)
        embed.add_field(name = "!proverb", value = "Spits out a common Raguk proverb.", inline=False)
        embed.add_field(name = "!calendar", value = "Displays all associated commands for 'Calendar.'(TBA)", inline=False)
        embed.add_field(name = "!music", value = "Displays all associated commands for 'Music.'(TBA)", inline=False)
        
        await client.send_message(message.channel, embed=embed)
        
        
    elif message.content.lower().startswith("!skin"):
        if "480769658501333002" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, ":speech_balloon:**{0.author.mention}, 'eres lat uniform, grunt!** https://bit.ly/2PCWbjf".format(message))
        elif "480769399352066059" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, ":speech_balloon:**{0.author.mention}, 'eres lat uniform, troopa!** [skin]".format(message))
        elif "480769306016350219" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, ":speech_balloon:**{0.author.mention}, 'eres lat uniform, boss!** [skin]".format(message))
        elif "480769254665224212" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, ":speech_balloon:**{0.author.mention}, 'eres lat uniform, elda!** [skin]".format(message))
        else:
            await client.send_message(message.channel, ":speech_balloon:**{0.author.mention}, lat ain' auforized for dat! Skah off 'fore mi lop off lat 'ead.**".format(message))
            
    elif message.content.lower().startswith("!proverb"):
        lines = open('proverbs.txt').read().splitlines()
        proverbs = random.choice(lines)
        msg = (":speech_balloon:{0.author.mention}".format(message) + proverbs)
        await client.send_message(message.channel, msg)
        
        
@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    if reaction.emoji == ":one:":
        if "481458248877080590" in [role.id for role in message.author.roles]:
            await client.sendmessage(channel, "bitch idiot")
               
@client.event
async def on_member_join(member):
    newUserMessage = (":speech_balloon:**Throm'ka, grunt {}! Da boss, <@310498610527862784>, will get lat sorted wiv roles agh all dat skah. If lat wanna interact wiv me, do:** _!help_".format(member.mention))
    for channel in member.server.channels:
        if channel.name == 'join-log':
            await client.send_message(channel, newUserMessage)
                          
client.run(os.getenv('TOKEN'))
