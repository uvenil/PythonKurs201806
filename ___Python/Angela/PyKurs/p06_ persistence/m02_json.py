import json

from p01_kennenlernen.m01_kennenlernen import teilnehmerliste

# "Pickling" / Serialization / Marshalling / Flattening
with open("teilnehmer.json", "w") as datei:     # write
    json.dump(teilnehmerliste, datei, default=str)             # das ganze Modul wird ausgefuehrt; Datumsangaben nun als string
    # TypeError: Object of type 'date' is not JSON serializable

# "Unpickling" / Deserialization / Unmarshalling
with open("teilnehmer.json", "r") as datei:     # write
    liste = json.load(datei)

print(liste)