import os
import discord
from dotenv import load_dotenv
import json
import re
from discord.ext import commands, tasks
from time import gmtime, strftime

bot = commands.Bot(command_prefix='pp ')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')
GUILDID = int(os.getenv('GUILDID'))
BOTTESTCHANNEL = os.getenv('BOTTESTCHANNEL')
bot = commands.Bot(command_prefix='pp ')

@bot.command(name='tripo',pass_context=True,help = 'tripoloski babyyyy')
async def tripo(ctx):
    response = "tripo tripo tripoloski"
    print(response)
    await ctx.send(response)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord')

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command(help = 'the bot will say hello to you because your friends won\'t')
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        member_mention = '<@{}>'.format(member.id)
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {}~'.format(member_mention))
        else:
            await ctx.send('{}... Once is enough, get a life.'.format(member_mention))
        self._last_member = member


client = discord.Client()

class MyCog(commands.Cog):
    def __init__(self,bot):
        self.index = 0
        self.bot = bot
        self.throw_fact.start()

    def cog_unload(self):
        self.throw_fact.cancel()

    @tasks.loop(hours=5.0)
    async def throw_fact(self):
        # print(self.index)
        self.index += 1
        guild = bot.get_guild(id=GUILDID)
        
        for channel in guild.channels:
            if channel.name == BOTTESTCHANNEL:
                break
        #printing guild name and text channel object type for debugging
        print(guild)
        # print(type(guild))
        print(type(channel))
        #sends a message for looping test
        await channel.send("Loop test every 5 hours: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    @throw_fact.before_loop
    async def before_throw_fact(self):
        print('waiting...')
        await self.bot.wait_until_ready()

class ImDad(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == bot.user:
            return 

        cykaObj = re.compile(r'cyka', re.IGNORECASE)
        dadObj = re.compile(r'^im |^i\'m | im | i\'m ', re.IGNORECASE)
        if cykaObj.search(message.content):
            print(message.channel)
            await message.channel.send("cyka blyat")


        if dadObj.search(message.content):
            dadName = message.content[(dadObj.search(message.content).span()[1]): ]
            nameCheck = re.compile(r'dad', re.IGNORECASE)

            if nameCheck.search(dadName):
                await message.channel.send(f'Hi {dadName}, I\'m grandad')
            
            else: 
                await message.channel.send(f'Hi {dadName}, I\'m dad')

bot.add_cog(MyCog(bot))
bot.add_cog(Greetings(bot))
bot.add_cog(ImDad(bot))

bot.run(TOKEN)