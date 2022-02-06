from distutils import command
from discord.ext import commands
import asyncio
import discord
from matplotlib.image import thumbnail

class help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        bot.remove_command('help')

    @commands.command()
    async def help(self, ctx, topic= "default"):
      if topic.lower() == "music":
        sb_music_commands = """
        **`play`**- Play a song
        **`search`**- Search for a song
        **`now`**- Get the currently playing song
        **`leave`**- Bot will leave the voice channel
        **`shuffle`**- Shuffle the queue
        **`queue`**- Displays the queue
        **`remove`**- Removes a song from the queue
        **`skip`**- Skip the current song
        **`pause`**- Pause the song
        **`resume`**- Resumes the song
        .
        """
        embed = discord.Embed(
                        colour = discord.Colour.red(),
                        description = sb_music_commands
                        )
        embed.set_author(name='SovietBot Music Commands',icon_url="https://i.imgur.com/JK0nuGV.jpg")
        embed.set_footer(text='For general and server commands use `pp help`and `pp help server`')
        await ctx.send(embed=embed)

      elif topic.lower() == "server":
        sb_server_commands = """
        **`setup`**- Add channels for periodic memes, facts and nsfw content
        **`update_meme`**- Change/add channel for memes
        **`update_nsfw`**- Change/add channel for nsfw
        **`update_logs`**- Change/add channel for server logs
        **`update_facts`**- Change/add channel for facts
        **`update_welcome`**- Change the message the bot sends when a new member joins the server
        **`update_exit`**- Change the message bot sends when a member leaves the server
        .
        """
        embed = discord.Embed(
                        colour = discord.Colour.red(),
                        description = sb_server_commands
                        )
        embed.set_author(name='SovietBot Server Commands',icon_url="https://i.imgur.com/JK0nuGV.jpg")
        embed.set_footer(text='For general and music commands use `pp help`and `pp help music`')
        await ctx.send(embed=embed)


      else:
        #https://imgur.com/JK0nuGV


        sb_default_commands = """
        **`hello`**- The bot will say hello to you because your friends won't
        **`changenick`**- Changes nickname of a user
        **`clear`**- Clear messages, accepts amount defaults to 10
        **`poll`**- Start a poll. Example: pp poll "is SovietBot amazing?" "yes" "YES in capital" "option 1 and 2"
        **`gif`**- Get a random gif based on a search term; Example: pp gif dancing dog. Leave search term black for trending gifs
        **`comeback`**- Time for a good comeback
        **`nuke`**- Deletes all the messages in a text channel
        **`simp`**- For when you come across a simp
        **`tripo`**- Tripoloski babyyyyy
        **`remindme`**- Reminds you with time duration mentioned; example: pp remindme 1h10m dance.
        **`activty/playing`**- Check what members of the server are playing a game; example: pp activity rainbow six
        .
        """
        embed = discord.Embed(
                        colour = discord.Colour.red(),
                        description = sb_default_commands,
                        set_thumbnail = "https://i.imgur.com/JK0nuGV.jpg"
                        )
        embed.set_author(name='SovietBot Commands',icon_url="https://i.imgur.com/JK0nuGV.jpg")
        embed.set_footer(text='For music and server commands use `pp help music`and `pp help server`')
        # embed.set_thumbnail(url="https://i.imgur.com/JK0nuGV.jpg")
        await ctx.send(embed=embed)


        
def setup(bot):
    bot.add_cog(help(bot))
