import discord
import re
from discord.ext import commands, tasks
from dotenv import load_dotenv
import asyncio
import pymongo

class ImDad(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
        self.mydb = self.myclient["tesdb"] 
        self.mycol = self.mydb["testcollection"]
        self.f_count = {}
        self.f_counts = {}
        self.update_server_f_counts.start()
        self.current = False
        
    def cog_unload(self):
        self.update_server_f_counts.cancel()

    def get_server_f_counts(self):
        for x in self.mycol.find():
            self.f_counts[x['guildID']] = x['f_count']
        return self.f_counts

    @tasks.loop(minutes=30.0)
    async def update_server_f_counts(self):
        try:
            for i in self.f_count:
                myquery = {"guildID": i}
                newvalues = { "$set": { "f_count": self.f_count[i] } } #change
                self.mycol.update_one(myquery, newvalues)
            self.f_counts.update(self.f_count)
            self.f_count = {}
        except Exception as e:
            print(e)

    # @commands.Cog.listener()
    # async def on_member_update(self,before,after):
    #     if after.id == 453110852908744706:
    #         # print('ashwin changed something')
    #         if str(before.nick) != str(after.nick):
    #             await after.edit(nick='racist boi')


    @commands.Cog.listener()
    async def on_message(self,message):

        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="pp help"))

        if message.author == self.bot.user or message.author.bot:
            return 

        cykaObj = re.compile(r'cyka', re.IGNORECASE)
        dadObj = re.compile(r'^im | ^i\'m | im | i\'m |i am ', re.IGNORECASE)
        if cykaObj.search(message.content):
            # print(message.channel)
            await message.channel.send("cyka blyat")

        if dadObj.search(message.content):
            dadName = message.content[(dadObj.search(message.content).span()[1]): ]
            nameCheck = re.compile(r'dad', re.IGNORECASE)
            if nameCheck.search(dadName):
                try:
                    granCheck = re.compile(r'gran', re.IGNORECASE)
                    gran_occ = re.findall(granCheck, message.content)
                    len_occ = len(gran_occ)
                    if len_occ > 9:
                        await message.channel.send('bro, this is just sad, you gotta get a life')
                    else:
                        msgg = f'Hi {dadName} I\'m ' +  (len_occ+1)*'gran' + 'dad'
                        await message.channel.send(msgg)
                except Exception as e:
                    await message.channel.send(e)
            
            else: 
                await message.channel.send(f'Hi {dadName}, I\'m dad')

        if message.content.lower() == 'f':
            try:
                if self.f_counts:
                    guildID = str(message.guild.id)
                    if guildID in self.f_count:
                        self.f_count[guildID] += 1
                    else:
                        self.f_count[guildID] = self.f_counts[guildID] + 1
                    await message.channel.send('Respects were paid {} times.'.format(self.f_count[guildID]))
                else:
                    self.f_counts = self.get_server_f_counts()
                    guildID = str(message.guild.id)
                    if guildID in self.f_count:
                        self.f_count[guildID] += 1
                    else:
                        self.f_count[guildID] = self.f_counts[guildID] + 1
                    await message.channel.send('Respects were paid {} times.'.format(self.f_count[guildID]))
            except Exception as e:
                await message.channel.send(e)

        # if message.content.lower() == 'bot no more':
        #     await message.channel.send('psych bitches bot is not dead')

        if message.content.lower() == 'st':
            if not message.channel.author.voice or not message.channel.author.voice.channel:
                await message.channel.send("You gotta connect to the Among Us voice channel dumbass")
            else:
                if not self.current:
                    self.current=True
                    try:
                        role = discord.utils.find(lambda r: r.name == 'AmongUs', message.guild.roles)
                        if role in message.author.roles or message.author.guild_permissions.administrator:
                            voice_channel = self.bot.get_channel(749156355688104036)
                            members = voice_channel.members
                            for member in members:
                                if member.id == 234395307759108106:
                                    continue
                                else:
                                    await member.edit(mute=True)
                                    await asyncio.sleep(0.1)
                            embed = discord.Embed(title="Have fun!")
                            await message.channel.send(embed = embed)
                        else:
                            await message.channel.send("You don't have the required role to use this command")
                    except Exception as e:
                        await message.channel.send(e)
                    self.current=False
            
        if message.content.lower() == 'sp':
            if not message.channel.author.voice or not message.channel.author.voice.channel:
                await message.channel.send("You gotta connect to the Among Us voice channel dumbass")
            else:
                if not self.current:
                    self.current=True
                    try:
                        role = discord.utils.find(lambda r: r.name == 'AmongUs', message.guild.roles)
                        if role in message.author.roles or message.author.guild_permissions.administrator:
                            voice_channel = self.bot.get_channel(749156355688104036)
                            members = voice_channel.members
                            for member in members:
                                await member.edit(mute=False)
                                await asyncio.sleep(0.1)
                            await message.channel.send("**Members unmuted**")
                        else:
                            await message.channel.send("You don't have the required role to use this command")
                    except Exception as e:
                        await message.channel.send(e)
                    self.current=False



        # await self.bot.process_commands(message)

    @update_server_f_counts.before_loop
    async def before_server_f_count_update(self):
        print('server update waiting...')
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(ImDad(bot))