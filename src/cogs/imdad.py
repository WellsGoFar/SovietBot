import discord
import re
from discord.ext import commands, tasks
from dotenv import load_dotenv

class ImDad(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
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

def setup(bot):
    bot.add_cog(ImDad(bot))