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

    @commands.command(help = ':: change nickname, if you have the manage nickname permission')
    @commands.has_permissions(manage_nicknames = True)
    async def changenick(self, ctx, member: discord.Member, *, new_nick):
        try:
            await member.edit(nick=new_nick)
            await ctx.send("**{}**'s nick name changed to **{}**".format(member, new_nick))
        except Exception as e:
            print(e)
            
    @changenick.error
    async def changenick_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'member' or error.param.name == 'new_nick':
                embed = discord.Embed(title="Cyka blyat! That's not the correct syntax for that command",
                description='This command accepts two arguments: user mention and the new nickname. \n\nExample: pp changenick @user new_nickname',
                colour = discord.Colour.blue())
                await ctx.send(embed=embed)

    @commands.command(help = ':: time for a good comeback')
    async def hi(self, ctx):  
        await ctx.send('hi')

def setup(bot):
    bot.add_cog(updatenick(bot))