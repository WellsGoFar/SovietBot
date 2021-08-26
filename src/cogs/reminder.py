from discord.ext import commands
import asyncio
import discord

class reminder(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    def get_remind_embed(self):
        return discord.Embed(title="Cyka blyat! That's not the correct syntax for that command",
                description='This command accepts two arguments: time to remind and a reminder title. \n\n The correct way of writing the command is: **pp remindme \{time\} reason**\n\n example: `pp remindme 2h30m do my homework :(` This sets a reminder for 2 hours and 30 minutes\n\n **\{time\}** can be written as: \n`2m10s` which is *2 minutes and 10 seconds*, \n`2d3h20m` which is *2 days 3 hours and 20 minutes*, \n`10m` which is *10 minutes*, \n`1h30m` which is *1 hour and 30 minutes* and so on....',
                colour = discord.Colour.blue())

    @commands.command()
    async def remindme(self, ctx, time_to, *, about_remind):
        time_letter = ['s','m','h','d']
        time_multiplier = [1,60,3600,86400]
        time_word = ['seconds', 'minutes', 'hours', 'days']
        running_time_string = ''
        running_number = ''
        total_time_to = 0


        if time_to[0] == '-':
            embed = discord.Embed(title="I can't go back in time yet. That feature is still in development. For now try using positive value for time :)",
                colour = discord.Colour.blue())
            await ctx.send(embed=embed)
            return

        if not time_to[-1].isdigit():
            for i in time_to:
                if i.isdigit() or i == '.':
                    running_number +=  i
                elif not i.isdigit() and i in time_letter:
                    idx = time_letter.index(i)
                    running_time_string = running_time_string + running_number + ' ' + time_word[idx]  + ' '
                    total_time_to = total_time_to + float(running_number) * time_multiplier[idx]
                    running_number = ''
                else: 
                    print('what in the reminder?')
                    # running_time_string, total_time_to = None, None
                    await ctx.send(embed = self.get_remind_embed())
                    return
        else:
            running_time_string, total_time_to = None, None
            print('what in the reminder?')
            await ctx.send(embed = self.get_remind_embed())
            return 
                
        if total_time_to > 864000:
            await ctx.send("Cyka blyat! I cannot set reminders more than 10 days long :(")
            return


        success_message = "I'll remind you in {}".format(running_time_string)

        embed = discord.Embed(title = success_message,
            description = 'React to this message if you are not the author of the above message but want to be reminded about this too')
        
        msg = await ctx.send(embed=embed)
        msg_id = msg.id

        await msg.add_reaction('☑️')

        await asyncio.sleep(total_time_to)

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