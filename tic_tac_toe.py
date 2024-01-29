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
    print(f'{bot.user} is now purring!')
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
        # Get the user who clicked the button (Player2)
        player2 = interaction.user

        # Get the information about the command initiator (Player1)
        player1 = await bot.fetch_user(self.player1_id)

        # Update the message with the new embed mentioning both players
        embed_challenge_accept = discord.Embed(
            title="TTT-Game started",
            description=f"<@{player1.id}> is playing against {player2.mention}",
            color=embedGamesColour
        )

        # Update the message with the new embed
        await interaction.message.edit(embed=embed_challenge_accept, view=None)


async def startTTT(interaction: discord.Interaction):
    player1 = interaction.user
    embedTTT = discord.Embed(
        title="TTT-Game search",
        description=f"{player1.mention} wants to play a TicTacToe game.\nWho wants to play against {player1.mention}",
        color=embedGamesColour
    )
    await interaction.response.send_message(embed=embedTTT, ephemeral=False, view=start_button(player1.id))
    return player1


@bot.tree.command(name="tictactoe", description="TicTacToe")
async def ttt(interaction: discord.Interaction):
    # Get the user who triggered the slash command
    startPlayer = interaction.user
    startMsg = await startTTT(interaction)


# running bot with token
bot.run(token[0])