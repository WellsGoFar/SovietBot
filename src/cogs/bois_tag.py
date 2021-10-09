import discord
from datetime import datetime
from discord.ext import commands

class bois_tag(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.current_count = 0
        self.empty_time_start = datetime.now()
        # for server in self.bot.guilds:
        #     if server.id == 547139967529517059:
        #         self.guild = server
        # self.role = discord.utils.find(lambda r: r.name == 'bois', self.guild.roles)
        # self.text_channel = discord.utils.find(lambda c: c.name == 'spacestation', self.guild.text_channels)
        # self.bois = []
        # for member in self.guild.members:
        #     if self.role in member.roles:
        #         self.bois.append(member)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after): 
        try:
            if ((before.channel is not None and after.channel is None) or (before.channel.name is not "shadow realm" and after.channel.name is "shadow realm")) and self.role in member.roles:
                self.current_count = len(before.channel.members)
                if self.current_count == 0:
                    self.empty_time_start = datetime.now()
                    for boi in self.bois:
                        if boi.voice and boi.voice.channel.name != "shadow realm":
                            self.current_count = len(boi.voice.channel.members)
            
            if before.channel is None and after.channel is not None and self.current_count == 0 and (datetime.now() - self.empty_time_start).total_seconds() > 1800 and len(after.channel.members) == 1 and self.role in member.roles:
                await self.text_channel.send(self.role.mention + " " + member.name + " has joined " + after.channel.name + "...")
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(bois_tag(bot))