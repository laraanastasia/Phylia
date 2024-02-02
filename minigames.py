import asyncio
import discord
import random
from discord.ext import commands,tasks


bot = commands.Bot(command_prefix="!",intents = discord.Intents.all())

def guessing(interaction: discord.Interaction, start, end):
    channel_id = interaction.channel.id
    channel = bot.get_channel(channel_id)

    randNumber = random.randint(start, end)

    channel.send(f"Guess the number between {start} and {end}!")

    
    while True:
        def check(message):  
            return message.author and message.channel and message.content.isdigit()
        try:
            user_guess = bot.wait_for('message', check=check, timeout=30)
            guess = int(user_guess.content)
            if guess == randNumber:
                user_guess.add_reaction("✅")
                
            else:
                user_guess.add_reaction("❌")
        except TimeoutError:
            channel.send(f"You lose...the number was {randNumber}.")
            break