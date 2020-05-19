from discord.ext import commands
import asyncio
import discord

class help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        bot.remove_command('help')

    @commands.command()
    async def help(self, ctx):
        await ctx.send ("""```nimrod
Commands:\n
  "hello"      :: the bot will say hello to you because your friends won't
  "changenick" :: Changes nickname of a user
  "clear"      :: Clear messages, accepts amount defaults to 10
  "comeback"   :: Time for a good comeback
  "nuke"       :: Deletes all the messages in a text channel
  "stfu"       :: Shut the fuck up!!
  "tripo"      :: Tripoloski babyyyyy
  "remindme"   :: Reminds you with time duration mentioned
  "activty"    :: Check what members of the server are playing a game: example: pp activity rainbow six\n
--------------------------------------------
```""")
        
def setup(bot):
    bot.add_cog(help(bot))