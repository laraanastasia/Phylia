# imports and extensions
from datetime import date, datetime, timedelta
import discord
import discord.utils
from discord.ext import commands,tasks
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
        regular_lecture.start()
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

# printing lecture plan of the next day ever 24 hours
@tasks.loop(hours=24)
async def regular_lecture():
    # Get the current time
    now = datetime.now()
    # sends message when hour ist 18
    if now.hour == 22:
        channel_id = 1201958342990508043  
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