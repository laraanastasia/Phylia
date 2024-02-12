import datetime
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!",intents = discord.Intents.all())

mainColour = 0xa2c188
embedGamesColour = 0xd9a4fc

class start_button(discord.ui.View):
    def __init__(self, player1, **kwargs):
        super().__init__(**kwargs)
        self.player1 = player1
        self.player2 = None
        self.message = None
        self.current_player = None

    @discord.ui.button(custom_id="challenge_start_button", label="I want to play!", style=discord.ButtonStyle.grey, row=1, emoji="<a:haken:1024262765721948251>")
    async def challenge_start_callback(self, interaction:discord.Interaction, button):
        player1 = self.player1
        if interaction.user != player1:
            self.player2 = interaction.user
            self.current_player = player1
            player2 = interaction.user

            self.message = interaction.message

            embed_challenge_accept = await startEmbed(player1)
            embed_challenge_accept.description = f":green_circle: {player1.mention} (X) is playing against :blue_circle: {player2.mention} (O)"

            
            await interaction.message.edit(embed=embed_challenge_accept, view=None)
            gameField = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            embedGame = await gameEmbed(player1)
            await interaction.channel.send(f"It's {player1.mention}'s turn.", embed=embedGame, view=TicTacToe(player1, player2, gameField))
        else:
            await interaction.response.send_message(":confused: You can't play against yourself. I am sorry!", ephemeral=True)


class TicTacToe(discord.ui.View):
    def __init__(self, player1, player2, gameField, **kwargs):
        super().__init__(**kwargs)
        self.player1 = player1
        self.player2 = player2
        self.gameField = gameField
        self.current_player = player1
        
        for i in range(1, 10):
            button = discord.ui.Button(custom_id=str(i), label="‎", style=discord.ButtonStyle.secondary, row=(i - 1) // 3)
            self.add_item(button)
            button.callback = lambda interaction, button=button: self.button_callback(interaction, button)

    #function get triggered on button-click
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        player1 = self.player1
        player2 = self.player2
        current_player = self.current_player

        if interaction.user == current_player:
            newView = await self.update_game_field(button, 1 if interaction.user == player1 else 2)
            winner = await self.check_winner()
            if winner == player1 or winner == player2:
                winEmbedMessage = await winEmbed(winner, player1 if winner == player2 else player2)
                await interaction.response.edit_message(content=None, embed=winEmbedMessage, view=newView)
            elif winner == "NoWinner":
                embedTieMessage = await tieEmbed(player1, player2)
                await interaction.response.edit_message(content=None, embed=embedTieMessage, view=newView)
            else:
                next_player = player2 if current_player == player1 else player1
                embedGameMessage = await gameEmbed(next_player)
                await interaction.response.edit_message(content=next_player.mention, embed=embedGameMessage, view=newView)
                self.current_player = next_player
        elif interaction.user == player1 or interaction.user == player2:
            await interaction.response.send_message(":confused: It's not your turn.", ephemeral=True)
        else:
            await interaction.response.send_message("It's not your game. Start your own one with `/tictactoe`", ephemeral=True)

    async def update_game_field(self, button, player):
        gameField = self.gameField
        index = int(button.custom_id) - 1
        if gameField[index] == 0:
            gameField[index] = player
            button.disabled = True
            button.label = "X" if player == 1 else "O"
            button.style = discord.ButtonStyle.green if player == 1 else discord.ButtonStyle.blurple
        return self

    async def check_winner(self):
        player1 = self.player1
        player2 = self.player2
        gameField = self.gameField

        #check horizonatal, vertical and diagonal
        for i in range(0, 9, 3):
            if gameField[i] == gameField[i + 1] == gameField[i + 2] != 0:
                return player1 if gameField[i] == 1 else player2
        for i in range(3):
            if gameField[i] == gameField[i + 3] == gameField[i + 6] != 0:
                return player1 if gameField[i] == 1 else player2
        if gameField[0] == gameField[4] == gameField[8] != 0:
            return player1 if gameField[0] == 1 else player2
        if gameField[2] == gameField[4] == gameField[6] != 0:
            return player1 if gameField[2] == 1 else player2
        
        #check tie
        full = True
        for i in range(9):
            if gameField[i] == 0:
                full = False
        if full:
            return "NoWinner"
        else:
            return None

#return embed of current game
async def gameEmbed(userToMention: discord.User):
    embedGame = discord.Embed(
        title=f"Current game:",
        description=f"It's {userToMention.mention}'s turn.",
        color=embedGamesColour
    )
    return embedGame

#return embed of tie
async def tieEmbed(player1: discord.User, player2: discord.User):
    embedTie = discord.Embed(
        title=f"There is no winner!",
        description=f"In the game: \n**{player1} vs. {player2}**\nis no winner.",
        color=embedGamesColour
    )
    embedTie.set_thumbnail(url="https://cdn.discordapp.com/attachments/1029502275208630414/1032604347793682492/blobWooble.gif?ex=65cdea3d&is=65bb753d&hm=fcb98ecfca500cbeef4fa6ab27c42bfe49042b02a8e2bbcd66d519a1ca6da581&")
    embedTie.set_footer(text="Use /tictactoe to start a new game.", icon_url="https://cdn.discordapp.com/attachments/1203830894050279435/1203831134522449920/Branding_Raged_alles_voll_2.png?ex=65d2861c&is=65c0111c&hm=eb56193f240d629c4e5e26810f85224801047c152164d5a4fcdcc15618d741ae&")
    return embedTie

#return embed of win
async def winEmbed(winner: discord.User, looser: discord.User):
    embedWin = discord.Embed(
        title=f"The Winner is {winner} !",
        description=f"{winner.mention} won the game against {looser.mention} !",
        color=embedGamesColour
    )
    embedWin.set_thumbnail(url="https://cdn.discordapp.com/attachments/1029502275208630414/1032604402202189844/tadaa.gif?ex=65cdea4a&is=65bb754a&hm=3ade322bbf2c1fe6edb8ecba0961e0b11697c1100dd1d1b0e15f5ee32c7aba08&")
    embedWin.set_footer(text="Use /tictactoe to start a new game.", icon_url="https://cdn.discordapp.com/attachments/1203830894050279435/1203831134522449920/Branding_Raged_alles_voll_2.png?ex=65d2861c&is=65c0111c&hm=eb56193f240d629c4e5e26810f85224801047c152164d5a4fcdcc15618d741ae&")
    return embedWin

#return embed of game request
async def startEmbed(player1: discord.user):
    embedStart = discord.Embed(
        title="TTT-Game search",
        description=f"{player1.mention} wants to play a TicTacToe game.\nWho wants to play against {player1.mention}",
        color=embedGamesColour,
        timestamp=datetime.datetime.now()
    )
    return embedStart

async def ttt(interaction: discord.Interaction):
    player1 = interaction.user
    startEmbedMessage = await startEmbed(player1)
    start_button_view = start_button(player1)
    await interaction.response.send_message(embed=startEmbedMessage, view=start_button_view)