import json
# from bson import json_util

from p01_kennenlernern.m01_kennenlernen import teilnehmerliste

with open("teilnehmer.json", "w") as datei:
    json.dump(teilnehmerliste, datei, default=str)

with open("teilnehmer.json", "r") as datei:
    liste = json.load(datei)

print(liste)
