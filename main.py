import discord
import os
import random


client = discord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    """Function for text commands that require responses"""
    global help
    if message.author == client.user:
        return

    elif message.content.startswith('$country'):
        # uploads random meme from folder
        random_country=random.choice(os.listdir("countries"))
        country_name = random_country[:]
        await message.channel.send(file=discord.File(f'countries\{random_country}'))


with open('token') as token:
    TOKEN = token.readlines()[0]

client.run(TOKEN)
