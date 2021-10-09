import os
import discord
import numpy as np
from dotenv import load_dotenv

import json
from discord.ext import commands, tasks
intents = discord.Intents.all()
# intents.members = True
# intents.presences = True

bot = commands.Bot(command_prefix='pp ')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')
bot = commands.Bot(command_prefix=['pp ','Pp ','pP ', 'PP'], intents = intents)

bot.load_extension("cogs.bot_commands_file")
bot.load_extension("cogs.greetings")
bot.load_extension("cogs.imdad")
bot.load_extension("cogs.reddithandler")
bot.load_extension('cogs.poll')
bot.load_extension('cogs.npoll')
bot.load_extension('cogs.among_us')
bot.load_extension("cogs.bot_management")
bot.load_extension("cogs.reminder")
bot.load_extension("cogs.help")
bot.load_extension("cogs.server_config")
bot.load_extension("cogs.music")
bot.load_extension("cogs.bois_tag")

bot.run(TOKEN)#D:\SovietBot\src\cogs\__pycache__