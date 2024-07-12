import discord
from discord.ext import commands
import os, random
import requests
#note nama folder bisa diganti

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

@bot.command()
async def permasalahan(ctx):
    img_name = random.choice(os.listdir('permasalahan'))#note:kalau menganti nama folder ini harus diganti juga sesuai dengan nama folder
    with open(f'peermasalahan/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def pemilahan(ctx):
    img_name = random.choice(os.listdir('pemilahan'))
    with open(f'pemilahan/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

@bot.command()
async def daur_ulang(ctx):
    img_name = random.choice(os.listdir('daur_ulang'))
    with open(f'daur_ulang/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

@bot.command()
async def pencegahan(ctx):
    img_name = random.choice(os.listdir('pencegahan'))
    with open(f'pencegahan/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

bot.run("token")




