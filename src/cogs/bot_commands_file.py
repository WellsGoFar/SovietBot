import asyncio
import discord
from discord.ext import commands, tasks

class bot_commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(help = ':: Tripoloski babyyyyy')
    async def tripo(self, ctx):
        response = "Tri poloski, tripo tri poloski - Три полоски, три по три полоски"
        await ctx.send(response)

    @commands.command(help = ':: Clear messages, accepts amount and defaults to 10')
    @commands.has_permissions(manage_messages = True)
    async def clear(self,ctx,amount=10):
        await ctx.channel.purge(limit=amount+1)
        await ctx.channel.send("Cleared **{}** messages".format(amount+1))
        await asyncio.sleep(1.5)
        await ctx.channel.purge(limit=1)
        
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
            await ctx.send('SHUT THE FUCK UP {0.mention}!'.format(member))
        else:
            await ctx.send('SHUT THE FUCK UP!')

    @commands.command(help = ':: Changes nickname of a user')
    @commands.has_permissions(manage_nicknames = True)
    async def changenick(self, ctx, member: discord.Member, *, new_nick=None):
        try:
            await member.edit(nick=new_nick)
            await ctx.send("**{}**'s nick name changed to **{}**".format(member, new_nick))
        except Exception as e:
            print(e)

    @changenick.error
    async def changenick_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'member':
                embed = discord.Embed(title="Cyka blyat! That's not the correct syntax for that command",
                description='This command accepts two arguments: user mention and the new nickname. \n\nExample: pp changenick @user new_nickname',
                colour = discord.Colour.blue())
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(bot_commands(bot))