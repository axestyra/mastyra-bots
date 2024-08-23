import discord
import random
import os
from pprint import pprint as pp
from discord import app_commands
from discord.ext import commands
from discord.utils import get
from typing import List
from typing import Literal
from typing import Optional



bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())


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

### You must specify ROLE_NAME_HERE, CHANNEL_ID_HERE, and ROLE_ID_HERE
@bot.tree.command(name="case-notify", description="ROLE_NAME_HERE role required: Universally ping for vanilla case runs that are being hosted!")
@app_commands.checks.has_role('ROLE_NAME_HERE')
@app_commands.describe(case_name = "What is the name of the case?")
@app_commands.describe(case_link = "What is the case document link?")
@app_commands.describe(case_server = "What server is the case being hosted in?")
@app_commands.describe(case_room = "What room is the case being hosted in?")
@app_commands.describe(case_roles = "What roles need to be filled for the case?")
@app_commands.describe(case_notes = "Any additional notes regarding the case?")
@app_commands.describe(case_image = "If you have a graphic, specify the image URL here!")
async def notify(interaction: discord.Interaction, case_name: str, case_link: str, case_server: str, case_room: str, case_roles: str, case_notes: Optional[str], case_image: Optional[str]):
    emb=discord.Embed(title="A CASE IS BEING HOSTED", description=f"{interaction.user.name} is hosting a case run.", color=discord.Color.orange())
    emb.add_field(name="Case Name", value=f"{case_name}", inline=False)
    emb.add_field(name="Document Link", value=f"{case_link}", inline=False)
    emb.add_field(name="Server", value=f"{case_server}", inline=True)
    emb.add_field(name="Room", value=f"{case_room}", inline=True)
    emb.add_field(name="Roles Needed", value=f"{case_roles}", inline=False)
    if case_notes != None:
        emb.add_field(name="Additional Notes", value=f"{case_notes}", inline=False)
    if case_image != None:
        emb.set_image(url=case_image)
    if case_server.lower() == "ole" or case_server.lower() == "official law empire":
         emb.set_thumbnail(url="https://files.catbox.moe/b83mpg.png")
    elif case_server.lower() == "cc" or case_server.lower() == "case cafe":
         emb.set_thumbnail(url="https://files.catbox.moe/kgx0pr.png")
    elif case_server.lower() == "vanilla":
         emb.set_thumbnail(url="https://files.catbox.moe/buwdg6.png")
    elif case_server.lower() == "kv2" or case_server.lower() == "knight's vanilla 2" or case_server.lower() == "knights vanilla 2":
         emb.set_thumbnail(url="https://files.catbox.moe/cu3xwh.png")
    else:
         emb.set_thumbnail(url="https://files.catbox.moe/rt9r8p.png")
    
    coa_channel = await interaction.guild.fetch_channel(CHANNEL_ID_HERE)
    await coa_channel.send(f"<@&ROLE_ID_HERE>\n", embed=emb, allowed_mentions=discord.AllowedMentions(roles=True))
    await interaction.response.send_message(f"{interaction.user.name}, other users have been notified about your case run!")

### You must specify PUT_TOKEN_HERE before starting the bot
bot.run('PUT_TOKEN_HERE')
