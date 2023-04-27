import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def You_need_Pelmeni(ctx):
    await ctx.send(f'Хочешь пельменей? {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


        
bot.run("MTA5NzkyOTMxODYxMDUwOTg0NQ.GYgAqN.yoYamLbudJ2OKGgssFbyg7ESgLIUc8Ze1cooAY")
