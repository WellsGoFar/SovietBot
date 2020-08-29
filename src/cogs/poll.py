import discord
from discord.ext import commands, tasks
import random
import re
import sys

class bot_commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.reactions = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']

    def format_option(self,opts, score):
        result = ""
        print('hi')
        try:
            for i, j, k in zip(opts,score, range(len(opts))):
                result += "{}. \"{}\":\t{}\n".format(k+1,i,j)
        except Exception as e:
            print(e)
        return result

    @commands.command()
    async def poll(self, ctx, question, *, options):
        reactions = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']
        opts = re.findall(r'"([^"]*)"', options)
        if len(opts) > 10:
            await ctx.send("No more than 10 options allowed")
        else:
            await ctx.send("**"+question+"**")          
            bars = [0] * len(opts) 
            formatted_options = self.format_option(opts,bars)
            print(formatted_options)
            poll = """```css\n{}\n```""".format(formatted_options)
            poll_msg = await ctx.send(poll)
            try:
                for i in range(len(opts)):
                    await poll_msg.add_reaction(reactions[i])
            except Exception as e:
                print(e)
            poll_id = poll_msg.id
            ids=[]
            with open('resources/tracks/polls.txt', 'r') as filehandler:
                for line in filehandler:
                    idd = line[:-1]
                    ids.append(idd)
            ids.append(poll_id)
            with open('resources/tracks/polls.txt', 'w') as filehandler:
                for listitem in ids:
                    filehandler.write('%s\n' % listitem)

    @poll.error
    async def poll_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == "options":
                embed = discord.Embed(title="Cyka blyat! That's not the correct syntax for that command",
                description='This command accepts a question and options: Example: pp poll "do you understand?" "yes" "no"',
                colour = discord.Colour.blue())
                await ctx.send(embed=embed)
            if error.param.name == "question":
                embed = discord.Embed(title="Cyka blyat! That's not the correct syntax for that command",
                description='You forgot to give a question on what the poll is about: Example: pp poll "do you understand?" "yes" "no"',
                colour = discord.Colour.blue())
                await ctx.send(embed=embed)



    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        user = self.bot.get_user(payload.user_id)
        if not user.bot:
            ids=[]
            try:
                emoji_index = self.reactions.index(payload.emoji.name)
                with open('resources/tracks/polls.txt', 'r') as filehandler:
                    for line in filehandler:
                        idd = line[:-1]
                        ids.append(idd)
                try:
                    if str(payload.message_id) in ids:
                        chnl = self.bot.get_channel(payload.channel_id)
                        msg = await chnl.fetch_message(payload.message_id)
                        content_of_msg = msg.content
                        new_content = ""
                        msg_iter = iter(content_of_msg.splitlines())
                        for line in msg_iter:
                            if line.startswith(str(emoji_index+1)):
                                votes = int(line.split(":")[1].strip())
                                new_line = line.split(':')[0]+':\t'+str(votes+1)
                                new_content += new_line+'\n'
                            else:
                                new_content += line+'\n'
                        await msg.edit(content=new_content)
                except Exception as e:
                    print(e)
            except ValueError:
                pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):
        user = self.bot.get_user(payload.user_id)
        if not user.bot:
            ids=[]
            try:
                emoji_index = self.reactions.index(payload.emoji.name)
                with open('resources/tracks/polls.txt', 'r') as filehandler:
                    for line in filehandler:
                        idd = line[:-1]
                        ids.append(idd)
                try:
                    if str(payload.message_id) in ids:
                        chnl = self.bot.get_channel(payload.channel_id)
                        msg = await chnl.fetch_message(payload.message_id)
                        content_of_msg = msg.content
                        new_content = ""
                        msg_iter = iter(content_of_msg.splitlines())
                        for line in msg_iter:
                            if line.startswith(str(emoji_index+1)):
                                votes = int(line.split(":")[1].strip())
                                new_line = line.split(':')[0]+':\t'+str(votes-1)
                                new_content += new_line+'\n'
                            else:
                                new_content += line+'\n'
                        await msg.edit(content=new_content)
                except Exception as e:
                    print(e)
            except ValueError:
                pass


def setup(bot):
    bot.add_cog(bot_commands(bot))