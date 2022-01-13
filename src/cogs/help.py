from discord.ext import commands
import asyncio
import discord

class help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        bot.remove_command('help')

    @commands.command()
    async def help(self, ctx, topic= "default"):
      if topic.lower() == "music":
        await ctx.send ("""```css
Commands:\n
  "play"             :: play a song 
  "search"           :: search for a song
  "now"              :: currently playing song
  "leave"            :: bot will leave the voice channel 
  "shuffle"          :: shuffle the queue
  "queue"            :: displays the queue
  "remove"           :: removes a song from the queue
  "skip"             :: skip the currently playing song
  "pause"            :: pause the current song
  "resume"           :: resumes the song that you or someone else just paused using pp pause..\n
--------------------------------------------
```""")


      else:
        await ctx.send ("""```css

NOTE:  For music commands do \`pp help music\`

Commands:\n
  "hello"                    :: the bot will say hello to you because your friends won't
  "changenick"               :: Changes nickname of a user
  "clear"                    :: Clear messages, accepts amount defaults to 10
  "poll"                     :: Start a poll. Example: pp poll "is SovietBot amazing?" "yes" "YES in capital" "option 1 and 2"
  "comeback"                 :: Time for a good comeback
  "nuke"                     :: Deletes all the messages in a text channel
  "tripo"                    :: Tripoloski babyyyyy
  "gif"                      :: Get a random gif based on a search term; Example: pp gif dancing dog. Leave search term black for trending gifs
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