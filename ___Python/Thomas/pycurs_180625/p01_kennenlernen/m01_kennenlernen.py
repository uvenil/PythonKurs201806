import statistics
from datetime import date

from p01_kennenlernen import my_pycurse_utilities

torsten = ["Torsten", "Aachen", date(1967, 1,1), ["C"]]
michael = ["Michael", "Moormerland", date(1981, 1, 10), ["Javascript"]]
karpoo = ["Karpoo", "Düsseldorf", date(1969, 1,1), ["ABAP"]]
carsten = ["Carsten", "Aachen", date(1971, 2, 3), ["Basic"]]
thomas = ["Thomas", "Bielefeld", date(1964, 10, 12), ["Pascal"]]
angela = ["Angela", "Lingen", date(1983, 12, 31), ["C", "Java"]]
jonas = ["Jonas", "Löhne", date(1997, 4, 4), []]
marco = ["Marco", "Bielefeld", date(1975, 6, 24), []]
roman = ["Roman", "Hannover", date(1984, 2, 28), []]
daniel = ["Daniel", "Bielefeld", date(1980, 1, 1), ["Python"]]

teilnehmerliste = [torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel]

# 1) Anzahl der Teilnehmer
anzahl = len(teilnehmerliste)
print(anzahl)

# 2) Alle Teilnehmer aus Bielefeld
for teilnehmer in teilnehmerliste: # Schleife, lies: "für jeden teilnehmer in der liste wiederhole:"
    if teilnehmer[1] == "Bielefeld": # == ist ein Vergleichsoperator (hier: auf Gleichheit)
        print(teilnehmer[0]+' '+str(teilnehmer[2]))

# 3) Alter ermitteln
geburtsdatum = date(2000, 12, 1)
heute = date.today()
jahre = heute.year-geburtsdatum.year
#   Pos 0               Pos 1                   Pos 2       Pos 3
if (geburtsdatum.month, geburtsdatum.day) >= (heute.month, heute.day): # tuple Vergleich Pos0 Pos2 wenn gleich dann Vergleich Pos1 Pos3
    jahre -= 1 # Kurzform für: jahre = jahre -1
print(jahre)

geburtsdatum = date(1964, 12, 31)
print(my_pycurse_utilities.alter(geburtsdatum))

print("Teilnehmerliste Alter")

# 4) Für alle Teilnehmer das Alter ermitteln -> Teilnehmerliste
altersangaben = []
for teilnehmer in teilnehmerliste:
    altersangaben.append(my_pycurse_utilities.alter(teilnehmer[2]))

print(altersangaben)

# 5) Durchsnittliches Alter
zwischensumme = sum(altersangaben)
durchschnitt = zwischensumme/ len(altersangaben)
print(durchschnitt)

# 6) Median der Altersangabe
print(statistics.median(altersangaben)) #Median-Wert der Altersgaben
print(statistics.mean(altersangaben)) #Durchschnitt-Wert der Altersangaben