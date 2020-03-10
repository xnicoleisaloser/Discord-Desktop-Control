import discord
import pyscreenshot as ImageGrab

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("Discord Desktop Control System Initialized")
@client.event
async def on_message(message):
    if message.author != client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send('Included here are a list of all available commands:\n**!viewscreen**: Sends the user a screenshot of their current desktop')





client.run('super secret big boy tokenn')
