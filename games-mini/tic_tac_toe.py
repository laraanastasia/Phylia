import discord
import os
from discord.ext import commands
from discord import app_commands

print("---Speicherort:", os.getcwd())

with open('token.txt') as file:
    token = file.readlines()

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now purring!')
    status = discord.CustomActivity("p!help or /help")
    await bot.change_presence(status=discord.Status.online, activity=status)
    print(f"Status set to: {status}!")

    try:
        synced = await bot.tree.sync()
        print (f"Synced {len (synced)} command(s)")
    except Exception as e:
        
        print(e)
    
    user = await bot.fetch_user("721404393664020560")
    await user.send("Hello there, I am online now!")

mainColour = 0xa2c188
embedGamesColour = 0xF5E6FE

@bot.tree.command (name="tictactoe", description="TicTacToe")
async def ttt(interaction: discord.Interaction):
    embedTTT=discord.Embed(title="TTT-Game started", description=f"{interaction.user.mention} want's to play a TicTacToe game. \nWho want's to play against {interaction.user.mention}", color=embedGamesColour)
    embedTTT.add_field(name="Field 1", value="bla bla bla", inline=True)
    await interaction.response.send_message(embed=embedTTT)
    await interaction.channel.send(embed=embedTTT); return

async def checkWin(activPlayer, ):

    return

bot.run(token[0])