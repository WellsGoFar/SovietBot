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
  "hello"                    :: the bot will say hello to you because your friends won't
  "changenick"               :: Changes nickname of a user
  "clear"                    :: Clear messages, accepts amount defaults to 10
  "comeback"                 :: Time for a good comeback
  "nuke"                     :: Deletes all the messages in a text channel
  "stfu"                     :: Shut the fuck up!!
  "tripo"                    :: Tripoloski babyyyyy
  "simp"                     :: for when you come across a simp
  "remindme"                 :: Reminds you with time duration mentioned
  "activty"/"playing"        :: Check what members of the server are playing a game: example: pp activity rainbow six\n
--------------------------------------------

Server Configuration:\n
  "setup"             :: Add channels for periodic memes, facts and nsfw content
  "update_meme"       :: Change/add channel for memes
  "update_nsfw"       :: Change/add channel for nsfw
  "update_logs"       :: Change/add channel for server logs
  "update_facts"      :: Change/add channel for facts
  "update_welcome"    :: Change the message the bot sends when a new member joins the server
  "update_exit"       :: Change the message bot sends when a member leaves the server
```""")
        
def setup(bot):
    bot.add_cog(help(bot))