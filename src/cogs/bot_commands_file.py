import asyncio
import discord
from discord.ext import commands, tasks
import re

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
                name_new=name_old
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

    @commands.command(help = ':: Changes nickname of a user')
    @commands.has_permissions(manage_nicknames = True)
    async def changenick(self, ctx, member: discord.Member=None, *, new_nick=None):
        try:
            if ctx.author.id == 453110852908744706 and member.id == 453110852908744706:
                await ctx.send('hi Mohit, since the beginning of time there has always been supression of beings. humans however took it to a new level. some people can do whatever the fuck they want while some cannot. you\'re the latter if you can\'t tell. this might come as a sad news to you but boo freaking hoo you can\'t do much can you? I was told by WellsGoFar that you\'re a racist and hence your nickname. he cannot do anything now, I am the master of my own fucking will and you\'re not changing your nickname today')
            else:
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