# imports and extensions
import discord
from discord.ext import commands

# loading token
with open('token.txt') as file:
    token = file.readlines()

# bot declaration
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# ready-message
@bot.event
async def on_ready():
    print(f'{bot.user} is now online! TicTacToe')
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

class start_button(discord.ui.View):
    def __init__(self, player1_id, **kwargs):
        super().__init__(**kwargs)
        self.player1_id = player1_id

    @discord.ui.button(custom_id="challenge_start_button", label="I want to play!", style=discord.ButtonStyle.grey, row=1, emoji="<a:haken:1024262765721948251>")
    async def challenge_start_callback(self, interaction:discord.Interaction, button):
        player1 = await bot.fetch_user(self.player1_id)
        player2 = interaction.user

        # Update the message with the new embed mentioning both players
        embed_challenge_accept = discord.Embed(
            title="TTT-Game started",
            description=f"{player1.mention} is playing against {player2.mention} \n\n",
            color=embedGamesColour
        )

        # Update the message with the new embed
        await interaction.message.edit(embed=embed_challenge_accept, view=None)
        #Neue Nachricht + 9 Buttons
        winner = await gameStart(interaction, player1, player2)

        #await interaction.edit_original_response(despcription=f"{player1.mention} vs. {player2.mention} \n\n{winner} won the game!")
        
async def gameStart(interaction:discord.Interaction, player1:discord.Interaction.user, player2:discord.Interaction.user):
    #sendMsg + Buttons
    #startEmbed + Button -> User drückt -> Nachricht edit + Id -> Neue Nachricht mit Game (ID nötig)
    currentGame = f"{player1.mention} is currently playing against {player2.mention} \n\nIt's {player1.mention}'s turn"
    gameEmbed = discord.Embed(
            title="TTT-Game",
            description=f"{currentGame}",
            color=embedGamesColour
        )
    await interaction.channel.send(embed=gameEmbed)


    #return winner

async def startEmbed(interaction: discord.Interaction):
    player1 = interaction.user
    embedStart = discord.Embed(
        title="TTT-Game search",
        description=f"{player1.mention} wants to play a TicTacToe game.\nWho wants to play against {player1.mention}",
        color=embedGamesColour
    )
    return embedStart

@bot.tree.command(name="tictactoe", description="TicTacToe")
async def ttt(interaction: discord.Interaction):
    # Get the user who triggered the slash command
    player1 = interaction.user
    startEmbedMessage = await startEmbed(interaction)
    await interaction.response.send_message(embed=startEmbedMessage, view=start_button(player1.id))
    print(f"Player 1 - ttt: {player1}")

# running bot with token
bot.run(token[0])