#############################################################################################################
#############################################################################################################
#############################################################################################################
######                                                                                                 ###### 
######      For questions concerning the lecture plan pls contact @alex1401 on discord                 ######
######                                                                                                 ######
#############################################################################################################
#############################################################################################################
#############################################################################################################
import discord
import discord
import random
import datetime

def password(length):
    all = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!%&/><+-()@"
    password = ""
    for _ in range(length):
        password += random.choice(all)
    return password

# creating a list with number (= dice)
dice = [1,2,3,4,5,6]

# getting random number
def roll():
    global choice
    choice = random.choice(dice)
    return choice

def dice_embed(choice):
    embed = discord.Embed(
                            title = f"**Congratulations!**",
                            
                            description="\n\n",
                            color=0xD9A4FC        
                            )
   # embed.add_field(name="┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄",value='',inline=True)
    embed.add_field(name="",value=f"You rolled a **{choice}**.", inline=False)
    embed.set_footer(text="Don't get addicted to gambling!",icon_url="https://cdn.discordapp.com/attachments/909054108235862066/1178115964152328232/guycoding.png?ex=65beccfe&is=65ac57fe&hm=e434044069bea56e66c39fd651e713d7f189e84f069ad0f9ea89c98a012eaaac&")
    if choice == 1:
        embed.set_image(url="https://cdn.discordapp.com/attachments/909054108235862066/1202171813098950656/number1-removebg-preview.png?ex=65cc7cbf&is=65ba07bf&hm=31836eb32da9b1d6f80bcda940577a74b8dd17f3af5f35426ee63bbecd4791f0&")
    elif choice == 2:
        embed.set_image(url="https://cdn.discordapp.com/attachments/909054108235862066/1202171830148792340/number2-removebg-preview.png?ex=65cc7cc3&is=65ba07c3&hm=f1f4cb3d6160bbbe8d29e03fcfe74b782d7c3b03e2bb8a71edb5d706d61d85bd&")
    elif choice == 3:
        embed.set_image(url="https://cdn.discordapp.com/attachments/909054108235862066/1202171841477886003/number3-removebg-preview.png?ex=65cc7cc6&is=65ba07c6&hm=0afacac458988eaac37c3c35a1bbc13d93ce45e05cf21c69072b3453e8f72214&") 
    elif choice == 4:
        embed.set_image(url="https://cdn.discordapp.com/attachments/909054108235862066/1202171851271311361/number4-removebg-preview.png?ex=65cc7cc8&is=65ba07c8&hm=a006d03c33b57486ed91a9ffb1198246b077b1819cfa3a77809176291b0a9618&")
    elif choice == 5:
        embed.set_image(url="https://cdn.discordapp.com/attachments/909054108235862066/1202171860662362192/number5-removebg-preview.png?ex=65cc7cca&is=65ba07ca&hm=5386665b5dd676e26e82019e15bb02db01812901a00b546471cdff7bcdf2ccdd&")
    elif choice == 6:
        embed.set_image(url="https://cdn.discordapp.com/attachments/909054108235862066/1202171964614262804/imagenew-removebg-preview.png?ex=65cc7ce3&is=65ba07e3&hm=e9ab0a94116d385f978c64cb95390217055ab9741a0a5251a330a612eeef4a31&")
    return embed
#############################################################################################################
#############################################################################################################
#############################################################################################################
######                                                                                                 ###### 
######      For questions concerning the lecture plan pls contact @ragednicmaster on discord           ######
######                                                                                                 ######
#############################################################################################################
#############################################################################################################
#############################################################################################################
# Tic Tac Toe
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

# rock paper scissor
    
mainColour = 0xa2c188
embedGamesColour = 0xd9a4fc
rockEmoji = "https://cdn.discordapp.com/attachments/1203830894050279435/1204024973631553567/HcwAAAAASUVORK5CYII.png?ex=65d33aa3&is=65c0c5a3&hm=e9b5915f5b929d960f0cded66f9079ee7a15be25a06c7bc0c535cbd8d03edd20&"
paperEmoji = "https://cdn.discordapp.com/attachments/1203830894050279435/1204026198775300147/fAHap1cbW0NmmcB0RhFBzDIWG2saZmjV8lyneVClDEhPTaHYzxaDTCuNNuNsctXSlLZVnTIDSMhkezkDh2Po0KoCniR19ayz6CGoiEICqGGtJPFF4Q9JV2QZAAChhvpLjx63JPLVvPoUSHHWiNOXjestGoMBhEgG1ROCpPA3olSHpmHA4dJzg1UaEuZ3cyxTLIXQ6DqMxGG6oq7l7ZaNITJN0xAzgszH6cKz3CA5bmPCHFvNt0nhFCcOX3jEn2l2WCWUBiKUJu9ZGoYx2Ud3gxXQ3HyECARY3vyE8Yix7e7qnqZAtdD8cvknAvve4UUReVGcaO4UfyRLSQ16DhmriwAAAAAElFTkSuQmCC.png?ex=65d33bc7&is=65c0c6c7&hm=c0ef1f38e27d97c0f2263256a867088256c992f0e4deb6e514299428f893cac0&"
scissorsEmoji = "https://cdn.discordapp.com/attachments/1203830894050279435/1204025557558497380/jd80ftP42fgbvxdrliNRoxAAAAAASUVORK5CYII.png?ex=65d33b2e&is=65c0c62e&hm=72bc21d085be27593d86d09672476fc794f0792364422fd4060d858ade339114&"

async def playRPS(interaction:discord.Interaction, choice: str):
        choices = ["rock", "paper", "scissors"]
        bot_choice = random.choice(choices)

        if choice.lower() not in choices:
            await interaction.response.send_message("Invalid choice. Please choose `rock`, `paper`, or `scissors`.", ephemeral=True)
            return

        if choice.lower() == bot_choice:
            embedTie = discord.Embed(
                title=f"It's a tie!",
                description=f"Both chose `{choice.capitalize()}`.",
                color=embedGamesColour
            )
            if choice.lower() == "rock":
                embedTie.set_thumbnail(url=rockEmoji)
            elif choice.lower() == "paper":
                embedTie.set_thumbnail(url=paperEmoji)
            else:
                embedTie.set_thumbnail(url=scissorsEmoji)
            embedTie.set_footer(text="Use /rock-paper-scissors to start a new game.", icon_url="https://cdn.discordapp.com/attachments/1203830894050279435/1203831134522449920/Branding_Raged_alles_voll_2.png?ex=65d2861c&is=65c0111c&hm=eb56193f240d629c4e5e26810f85224801047c152164d5a4fcdcc15618d741ae&")
            await interaction.response.send_message(embed=embedTie)
        elif (choice.lower() == "rock" and bot_choice == "scissors") or \
             (choice.lower() == "paper" and bot_choice == "rock") or \
             (choice.lower() == "scissors" and bot_choice == "paper"):
            embedWin = discord.Embed(
                title=f"You win!",
                description=f"**{choice.capitalize()}** beats {bot_choice}.",
                color=embedGamesColour
            )
            if choice.lower() == "rock":
                embedWin.set_thumbnail(url=rockEmoji)
            elif choice.lower() == "paper":
                embedWin.set_thumbnail(url=paperEmoji)
            else:
                embedWin.set_thumbnail(url=scissorsEmoji)
            embedWin.set_footer(text="Use /rock-paper-scissors to start a new game.", icon_url="https://cdn.discordapp.com/attachments/1203830894050279435/1203831134522449920/Branding_Raged_alles_voll_2.png?ex=65d2861c&is=65c0111c&hm=eb56193f240d629c4e5e26810f85224801047c152164d5a4fcdcc15618d741ae&")
            await interaction.response.send_message(embed=embedWin)
        else:
            embedLoose = discord.Embed(
                title=f"You lose!",
                description=f"**{bot_choice.capitalize()}** beats {choice}.",
                color=embedGamesColour
            )
            if bot_choice.lower() == "rock":
                embedLoose.set_thumbnail(url=rockEmoji)
            elif bot_choice.lower() == "paper":
                embedLoose.set_thumbnail(url=paperEmoji)
            else:
                embedLoose.set_thumbnail(url=scissorsEmoji)
            embedLoose.set_footer(text="Use /rock-paper-scissors to start a new game.", icon_url="https://cdn.discordapp.com/attachments/1203830894050279435/1203831134522449920/Branding_Raged_alles_voll_2.png?ex=65d2861c&is=65c0111c&hm=eb56193f240d629c4e5e26810f85224801047c152164d5a4fcdcc15618d741ae&")
            await interaction.response.send_message(embed=embedLoose)


async def helpMsg(interaction: discord.Interaction):
    
    embed = discord.Embed(title="Command Overview",
                      colour=0xbe63f9,
                      timestamp=datetime.datetime.now())

    embed.set_author(name="Pyhlia - sister of Python ♡",
                    icon_url="https://cdn.discordapp.com/attachments/1203830894050279435/1204089467137163294/Pyhlia_Profilbild.png?ex=65d376b3&is=65c101b3&hm=3a54da6cf23cec4764a743f746922db2b35f8fc91936153f76c296fbd1a79db8&")

    embed.add_field(name="Lecture Plan",
                    value="**`/lecture`** - get the current lecture plan for INF23A on DHBW MOS as default.\nUse the _**awesome interaction-menu**_ to get the plan of ***other days***\n‎",
                    inline=False)
    embed.add_field(name="Weather",
                    value="**`/temperatur [plz]`** - get the weather for **today** and the weather forecast of the next **5 days**\n‎",
                    inline=False)
    embed.add_field(name="Tarot",
                    value="`/tarot` - Whats your destiny? - draw ***as many cards as you like***\n`/tarot_with_cards` - Whats your destiny? - draw ***up to 3 graphically displayed card's***\n‎",
                    inline=False)
    embed.add_field(name="Mini-Games",
                    value="**`/guess_the_number [start] [end]`** - guess a random number between *[start]* and *[end]*\n**`/rock_paper_scissors`** - make the right decision\n**`/roll_a_dice`** - roll a dice\n**`/start_counting`** - count up but stay concentrated :)\n**`/tic_tac_toe`** - play tic-tac-toe against another user",
                    inline=False)
    
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1203830894050279435/1204089467137163294/Pyhlia_Profilbild.png?ex=65d376b3&is=65c101b3&hm=3a54da6cf23cec4764a743f746922db2b35f8fc91936153f76c296fbd1a79db8&")
    embed.set_footer(text="INF23", icon_url="https://media.discordapp.net/attachments/1203830894050279435/1203831134522449920/Branding_Raged_alles_voll_2.png?ex=65d2861c&is=65c0111c&hm=eb56193f240d629c4e5e26810f85224801047c152164d5a4fcdcc15618d741ae&=&format=webp&quality=lossless&width=733&height=733")
    await interaction.response.send_message(embed=embed, ephemeral=True)