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
# bot.remove_command('help')
# @bot.event
# async def on_ready():
#         await bot.change_presence(game=discord.game(name='pp help'))
#         # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="pp help"))
#         print('hi')

bot.load_extension("cogs.bot_commands_file")
bot.load_extension("cogs.greetings")
bot.load_extension("cogs.imdad")
bot.load_extension("cogs.reddithandler")
bot.load_extension("cogs.bot_management")
bot.load_extension("cogs.reminder")
bot.load_extension("cogs.help")
bot.load_extension("cogs.server_config")

bot.run(TOKEN)#D:\SovietBot\src\cogs\__pycache__