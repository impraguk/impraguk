import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@commands.command()
async def ug(ctx):
    await ctx.send("Nub blahin', get back ta' work!")
    
bot.add_command(ug)

bot.run('NDI5MzE1NDA4NTA4NjE2NzA1.DmDCQQ.qgFaBYsOSlm-Uc5UnEc5yZ_Zd40')
