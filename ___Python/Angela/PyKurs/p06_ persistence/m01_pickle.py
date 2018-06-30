import pickle

from p01_kennenlernen.m01_kennenlernen import teilnehmerliste

# "Pickling" / Serialization / Marshalling / Flattening
with open("teilnehmer.pickle", "wb") as datei:     # write binary
    pickle.dump(teilnehmerliste, datei)             # das ganze Modul wird ausgefuehrt

# "Unpickling" / Deserialization / Unmarshalling
with open("teilnehmer.pickle", "rb") as datei:     # write binary
    liste = pickle.load(datei)

print(liste)