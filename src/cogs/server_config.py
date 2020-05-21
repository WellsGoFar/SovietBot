import discord 
from discord.ext import commands, tasks
import pymongo
import asyncio 

class server_config(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["tesdb"]
        self.mycol = self.mydb["testcollection"]

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="You don't have the permission required",
                colour = discord.Colour.blue())
            await ctx.channel.send(embed=embed)
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=1)
            

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        # mydb = myclient["tesdb"]
        # mycol = mydb["testcollection"]

        data = {'guildID': str(guild.id), 'nsfw_channel': '0', 'meme_channel': '0', 'facts_channel': '0', 'logs_channel': '0', 'welcome_message': 'Hello {user.name} welcome to {server.name}', 'exit_message': 'Sad to see you leave {user.name}'}
        x = self.mycol.insert_one(data)
        embed = discord.Embed(title = "Hello there! Thanks for adding me to your server. To get started type pp setup")
        for channel in guild.text_channels:
            await channel.send(embed=embed)
            break


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        myquery = { "guildID": str(guild.id) }
        self.mycol.delete_one(myquery) 


    @commands.command(name = 'update_welcome')
    @commands.has_permissions(administrator=True)
    async def update_welcome_message(self,ctx):
        id = str(ctx.guild.id)
        embed = discord.Embed(title = 'Enter a welcome message that you want your user to see when they enter the server:',
            description = "To mention a user type '{user.name}' and to mention the server name type '{server.name}'\n Example: 'Hello {user.name} welcome to {server.name}'") #change

        await ctx.send(embed = embed)
        try:
            msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout = 120.0)
        except asyncio.TimeoutError:
            await ctx.channel.purge(limit=1)
            return await ctx.send("oh heck, you waited too long. type 'pp setup' again to begin the setup process")          
        except Exception as e:
            return await ctx.send(e)

        myquery = {"guildID": id}
        newvalues = { "$set": { "welcome_message": msg.content } } #change
        self.mycol.update_one(myquery, newvalues)


    @commands.command(name='update_exit')
    @commands.has_permissions(administrator=True)
    async def update_exit_message(self,ctx):
        id = str(ctx.guild.id)
        embed = discord.Embed(title = 'Enter an exit message that you want to see when a user leaves the server:',
            description = "To mention a user type '{user.name}' and to mention the server name type '{server.name}'\n Example: 'Sad to see you go {user.name}'") #change

        await ctx.send(embed = embed)
        try:
            msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout = 120.0)
        except asyncio.TimeoutError:
            await ctx.channel.purge(limit=1)
            return await ctx.send("oh heck, you waited too long. type 'pp setup' again to begin the setup process")          
        except Exception as e:
            return await ctx.send(e)

        myquery = {"guildID": id}
        newvalues = { "$set": { "exit_message": msg.content } } #change
        self.mycol.update_one(myquery, newvalues)





    @commands.command()
    @commands.has_permissions(administrator=True)
    async def update_nsfw(self,ctx):

        channel = None
        # print('setup started: ', channel)
        id = str(ctx.guild.id)
        embed = discord.Embed(title = 'Copy and paste the exact name of the channel that you want nfsw on:', 
            description = "Enter 0 if you dont want a nsfw channel, 'skip' if you don't want to change the channel for nsfw. You can always change that later by using 'pp setup'") #change

        await ctx.send(embed = embed)
        try:
            msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout = 120.0)
        except asyncio.TimeoutError:
            await ctx.channel.purge(limit=1)
            await ctx.send("oh heck, you waited too long. type 'pp setup' again to begin the setup process")          
            return 1
        except Exception as e:
            return await ctx.send(e)
        guild = self.bot.get_guild(id=int(id))
        if msg.content == '0':
            myquery = {"guildID": id}
            newvalues = { "$set": { "nsfw_channel": '0' } } #change
            self.mycol.update_one(myquery, newvalues)
        elif msg.content == 'skip':
            return await ctx.send('nsfw skipped!')

        else:
            guild = self.bot.get_guild(id=int(id))
            for channel_g in guild.channels:
                if channel_g.name == msg.content:
                    channel = channel_g
                    break

            # await ctx.send('successfully updated nsfw channel')
            if(channel):
                myquery = {"guildID": id}
                newvalues = { "$set": { "nsfw_channel": str(channel.id) } } #change
                self.mycol.update_one(myquery, newvalues)
                await ctx.send('successfully updated nsfw channel') #change
            else:
                await ctx.send("**I couldn't find that channel. Check the spelling and try again, NSFW skipped for now, you can choose a channel for nsfw by typing 'pp update_nsfw'**")
                await asyncio.sleep(3.0)
            return 





    @commands.command()
    @commands.has_permissions(administrator=True)
    async def update_meme(self,ctx):

        id = str(ctx.guild.id)
        channel = None
        embed = discord.Embed(title = 'Copy and paste the exact name of the channel that you want memes on:', 
            description = "Enter 0 if you dont want a meme channel, 'skip' if you don't want to change the channel for memes. You can always change that later by using 'pp setup'") #change

        await ctx.send(embed = embed) 
        try:
            msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout = 120.0) 
        except asyncio.TimeoutError:
            await ctx.channel.purge(limit=1)
            await ctx.send("oh heck, you waited too long. type 'pp setup' again to begin the setup process")
            return 1
        except Exception as e:
            return await ctx.send(e)

        guild = self.bot.get_guild(id=int(id))
        if msg.content == '0':
            myquery = {"guildID": id}
            newvalues = { "$set": { "meme_channel": '0' } } #change
            self.mycol.update_one(myquery, newvalues)
            return 
        elif msg.content == 'skip':
            return await ctx.send('meme skipped!')
        else:
            # guild = self.bot.get_guild(id=int(id))
            for channel_g in guild.channels:
                if channel_g.name == msg.content:
                    channel = channel_g
                    break
            # await ctx.send('successfully updated nsfw channel')
            if channel:
                myquery = {"guildID": id}
                newvalues = { "$set": { "meme_channel": str(channel.id) } } 
                self.mycol.update_one(myquery, newvalues)
                await ctx.send('successfully updated meme channel') 
            else:
                await ctx.send("**I couldn't find that channel. Check the spelling and try again, memes skipped for now, you can choose a channel for memes by typing 'pp update_meme'**")
                await asyncio.sleep(3.0)

            return


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def update_facts(self,ctx):
        
        channel = None
        id = str(ctx.guild.id)
        embed = discord.Embed(title = 'Copy and paste the exact name of the channel that you want facts on:', 
            description = "Enter 0 if you dont want a facts channel, 'skip' if you don't want to change the channel for facts. You can always change that later by using 'pp setup'") #change

        await ctx.send(embed = embed) 
        try:
            msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout = 120.0) 
        except asyncio.TimeoutError:
            await ctx.channel.purge(limit=1)
            await ctx.send("oh heck, you waited too long. type 'pp setup' again to begin the setup process")          
            return 1
        except Exception as e:
            return await ctx.send(e)

        guild = self.bot.get_guild(id=int(id))
        if msg.content == '0':
            myquery = {"guildID": id}
            newvalues = { "$set": { "facts_channel": '0' } } #change
            self.mycol.update_one(myquery, newvalues)
            return 
        elif msg.content == 'skip':
            return await ctx.send('facts skipped!')
        else:
            # guild = self.bot.get_guild(id=id)
            for channel_g in guild.channels:
                if channel_g.name == msg.content:
                    channel = channel_g
                    break
            # await ctx.send('successfully updated nsfw channel')
            if channel:
                myquery = {"guildID": id}
                newvalues = { "$set": { "facts_channel": str(channel.id) } } #change
                self.mycol.update_one(myquery, newvalues)
                await ctx.send('successfully updated facts channel') #change
            else:
                await ctx.send("**I couldn't find that channel. Check the spelling and try again , facts skipped for now, you can choose a channel for facts by typing 'pp update_facts'**")
                await asyncio.sleep(3.0)
            return




    @commands.command()
    @commands.has_permissions(administrator=True)
    async def update_logs(self,ctx):


        id = str(ctx.guild.id)
        channel = None
        embed = discord.Embed(title = 'Copy and paste the exact name of the channel that you want logs on:', 
            description = "Enter 0 if you dont want a logs channel, 'skip' if you don't want to change the channel for logs. You can always change that later by using 'pp setup'") #change

        await ctx.send(embed = embed)
        try:
            msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout = 120.0) 
        except asyncio.TimeoutError:
            await ctx.channel.purge(limit=1)
            await ctx.send("oh heck, you waited too long. type 'pp setup' again to begin the setup process")  
            return 1
        except Exception as e:
            return await ctx.send(e)

        guild = self.bot.get_guild(id=int(id))
        if msg.content == '0':
            myquery = {"guildID": id}
            newvalues = { "$set": { "logs_channel": '0' } } #change
            self.mycol.update_one(myquery, newvalues)
            return
        elif msg.content == 'skip':
            return await ctx.send('logs skipped')
        else:
            # guild = self.bot.get_guild(id=id)
            for channel_g in guild.channels:
                if channel_g.name == msg.content:
                    channel = channel_g
                    break
            # await ctx.send('successfully updated nsfw channel')
            if channel:
                myquery = {"guildID": id}
                newvalues = { "$set": { "logs_channel": str(channel.id) } } #change
                self.mycol.update_one(myquery, newvalues)
                await ctx.send('successfully updated logs channel') #change
                
            else:
                await ctx.send("**I couldn't find that channel. Check the spelling and try again , logs skipped for now, you can choose a channel for logs by typing 'pp update_logs'**")
                await asyncio.sleep(3.0)

            return 
                


    @commands.command(help='config')
    @commands.has_permissions(administrator=True)
    async def setup(self,ctx):
        

        temp = await self.update_meme(ctx)
        if temp == 1:
            return 
        temp = 0
        temp = await self.update_nsfw(ctx)
        if temp == 1:
            return 
        temp = 0
        temp = await self.update_facts(ctx)
        if temp == 1:
            return 
        temp = 0
        temp = await self.update_logs(ctx)
        if temp == 1:
            return 

        embed = discord.Embed(title= "Setup complete, if you want custom Welcome and Exit messages type: 'pp update_welcome' and 'pp update_exit'",
            description = 'Enter pp help for more commands')
        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(server_config(bot))
