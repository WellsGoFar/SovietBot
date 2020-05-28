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
            mydoc = self.mycol.find()
            myquery = { "guildID": str(message.guild.id) }
            # mydoc = self.mycol.find() 
            # for x in mydoc:
            newvalues = { "$inc": { 'f_count': +1 } }
            self.mycol.update_one(myquery, newvalues)
            for x in mydoc:
                if x['guildID'] == str(message.guild.id):
                    await message.channel.send('Respects were paid {} times.'.format(x['f_count'] ))


def setup(bot):
    bot.add_cog(ImDad(bot))