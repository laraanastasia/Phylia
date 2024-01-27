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
message = ''
week = 1
month = 1
year = date.today().year


# ready-message
@bot.event
async def on_ready():
    print("I am ready for work! ~Pyhlia")
    try:
        synced = await bot.tree.sync()
        print(f"Currently listening to {len(synced)} command(s).")
    except Exception as e:
        print(e)

# Lecture command for getting todays lecture-plan
@bot.tree.command(name="lecture")
async def lecture(interaction: discord.ui.Button):
    channel = bot.get_channel(1184076609779671111)
    printing_lecture = await lecture_data(date.today()+timedelta(days=2))
    global message    
    message=await interaction.response.send_message(embed=printing_lecture, view = embed_buttons())
    print(type(message))

def get_firstmonday_jan():
  jan1 = datetime(int(year), month, 1, 0, 0, 0, 0).weekday()
  for i in range(0,6):
    if jan1 == 0:
        firstmonday_jan = datetime(int(year), month, 1, 12, 0, 0, 0)
    else:
        firstmonday_jan = datetime(int(year), month, 1, 12, 0, 0, 0) + timedelta(days=7-i)
  return firstmonday_jan

def get_firstmondaymonth(month,week):
    if month == 1:
            if week == 1:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=0)
            elif week == 2:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=7)
            elif week == 3:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=14)
            elif week == 4:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=21)
            elif week == 5:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=28) 
    elif month == 2:
            if week == 1:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=31)
            elif week == 2:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=38)
            elif week == 3:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=45)
            elif week == 4:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=52)
            elif week == 5:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=59)         
    elif month == 3:
            if week == 1:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=60)
            elif week == 2:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=67)
            elif week == 3:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=74)
            elif week == 4:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=81)
            elif week == 5:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=88) 
    elif month == 4:
            if week == 1:  
                firstmonday_month = get_firstmonday_jan() + timedelta(days=91)
                print(firstmonday_month)
            elif week == 2:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=98)
            elif week == 3:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=105)
            elif week == 4:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=112)
            elif week == 5:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=119) 
    elif month == 5:
            if week == 1:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=121)
            elif week == 2:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=128)
            elif week == 3:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=135)
            elif week == 4:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=142)
            elif week == 5:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=149) 
    elif month == 6:
            if week == 1:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=152)
            elif week == 2:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=159)
            elif week == 3:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=166)
            elif week == 4:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=173)
            elif week == 5:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=180) 
    elif month == 7:
            if week == 1:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=182)
            elif week == 2:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=189)
            elif week == 3:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=196)
            elif week == 4:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=203)
            elif week == 5:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=210) 
    elif month == 8:
            if week == 1:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=213)
            elif week == 2:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=220)
            elif week == 3:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=227)
            elif week == 4:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=234)
            elif week == 5:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=241) 
    elif month == 9:
            if week == 1:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=244)
            elif week == 2:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=251)
            elif week == 3:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=258)
            elif week == 4:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=265)
            elif week == 5:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=272) 
    elif month == 10:
            if week == 1:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=274)
            elif week == 2:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=281)
            elif week == 3:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=289)
            elif week == 4:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=296)
            elif week == 5:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=303) 
    elif month == 11:
            if week == 1:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=305)
            elif week == 2:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=312)
            elif week == 3:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=319)
            elif week == 4:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=326)
            elif week == 5:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=333) 
    elif month == 12:
            if week == 1:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=335)
            elif week == 2:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=342)
            elif week == 3:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=349)
            elif week == 4:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=356)
            elif week == 5:
                firstmonday_month = get_firstmonday_jan() + timedelta(days=363) 
    return firstmonday_month

def set_month(input):
       global month
       month = input
       return month

def set_week(input):
       global week
       week = input
       return week

# Function called by buttonsclass (semi-copied)
async def lecture_data(date_entry):
    cal_url = "https://stuv.app/MOS-TINF23A/ical"
    target_date = date_entry #style 2023, 12, 20
    response = requests.get(cal_url)
    if response.status_code == 200:
                # Parsing the iCal data
                cal_data = response.text
                # Parse the iCal data using the icalendar library
                cal = Calendar.from_ical(cal_data)
                # Extract events from ical
                #target_date = pytz.timezone("America/Los_Angeles")
                target_date_events = []
                for event in cal.walk('VEVENT'):
                        start_time = event.get('dtstart').dt
                        # Comparing entry date with ALL dates
                        
                        if start_time.date()== target_date:
                            global lecturecounter
                            lecturecounter += 1
                            summary = event.get('summary')
                            end_time = event.get('dtend').dt
                            room = event.get('location')
                            # Converting UTC+0 to UTC+1
                            target_timezone = pytz.timezone('Europe/Paris')  # Replace with your target timezone
                            start_time = start_time.astimezone(target_timezone)
                            end_time = end_time.astimezone(target_timezone)
                            # Adding data to target_date_events
                            target_date_events.append({
                                'summary': summary,
                                'start_time': start_time.strftime("%H:%M" + ' Uhr'),
                                'end_time': end_time.strftime("%H:%M" + ' Uhr'),
                                'room': room
                            })

    lecture_lists = []
    # Printing out all lectures for the fitting date through discord-embeds
    for event in (target_date_events):
                            embed = discord.Embed(
                            title = f"**Vorlesung vom *{date_entry.strftime("%d.%m.%Y")}***",
                            
                            description="\n\n",
                            color=0xD9A4FC        
                            )
                            # Creating a list wie all the lecture data and adding it to the "big list"
                            lecture_info = [
                                event['summary'],
                                event['start_time'],
                                event['end_time'],
                                event['room']
                            ]
                            lecture_lists.append(lecture_info)
    print(month)                   
    # Adding the lecture data to the embed
    for i in range(lecturecounter):
        embed.add_field(name="┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄",value='',inline=True)
        embed.add_field(name="__"+lecture_lists[i][0]+"__:",value="- Beginn: "+"*"+lecture_lists[i][1]+"*"+ "   ┃   Ende: *"+lecture_lists[i][2]+"*"+ "\n"+"- Raum: *"+lecture_lists[i][3]+"*", inline=False)
        embed.set_footer(text="‎ ",icon_url="https://cdn.discordapp.com/attachments/909054108235862066/1178115964152328232/guycoding.png?ex=65beccfe&is=65ac57fe&hm=e434044069bea56e66c39fd651e713d7f189e84f069ad0f9ea89c98a012eaaac&")
    embed.set_image(url="https://cdn.discordapp.com/attachments/909054108235862066/1200276858088988682/541px-DHBW-Logo-2-2.webp?ex=65c597ef&is=65b322ef&hm=d04afcf8052adc2620286cc74f3fd58512542d6ce186ab5dd60d98f088335a9a&")
    return embed 
    
# class for creating embed_buttons
class embed_buttons(discord.ui.View):
    interaction=discord.Interaction
    @discord.ui.button(custom_id = f"{interaction.id}~days_button",label="ay", style=discord.ButtonStyle.gray,row=1,emoji="🇩")
    async def days_callback(self, interaction:discord.Interaction, button):
            await interaction.message.edit(view=buttons(interaction,4,month,datetime.today().strftime("%Y")))
            await interaction.response.defer()
        #await interaction.response.send_message(view=buttons(interaction,4,1,datetime.today().strftime("%Y")))
    @discord.ui.button(custom_id = f"{interaction.id}~week_button",label="eek", style=discord.ButtonStyle.gray,row=1,emoji="🇼")
    async def weeks_callback(self, interaction:discord.Interaction, button):
        await interaction.message.edit(view=WeekSelection())
        await interaction.response.defer()
    @discord.ui.button(custom_id = f"{interaction.id}~month:button",label="onth", style=discord.ButtonStyle.gray,row=1,emoji="🇲")
    async def month_callback(self, interaction:discord.Interaction, button):
        await interaction.message.edit(view=MonthSelection())
        await interaction.response.defer()
        
def buttons(interaction:discord.Interaction,week,month,year):
     # creating buttons
            day = 1
            days = day + week*7
            currentdate = datetime(int(year), month, days, 0, 0, 0, 0)
            buttons_view = View()
            for j in range(0,5):
                    if j % 2 != 0:
                        temp2 = j
                        j = (Button(custom_id = f"{interaction.id}~{currentdate+timedelta(days=temp2)}",style=discord.ButtonStyle.green, label=str((currentdate+timedelta(days=j)).strftime("%d.%m")),row=1))
                        buttons_view.add_item(j)                             
                        j.callback = lambda j: buttons_callback(j)                      
                    else:
                        temp2 = j
                        j = (Button(custom_id = f"{interaction.id}~{currentdate+timedelta(days=temp2)}",style=discord.ButtonStyle.blurple, label=str((currentdate+timedelta(days=j)).strftime("%d.%m")),row=1))
                        buttons_view.add_item(j)
                        j.callback = lambda j: buttons_callback(j)
            return buttons_view
async def buttons_callback(interaction: discord.Interaction):
                      date = interaction.data['custom_id'].split('~')[1]
                      global lecturecounter
                      lecturecounter = 0
                      await interaction.message.edit(embed = await lecture_data(datetime.strptime(date,"%Y-%m-%d %H:%M:%S").date()), view = embed_buttons())
                      await interaction.response.defer()

class WeekSelection(discord.ui.View):
                print(f"This is the month{month}")
                # the decorator that lets you specify the properties of the select menu 
                @discord.ui.select(
                    placeholder = "Choose a week!", # the placeholder text that will be displayed if nothing is selected
                    min_values = 1, # the minimum number of values that must be selected by the users
                    max_values = 1, # the maximum number of values that can be selected by the users
                    options = [ # the list of options from which users can choose, a required field
                    discord.SelectOption(
                        label="Week 1",
                        description= f"{(get_firstmondaymonth(month,1)).strftime("%d.%m")} - {(get_firstmondaymonth(month,1)+timedelta(days=4)).strftime("%d.%m")}",
                    ),
                    discord.SelectOption(
                        label="Week 2",
                        description=f"{(get_firstmondaymonth(month,2)).strftime("%d.%m")} - {(get_firstmondaymonth(month,2)+timedelta(days=4)).strftime("%d.%m")}",
                    ),
                    discord.SelectOption(
                        label="Week 3",
                        description=f"{(get_firstmondaymonth(month,3)).strftime("%d.%m")} - {(get_firstmondaymonth(month,3)+timedelta(days=4)).strftime("%d.%m")}",
                    ),
                    discord.SelectOption(
                        label="Week 4",
                        description=f"{(get_firstmondaymonth(month,4)).strftime("%d.%m")} - {(get_firstmondaymonth(month,4)+timedelta(days=4)).strftime("%d.%m")}",
                    ),
                    discord.SelectOption(
                        label="Week 5",
                        description=f"{(get_firstmondaymonth(month,5)).strftime("%d.%m")} - {(get_firstmondaymonth(month,5)+timedelta(days=4)).strftime("%d.%m")}",
                    ) 
                        ])
                async def select_callback(self,interaction,select): # the function called when the user is done selecting options
                    
                        await interaction.response.send_message()
                            
class MonthSelection(discord.ui.View):
               @discord.ui.select( # the decorator that lets you specify the properties of the select menu 
                    placeholder = "Choose a month!", # the placeholder text that will be displayed if nothing is selected
                    min_values = 1, # the minimum number of values that must be selected by the users
                    max_values = 1, # the maximum number of values that can be selected by the users
                    options = [ # the list of options from which users can choose, a required field
                    discord.SelectOption(
                        label="January",
                        description="first month"
                    ),
                    discord.SelectOption(
                        label="February",
                        description="second month"
                    ),
                    discord.SelectOption(
                        label="March",
                        description="third month"
                    ),
                    discord.SelectOption(
                        label="April",
                        description="fourth month"
                    ),
                    discord.SelectOption(
                        label="May",
                        description="fifth month"
                    ),
                    discord.SelectOption(
                        label="June",
                        description="sixth month"
                    ),
                    discord.SelectOption(
                        label="July",
                        description="seventh month"
                    ),
                    discord.SelectOption(
                        label="August",
                        description="eighth month"
                    ),
                    discord.SelectOption(
                        label="September",
                        description="nineth month"
                    ),
                    discord.SelectOption(
                        label="October",
                        description="tenth month"
                    ),
                    discord.SelectOption(
                        label="November",
                        description="eleventh"
                    ),
                    discord.SelectOption(
                        label="Dezember",
                        description="twelveth month"
                    )
                        ]
                    )
               # this function is triggered when you hit the month-menu, the function defines the buttons new
               async def select_callback(self,interaction,select): # the function called when the user is done selecting options
                  if select.values[0] == "January":  
                        set_month(1)
                        await interaction.message.edit(view=buttons(interaction,week,set_month(1),year))
                        await interaction.response.defer()
                  elif select.values[0] == "February":
                        await interaction.message.edit(view=buttons(interaction,week,set_month(2),year))
                        await interaction.response.defer()
                  elif select.values[0] == "March":
                        await interaction.message.edit(view=buttons(interaction,week,set_month(3),year))
                        await interaction.response.defer()
                  elif select.values[0] == "April":
                        await interaction.message.edit(view=buttons(interaction,week,set_month(4),year))
                        await interaction.response.defer()
                  elif select.values[0] == "May":
                        await interaction.message.edit(view=buttons(interaction,week,set_month(5),year))
                        await interaction.response.defer()
                  elif select.values[0] == "June":
                        await interaction.message.edit(view=buttons(interaction,week,set_month(6),year))
                        await interaction.response.defer()
                  elif select.values[0] == "July":
                        await interaction.message.edit(view=buttons(interaction,week,set_month(7),year))
                        await interaction.response.defer()
                  elif select.values[0] == "August":
                        await interaction.message.edit(view=buttons(interaction,week,set_month(8),year))
                        await interaction.response.defer()
                  elif select.values[0] == "September":
                        await interaction.message.edit(view=buttons(interaction,week,set_month(9),year))
                        await interaction.response.defer()
                  elif select.values[0] == "October":
                        await interaction.message.edit(view=buttons(interaction,week,set_month(10),year))
                        await interaction.response.defer()
                  elif select.values[0] == "November":
                        await interaction.message.edit(view=buttons(interaction,week,set_month(11),year))
                        await interaction.response.defer()
                  else:
                        await interaction.message.edit(view=buttons(interaction,week,set_month(12),year))
                        await interaction.response.defer()




# Running bot with token
bot.run(token[0])

