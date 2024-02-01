# imports and extensions
import discord
from discord.ext import commands
import discord
import random

# loading token
with open('token.txt') as file:
    token = file.readlines()

# bot declaration
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# ready-message
@bot.event
async def on_ready():
    print(f'{bot.user} is now online!')
    status = discord.CustomActivity("Ich werde gerade programmiert ._.")
    await bot.change_presence(status=discord.Status.online, activity=status)
    print(f"Status set to: {status}!")

    try:
        synced = await bot.tree.sync()
        print(f"Currently listening to {len(synced)} command(s).")
    except Exception as e:
        print(e)

mainColour = 0xa2c188
embedGamesColour = 0xd9a4fc

@bot.tree.command(name="rock-paper-scissors", description="rock-paper-scissors")
async def playRPS(interaction:discord.Interaction, choice: str):
        choices = ["rock", "paper", "scissors"]
        bot_choice = random.choice(choices)

        if choice.lower() not in choices:
            await interaction.response.send_message("Invalid choice. Please choose rock, paper, or scissors.")
            return

        if choice.lower() == bot_choice:
            await interaction.response.send_message(f"It's a tie! Both chose {choice}.")
        elif (choice.lower() == "rock" and bot_choice == "scissors") or \
             (choice.lower() == "paper" and bot_choice == "rock") or \
             (choice.lower() == "scissors" and bot_choice == "paper"):
            await interaction.response.send_message(f"You win! {choice.capitalize()} beats {bot_choice}.")
        else:
            await interaction.response.send_message(f"You lose! {bot_choice.capitalize()} beats {choice}.")

# running bot with token
bot.run(token[0])