import os
from discord.ext import commands
import random


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

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)

@bot.event
async def on_message(message):
    if message.content == "!hello":
        await message.channel.send("pies are better than cakes. change my mind.")

    await bot.process_commands(message)

@bot.command()
async def flipcoin(ctx):
    pile_ou_face = ['Pile', 'Face']

    choice = random.choice(pile_ou_face)

    await ctx.send(choice)


bot.run(token)  # Starts the bot