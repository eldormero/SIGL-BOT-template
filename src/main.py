import os
from discord.ext import commands

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

token = "ODkyODIzMDM2MDk5Njk0NjAy.YVSgPw.rv-O_XADhQfmOmuxYM2DjkDk2NM"
bot.run(token)  # Starts the bot