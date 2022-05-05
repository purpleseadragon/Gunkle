import discord
import os
import random


client = discord.Client()
country_name = 'Invalid'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    """Function for text commands that require responses"""
    global country_name
    
    if message.author == client.user:
        return

    if message.content.startswith('$country'):
        # uploads random meme from folder
        random_country=random.choice(os.listdir("countries"))
        country_name = random_country[:-4]
        await message.channel.send(file=discord.File(f'countries\{random_country}'))
    
    if message.content.startswith('$country'):
        await message.channel.send(f'Try guess this country!')

    elif message.content.lower().startswith(country_name.lower()):
        author_id = message.id
        country_name = 'Invalid'
        await message.channel.send(f'You were correct {author_id}')

with open('token') as token:
    TOKEN = token.readlines()[0]

client.run(TOKEN)
