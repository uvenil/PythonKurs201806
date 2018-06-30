from datetime import date
from p01_kennenlernen import mybib
import statistics

"""
Teilnehmerliste(n)
"""
# variable      [0]             [1]             [2]               [3]
torsten =   ["Torsten",     "Aachen",       date(1967,1,1),     ["C"]]
michael =   ["Michael",     "Moormerland",  date(1981,1,10),    ["Python"]]
karpoo =    ["Karpoo",      "Düsseldorf",   date(1969,1,1),     ["ABAP"]]
carsten =   ["Carsten",     "Aachen",       date(1971,2,3),     ["Basic"]]
thomas =    ["Thomas",      "Bielefeld",    date(1964,10,12),   ["Pascal"]]
angela =    ["Angela",      "Lingen",       date(1983,12,31),   ["C, Java"]]
jonas =     ["Jonas",       "Löhne",        date(1997,4,4),     []]
marco =     ["Marco",       "Bielefeld",    date(1975,6,24),    []]
roman =     ["Roman",       "Hannover",     date(1984,2,28),    []]
daniel =    ["Daniel",      "Bielefeld",    date(1980,1,1),     ["Python"]]

teilnehmerliste = [torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel]

"""
Programmbegin
"""

# 0) Wieviele Teilnehmer?

#anzahl = len(teilnehmerliste)
#print ("Anzahl Teilnehmer=", anzahl)


# 1) Alle Teilnehmer aus Bielefeld
for teilnehmer in teilnehmerliste:          #Schleife, lies: "für jeden teilnehmer in der Liste teilnehmerliste wiederhole:"
    print(teilnehmer)
print()


# 2) Alle Teilnehmer aus Bielefeld
for teilnehmer in teilnehmerliste:
    if teilnehmer[1] == "Bielefeld":  # == entspricht Vergleich auf Gleichheit
        print(teilnehmer)

print()

# 3) Wie alt sind die Teilnehmer?
geburtsdatum = date(2000,1,1)
print(mybib.alter(geburtsdatum))

print()

# 4) Für alle teilnehmer Alter ermitteln
altersangaben = []
for teilnehmer in teilnehmerliste:
    altersangaben.append(mybib.alter(teilnehmer[2]))
print(altersangaben)

# 5) Durschnittliches Alter
print(altersangaben)
durchschnitt =  sum(altersangaben)/len(altersangaben)
print("Avg. Age:",durchschnitt)


# 6) Median
print("Alters median", statistics.median(altersangaben))



print("End of Program")