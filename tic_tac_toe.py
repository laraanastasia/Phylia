# imports and extensions
import discord
from discord.ext import commands

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

#for j in range(1,10):
#    print(j)

mainColour = 0xa2c188
embedGamesColour = 0xF5E6FE

class clickMe(discord.ui.View): # Create a class called clickMe that subclasses discord.ui.View
    @discord.ui.button(label="I want to play!", style=discord.ButtonStyle.grey, emoji="✅")
    async def button_callback(self, interaction:discord.Interaction, button):
        await interaction.message.edit()
        await interaction.response.send_message(f"{interaction.user.mention} clicked the button!") # Send a message when the button is clicked


@bot.tree.command (name="tictactoe", description="TicTacToe")
async def ttt(interaction: discord.Interaction):
    embedTTT=discord.Embed(title="TTT-Game started", 
                           description=f"{interaction.user.mention} want's to play a TicTacToe game. \nWho want's to play against {interaction.user.mention}", 
                           color=embedGamesColour)
    embedTTT.add_field(name="Field 1", value="bla bla bla", inline=True)
    await interaction.response.send_message(embed=embedTTT, ephemeral=False, view=clickMe())


# async def checkWin(activPlayer, ):

#     return

# async def checkPlayer():
#     #if input.user=activPlayer

# async def rightPlayer():
# async def wrongPlayer():

# async def renderField():
#     for j in range(1,10):
#         print(j)

# running bot with token
bot.run(token[0])