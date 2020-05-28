import discord
import re
from discord.ext import commands, tasks
from dotenv import load_dotenv
import asyncio
import pymongo

class ImDad(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
        self.mydb = self.myclient["tesdb"] 
        self.mycol = self.mydb["testcollection"]
        self.f_count = {}
        self.f_counts = {}
        self.update_server_f_counts.start()
        
    def cog_unload(self):
        self.update_server_f_counts.cancel()

    def get_server_f_counts(self):
        for x in self.mycol.find():
            self.f_counts[x['guildID']] = x['f_count']
        return self.f_counts

    @tasks.loop(minutes=30.0)
    async def update_server_f_counts(self):
        try:
            for i in self.f_count:
                myquery = {"guildID": i}
                newvalues = { "$set": { "f_count": self.f_count[i] } } #change
                self.mycol.update_one(myquery, newvalues)
            self.f_counts.update(self.f_count)
            self.f_count = {}
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_message(self,message):

        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="pp help"))

        if message.author == self.bot.user or message.author.bot:
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


        if message.content.lower() == 'f':
            try:
                if self.f_counts:
                    guildID = str(message.guild.id)
                    if guildID in self.f_count:
                        self.f_count[guildID] += 1
                    else:
                        self.f_count[guildID] = self.f_counts[guildID] + 1
                    await message.channel.send('Respects were paid {} times.'.format(self.f_count[guildID]))
                else:
                    self.f_counts = self.get_server_f_counts()
                    guildID = str(message.guild.id)
                    if guildID in self.f_count:
                        self.f_count[guildID] += 1
                    else:
                        self.f_count[guildID] = self.f_counts[guildID] + 1
                    await message.channel.send('Respects were paid {} times.'.format(self.f_count[guildID]))
            except Exception as e:
                await message.channel.send(e)

    @update_server_f_counts.before_loop
    async def before_server_f_count_update(self):
        print('server update waiting...')
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(ImDad(bot))