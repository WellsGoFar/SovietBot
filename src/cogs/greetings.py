import discord
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
import pymongo

load_dotenv()
LOGCHANNEL = os.getenv('LOGCHANNEL')
WELCOMECHANNEL = os.getenv('WELCOMECHANNEL')

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["tesdb"]
        self.mycol = self.mydb["testcollection"] 

    @commands.Cog.listener()
    async def on_member_join(self, member):
        mydoc = self.mycol.find()
        for x in mydoc:
            if member.guild.id == int(x['guildID']):
                break
        channel = self.bot.get_channel(int(x['logs_channel']))
        if channel is not None:
            message = x['welcome_message']
            message = (member.mention).join(message.split('{user.name}'))
            message = ("**" + member.guild.name + "**"). join(message.split('{server.name}'))
            await channel.send(message)



    @commands.Cog.listener()
    async def on_member_remove(self, member):
        mydoc = self.mycol.find()
        for x in mydoc:
            if member.guild.id == int(x['guildID']):
                break
        channel = self.bot.get_channel(int(x['logs_channel']))
        if channel is not None:
            message = x['exit_message']
            message = ("**" + member.name + "**").join(message.split('{user.name}'))
            message = ("**" + member.guild.name + "**").join(message.split('{server.name}'))
            await channel.send(message)
    @commands.command(help = ':: the bot will say hello to you because your friends won\'t')
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.mention}~'.format(member))
        else:
            # emoji_saved = discord.utils.get(member.guild.emojis, name="triggered")
            print(emoji_saved)
            await ctx.send('{0.mention}... Once is enough, get a life. :snowman2:')
        self._last_member = member

def setup(bot):
    bot.add_cog(Greetings(bot))