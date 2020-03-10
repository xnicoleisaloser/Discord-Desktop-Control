import subprocess
import discord

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("Discord SSH dSystem Initialized")
    
@client.event
async def on_message(message):
    if message.author != client.user:
        return

    if message.content.startswith('!cmd'):
        await message.channel.send('Please ')





client.run('super secret big boy tokenn')
