import discord
from discord.ext import commands
from discord.utils import find

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def thromka(ctx):
    await ctx.send("Nub blahin', get back ta' work")
