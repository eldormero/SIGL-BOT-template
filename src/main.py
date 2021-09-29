import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)


bot.author_id = 729411905399292075  # Discord ID of Martin
# Discord ID of Léo : 375294792051195904

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

# Load Token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(token)  # Starts the bot