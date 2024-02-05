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
    print(f'{bot.user} is now online! - Rock Paper Scissors')
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
rockEmoji = "https://cdn.discordapp.com/attachments/1203830894050279435/1204024973631553567/HcwAAAAASUVORK5CYII.png?ex=65d33aa3&is=65c0c5a3&hm=e9b5915f5b929d960f0cded66f9079ee7a15be25a06c7bc0c535cbd8d03edd20&"
paperEmoji = "https://cdn.discordapp.com/attachments/1203830894050279435/1204026198775300147/fAHap1cbW0NmmcB0RhFBzDIWG2saZmjV8lyneVClDEhPTaHYzxaDTCuNNuNsctXSlLZVnTIDSMhkezkDh2Po0KoCniR19ayz6CGoiEICqGGtJPFF4Q9JV2QZAAChhvpLjx63JPLVvPoUSHHWiNOXjestGoMBhEgG1ROCpPA3olSHpmHA4dJzg1UaEuZ3cyxTLIXQ6DqMxGG6oq7l7ZaNITJN0xAzgszH6cKz3CA5bmPCHFvNt0nhFCcOX3jEn2l2WCWUBiKUJu9ZGoYx2Ud3gxXQ3HyECARY3vyE8Yix7e7qnqZAtdD8cvknAvve4UUReVGcaO4UfyRLSQ16DhmriwAAAAAElFTkSuQmCC.png?ex=65d33bc7&is=65c0c6c7&hm=c0ef1f38e27d97c0f2263256a867088256c992f0e4deb6e514299428f893cac0&"
scissorsEmoji = "https://cdn.discordapp.com/attachments/1203830894050279435/1204025557558497380/jd80ftP42fgbvxdrliNRoxAAAAAASUVORK5CYII.png?ex=65d33b2e&is=65c0c62e&hm=72bc21d085be27593d86d09672476fc794f0792364422fd4060d858ade339114&"

@bot.tree.command(name="rock-paper-scissors", description="rock-paper-scissors")
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

# running bot with token
bot.run(token[0])