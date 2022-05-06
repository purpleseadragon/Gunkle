import discord
import os
import random
from score_update import print_leaderboard, updatecsv

client = discord.Client()
country_name = 'Invalid'
names_dict = {237337567534514176: 'Leo', 274757752398544899: 'Liam', 172980261192073217: 'Oscar', 852134374673088533: 'Khy', 358219168757317633: 'Zach'}

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
        author_id = message.author.id
        country_name = 'Invalid'
        updatecsv(author_id)
        await message.channel.send(f'You were correct {names_dict[author_id]}')

    if message.content.startswith('$leaderboard'):
        await message.channel.send(f'{print_leaderboard()}')

    author_id = message.author.id
    print(author_id)

with open('token') as token:
    TOKEN = token.readlines()[0]

client.run(TOKEN)
