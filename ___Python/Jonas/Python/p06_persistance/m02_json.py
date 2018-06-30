import json

from p01_kennenlernen.m01_kennenlernen import teilnehmerListe


# pickling / serialization / marshalling / flattening
with open("teilnehmer.json", "w") as datei:
    json.dump(teilnehmerListe, datei, default=str) # Datumsangaben werden als string serialisiert

# unpickling / deserialization / unmarshalling
with open("teilnehmer.json", "r") as datei:
    liste = json.load(datei)

print(liste)
