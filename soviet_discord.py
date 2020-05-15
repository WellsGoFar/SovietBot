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
    for guild in client.guilds:
        print(f'{guild.name}(id: {guild.id})')

client.run(TOKEN)