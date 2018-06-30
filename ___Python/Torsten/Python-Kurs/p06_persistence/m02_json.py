import json

from p01_kennenlernen.m01_kennenlernen import teilnehmerliste

# date-Objekt wird in String gewandelt

# Pickling
with open("teilnehmer.json", "w") as datei:
    json.dump(teilnehmerliste, datei, default=str)

# Un-Pickling
with open("teilnehmer.json", "r") as datei:
    liste = json.load(datei)

print(liste)



