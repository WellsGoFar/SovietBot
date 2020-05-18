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

    @commands.command()
    async def remindme(self, ctx, time_to, *, about_remind):
        time_letter = ['s','m','h','d']
        time_multiplier = [1,60,3600,86400]

        if time_to[-1].lower() not in time_letter:
            await ctx.send(embed = self.get_remind_embed())
            return

        try:
            int(time_to[:-1])
        except:
            await ctx.send(embed = self.get_remind_embed())
            return
        
        if int(time_to[:-1])>30 and time_to[-1] == 'd':
            await ctx.send("Cyka blyat! I cannot set reminders more than 30 days long :(")
            return

        if time_to[-1].lower() in time_letter:
            idx = time_letter.index(time_to[-1])
        
        time_word = ['second/s', 'minute/s', 'hour/s', 'day/s']

        await ctx.send("I'll remind you in {} {}".format(time_to[:-1],time_word[idx]))

        await asyncio.sleep((int(time_to[:-1]) * time_multiplier[idx]))

        await ctx.author.create_dm()

        await ctx.author.dm_channel.send(
            f'Hi {ctx.author.name}, you asked me to remind you about {about_remind}'
        )

    @remindme.error
    async def remindme_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'time_to' or error.param.name == 'about_remind':
                await ctx.send(embed = self.get_remind_embed())

def setup(bot):
    bot.add_cog(ImDad(bot))