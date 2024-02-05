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
    print(f"I am ready for work! ~{bot.user}")
    status = discord.CustomActivity("Use /help for help")
    await bot.change_presence(status=discord.Status.online, activity=status)
    print(f"Status set to: {status}")
    try:
        synced = await bot.tree.sync()
        print(f"Currently listening to {len(synced)} command(s).")
    except Exception as e:
        print(e)

@bot.tree.command(name="tictactoe", description="TicTacToe")
async def tttGame(interaction: discord.Interaction):
    await tic_tac_toe.ttt(interaction)

# running bot with token
bot.run(token[0])

