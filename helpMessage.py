import datetime
import discord

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