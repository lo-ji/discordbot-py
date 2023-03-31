from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'call':
        await message.channel.send("callback!")

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
              message.channel.send('H222222')
        
    if message.content.startswith(f'{PREFIX}RandomNumber'):
        await message.channel.send(str(random.randrange(1,100))) 


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
