import asyncio
import discord
from discord.ext import commands, tasks
import re
import requests
import json
from reddit_connect import *
import reddit_connect
import random
import aiohttp





class bot_commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(help = ':: Tripoloski babyyyyy')
    async def tripo(self, ctx):
        # await bot.user
        response = "Tri poloski, tripo tri poloski - Три полоски, три по три полоски"
        await ctx.send(response)

    @commands.command(help = ':: Clear messages, accepts amount and defaults to 10')
    @commands.has_permissions(manage_messages = True)
    async def clear(self,ctx,amount=10):
        await ctx.channel.purge(limit=amount+1)
        msg = await ctx.send("Cleared **{}** messages".format(amount+1), delete_after = 1.5)
        await asyncio.sleep(1.5)


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="You don't have the permission required",
                colour = discord.Colour.blue())
            await ctx.channel.send(embed=embed)
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=2)

    @commands.command(help = ':: Time for a good comeback')
    async def comeback(self, ctx):  
        await ctx.send('no u')
        # await self.bot.send_typing(ctx.channel)
        async with ctx.typing():
            await ctx.send(file=discord.File('D:/SovietBot/src/resources/no_u.gif'))

    @commands.command()
    async def simp(self, ctx, *, member: discord.Member = None):
        try:
            if member:
                await ctx.send("pathetic {0.mention}".format(member))
                await ctx.send(file=discord.File('D:/SovietBot/src/resources/simp.jpg'))
            else:
                await ctx.send(file=discord.File('D:/SovietBot/src/resources/simp.jpg'))
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    async def dance(self, ctx):
        # await self.bot.send_typing(ctx.channel)
        async with ctx.typing():
            await ctx.send(file=discord.File('D:/SovietBot/src/resources/pepe_dance.gif'))

    @commands.command(name = 'lockdown', help = 'Puts a Channel Under lockdown')
    @commands.has_permissions(administrator = True)
    async def lockdown(self,ctx):
        try:
            old_perm = ctx.channel.overwrites_for(ctx.guild.default_role)
            overwrite=None
            for x,y in old_perm:
                if x == 'read_messages':
                    overwrite = {
                        ctx.guild.default_role: discord.PermissionOverwrite(
                            send_messages=False,
                            read_messages = y
                    )
                    }
            embed = discord.Embed(title = 'Channel Lockeddown',description = f'{ctx.channel.mention} has been put under lockdown')
            embed.set_footer(text = f'This channel is under quarantine', icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = embed)
            name_old = str(ctx.channel.name)
            name_new=None
            if not name_old.startswith('quarantine-'):
                name_new = 'quarantine-'+name_old
            else:
                name_new = name_old
            await ctx.channel.edit(overwrites = overwrite)
            await ctx.channel.edit(name = name_new)
        except Exception as e:
            print(e)

    @commands.command(help = ':: Deletes all the messages in a text channel')
    @commands.has_permissions(administrator=True)
    async def nuke(self, ctx):
        position = ctx.channel.position
        new_channel = await ctx.channel.clone()
        await ctx.channel.delete()
        # await new_channel.edit(position=position)

    @commands.command(help = ':: Shut the fuck up!!')
    async def stfu(self, ctx, *, member: discord.Member = None): 
        if member is not None: 
            if member.name == 'SovietBot':
                await ctx.send(f'no you shut the fuck up you retard {ctx.author.mention}')
            else:
                await ctx.send('SHUT THE FUCK UP {0.mention}!'.format(member))
        else:
            await ctx.send('SHUT THE FUCK UP!')


    async def fetch(self, session, url):
        async with session.get(url, raise_for_status=True) as response:
            if response.status is not 200:
                return None
            else:
                return await response.text()

    async def get_gif_tenor(self, search_term, ctx):
        try:
            if "ashwin" in search_term.lower():
                await ctx.send("**fuck off retard**")
            else:
                apikey = "8LKJCTB3AWSH"  
                lmt = 10
                search_term = search_term
                # async with ctx.typing():
                await ctx.trigger_typing()
                async with aiohttp.ClientSession() as session:    
                    if search_term == 'trending_right_now_19190572':
                        r = await self.fetch(session, "https://api.tenor.com/v1/trending?key=%s&limit=%s" % (apikey, lmt))
                    else:
                        r = await self.fetch(session, "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
                    top_gifs = json.loads(r)

                if top_gifs is not None and len(top_gifs['results']) != 0:
                    n = random.randint(0,len(top_gifs['results']))
                    gif_msg = await ctx.send(top_gifs['results'][n]['url'])
                    msg_id = gif_msg.id

                    # await gif_msg.add_reaction('✅')
                    # await gif_msg.add_reaction('❎')
            
                else:
                    await ctx.send('**cyka blyat, that returned no results**')

        except Exception as e:
            await ctx.send('**cyka blyat, that returned no results**')
            print(e)


    @commands.command()
    async def gif (self, ctx, *, search_term='trending_right_now_19190572'):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.get_gif_tenor(search_term, ctx))

    @gif.error
    async def gif_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'search_term':
                embed = discord.Embed(title="Cyka blyat! That's not the correct syntax for that command",
                description='This command accepts one argument: search term; what do you want a gif about? Example: pp gif dancing dog',
                colour = discord.Colour.blue())
                await ctx.send(embed=embed)

    roasts=[]

    @commands.command()
    async def roast(self, stc, member: discord.Member=None):
        pass

    @commands.command()
    async def mock(self,ctx, *, message = None):
        # await ctx.send("new command")
        if message is None and ctx.message.reference:
            try:
                message = ctx.message.reference
                mocking_message_id = message.message_id
                # await ctx.send(message.message_id)
                message = await ctx.channel.fetch_message(mocking_message_id)
                message_content = message.content
                mocked_message =''
                b = True
                for c in message_content:
                    mocked_message += c.upper() if b else c.lower()
                    if c.isalpha():
                        b = not b
                await ctx.send(mocked_message)
                await ctx.send('https://cdn.betterttv.net/emote/607873e039b5010444cffcab/3x')
                # await ctx.send(file=discord.File('D:/SovietBot/src/resources/feelsdankman.png'))
            except Exception as e:
                ctx.send(e)
        elif message is not None:
            message_content = message
            mocked_message =''
            b = True
            for c in message_content:
                mocked_message += c.upper() if b else c.lower()
                if c.isalpha():
                    b = not b
            await ctx.send(mocked_message)
            await ctx.send('https://cdn.betterttv.net/emote/607873e039b5010444cffcab/3x')
            # await ctx.send(file=discord.File('D:/SovietBot/src/resources/feelsdankman.png'))
        else:
            await ctx.send("The only thing to mock here is your dumbass")
            await ctx.send('https://cdn.betterttv.net/emote/607873e039b5010444cffcab/3x')
            # await ctx.send(file=discord.File('D:/SovietBot/src/resources/feelsdankman.png'))


    @commands.command(help = ':: Changes nickname of a user')
    @commands.has_permissions(manage_nicknames = True)
    async def changenick(self, ctx, member: discord.Member=None, *, new_nick=None):
        try:
            await member.edit(nick=new_nick)
            await ctx.send("**{}**'s nick name changed to **{}**".format(member, new_nick))
        except Exception as e:
            print(e)
            await ctx.send ("**looks like the user you're trying to change the nickname for has a role higher than me :(**")

    @changenick.error
    async def changenick_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'member':
                embed = discord.Embed(title="Cyka blyat! That's not the correct syntax for that command",
                description='This command accepts two arguments: user mention and the new nickname. \n\nExample: pp changenick @user new_nickname',
                colour = discord.Colour.blue())
                await ctx.send(embed=embed)

    @commands.command(aliases = ['latency'])
    async def ping(self, ctx):
        await ctx.send('Pong! {0}'.format(self.bot.latency))

    # @commands.command()
    # async def testreddit(self,ctx):
    #     try:
    #         import os
    #         cwd = os.getcwd()
    #         await ctx.send(cwd)
    #         ttt = reddit_connect.get_test()
    #         await ctx.send(ttt)
    #         # link_test = reddit_connect.get_meme()
    #         # await ctx.send(link_test)
    #     except Exception as e:
    #         await ctx.send(e)



    @commands.command()
    async def ding(self,ctx):
        await ctx.send('dong motherfucker!')

    @commands.command()
    async def scooby(self,ctx):
        await ctx.send('dooby doo!')

    intents = discord.Intents.default()
    intents.members = True
    intents.presences = True

    @commands.command(aliases = ['playing'])
    async def activity(self,ctx, *, game_name):
        result = []
        game_match = re.compile(game_name, re.IGNORECASE)
        print('hi')
        try:
            # members = await ctx.guild.fetch_members(limit=10)
            # members = ctx.guild.members
            # async for mem in ctx.guild.fetch_members():
            for mem in ctx.guild.members:
                # await ctx.send(mem.activities)
                for act in mem.activities:
                    # await ctx.send(act)
                    if game_match.search(str(act.name)):
                        result.append(mem.name)
            result = list(dict.fromkeys(result))

            if(not result):
                await ctx.send("No one is playing that game. Make sure the spelling is correct")
            else:
                await ctx.send(', '.join(result))

            # await ctx.send(members[10])
        except Exception as e:
            await ctx.send(e)

def setup(bot):
    bot.add_cog(bot_commands(bot))