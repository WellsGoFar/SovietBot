from reddit_helper import *
import discord
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
import asyncio

load_dotenv()
GUILDID = int(os.getenv('GUILDID'))
FACTSCHANNEL = os.getenv('FACTSCHANNEL')
MEMECHANNEL = os.getenv('MEMECHANNEL')
NSFWCHANNEL = os.getenv('NSFWCHANNEL')
BOTTESTCHANNEL = os.getenv('BOTTESTCHANNEL')

class reddit_handler(commands.Cog):
    def __init__(self,bot):
        self.index = 0
        self.bot = bot
        self.throw_fact.start()
        self.throw_meme.start()
        self.throw_pifs.start()
        # self.throw_mess.start()

    def cog_unload(self):
        self.throw_fact.cancel()
        self.throw_meme.cancel()
        self.throw_pifs.cancel()
        # self.throw_mess.cancel()

    @tasks.loop(hours=8.0)
    async def throw_fact(self):
        
        guild = self.bot.get_guild(id=GUILDID)
        for channel in guild.channels:
            if channel.name == FACTSCHANNEL:
                break
            
        # print('pre call to reddit helper.............')
        titles, links = get_til()
        print('fact new cycle...')
        for i in range(len(titles)):
            message_string = titles[i]
            message_url = links[i]
            print('SENDING FACT....')
            await channel.send(str("""```css\n{}```Source: <{}>\n.""".format(message_string, message_url)))
            await asyncio.sleep(5400)
            # await asyncio.sleep(10)

    @tasks.loop(hours=3.0)
    async def throw_meme(self):
        guild = self.bot.get_guild(id=GUILDID)
        for channel in guild.channels:
            if channel.name == MEMECHANNEL:
                break
        titles, links = get_meme()
        print('meme new cycle...')
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
            await asyncio.sleep(1)

    @tasks.loop(hours=4.0)
    async def throw_pifs(self):
        guild = self.bot.get_guild(id=GUILDID)
        for channel in guild.channels:
            if channel.name == NSFWCHANNEL:
                break
        links = get_pifs()
        print('pifs new cycle...')
        for link in links:
            if(link.startswith('https://redgifs.com/')):
                link_id = link.split('/')[-1].split('-')[0]
                print('SENDING PIFS....')
                await channel.send('https://gfycat.com/{}'.format(link_id))
            else:
                print('SENDING PIFS....')
                await channel.send(link)     
            await asyncio.sleep(1)

    @tasks.loop(hours=4)
    async def throw_mess(self):
        guild = self.bot.get_guild(id=GUILDID)
        for channel in guild.channels:
            if channel.name == BOTTESTCHANNEL:
                break
        await channel.send('hi')

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

    @throw_mess.before_loop
    async def before_throw_mess(self):
        print('mess waiting...')
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(reddit_handler(bot))