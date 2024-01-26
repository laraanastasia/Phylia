# imports and extensions
import discord
from discord.ext import commands
import tic_tac_toe

# loading token
with open('token.txt') as file:
    token = file.readlines()
    
# bot declaration
bot = commands.Bot(command_prefix="!",intents = discord.Intents.all())

# ready-message
@bot.event
async def on_ready():
    print("I am ready for work! ~Pyhlia")
    try:
        synced = await bot.tree.sync()
        print(f"Currently listening to {len(synced)} command(s).")
    except Exception as e:
        print(e)
    #user = await bot.fetch_user("721404393664020560")
    #await user.send("Hello there, I am online now!")


# running bot with token
bot.run(token[0])

