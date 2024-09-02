import discord
import random
import os
from discord import app_commands
from discord.ext import commands
from discord.utils import get
from typing import List
from typing import Optional
from typing import Literal

### SPECIFY THE TOKEN TO THE BOT HERE BEFORE RUNNING
BOT_TOKEN_HERE = ''

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

import_ball = open("8ball.txt", "r")
import_vcl = open("vclcases.txt", "r")
import_easy = open("easycases.txt", "r")
import_medium = open("mediumcases.txt", "r")
import_hard = open("hardcases.txt", "r")
import_pap = open("papirinicases.txt", "r")

responses = import_ball.read()
balleight_list = responses.splitlines()

responses = import_vcl.read()
case_list = responses.splitlines()

responses = import_easy.read()
easy_vcl = responses.splitlines()

responses = import_medium.read()
medium_vcl = responses.splitlines()

responses = import_hard.read()
hard_vcl = responses.splitlines()

responses = import_pap.read()
papirini_list = responses.splitlines()

@bot.event
async def on_ready():
    print("Bot is up and ready!")
    for guild in bot.guilds:
        print(guild.id)
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print (e)
    ### This section looks for the amount of servers the
    ### bot is in and displays it as a status message
    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    await bot.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'{servers} servers and {members} members'
    ))



@bot.tree.command(name="8ball", description="Ask for an 8ball response!")
@app_commands.describe(question = "What do you want to ask 8ball?")
async def hello(interaction:discord.Interaction, question: str):
    choosing = random.choice(balleight_list)
    choosinglist = choosing.split(",")
    resname = choosinglist[0]
    giflink = choosinglist[1]
    iconlink = choosinglist[2]
    chosencolor = discord.Color.dark_red()
    if choosinglist[3] == "green":
        chosencolor = discord.Color.green()
    elif choosinglist[3] == "orange":
        chosencolor = discord.Color.orange()
    else:
        chosencolor = discord.Color.dark_red()
    emb=discord.Embed(title=f"{resname}", description=f"{interaction.user.name} asked: {question}", color=chosencolor)
    emb.set_image(url=giflink)
    emb.set_thumbnail(url=iconlink)
    await interaction.response.send_message(embed=emb, ephemeral=False)

@bot.tree.command(name="caselist", description="Provide links to Attorney Online case resources!")
async def hello(interaction: discord.Interaction):
    emb=discord.Embed(title="AO Casing Resources", description="Here is a list of resources related to casing in Attorney Online!", color=discord.Color.orange())
    emb.add_field(name="Vanilla Case List", value="https://docs.google.com/document/d/1DgFg6CTjKMST69qlyQuhFzqYMZlA7pUZ8MHcrREdnm8/edit", inline=False)
    emb.add_field(name="Vanilla Resource Library", value="https://docs.google.com/document/d/1XS_D2jgcGp_61gl2dnAozOop3shUC06HEPOT3iuaU-s/edit", inline=False)
    emb.add_field(name="Papirini's Case Library", value="https://docs.google.com/document/d/1H-tGN8iWVnmOUvS-EoVUb75G9MmO_8h3rIuPBdW1upE/edit", inline=True)
    emb.add_field(name="The Ultimate Attorney Online Case List", value="https://docs.google.com/document/d/15tXoy9uWh0KCfCpLQjaMKaa8Kajnb4DKoW7eSKh6Z4E/edit", inline=True)
    emb.set_thumbnail(url="https://files.catbox.moe/2y6j5e.png")
    emb.set_footer(text="PollyBot has returned the resources!")
    await interaction.response.send_message(embed=emb, ephemeral=False)


@bot.tree.command(name="randomvcl", description="Get a random case document from Vanilla Case List!")
async def hello(interaction:discord.Interaction):
    choosing = random.choice(case_list)
    choosinglist = choosing.split(",")
    case_name = choosinglist[0]
    case_author = choosinglist[1]
    case_difficulty = choosinglist[2]
    case_link = choosinglist[3]
    emb=discord.Embed(title="Random VCL Case", description=f"{interaction.user.name} has requested the following case.", color=discord.Color.blue())
    emb.add_field(name="Case Name", value=f"{case_name}", inline=False)
    emb.add_field(name="Author", value=f"{case_author}", inline=True)
    emb.add_field(name="Difficulty", value=f"{case_difficulty}", inline=True)
    emb.add_field(name="Link", value=f"{case_link}", inline=False)
    emb.set_thumbnail(url="https://files.catbox.moe/s18tz9.png")
    emb.set_footer(text="A case has been acquired!")
    await interaction.response.send_message(embed=emb, ephemeral=False)

@bot.tree.command(name="easyvcl", description="Get a random easy case document from Vanilla Case List!")
async def hello(interaction:discord.Interaction):
    choosing = random.choice(easy_vcl)
    choosinglist = choosing.split(",")
    case_name = choosinglist[0]
    case_author = choosinglist[1]
    case_difficulty = choosinglist[2]
    case_link = choosinglist[3]
    emb=discord.Embed(title="Random VCL Easy Case", description=f"{interaction.user.name} has requested the following case.", color=discord.Color.green())
    emb.add_field(name="Case Name", value=f"{case_name}", inline=False)
    emb.add_field(name="Author", value=f"{case_author}", inline=True)
    emb.add_field(name="Difficulty", value=f"{case_difficulty}", inline=True)
    emb.add_field(name="Link", value=f"{case_link}", inline=False)
    emb.set_thumbnail(url="https://files.catbox.moe/s18tz9.png")
    emb.set_footer(text="A case has been acquired!")
    await interaction.response.send_message(embed=emb, ephemeral=False)


@bot.tree.command(name="mediumvcl", description="Get a random medium case document from Vanilla Case List!")
async def hello(interaction:discord.Interaction):
    choosing = random.choice(medium_vcl)
    choosinglist = choosing.split(",")
    case_name = choosinglist[0]
    case_author = choosinglist[1]
    case_difficulty = choosinglist[2]
    case_link = choosinglist[3]
    emb=discord.Embed(title="Random VCL Medium Case", description=f"{interaction.user.name} has requested the following case.", color=discord.Color.yellow())
    emb.add_field(name="Case Name", value=f"{case_name}", inline=False)
    emb.add_field(name="Author", value=f"{case_author}", inline=True)
    emb.add_field(name="Difficulty", value=f"{case_difficulty}", inline=True)
    emb.add_field(name="Link", value=f"{case_link}", inline=False)
    emb.set_thumbnail(url="https://files.catbox.moe/s18tz9.png")
    emb.set_footer(text="A case has been acquired!")
    await interaction.response.send_message(embed=emb, ephemeral=False)

@bot.tree.command(name="hardvcl", description="Get a random hard case document from Vanilla Case List!")
async def hello(interaction:discord.Interaction):
    choosing = random.choice(hard_vcl)
    choosinglist = choosing.split(",")
    case_name = choosinglist[0]
    case_author = choosinglist[1]
    case_difficulty = choosinglist[2]
    case_link = choosinglist[3]
    emb=discord.Embed(title="Random VCL Hard Case", description=f"{interaction.user.name} has requested the following case.", color=discord.Color.red())
    emb.add_field(name="Case Name", value=f"{case_name}", inline=False)
    emb.add_field(name="Author", value=f"{case_author}", inline=True)
    emb.add_field(name="Difficulty", value=f"{case_difficulty}", inline=True)
    emb.add_field(name="Link", value=f"{case_link}", inline=False)
    emb.set_thumbnail(url="https://files.catbox.moe/s18tz9.png")
    emb.set_footer(text="A case has been acquired!")
    await interaction.response.send_message(embed=emb, ephemeral=False)



@bot.tree.command(name="randompapirini", description="Get a random case document from Papirini's Case Library!")
async def hello(interaction:discord.Interaction):
    choosing = random.choice(papirini_list)
    choosinglist = choosing.split(",")
    case_name = choosinglist[0]
    case_author = choosinglist[1]
    case_difficulty = choosinglist[2]
    case_link = choosinglist[3]
    emb=discord.Embed(title="Random Papirini Case", description=f"{interaction.user.name} has requested the following case.", color=discord.Color.purple())
    emb.add_field(name="Case Name", value=f"{case_name}", inline=False)
    emb.add_field(name="Author", value=f"{case_author}", inline=True)
    emb.add_field(name="Difficulty", value=f"{case_difficulty}", inline=True)
    emb.add_field(name="Link", value=f"{case_link}", inline=False)
    emb.set_thumbnail(url="https://files.catbox.moe/s18tz9.png")
    emb.set_footer(text="A case has been acquired!")
    await interaction.response.send_message(embed=emb, ephemeral=False)


bot.run(BOT_TOKEN_HERE)
