import discord
import re
from discord.ext import commands, tasks
from dotenv import load_dotenv
import asyncio

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

    def get_remind_embed(self):
        return discord.Embed(title="Cyka blyat! That's not the correct syntax for that command",
                description='This command accepts two arguments: time to remind and a reason \n\n The correct way of writing the command is: **pp remindme \{number\}\{s/m/h/d for seconds/minutes/hours/days respectively\} reason**\n\n example: pp remindme 2m do my homework :(',
                colour = discord.Colour.blue())

def setup(bot):
    bot.add_cog(ImDad(bot))