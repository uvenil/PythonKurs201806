import json

from p01_kennenlernen.m01_kennenlernen import teilnehmerliste

# "Pickling" / Serialization / Marshalling / Flattening
with open("teilnehmer.json", "w") as datei:
    json.dump(teilnehmerliste, datei, default=str) # Datumsangaben werden hier als string serialisiert

# "Unpickling" / Deserialization / Unmarshalling
with open("teilnehmer.json", "r") as datei:
    liste = json.load(datei)

print(liste)
