import time
import aiohttp
import discord
import importlib
import os
import sys

from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, name: str):
        self.bot.load_extension(f"cogs.{name}")
        await ctx.send(f"Loaded extension **{name}.py**")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, name: str):
        self.bot.unload_extension(f"cogs.{name}")
        await ctx.send(f"Unloaded extension **{name}.py**")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, name: str):
        self.bot.reload_extension(f"cogs.{name}")
        await ctx.send(f"Reloaded extension **{name}.py**")

def setup(bot):
    bot.add_cog(Admin(bot))