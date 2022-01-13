import discord
from discord.ext import commands
import sys
import re
import asyncio

class among_us(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.current = False

    @commands.command(aliases = ['st'])
    async def astart(self, ctx):
        if not ctx.author.voice or not ctx.author.voice.channel:
            await ctx.send("You gotta connect to the Among Us voice channel dumbass")
        else:
            if not self.current:
                self.current=True
                try:
                    role = discord.utils.find(lambda r: r.name == 'AmongUs', ctx.message.guild.roles)
                    if role in ctx.author.roles or ctx.author.guild_permissions.administrator:
                        voice_channel = self.bot.get_channel(749156355688104036)
                        members = voice_channel.members
                        for member in members:
                            if member.id == 234395307759108106:
                                continue
                            else:
                                await member.edit(mute=True)
                                await asyncio.sleep(0.1)
                        embed = discord.Embed(title="Have fun!")
                        # await ctx.send(members[0].avatar_url)
                        await ctx.send(embed = embed)
                    else:
                        await ctx.send("You don't have the required role to use this command")
                except Exception as e:
                    ctx.send(e)
                self.current=False

    @commands.command(aliases = ['sp'])
    async def astop(self, ctx):
        if not ctx.author.voice or not ctx.author.voice.channel:
            await ctx.send("You gotta connect to the Among Us voice channel dumbass")
        else:
            if not self.current:
                self.current = True
                try:
                    role = discord.utils.find(lambda r: r.name == 'AmongUs', ctx.message.guild.roles)
                    if role in ctx.author.roles or ctx.author.guild_permissions.administrator:
                        voice_channel = self.bot.get_channel(749156355688104036)
                        members = voice_channel.members
                        for member in members:
                            await member.edit(mute=False)
                            await asyncio.sleep(0.1)
                        await ctx.send("**Members unmuted**")
                    else:
                        await ctx.send("You don't have the required role to use this command")
                except Exception as e:
                    ctx.send(e)
                self.current=False

def setup(bot):
    bot.add_cog(among_us(bot))