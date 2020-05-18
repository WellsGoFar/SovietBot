import asyncio
import discord
from discord.ext import commands, tasks

class bot_commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(help = ':: tripoloski babyyyyy')
    async def tripo(self, ctx):
        response = "Tri poloski, tripo tri poloski - Три полоски, три по три полоски"
        await ctx.send(response)

    @commands.command(help = ':: clear messages, accepts amount and defaults to 10')
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

def setup(bot):
    bot.add_cog(bot_commands(bot))