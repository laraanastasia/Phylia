<!-- https://github.com/skills/communicate-using-markdown -->


# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## Link zum Git
[link](https://github.com/laraanastasia/Phylia)

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
- Algorithmenbeschreibung

- Datentypen

- E/A-Operationen und Dateiverarbeitung

- Operatoren

- Kontrollstrukturen

- Funktionen

- Stringverarbeitung

- Strukturierte Datentypen

# Sie können die Syntax und Semantik von Python (10)

```python
 buttons_view = View()
            for j in range(0,5):
                    if j % 2 != 0:
                        temp2 = j
                        j = (Button(custom_id = f"{interaction.id}~{currentdate+timedelta(days=temp2)}",style=discord.ButtonStyle.green, label=str((currentdate+timedelta(days=j)).strftime("%d.%m")),row=1))
                        buttons_view.add_item(j)                             
                        j.callback = lambda j: buttons_callback(j)   # lambda: one-line function that points to the callback (when clicking button) in a fast anonymous way                  
                    else:
                        temp2 = j
                        j = (Button(custom_id = f"{interaction.id}~{currentdate+timedelta(days=temp2)}",style=discord.ButtonStyle.blurple, label=str((currentdate+timedelta(days=j)).strftime("%d.%m")),row=1))
                        buttons_view.add_item(j)
                        j.callback = lambda j: buttons_callback(j)
            return buttons_view 
```
Warum sind wir stolz auf diesen Codeausschnitt: 


# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)

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

Dict to List (!!) :

![Alt Text](/screenshots/dict.png)

![Alt Text](/screenshots/list.png)

Ausnutzen der ganzzahligen integer Eigenschaft:

![Alt Text](/screenshots/button.png)

Stringkonvertierung eines hochgezählten Integers um dieses im Menü anzuzeigen.

![Alt Text](/screenshots/index.png)

## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->
Git: 
![Alt Text](/screenshots/git.png)

![Alt Text](/screenshots/gitlog.png)

VSC: 
![Alt Text](/screenshots/vsc.png)

Copilot:
![Alt Text](/screenshots/copilot.png)

## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->



## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->



## Kenntnisse in prozeduraler Programmierung:

# - Algorithmenbeschreibung

# - Datentypen

# - E/A-Operationen und Dateiverarbeitung

# - Operatoren

# - Kontrollstrukturen

# - Funktionen

# - Stringverarbeitung

# - Strukturierte Datentypen


