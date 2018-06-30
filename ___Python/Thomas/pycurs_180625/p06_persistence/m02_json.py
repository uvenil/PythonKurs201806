import json

#json.dumps(anObject, default=json_util.default)

from p01_kennenlernen.m01_kennenlernen import teilnehmerliste

with open("teilnehmer.json", "w") as datei:
    json.dumps(teilnehmerliste, datei, default=str) # In diesem Beispiel werden Datumsangaben nicht exportiert -> Umwandlung aller Daten in strings

with open("teilnehmer.json", "b") as datei:
    liste = json.load(datei)

print(liste)