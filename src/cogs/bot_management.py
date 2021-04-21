import time
import aiohttp
import discord
import importlib
import os
import sys
import pymongo

from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
        self.mydb = self.myclient["tesdb"] 
        self.mycol = self.mydb["testcollection"]


    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, name: str):
        try:
            self.bot.load_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(e)
        await ctx.send(f"Loaded extension **{name}.py**")

    @commands.command(help = ":: Unload an extension")
    @commands.is_owner()
    async def unload(self, ctx, name: str):
        try:
            self.bot.unload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(e)
        await ctx.send(f"Unloaded extension **{name}.py**")

    @commands.command(help = ":: Reload an extension")
    @commands.is_owner()
    async def reload(self, ctx, name: str):
        try:
            self.bot.reload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(e)
        await ctx.send(f"Reloaded extension **{name}.py**")

    # @commands.command(help = ":: send bot updates to every server")
    # @commands.is_owner()
    # async def announce(self, *, announcement):
    #     embed = discord.Embed(title= "@every",
    #         description = 'Enter pp help for more commands')
    #     await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def announce(self,ctx):
        try:
            mydoc = self.mycol.find() 
            for x in mydoc:
                if int(x['nsfw_channel'])==0:
                    continue
                else:
                    channel = self.bot.get_channel(int(x['nsfw_channel']))
                    if channel:
                        embed = discord.Embed(title = 'Updates to SovietBot\'s NSFW channels', 
                            description = 'To comply with Discord\'s community guidlines, SovietBot will only post NSFW content on channels marked as NSFW \n\n Contact server admins to make the channel NSFW if it is already not so.', colour = discord.Colour.purple())
                        embed.add_field(name='Click here to see how to set up a NSFW channel', value = 'https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content#h_adc93a2c-8fc3-4775-be02-bbdbfcde5010', inline = False)
                        await channel.send(embed = embed)
                    else:
                        continue
            await ctx.send('announcement made')
        except e as Exception:
            print(e)
            await ctx.send(e)


def setup(bot):
    bot.add_cog(Admin(bot))