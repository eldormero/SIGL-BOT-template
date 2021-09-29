import os
from discord.ext import commands
import random
import discord
from datetime import date

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

@bot.command(pass_context=True)
async def addrole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await client.add_roles(member, role)

@bot.command()
async def ar(ctx, arg):
    member = arg
    var = discord.utils.get(message.guild.roles, name = "Admin")
    member.add_role(var)

# BONUS : time : command to get the today's date 
@bot.command()
async def time(ctx):
    today = date.today()
    await ctx.send(today) 

bot.run(token)  # Starts the bot