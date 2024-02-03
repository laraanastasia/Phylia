# imports and extensions
import asyncio
from datetime import date, datetime, timedelta
import random
import discord
import discord.utils
from discord.ext import commands,tasks
import discord.utils
import lecturedata
import dice
import password_generator
from discord import Intents, Client,Message
import counting
import minigames
message = int


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
        regular_lecture.start()
        print(f"Currently listening to {len(synced)} command(s).")
    except Exception as e:
        print(e)

# lecture command for getting todays lecture plan
@bot.tree.command(name="lecture",description="Check the lecture plan!")
async def lecture(interaction: discord.ui.Button):
    global lecturecounter
    lecturecounter = 0
    printing_lecture = lecturedata.lecture_data(date.today())
    global message    
    message = await interaction.response.send_message(embed=printing_lecture, view = lecturedata.embed_buttons())

@bot.tree.command(name="roll-a-dice",description="You have a gambling addiction and love discord? Try both at the same time!")
async def rolladice(interaction:discord.Interaction):
  await interaction.response.send_message(embed=dice.dice_embed(dice.roll()))
# printing lecture plan of the next day ever 24 hours

@bot.tree.command(name="generate_password",description="Generate a password with the length of your choice!")
async def generatepassword(interaction: discord.Interaction,length :int):
    member = interaction.user
    try: 
            await member.send(password_generator.password(length))
            await interaction.response.send_message(f"Password has been sent to {member.global_name}.", ephemeral=True)
    except:
            await interaction.response.send_message(f"Wished password-length is too long, sorry :(",ephemeral = True)

     
@bot.tree.command(name="start_counting",description="Count up but stay concentrated :)")
async def start_counting(interaction:discord.Interaction):
        global exit2
        exit2 = 0
        channel_id = interaction.channel.id
        channel = bot.get_channel(channel_id)
        global author
        author = interaction.user
        await interaction.response.send_message("Count up from **1**. *Wrong answers have consequences...*")
        def check(message):
             return message.author and message.channel and message.content.isdigit()
        preNumber = 1
        while True:
                user_guess = await bot.wait_for('message', check=check,timeout=None)
                number = int(user_guess.content)
                if user_guess.author != author:
                    if number == preNumber + 1:
                        await user_guess.add_reaction("✅")
                        preNumber = number
                        author = user_guess.author
                    else:
                        await user_guess.add_reaction("❌")
                        preNumber = preNumber - 5
                        await channel.send(f"Uh ohhh, new number is **{preNumber}**. Fix your mistake <@{user_guess.author.id}> 😉")
                        if preNumber <= 0:
                            await channel.send(f"You lost...try again 😭")
                            exit2 = 1
                    if exit2 == 1:
                        break
                else: 
                     await channel.send("Not so greedy! This is a team-game.")
                        

@bot.tree.command(name="guess_the_number",description="Guess a number between 'start' and 'length'!")
async def guess_the_number(interaction:discord.Interaction,start: int, end:int):
        global exit 
        exit = 0
        channel_id = interaction.channel.id
        channel = bot.get_channel(channel_id)
        randNumber = random.randint(start, end)
        await interaction.response.send_message(f"Guess the number between {start} and {end}!")
        def check(message):
             return message.author and message.channel and message.content.isdigit()
        while True:
            try:
                user_guess = await bot.wait_for('message', check=check,timeout=30)
                guess = int(user_guess.content)
                if guess == randNumber:
                    await user_guess.add_reaction("✅")
                    exit = 1
                else:
                    await user_guess.add_reaction("❌")
                if exit == 1:
                    break
            except TimeoutError:
                await channel.send(f"You lose...the number was {randNumber}.")
                break

@tasks.loop(hours=24)
async def regular_lecture():
    # Get the current time
    now = datetime.now()
    # sends message when hour ist 18
    if now.hour == 18:
        channel_id = 1184076609779671111  
        channel = bot.get_channel(channel_id)
        try:    
                message = await channel.fetch_message(
                channel.last_message_id) 
                await message.delete()
        except Exception as e:
                print(e)
        await channel.send(embed=lecturedata.regular_data(date.today()+timedelta(days=1)))   
        print("done")


# running bot with token
bot.run(token[0])