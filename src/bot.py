import os
import discord
from dotenv import load_dotenv
import json
import re
from discord.ext import commands, tasks
from time import gmtime, strftime
from reddit_helper import *
import asyncio
import urllib.request


bot = commands.Bot(command_prefix='pp ')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')
GUILDID = int(os.getenv('GUILDID'))
FACTSCHANNEL = os.getenv('FACTSCHANNEL')
MEMECHANNEL = os.getenv('MEMECHANNEL')
LOGCHANNEL = os.getenv('LOGCHANNEL')
NSFWCHANNEL = os.getenv('NSFWCHANNEL')
bot = commands.Bot(command_prefix=['pp ','Pp ','pP ', 'PP'])
# guild = bot.get_guild(id=GUILDID)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord')

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        all_channels = member.guild.text_channels
        emoji1 = discord.utils.get(member.guild.emojis, name='ussrstar')
        emoji2 = discord.utils.get(member.guild.emojis, name='ussr')
        channel = [channel for channel in all_channels if channel.name == LOGCHANNEL][0]
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


client = discord.Client()

class reddit_handler(commands.Cog):
    def __init__(self,bot):
        self.index = 0
        self.bot = bot
        self.throw_fact.start()
        self.throw_meme.start()
        self.throw_pifs.start()

    def cog_unload(self):
        self.throw_fact.cancel()
        self.throw_meme.cancel()
        self.throw_pifs.cancel()

    @tasks.loop(hours=8.0)
    async def throw_fact(self):
        
        guild = bot.get_guild(id=GUILDID)
        for channel in guild.channels:
            if channel.name == FACTSCHANNEL:
                break
        #printing guild name and text channel object type for debugging
        # print(guild)
        # print(type(guild))
        # print(type(channel))
        #sends a message for looping test
        titles, links = get_til()
        for i in range(len(titles)):
            message_string = titles[i]
            message_url = links[i]
            print('SENDING FACT....')
            await channel.send(str("""```css\n{}```\n<{}>""".format(message_string, message_url)))
            await asyncio.sleep(5400)
            # await asyncio.sleep(10)

    @tasks.loop(hours=6.0)
    async def throw_meme(self):
        guild = bot.get_guild(id=GUILDID)
        for channel in guild.channels:
            if channel.name == MEMECHANNEL:
                break
        titles, links = get_meme()
        for i in range(len(titles)):
            meme_title = titles[i]
            meme_url = links[i]
            embed = discord.Embed(
                title = meme_title,
                colour = discord.Colour.blue()
                )
            embed.set_image(url=meme_url)
            print('SENDING MEME....')
            await channel.send(embed=embed)
            await asyncio.sleep(100)

    @tasks.loop(hours=6.0)
    async def throw_pifs(self):
        guild = bot.get_guild(id=GUILDID)
        for channel in guild.channels:
            if channel.name == NSFWCHANNEL:
                break
        links = get_pifs()
        for link in links:
            if(link.startswith('https://redgifs.com/')):
                link_id = link.split('/')[-1].split('-')[0]
                print('SENDING PIFS....')
                await channel.send('https://gfycat.com/{}'.format(link_id))
            else:
                print('SENDING PIFS....')
                await channel.send(link)     
            await asyncio.sleep(1440)

    @throw_fact.before_loop
    async def before_throw_fact(self):
        print('waiting...')
        await self.bot.wait_until_ready()
    
    @throw_meme.before_loop
    async def before_throw_meme(self):
        print('meme waiting...')
        await self.bot.wait_until_ready()

    @throw_pifs.before_loop
    async def before_throw_pif(self):
        print('pif gif waiting...')
        await self.bot.wait_until_ready()

class ImDad(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == bot.user or message.author.bot:
            return 

        cykaObj = re.compile(r'cyka', re.IGNORECASE)
        dadObj = re.compile(r'^im |^i\'m | im | i\'m ', re.IGNORECASE)
        if cykaObj.search(message.content):
            # print(message.channel)
            await message.channel.send("cyka blyat")

        if dadObj.search(message.content):
            dadName = message.content[(dadObj.search(message.content).span()[1]): ]
            nameCheck = re.compile(r'dad', re.IGNORECASE)

            if nameCheck.search(dadName):
                await message.channel.send(f'Hi {dadName}, I\'m grandad')
            
            else: 
                await message.channel.send(f'Hi {dadName}, I\'m dad')


class bot_commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(help = ':: tripoloski babyyyy')
    async def tripo(self, ctx):
        response = "Tri poloski, tripo tri poloski - Три полоски, три по три полоски"
        await ctx.send(response)

    @commands.command(help = ':: clear messages, accepts amount and defaults to 10')
    @commands.has_permissions(manage_messages = True)
    async def clear(self,ctx,amount=10):
        await ctx.channel.purge(limit=amount+1)
        await ctx.channel.send("Cleared **{}** messages".format(amount+1))
        await asyncio.sleep(1.5)
        await ctx.channel.purge(limit=1)
        


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="You don't have the permission",
                colour = discord.Colour.blue())
            await ctx.channel.send(embed=embed)

bot.add_cog(reddit_handler(bot))
bot.add_cog(Greetings(bot))
bot.add_cog(ImDad(bot))
bot.add_cog(bot_commands(bot))

bot.run(TOKEN)