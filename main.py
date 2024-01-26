# imports and extensions
from icalendar import Calendar
from datetime import date, datetime, timedelta
import discord
import discord.utils
from discord.ui import Button, View
from discord.ext import commands
import discord.utils
import pytz
import requests
import pyhlia_lecture

# loading token
with open('token.txt') as file:
    token = file.readlines()

# bot declaration
bot = commands.Bot(command_prefix="!",intents = discord.Intents.all())
counter = 0
lecturecounter = 0

# ready-message
@bot.event
async def on_ready():
    print("I am ready for work! ~Pyhlia")
    try:
        synced = await bot.tree.sync()
        print(f"Currently listening to {len(synced)} command(s).")
    except Exception as e:
        print(e)

@bot.tree.command(name="lecture")
async def lecture(interaction: discord.ui.Button):
    print(datetime.today())
    printing_lecture = await lecture_data(date.today())
    await interaction.response.send_message(embed=printing_lecture)


# method called by buttonsclass (copied)
async def lecture_data(date_entry):
    cal_url = "https://stuv.app/MOS-TINF23A/ical"
    target_date = date_entry #style 2023, 12, 20
    print(date_entry)
    print(type(date_entry))
    response = requests.get(cal_url)
    if response.status_code == 200:
                # Parse the iCal data
                cal_data = response.text
                # Parse the iCal data using the icalendar library
                cal = Calendar.from_ical(cal_data)
                # Extract and print events
                target_date_events = []
                for event in cal.walk('VEVENT'):
                        start_time = event.get('dtstart').dt
                       
                        #print(start_time)
                        #print(target_date)
                        if start_time.date() == target_date:
                            global lecturecounter
                            lecturecounter += 1

                            summary = event.get('summary')
                            end_time = event.get('dtend').dt
                            room = event.get('location')
                            if (len(room)==22):
                                   room = room[:7]
                            elif(len(room)==23):
                                   room = room[:8]
                            elif(len(room)==25):
                                   room = room[:10]
                                   
                            # Converting UTC+0 to UTC+1
                            target_timezone = pytz.timezone('Europe/Paris')  # Replace with your target timezone
                            start_time = start_time.astimezone(target_timezone)
                            end_time = end_time.astimezone(target_timezone)
                            target_date_events.append({
                                'summary': summary,
                                'start_time': start_time.strftime("%H:%M" + ' Uhr'),
                                'end_time': end_time.strftime("%H:%M" + ' Uhr'),
                                'room': room
                            })

                lecture_lists = []       
                # printing out all lectures for the fitting date through discord-embeds
                for event in (target_date_events):
                            embed = discord.Embed(
                            title = f"**Vorlesung vom *{date_entry.strftime("%d.%m.%Y")}***",
                            
                            description="\n\n",
                            color=0xD9A4FC
  # You can set the color of the embed
                            
                            )
                            # Add fields to the embed
                            lecture_info = [
                                event['summary'],
                                event['start_time'],
                                event['end_time'],
                                event['room']
                            ]
                            lecture_lists.append(lecture_info)
                            
                            print("reached")
                            time = str(lecture_lists[0][1]) + " - " + str(lecture_lists[0][2])
                            print(time)
                           
                            
                print(lecture_lists)#═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═
                for i in range(lecturecounter):
                    
                      embed.add_field(name="══════════════════════════════",value='',inline=True)
                      embed.add_field(name="__"+lecture_lists[i][0]+"__:",value="- Beginn: "+"*"+lecture_lists[i][1]+"*"+ "   ┃   Ende: *"+lecture_lists[i][2]+"*"+ "\n"+"- Raum: *"+lecture_lists[i][3]+"*", inline=False)
                      embed.set_footer(text=f"Made by" + " @ragednicmaster"+" and Alex")
                    
                      embed.set_footer(text="‎ ",icon_url="https://cdn.discordapp.com/attachments/909054108235862066/1178115964152328232/guycoding.png?ex=65beccfe&is=65ac57fe&hm=e434044069bea56e66c39fd651e713d7f189e84f069ad0f9ea89c98a012eaaac&")
                embed.set_image(url="https://cdn.discordapp.com/attachments/909054108235862066/1200276858088988682/541px-DHBW-Logo-2-2.webp?ex=65c597ef&is=65b322ef&hm=d04afcf8052adc2620286cc74f3fd58512542d6ce186ab5dd60d98f088335a9a&")
                
                            
                return embed
                            
                     #┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄       
                
# running bot with token
bot.run(token[0])

