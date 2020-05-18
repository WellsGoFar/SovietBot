import discord
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
LOGCHANNEL = os.getenv('LOGCHANNEL')
WELCOMECHANNEL = os.getenv('WELCOMECHANNEL')

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        all_channels = member.guild.text_channels
        emoji1 = discord.utils.get(member.guild.emojis, name='ussrstar')
        emoji2 = discord.utils.get(member.guild.emojis, name='ussr')
        channel = [channel for channel in all_channels if channel.name == WELCOMECHANNEL][0]
        # member_mention = '<@{}>'.format(member.id)
        if channel is not None:
            await channel.send('Hey! {0.mention} now serves the Soviet Union. Welcome to the **{1}**, comrade! {2}{3}.'.format(member, member.guild.name, str(emoji1), str(emoji2)))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        all_channels = member.guild.text_channels
        emoji1 = discord.utils.get(member.guild.emojis, name='roadwarrior')
        channel = [channel for channel in all_channels if channel.name == LOGCHANNEL][0]
        if channel is not None:
            await channel.send('**{0.name}** is no longer a comrade. {1}'.format(member, str(emoji1)))

    @commands.command(help = ':: the bot will say hello to you because your friends won\'t')
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.mention}~'.format(member))
        else:
            emoji_saved = discord.utils.get(member.guild.emojis, name="triggered")
            print(emoji_saved)
            await ctx.send('{0.mention}... Once is enough, get a life.{1}'.format(member,str(emoji_saved)))
        self._last_member = member

    @commands.command(help = ':: shut the fuck up')
    async def stfu(self, ctx, *, member: discord.Member = None): 
        if member is not None: 
            await ctx.send('SHUT THE FUCK UP {0.mention}!'.format(member))
        else:
            await ctx.send('SHUT THE FUCK UP!')


def setup(bot):
    bot.add_cog(Greetings(bot))