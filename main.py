# imports and extensions
from icalendar import Calendar
from datetime import date, datetime, timedelta
import discord
import discord.utils
from discord.ui import Button, View
from discord.ext import commands
import discord.utils
import lecturedata

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

# lecture command for getting todays lecture plan
@bot.tree.command(name="lecture")
async def lecture(interaction: discord.ui.Button):
    global lecturecounter
    lecturecounter = 0
    printing_lecture = lecturedata.lecture_data(date.today())
    global message    
    message = await interaction.response.send_message(embed=printing_lecture, view = lecturedata.embed_buttons())

# running bot with token
bot.run(token[0])