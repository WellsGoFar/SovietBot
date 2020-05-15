import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to discord')
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

client.run(TOKEN)