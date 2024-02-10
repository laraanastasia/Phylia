<!-- https://github.com/skills/communicate-using-markdown -->


# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## Link zum Git
[link](https://github.com/laraanastasia/Phylia)

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
!!!
- Algorithmenbeschreibung
```python 
def getcordinats(plz:str):
def set_month(input):
async def check_winner(self):
```
- Datentypen;Beispiele aus unserem Code: 
```python 
# Hier werden für jeden Operatur nur ein Beispiel gezeigt um dieses File kurz zu halten 
#String
description = f"{str(int(months.index(element))+1)}. month"
#Integer
 if select.values[0] == f"Week {i}":
    week = i
#Timestamp
 dates_clean= [datetime.strftime(ts, '%d-%m-%Y') for ts in date]
#Boolean 
 full = True
        for i in range(9):
            if gameField[i] == 0:
                full = False
```

- E/A-Operationen und Dateiverarbeitung;Beispiele aus unserem Code: 
```python
#User übergibt die Postleitzahl als String, diese wird an die Funktion "getcoordinats" übergeben um der API so den Standort für die Wetterdaten bereitzustellen. Der User erhält die minimal und maximal Temperaturen für den gegebenen Ort für 6 Tage
@app_commands.describe(plz="What is the postcode of your town?")
async def temperatur(interaction: discord.Interaction,plz: str):
    print(f"User: {interaction.user.name}, Plz: {plz}, Guild: {interaction.guild}, Channel: {interaction.channel}")
    x=weather.feature(plz)
#Der User übergibt den Bot die gewünschte Passwortlänge als Integer. Dieser generiert ein entspechendes Passwort und schickt dieses dem Unser in den Direktnachrichten zu 
async def generatepassword(interaction: discord.Interaction,length :int):
    member = interaction.user
    try: 
            await member.send(minigames.password(length))
```
- Operatoren;Beispiele aus unserem Code: 
```python 
# Hier werden für jeden Operatur nur ein Beispiel gezeigt um dieses File kurz zu halten 
if response.status_code == 200:
lecturecounter += 1
if user_guess.author != author:
if preNumber <= 0:
elif (choice.lower() == "rock" and bot_choice == "scissors") or \
if choice.lower() not in choices:

```

- Kontrollstrukturen;Beispiele aus unserem Code: 
If statement: 
```python
if amount==1:
        await interaction.response.send_message (f'You pulled {amount} card ', ephemeral=True)
        x= Karten.featureone(amount)
        await interaction.channel.send(embeds=x)
    elif amount==2:
        await interaction.response.send_message (f'You pulled {amount} cards ', ephemeral=True)
        x= Karten.featuretwo(amount)
        await interaction.channel.send(embeds=x)
    elif amount==3:
        await interaction.response.send_message (f'You pulled {amount} cards ', ephemeral=True)
        x= Karten.featurethree(amount)
        await interaction.channel.send(embeds=x)
    else:
        await interaction.response.send_message (f'Please choose between 1 and 3 cards', ephemeral=True)
```
while loop : 
```python 
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
```
for each: 
```python 
for j in range(0,5):
                    if j % 2 != 0:
                        temp2 = j
                        j = (Button(custom_id = f"{interaction.id}~{currentdate+timedelta(days=temp2)}",style=discord.ButtonStyle.green, label=str((currentdate+timedelta(days=j)).strftime("%d.%m")),row=1))
                        buttons_view.add_item(j) 
                        ...
```
...
- Funktionen; Selbsterstelle Funktionen aus unserem Code: 


```python
#Funktion, welche in der Main aufgerufen wird
 x= Karten.feature(amount) 
 # Dazu erstellte Funktionen, welche weitere selbsterstellte Funktionen aufruft: 
 def feature(x):
    y,d=ziehen(x)
    z= make_embed(x,y,d)
    return z
# Eine der weiteren erstellten Funktionen
def ziehen(x):
    Gezogen =[]
    Bedeutungen=[]
    Fotos=[]
    
    for _ in range(x):
        index= random.randint(0,78)
        Gezogen.append(Karten[index])
        Fotos.append(Pic[index])
        rev= random.randint(0,1)
        if rev == 0:
            Bedeutungen.append(Bedeutung[index])
            
        else:
            Bedeutungen.append(Gedreht[index])
           
   
    return Gezogen,Bedeutungen,Fotos
```
Weiteres Beispiel : 
```python
#Funktion, welche in der Main aufgerufen wird: 
printing_lecture = lecturedata.lecture_data(date.today())
# Dazu erstellte Funktion: 
def lecture_data(date_entry):
    cal_url = "https://stuv.app/MOS-TINF23A/ical"
    target_date = date_entry #style 2023, 12, 20
    response = requests.get(cal_url)
    if response.status_code == 200:
        ...
```
Weiteres selbsterstellte Funktion aus der Main: 
```python 
(embed=lecturedata.regular_data(date.today())) 
```
Es lassen sich einige weiterer Beispiele im Code finden


- Stringverarbeitung;Beispiele aus unserem Code: 


```python 
# Umordnung der Datumanzeige von '%m-%d-%Y'zu '%d-%m-%Y'durch strftime
dates_clean= [datetime.strftime(ts, '%d-%m-%Y') for ts in date]
#Formatierung der Länge der Zahlen (typ str) auf zwei Nachkommastellen
max_clean= ["{:.2f}".format(number) for number in max]
min_clean= ["{:.2f}".format(number) for number in min]
#Den Rest des Strings nach der Tilde abschneiden:
date = interaction.data['custom_id'].split('~')[1]
#Zufällige ziehung von Strings durch random Zahlen und die Indexfunktion von Listen: 
index= random.randint(0,78)
        Gezogen.append(Karten[index])
        Fotos.append(Pic[index])
#Füge random Chars aus der gegebenen Menge zusammen zu einem Passwort 
 all = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!%&/><+-()@"
    password = ""
    for _ in range(length):
        password += random.choice(all)
#Prüfung ob der eingegebene Str eine Zahl ist 
return message.author and message.channel and message.content.isdigit()
# Suche in einer Excel Tabelle nach einer PLZ, gebe den Index dieser PLZ und return die Daten welche mit dieser PLZ verbunden sind 
 ws= xw.Book("plzdoc.xlsx").sheets["Sheet1"]
    halfdata=ws['A2:A8299'].options(ndim=1).value
    fulldata = ws.range("A2:C8299").value
    index= halfdata.index(plz)
    x= fulldata[index]
```

- Strukturierte Datentypen;Beispiele aus unserem Code: 

Um diese Datei etwas kürzer zu gestalten wird für jeden Datentyp nur ein Beispiel gezeigt
 ```python 
# Dict: 
 daily_data = {"date": pd.date_range(
        start = pd.to_datetime(daily.Time(),unit="s").normalize(),
        end = pd.to_datetime(daily.TimeEnd(),unit="s").normalize(),
        inclusive = "left"
        )}
# Liste: 
 target_date_events.append({
                                'summary': summary,
                                'start_time': start_time.strftime("%H:%M" + ' Uhr'),
                                'end_time': end_time.strftime("%H:%M" + ' Uhr'),
                                'room': room
                            })
# Da in manchen Definitionen Klassen zu den strukturierten Datenstrukturen gezählt werden, zeigen wir für diese auch ein Beispiel: 
#Die Klasse wandelt die Daten der Funktion in ein Objekt der Klasse View um
class WeekSelectionView(discord.ui.View):
    def __init__(self,interaction:discord.Interaction):
        super().__init__()
        self.select = WeekSelection()
        self.add_item(self.select)
 ```

# Sie können die Syntax und Semantik von Python (10)
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->
Bei der Frage, auf welche Stelle wir im Code stolz sind bezüglich der Semantik und Syntax von Python, sind wir als Team bei unserem modularen Aufbau gelandet. Am Anfang des Projekts haben wir uns darauf geeinigt, so viele Zeilen unseres Codes aus der Main auszulagern wie möglich. Jeder von uns hat vor dem Projekt für die Daily Commits an einem Bot gearbeitet. Wir alle haben jegliche Funktionalität in der Main programmiert. In einem kleinen Botprojekt, an dem man selbstständig arbeitet, ist dieser Aufbau völlig in Ordnung. Da wir nun aber zu dritt an komplizierteren Funktionen arbeiten wollten, musste eine Lösung gefunden werden. Somit hatte jeder eine Aufgabe: erstelle deine Funktionalität in einem Repository (bei uns jeweils in anderen Dateien) und rufe (wenn möglich)nur noch die Funktionen in der Main auf. Diese Anforderung wurde von uns allen konsequent durchgezogen, obwohl einige zu Beginn Probleme hatten, ihre Denkweise umzustellen. Zum Schluss besitzen wir nun eine übersichtliche Main und leicht findbaren Funktionscode, welcher einfacher ergänzbar und vor allem verständlicher ist.
Beispiel :

 Der Funktionscode für "Tarot" ist 102 Zeilen lang und befindet sich im File: "Karten.py". In der Main hingegen befindet sich für den Command "Tarot" lediglich folgende Zeilen: 

 ```python 
 @bot.tree.command(name="tarot",description="Whats your destiny?") 
@app_commands.describe(amount="How many cards do you want to pull?")
async def tarot(interaction: discord.Interaction,amount:int):
    x= Karten.feature(amount)
    await interaction.response.send_message (f'You pulled {amount} cards ', ephemeral=True)
    await interaction.channel.send(embed=x)
```

# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
<!-- Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat -->

Zu Beginn wurde sich als Team zusammengesetzt und besprochen, wer welche Aufgaben erfüllen wird. 
Jedes Teammitglied entwickelte seinen Code auf einem branch (oder einem anderen Repository (ausversehen..ups)) 
[Alex sein Branch](https://github.com/laraanastasia/Phylia/tree/alex), 
[Nico sein Branch](https://github.com/laraanastasia/Phylia/tree/realNico), 
[Lara ihr repository](https://github.com/laraanastasia/Phylia-temp)

Aufteilung der Hauptfunktionen: 
Tarot und Wetter - Lara
TicTacToe, Rock-Paper-Scissor  - Nico
(regelmäßiger) Vorlesungsplan, Minigames - Alex

Getestet wurde immer, wenn eine Funktion fertig gestellt wurde von den zwei anderen Teammitgliedern (liebevoll Pentester genannt). Troubleshooting wurde wenn es verzwickt war  oft zu zweit und  manchmal sogar zu dritt betrieben. (Z.B bei der Button-Lambda Funktion, klare Blicke auf doppelten Code)

# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)

Ausnutzen der ganzzahligen integer Eigenschaft:

![alt Text](/screenshots/button.png)

Stringkonvertierung eines hochgezählten Integers um dieses im Menü anzuzeigen.

![alt Text](/screenshots/index.png)
Dict to List  : 

![alt Text](/screenshots/dict.png)

![alt Text](/screenshots/list.png)

## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->
Git: 
![alt Text](/screenshots/git.png)

![alt Text](/screenshots/gitlog.png)

VSC: 
![alt Text](/screenshots/vsc.png)

Copilot:
![alt Text](/screenshots/copilot.png)

Terminal:
![alt text](terminal.png)

## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)

Lara -> Nico (GIT) Nico: "Ich kann jetzt aus dem Terminal Git nutzen dank Lara uWu" 
Lara -> Alex (GIT) Alex: "Lara hat mich in die Künste des terminalbasierten Commitens eingeführt :P"
Nico -> Alex (Discord Embeds) Alex: "Dank Nico kann ich nur durch den Anblick meiner Embeds Leute verzaubern"
Nico -> Lara (Server-Management) Lara: "Nico hat mir die Vorteile Discord-Admin zu sein gezeigt :3"
Alex -> Nico (Button) Nico: "Alex hat mir geholfen Buttons korrekt zu erstellen, damit der Callback funktioniert :D"
Alex -> Lara (Bot-Initialisierung) Lara: "Mein Bot ist nun stets startklar dank Alex' Support 0^0"

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
Neue Technologien: 
- Raspberry Pi 4 / Terminal (linux)
- API
- Ical
- Excel (lmao)
- Copilot
- Discord development

<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->
Student im fünften Semester (Bad Mergentheim,https://github.com/fabtopf) 


## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
Alex: 
```python 
function for creating all buttons
def buttons(interaction:discord.Interaction,week,month,year):
            # first the days are calculated
            global day
            day = 1
            days = day + 7*(week-1)
            # global current date so I can use it everywhere (actually useful)
            global currentdate
            currentdate = datetime(int(year), month, days, 0, 0, 0, 0)
            buttons_view = View()
            # here happens the magic: for-loop iterates 7 times so each iteration creates one button
            for j in range(0,7):
                    # if-else-construction only differs in the color of the buttons which are being created (could be easily improved into smaller code but I think this is easier to understand)
                    if j % 2 != 0:
                        temp2 = j
                        # the button creation with elements id, color and text on button
                        j = (Button(custom_id = f"{interaction.id}~{currentdate+timedelta(days=temp2)}",style=discord.ButtonStyle.green, label=str((currentdate+timedelta(days=j)).strftime("%d.%m"))))
                        # adding the button to the "buttons-collection" (= view)
                        buttons_view.add_item(j)
                        # adding the callback-function (if you click on a button the callback gets triggered)
                        j.callback = lambda j: buttons_callback(j)   # lambda: one-line function that points to the callback (when clicking button) in a fast anonymous way
this part does the same as the one above but it differs in the buttoncolor
                    else:
                        temp2 = j
                        j = (Button(custom_id = f"{interaction.id}~{currentdate+timedelta(days=temp2)}",style=discord.ButtonStyle.blurple, label=str((currentdate+timedelta(days=j)).strftime("%d.%m"))))
                        buttons_view.add_item(j)
                        j.callback = lambda j: buttons_callback(j)
            # returning the "buttons-collection" so I can make them visible
            return buttons_view
I am very proud of this part of the code since I had to hardcode it in the first attempts of the project but over the time I managed to create them dynamically. The main problem was always to
dynamically add a callback to each button. The callback was always attached to the ID of the last button. To fix this problem I had to use the lambda function which points directly on the
callback (that helped me a lot). I was very happy when I had found that useful function (lambda)

```
Lara:
```python
#I'm proud of the following code snippet because I managed to force Discord to do something that is not natively accessible (aka bug-abuse :3 ). Discord only allows you to put one picture into an embed. I did not want to send four embeds to show three cards since that could almost be counted as spam. So, I went scavenging online to find a solution (the first place, of course, Stack Overflow). Shockingly, there was no well-documented answer for my problem. I was at my wit's end and one Google search away from abandoning my function. Then, my savior appeared: a random forum comment I found in the deepest, darkest place online. In one random sentence regarding a different issue, somebody suggested adding the same URL to different embeds. I was skeptical since that solution sounded too simple to be so unknown... but behold: code that mimics multiple pictures in a single embed:
def make_embed_three(x,Karten,Bedeutungen,y):
    #this is the url feature that safed my function 
    embed = discord.Embed(title="YOUR DESTINY", color=0xD9A4FC,url="https://insighttimer.com/blog/what-is-tarot/") 
    embed.set_footer(text="‎",icon_url="https://cdn.discordapp.com/attachments/1179867724592193637/1202193113389473832/image.png?ex=65cc9095&is=65ba1b95&hm=dddcb13b59f2772b6b4b352884d8c9424eea27a426e6ac544f854addb88a2ff1&" )
     #this creates the fields where the names of the cards + the meanings (reversed is possible!)   
    for i in range(x):
        embed.add_field(name=Karten[i], value=f"{'-'*5}\nReading:\n {Bedeutungen[i]}\n{'-'*5}", inline=False)
    # here is the magic: I still created 4 embeds, but since I give them all the same url Discord displays them as one ^^
    embed1= discord.Embed(url="https://insighttimer.com/blog/what-is-tarot/")
    embed1.set_image(url=y[0])
    embed2= discord.Embed(url="https://insighttimer.com/blog/what-is-tarot/")
    embed2.set_image(url=y[1])
    embed3=discord.Embed(url="https://insighttimer.com/blog/what-is-tarot/")
    embed3.set_image(url=y[2])
    return embed,embed1,embed2,embed3
```

Nico: 
```Python 
class TicTacToe(discord.ui.View):
    # Initialisierung der TicTacToe Klasse
    def __init__(self, player1, player2, gameField, **kwargs):
        super().__init__(**kwargs) # Aufruf des Konstruktors der übergeordneten Klasse
        # Setzen der Spieler und des Spielfelds
        self.player1 = player1
        self.player2 = player2
        self.gameField = gameField
        self.current_player = player1   # Der aktuelle Spieler wird auf player1 gesetzt
        
        # Erstellen von 9 Schaltflächen für das TicTacToe-Spiel
        for i in range(1, 10):
            # Erstellen eines Buttons mit einer eindeutigen ID, einem leeren Label, einem grauen Stil und der entsprechenden Zeile
            button = discord.ui.Button(custom_id=str(i), label="‎", style=discord.ButtonStyle.secondary, row=(i - 1) // 3)
            self.add_item(button) # Hinzufügen der Schaltfläche zur Ansicht
            # Setzen des Callbacks für die Schaltfläche auf die Methode button_callback
            button.callback = lambda interaction, button=button: self.button_callback(interaction, button)

    # Callback-Methode, die aufgerufen wird, wenn ein Button gedrückt wird
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Definieren der Spieler und des aktuellen Spielers als lokale Variablen
        player1 = self.player1
        player2 = self.player2
        current_player = self.current_player # Aufruf des aktuellen Spielers beim Aufruf der Funktion

    async def update_game_field(self, button, player):
        gameField = self.gameField [...] # Aufruf des aktuellen Spielfelds beim Aufruf der Funktion

    async def check_winner(self):
        player1 = self.player1
        player2 = self.player2
        gameField = self.gameField [...] # Aufruf des aktuellen Spielfelds beim Aufruf der Funktion
#Besonders stolz bin ich auf die Nutzung der class TicTacToe, denn in der challenge_start_callback() Funktion wird, wenn der "I want to play" button gedrückt wird eine neue Nachricht erstellt, die mit den Game-Buttons bestückt wird (`view=TicTacToe(...)`). Hier werden die Objekte `discord.user.player1` und `discord.user.player2`, sowie ein leeres, individuelles `gameField` benötigt. 
#Diese werden direkt an die Klasse übergeben
await interaction.channel.send([...] view=TicTacToe(player1, player2, gameField))
#Dadurch werden die Werte für jedes Event individuell gespeichert und sind für alle Funktionen in der Klasse zugänglich. Dadurch spare ich die Übergabe von Werten an die nächste Funktion und ermögliche einen übersichtlicheren Code, der leichter zu debugen ist.
```


<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->

Probleme: 
### Team management
- Missverständnisse, es wurde öfters aneinander vorbei geredet. Konnte aber durch ein Sitdown gelöst werden. Die Gruppenmoral stieg danach stark an. 
- Zeitmanagement, es war ziemlich schwierig Termine zu finden an denen jeder Zeit hatte. Konnte gelöst werden in dem einfache Probleme asynchron geklärt wurden und jeder für große Probleme Zeit geschaffen hat. 

###  Implementation
- Inkompatible Imports zwischen Funktionen (Ical und Openmeteo_requests). Konnte durch einen Interpreterabgleich gelöst werden. Hätte durch regelmäßigen mergen einfacher auffindbar sein können.  
- Raspberry Pi mit Python, aufgrund von Versionendrama. Konnte gelöst werden durch bruteforce
- Linux issues :C, konnte durch Stackoverflow und gutes Googeln gelöst werden

### Functionality 
- Discord Limitierung der Bilder in einem Embed; Discord erlaubt nativ nur ein Foto/Embed. Lösung durch bug abuse
- Kalendermanagement, Schwierigkeit dynamische Tagberechnung durchzuführen. Gelöst durch neuen Ansatz. Hätte durch bessere Planung zu Beginn verhindert werden können. 
- Button-press-event nicht auf korrektem Button ausgeführt, gelöst durch Troubleshooting (lambda Funktion). Hätte durch ausführlichere recherche schneller gelöst werden können. 






