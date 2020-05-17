import os
import discord
from dotenv import load_dotenv
import json
from discord.ext import commands, tasks


bot = commands.Bot(command_prefix='pp ')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')
bot = commands.Bot(command_prefix=['pp ','Pp ','pP ', 'PP'])

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord')

bot.load_extension("cogs.bot_commands_file")
bot.load_extension("cogs.greetings")
bot.load_extension("cogs.imdad")
bot.load_extension("cogs.reddithandler")

bot.run(TOKEN)