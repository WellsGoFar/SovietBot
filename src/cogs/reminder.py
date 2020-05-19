from discord.ext import commands
import asyncio
import discord

class reminder(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    def get_remind_embed(self):
        return discord.Embed(title="Cyka blyat! That's not the correct syntax for that command",
                description='This command accepts two arguments: time to remind and a reason \n\n The correct way of writing the command is: **pp remindme \{number\}\{s/m/h/d for seconds/minutes/hours/days respectively\} reason**\n\n example: pp remindme 2m do my homework :(',
                colour = discord.Colour.blue())

    @commands.command()
    async def remindme(self, ctx, time_to, *, about_remind):
        time_letter = ['s','m','h','d']
        time_multiplier = [1,60,3600,86400]
        time_word = ['second/s', 'minute/s', 'hour/s', 'day/s']

        if time_to[-1].lower() not in time_letter:
            await ctx.send(embed = self.get_remind_embed())
            return

        try:
            float(time_to[:-1])
        except:
            await ctx.send(embed = self.get_remind_embed())
            return

        if float(time_to[:-1]) < 0:
            embed = discord.Embed(title="I can't go back in time yet. That feature is still in development. For now try using positive value for time :)",
                colour = discord.Colour.blue())
            await ctx.send(embed=embed)
            return
            
        
        if float(time_to[:-1])>30 and time_to[-1] == 'd':
            await ctx.send("Cyka blyat! I cannot set reminders more than 30 days long :(")
            return

        #30s 45m
        if time_to[-1].lower() in time_letter:
            idx = time_letter.index(time_to[-1])

        success_message = "I'll remind you in {} {}".format(time_to[:-1],time_word[idx])
        # await ctx.send("I'll remind you in {} {}".format(time_to[:-1],time_word[idx]))
        embed = discord.Embed(title = success_message,
            description = 'React to this message if you are not the author of the above message but want to be reminded about this too')
        
        msg = await ctx.send(embed=embed)
        msg_id = msg.id

        await msg.add_reaction('☑️')

        await asyncio.sleep((float(time_to[:-1]) * time_multiplier[idx]))

        message = await ctx.channel.fetch_message(msg_id)
        reactions = message.reactions

        await ctx.author.create_dm()

        await ctx.author.dm_channel.send(
            f'Hi {ctx.author.name}, you asked me to remind you about {about_remind}'
        )

        for reaction in message.reactions:
            users= set()
            async for user in reaction.users():
                if user.id == message.author.id:
                    continue           
                else:
                    users.add(user)

        for user in users:
            await user.create_dm()

            await user.dm_channel.send(
                f'Hi {user.name}, you asked me to remind you about {about_remind}'
            )
        


    @remindme.error
    async def remindme_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'time_to' or error.param.name == 'about_remind':
                await ctx.send(embed = self.get_remind_embed())

def setup(bot):
    bot.add_cog(reminder(bot))