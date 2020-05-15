import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to discord')
    guild = discord.utils.get(client.guilds, name=GUILD)
    
    print(f'{guild.name}')
    members = "\n - ".join([members.name for members in guild.members])
    total = guild.member_count
    # print(f'Server members: \n {members}')
    print(f'total members are: {total}')

client.run(TOKEN)