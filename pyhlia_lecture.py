import main
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

# ready-message
@bot.event
async def on_ready():
    print("I am ready for work! ~Pyhlia")
    try:
        synced = await bot.tree.sync()
        print(f"Currently listening to {len(synced)} command(s).")
    except Exception as e:
        print(e)


data = None
counter = 0
day = datetime.today()


class MyView2(discord.ui.View):
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
                        await interaction.response.defer()
                        await buttons_message.edit(view=await create_buttons(interaction,1))
                  elif select.values[0] == "February":
                        await interaction.response.defer()
                        await buttons_message.edit(view=await create_buttons(interaction,2))
                  elif select.values[0] == "March":
                        await interaction.response.defer()
                        await buttons_message.edit(view=await create_buttons(interaction,3))
                  elif select.values[0] == "April":
                        await interaction.response.defer()
                        await buttons_message.edit(view=await create_buttons(interaction,4))
                  elif select.values[0] == "May":
                        await interaction.response.defer()
                        await buttons_message.edit(view=await create_buttons(interaction,5))
                  elif select.values[0] == "June":
                        await interaction.response.defer()
                        await buttons_message.edit(view=await create_buttons(interaction,6))
                  elif select.values[0] == "July":
                        await interaction.response.defer()
                        await buttons_message.edit(view=await create_buttons(interaction,7))
                  elif select.values[0] == "August":
                        await interaction.response.defer()
                        await buttons_message.edit(view=await create_buttons(interaction,8))
                  elif select.values[0] == "September":
                        await interaction.response.defer()
                        await buttons_message.edit(view=await create_buttons(interaction,9))
                  elif select.values[0] == "October":
                        await interaction.response.defer()
                        await buttons_message.edit(view=await create_buttons(interaction,10))
                  elif select.values[0] == "November":
                        await interaction.response.defer()
                        await buttons_message.edit(view=await create_buttons(interaction,11))
                  else:
                        await buttons_message.edit(view=await create_buttons(interaction,12))
                        await interaction.response.defer()

class MyView(discord.ui.View):
               @discord.ui.select( # the decorator that lets you specify the properties of the select menu 
                    placeholder = "Choose a week!", # the placeholder text that will be displayed if nothing is selected
                    min_values = 1, # the minimum number of values that must be selected by the users
                    max_values = 1, # the maximum number of values that can be selected by the users
                    options = [ # the list of options from which users can choose, a required field
                    discord.SelectOption(
                        label="Week 1",
                        description= f"{day} - {day +timedelta(days=4)}"
                    ),
                    discord.SelectOption(
                        label="Week 2",
                        description="08.01-12.01"
                    ),
                    discord.SelectOption(
                        label="Week 3",
                        description="15.01-19.01"
                    ),
                    discord.SelectOption(
                        label="Week 4",
                        description="22.01-26.01"
                    ),
                    discord.SelectOption(
                        label="Week 5",
                        description="29.01-03.02"
                    )   
                        ]
                    )
               async def select_callback(self,interaction,select): # the function called when the user is done selecting options
                  if select.values[0] == "Week 1":
                        await interaction.response.send_message("Cool")
                  elif select.values[0] == "Week 2":
                        await interaction.response.send_message("Cool")
                  elif select.values[0] == "Week 3":
                        await interaction.response.send_message("Cool")
                  elif select.values[0] == "Week 4":
                        await interaction.response.send_message("Cool")
                  elif select.values[0] == "Week 5":
                        await interaction.response.send_message("Cool")
                  
async def create_buttons(interaction: discord.Interaction,month):
      view4 = View()
      year = datetime.today().strftime("%Y")
      global day
      day = datetime(int(year), month, 1, 12, 0, 0, 0)
      for j in range(0,5):
                     if j % 2 != 0:                         
                            temp2 = j
                            j = (Button(custom_id = f"{interaction.id}~{day+timedelta(days=temp2)}",style=discord.ButtonStyle.green, label=str((day+timedelta(days=j)).strftime("%d.%m")),row=1))
                            view4.add_item(j)                             
                            j.callback = lambda j: callback2(j)       
                     else:
                            temp2 = j
                            j = (Button(custom_id = f"{interaction.id}~{day+timedelta(days=temp2)}",style=discord.ButtonStyle.blurple, label=str((day+timedelta(days=j)).strftime("%d.%m")),row=1))
                            view4.add_item(j)
                            j.callback = lambda j: callback2(j)
      return view4

async def callback2(interaction: discord.Interaction):
                      #date_entry=date.today()+ timedelta(days=1)####################
                   # try:
                      print(interaction.data)
                      date = interaction.data['custom_id'].split('~')[1]
                      await lecture_data(datetime.strptime(date,"%Y-%m-%d %H:%M:%S").date())
                      await interaction.response.defer()
      
# method called by buttonsclass (copied)
async def lecture_data(date_entry):
    print("erreicht")
    global data
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
    # printing out all lectures for the fitting date through discord-embeds
    for event in (target_date_events):
                            channel = bot.get_channel(1184076609779671111)
                            embed = discord.Embed(
                            title = "**"+str(event['summary'])+"**",
                            #description=date,
                            color=discord.Color.blurple()  # You can set the color of the embed
                            )
                            # Add fields to the embed
                            embed.add_field(name='__Beginn:__', value=event['start_time'], inline=False)
                            embed.add_field(name='__Ende:__', value=event['end_time'], inline=True)
                            embed.add_field(name='__Vorlesungsort:__', value=event['room'], inline=False)
                            embed.set_image(url="https://cdn.discordapp.com/attachments/909054108235862066/1197594048781893694/541px-DHBW-Logo.png?ex=65bbd55f&is=65a9605f&hm=8d57652450766fa4a11d1dc6ff195858d72c83b76dda26e898e8a59d1b8606a1&")
                            
                            print(f"Summary: {event['summary']}")
                            print(f"Start Time: {event['start_time']}")
                            print(f"End Time: {event['end_time']}")
                            print(f"Room: {event['room']}")
                            print("-----")
                            await channel.send(embed=embed)
                                                       
# copied
def jan1():
  year = datetime.today().strftime("%Y")
  jan1 = datetime(int(year), 1, 1, 0, 0, 0, 0).weekday()
  return jan1
# copied

@bot.tree.command(name="buttontest")
async def lecture(interaction: discord.ui.Button):
    channel = bot.get_channel(1184076609779671111)
    global data
    view = await buttons(interaction)
    
    await interaction.response.send_message(view=MyView2())
    global buttons_message
    buttons_message = await channel.send(view=view)
    await channel.send(view=MyView())
    
   
    
    

# copied
async def buttons(interaction: discord.Interaction):
       global data
       data = interaction
       # getting the first monday in the year
       for i in range(0,6):
              if jan1() == 0:
               year = datetime.today().strftime("%Y")
               firstmonday = datetime(int(year), 1, 1, 12, 0, 0, 0) + timedelta(days=i)
              else:
               firstmonday = datetime(int(year), 1, 1, 12, 0, 0, 0) + timedelta(days=7-i)
              view = View()
              # callback for buttons
              async def callback2(interaction: discord.Interaction):
                      #date_entry=date.today()+ timedelta(days=1)####################
                   # try:
                      print(interaction.data)
                      date = interaction.data['custom_id'].split('~')[1]
                      await lecture_data(datetime.strptime(date,"%Y-%m-%d %H:%M:%S").date())
                      await interaction.response.defer()
              
              # creating buttons
              for j in range(0,5):
                     if j % 2 != 0:
                            temp2 = j
                            j = (Button(custom_id = f"{interaction.id}~{firstmonday+timedelta(days=temp2)}",style=discord.ButtonStyle.green, label=str((firstmonday+timedelta(days=j)).strftime("%d.%m")),row=1))
                            view.add_item(j)                             
                            j.callback = lambda j: callback2(j)                      
                     else:
                            temp2 = j
                            j = (Button(custom_id = f"{interaction.id}~{firstmonday+timedelta(days=temp2)}",style=discord.ButtonStyle.blurple, label=str((firstmonday+timedelta(days=j)).strftime("%d.%m")),row=1))
                            view.add_item(j)
                            j.callback = lambda j: callback2(j)
                            
              
              return view
        
                                 
              
        
async def test(ctx):
    global data3
    data3 = ctx
    return data3