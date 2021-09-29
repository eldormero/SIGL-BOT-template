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


@bot.command(pass_context=True)
async def addrole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await client.add_roles(member, role)



@bot.command()
async def ar(ctx):
    member = message.author
    var = discord.utils.get(message.guild.roles, name = "Admin")
    member.ar(var)


# xkcd : get a random comic
@bot.command(pass_context=True)
async def xkcd(ctx):
    url = "https://c.xkcd.com/random/comic/"
    await ctx.send(url)


#ban : ban a member from the server
@bot.command(pass_context=True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)


# BONUS : time : command to get the today's date 
@bot.command()
async def time(ctx):
    today = date.today()
    await ctx.send(today) 

# BONUS : flipcoin : command to flip a coin
@bot.command()
async def flipcoin(ctx):
    pile_ou_face = ['Pile', 'Face']
    choice = random.choice(pile_ou_face)
    await ctx.send(choice)

# BONUS : miroir : command to know if you are la plus belle of the kingdom
@bot.command()
async def miroir(ctx):
    miroir = ['Ma reine, vous êtes la plus belle du royaume', 'Ma Reine, vous êtes vraiment laide, Blanche-Neige est la plus belle du royaume']
    choice = random.choice(miroir)
    await ctx.send('Miroir mon beau miroir, dis moi qui est la plus belle de ce royaume ?')
    await ctx.send(choice)

token = 'here is your token'

bot.run(token)  # Starts the bot