import time
import aiohttp
import discord
import importlib
import os
import sys

from discord.ext import commands

class updatenick(commands.Cog):
    def __init__(self,bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(updatenick(bot))