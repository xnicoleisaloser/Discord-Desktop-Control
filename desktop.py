import discord
import pyscreenshot as ImageGrab
import os
from pynput import mouse, keyboard
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("Discord Desktop Control System Initialized")
    
@client.event
async def on_message(message):
    if message.author != client.user:
        return

    if message.content.startswith('help'):
        await message.channel.send("""
>>> Included here are a list of all available commands:
**!viewscreen**: Sends the user a screenshot of their current desktop
**!left_click**: Clicks the left mouse button
**!right_click**: Clicks the right mouse button
**!left_click_hold**: Clicks the left mouse button until told to release
**!left_click_release**: Release the left mouse button
**!right_click_hold**: Clicks the right mouse button until told to release
**!right_click_release**: Releases the right mouse button
**!send_mouse_pos**: Sends the current mouse position
**!mouse_pos x y**: Sets the mouse position to provided cordinates
**!type "text"**: Types out provided text
**!press "key"**: Presses a specific keyboard key
**!press_and_hold "key"**: Presses a specific keyboard key until told to release
**!release "key"**: Release specified key
""")

    if message.content.startswith('!viewscreen'):
        im = ImageGrab.grab()
        im.save('screenshot.png')
        await message.channel.send(file=discord.File('screenshot.png'))
        os.remove("screenshot.png")

    if message.content.startswith('!left_click'):
        from pynput.mouse import Button, Controller
        mouse = Controller()
        mouse.press(Button.left)
        mouse.release(Button.left)

    if message.content.startswith('!right_click'):
        from pynput.mouse import Button, Controller
        mouse = Controller()
        mouse.press(Button.right)
        mouse.release(Button.right)

    if message.content.startswith('!left_click_hold'):
        from pynput.mouse import Button, Controller
        mouse = Controller()
        mouse.press(Button.left)

    if message.content.startswith('!left_click_release'):
        from pynput.mouse import Button, Controller
        mouse = Controller()
        mouse.release(Button.left)

    if message.content.startswith('!right_click_hold'):
        from pynput.mouse import Button, Controller
        mouse = Controller()
        mouse.press(Button.right)

    if message.content.startswith('!right_click_release'):
        from pynput.mouse import Button, Controller
        mouse = Controller()
        mouse.release(Button.right)
    
    if message.content.startswith('!send_mouse_pos'):
        from pynput.mouse import Button, Controller
        mouse = Controller()
        await message.channel.send(mouse.position)

       
        





client.run('big boy token', bot=False)
