import json
import bson
from bson import json_util

from p01_kennenlernen.m01_kennenlernen import teilnehmerliste

# "Pickling" / Serilization / Marshalling / Flattening
with open("teilnehmer.json", "w") as datei:
    json.dump(teilnehmerliste, datei)


# "Unpickling" / Unserilization / Unmarshalling / De? Flattening
with open("teilnehmer.json", "r") as datei:
    liste = json.load(datei)
print(liste)

# It's buggy!!!