from reddit_connect import *
import discord
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
import asyncio
import pymongo

load_dotenv()
# GUILDID = int(os.getenv('GUILDID'))
# FACTSCHANNEL = os.getenv('FACTSCHANNEL')
# MEMECHANNEL = os.getenv('MEMECHANNEL')
# NSFWCHANNEL = os.getenv('NSFWCHANNEL')
# BOTTESTCHANNEL = os.getenv('BOTTESTCHANNEL')

class reddit_handler(commands.Cog):
    def __init__(self,bot):
        self.index = 0
        self.bot = bot
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
        self.mydb = self.myclient["tesdb"] 
        self.mycol = self.mydb["testcollection"]
        self.throw_fact.start()
        self.throw_meme.start()
        self.throw_pifs.start()
        self.throw_nooz.start()
        # self.mydoc = mycol.find()
        # self.throw_mess.start()

    def cog_unload(self):
        self.throw_fact.cancel()
        self.throw_meme.cancel()
        self.throw_pifs.cancel()
        self.throw_nooz.cancel()
        # self.throw_mess.cancel()

    @tasks.loop(hours=8.0)
    async def throw_fact(self):
        # print('hi1')
        # mydoc = self.mycol.find()
        # print('hi2')
        titles, links = get_til()
        # print('hi2')
        print('fact new cycle...')
        for i in range(len(titles)):
            mydoc = self.mycol.find() 
            for x in mydoc:
                if int(x['facts_channel'])==0:
                    continue
                else:
                    channel = self.bot.get_channel(int(x['facts_channel']))
                    # channel = discord.utils.get(self.bot.guild.text_channels, id='Foo', bitrate=64000)
                    # print(type(channel))
                    message_string = titles[i] 
                    message_url = links[i]
                    print('SENDING FACT....')
                    if channel:
                        await channel.send(str("""```css\n{}```Source: <{}>\n.""".format(message_string, message_url)))
                    else:
                        continue
            await asyncio.sleep(1000)

    @tasks.loop(hours=5.0)
    async def throw_nooz(self):
        # print('hi1')
        # mydoc = self.mycol.find()
        # print('hi2')
        titles, links = get_nooz()
        # print('hi2')
        print('nooz new cycle...')
        for i in range(len(titles)):
            mydoc = self.mycol.find() 
            for x in mydoc:
                if int(x['nooz_channel'])==0:
                    continue
                else:
                    channel = self.bot.get_channel(int(x['nooz_channel']))

                    message_string = titles[i] 
                    message_url = links[i]
                    print('SENDING NOOZ ARTICLE....')
                    if channel:
                        await channel.send(str("""```css\n{}```Source: <{}>\n.""".format(message_string, message_url)))
                    else:
                        continue
            await asyncio.sleep(1000)


    @tasks.loop(hours=3.0)
    async def throw_meme(self):

        titles, links = get_meme()
        print(titles)
        print('meme new cycle...')
        # print(len(titles))
        for i in range(len(titles)):
            # print(titles[i],i)
            mydoc = self.mycol.find()
            # print(mydoc)
            for x in mydoc:
                # print(x['guildID'], titles[i])
                # print()
                if int(x['meme_channel'])==0:
                    continue
                else:
                    channel = self.bot.get_channel(int(x['meme_channel']))
                    meme_title = titles[i]
                    meme_url = links[i]
                    embed = discord.Embed(
                        title = meme_title,
                        colour = discord.Colour.blue()
                        )
                    embed.set_image(url=meme_url)
                    print('SENDING MEME....')
                    if channel:
                        await channel.send(embed=embed)
                    else:
                        continue
                    # await asyncio.sleep(1)

    @tasks.loop(hours=4.0)
    async def throw_pifs(self):
        # guild = self.bot.get_guild(id=GUILDID)
        # for channel in guild.channels:
        #     if channel.name == NSFWCHANNEL:
        #         break
        
        links = get_pifs()
        print(links)
        # print('new new new', links)
        # mydoc = self.mycol.find() 
        print('pifs new cycle...')
        for link in links:
            mydoc = self.mycol.find() 
            for x in mydoc:
                if int(x['nsfw_channel'])==0:
                    continue
                else:
                    channel = self.bot.get_channel(int(x['nsfw_channel']))
                    if channel and channel.is_nsfw():
                        print('SENDING PIFS....')
                        await channel.send(link)     
                    else:
                        continue
                    # await asyncio.sleep(1)


    # @tasks.loop(hours=4)
    # async def throw_mess(self):
    #     guild = self.bot.get_guild(id=GUILDID)
    #     for channel in guild.channels:
    #         if channel.name == BOTTESTCHANNEL:
    #             break
    #     await channel.send('hi')

    @throw_fact.before_loop
    async def before_throw_fact(self):
        print('fact waiting...')
        await self.bot.wait_until_ready()
    
    @throw_meme.before_loop
    async def before_throw_meme(self):
        print('meme waiting...')
        await self.bot.wait_until_ready()

    @throw_pifs.before_loop
    async def before_throw_pif(self):
        print('pif gif waiting...')
        await self.bot.wait_until_ready()

    @throw_nooz.before_loop
    async def before_throw_nooz(self):
        print('nooz waiting...')
        await self.bot.wait_until_ready()

    # @throw_mess.before_loop
    # async def before_throw_mess(self):
    #     print('mess waiting...')
    #     await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(reddit_handler(bot))