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
        self.player2 = None

    @discord.ui.button(custom_id="challenge_start_button", label="I want to play!", style=discord.ButtonStyle.grey, row=1, emoji="<a:haken:1024262765721948251>")
    async def challenge_start_callback(self, interaction:discord.Interaction, button):
        player1 = await bot.fetch_user(self.player1_id)
        self.player2 = interaction.user  # Set the player2 property here
        player2 = interaction.user

        # Update the message with the new embed mentioning both players
        embed_challenge_accept = discord.Embed(
            title="TTT-Game started",
            description=f"{player1.mention} is playing against {player2.mention} \n\n",
            color=embedGamesColour
        )

        # Update the message with the new embed
        await interaction.message.edit(embed=embed_challenge_accept, view=None)
        # Neue Nachricht + 9 Buttons
        gameField = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        await self.send_game_start_message(interaction.channel, player1, player2, gameField)

    async def send_game_start_message(self, channel, player1, player2, gameField):
        await channel.send("Game started", view=TicTacToe(player1, player2, gameField))


class TicTacToe(discord.ui.View):
    def __init__(self, player1, player2, gameField, **kwargs):
        super().__init__(**kwargs)
        self.player1 = player1
        self.player2 = player2
        self.gameField = gameField

        # Create 9 buttons
        for i in range(1, 10):
            button = discord.ui.Button(custom_id=str(i), label=str(i), style=discord.ButtonStyle.secondary, row=(i - 1) // 3)
            print(f"Button {i} created: {button}")
            self.add_item(button)
            button.callback = lambda interaction, button=button: self.button_callback(interaction, button)


    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        print(f"Button_callback {button.custom_id} was clicked by {interaction.user}")
        player1 = self.player1
        player2 = self.player2
        print(f"Player 1 - button_callback: {player1}")
        print(f"Player 2 - button_callback: {player2}")
        gameField = self.gameField

        if interaction.user == player1 or interaction.user == player2:
            newView = await self.update_game_field(button, 1 if interaction.user == player1 else 2)
            await interaction.response.edit_message(view=newView)
            winner = await self.check_winner()
            if winner:
                await interaction.channel.send(f"{winner.mention} won the game!")
            else:
                await interaction.channel.send("Next player's turn.")

    async def update_game_field(self, button, player):
        gameField = self.gameField
        index = int(button.custom_id) - 1
        if gameField[index] == 0:
            gameField[index] = player
            button.label = "X" if player == 1 else "O"
            button.style = discord.ButtonStyle.green
        return self

            # await button.edit(label="X" if player == 1 else "O", style=discord.ButtonStyle.green)

    async def check_winner(self):
        player1 = self.player1
        player2 = self.player2
        gameField = self.gameField
        # Check horizontal rows
        for i in range(0, 9, 3):
            if gameField[i] == gameField[i + 1] == gameField[i + 2] != 0:
                return player1 if gameField[i] == 1 else player2

        # Check vertical rows
        for i in range(3):
            if gameField[i] == gameField[i + 3] == gameField[i + 6] != 0:
                return player1 if gameField[i] == 1 else player2

        # Check diagonal rows
        if gameField[0] == gameField[4] == gameField[8] != 0:
            return player1 if gameField[0] == 1 else player2
        if gameField[2] == gameField[4] == gameField[6] != 0:
            return player1 if gameField[2] == 1 else player2

        return None

    async def buttonUpdate(self, id, label, style, row):
        @discord.ui.button(custom_id=id, label=label, style=style, row=row)
        async def callback(button, interaction):
            print("Button clicked")

        for i in range(1, 10):
            i = discord.ui.Button(style=discord.ButtonStyle.secondary, label=str(i), custom_id=str(i))
            self.add_item(i)
            i.callback = lambda i: self.button_callback(i)

    async def update_game_field(self, button, player):
        gameField = self.gameField
        index = int(button.custom_id) - 1
        if gameField[index] == 0:
            gameField[index] = player
            button.label = "X" if player == 1 else "O"
            button.style = discord.ButtonStyle.green
        return self
            # button(label="X" if player == 1 else "O", style=discord.ButtonStyle.green)
            # await self.update()
            # return await interaction.response.edit_message(view=self)
            # await button.edit(label="X" if player == 1 else "O", style=discord.ButtonStyle.green)

    async def check_winner(self):
        player1 = self.player1
        player2 = self.player2
        gameField = self.gameField
        # Check horizontal rows
        for i in range(0, 9, 3):
            if gameField[i] == gameField[i + 1] == gameField[i + 2] != 0:
                return player1 if gameField[i] == 1 else player2

        # Check vertical rows
        for i in range(3):
            if gameField[i] == gameField[i + 3] == gameField[i + 6] != 0:
                return player1 if gameField[i] == 1 else player2

        # Check diagonal rows
        if gameField[0] == gameField[4] == gameField[8] != 0:
            return player1 if gameField[0] == 1 else player2
        if gameField[2] == gameField[4] == gameField[6] != 0:
            return player1 if gameField[2] == 1 else player2

        return None

async def buttonUpdate(self, id, label, style, row):
    @discord.ui.button(custom_id=id, label=label, style=style, row=row)
    async def callback(button, interaction):
        print("Button clicked")

    return callback if self.player2 is not None else None


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

    start_button_view = start_button(player1.id)  # Create the view
    await interaction.response.send_message(embed=startEmbedMessage, view=start_button_view)
    
    player2 = start_button_view.player2  # Get the player2 property
    gameField = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # Initialize the game field
    # await interaction.channel.send("TTT-Game started", view=TicTacToe(player1, player2, gameField))
    print(f"Player 1 - ttt: {player1}")
    print(f"Player 2 - ttt: {player2}") #muss noch None sein

# running bot with token
bot.run(token[0])