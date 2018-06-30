import json
from p01_kennenlernen.m01_kennenlernen import teilnehmerliste

# Schreiben
with open("teilnehmer.json", "w") as datei:
    json.dump(teilnehmerliste, datei, default=str) # Datumsangaben werden als string serialisiert

# Lesen
with open("teilnehmer.json", "r") as datei:
    liste = json.load(datei)

print(liste)