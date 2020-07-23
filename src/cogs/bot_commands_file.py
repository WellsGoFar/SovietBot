import asyncio
import discord
from discord.ext import commands, tasks
import re
import requests
import json
import random


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
        await new_channel.edit(position=position)

    @commands.command(help = ':: Shut the fuck up!!')
    async def stfu(self, ctx, *, member: discord.Member = None): 
        if member is not None: 
            if member.name == 'SovietBot':
                await ctx.send(f'no you shut the fuck up you retard {ctx.author.mention}')
            else:
                await ctx.send('SHUT THE FUCK UP {0.mention}!'.format(member))
        else:
            await ctx.send('SHUT THE FUCK UP!')

    @commands.command()
    async def gif (self, ctx, *, search_term):
        
        try:
            if "ashwin" in search_term.split():
                await ctx.send("**fuck off retard**")
            else:
                apikey = "8LKJCTB3AWSH"  
                lmt = 10
                n = random.randint(0,9)
                search_term = search_term
                r = requests.get(
                    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

                if r.status_code == 200:
                    top_gifs = json.loads(r.content)
                    # n = random.randint(0,9)
                    # print (top_gifs['results'][n]['url'])
                else:
                    top_gifs = None

                if top_gifs is not None and len(top_gifs['results']) != 0:
                    await ctx.send(top_gifs['results'][n]['url'])
                
                else:
                    await ctx.send('**cyka blyat, that returned no results**')

        except Exception as e:
            # await ctx.send(e)
            await ctx.send('**cyka blyat, that returned no results**')
            print(e)

    @gif.error
    async def gif_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'search_term':
                embed = discord.Embed(title="Cyka blyat! That's not the correct syntax for that command",
                description='This command accepts one argument: search term; what do you want a gif about? Example: pp gif dancing dog',
                colour = discord.Colour.blue())
                await ctx.send(embed=embed)

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

    @commands.command(aliases = ['playing'])
    async def activity(self,ctx, *, game_name):
        result = []
        game_match = re.compile(game_name, re.IGNORECASE)
        try:
            for mem in ctx.guild.members:
                for act in mem.activities:
                    if game_match.search(str(act.name)):
                        result.append(mem.name)
            
            result = list(dict.fromkeys(result))

            if(not result):
                await ctx.send("No one is playing that game. Make sure the spelling is correct")
            else:
                await ctx.send(', '.join(result))
        except Exception as e:
            await ctx.send(e)

def setup(bot):
    bot.add_cog(bot_commands(bot))