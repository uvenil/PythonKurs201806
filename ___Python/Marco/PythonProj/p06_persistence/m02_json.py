import json

from p01.m_01 import teilnehmerliste

# "Pickling" / Serialization / Marshalling / Flattening
with open("teilnehmer.json", "w") as datei:
    json.dump(teilnehmerliste, datei, default=str)

# "Unpickling" / Deserialization / Unmarshalling
with open("teilnehmer.json", "r") as datei:
    liste = json.load(datei)

print(liste)
