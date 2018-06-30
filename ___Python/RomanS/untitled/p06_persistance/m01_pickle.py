import pickle

from p01_kennenlernen.m01_kennenlernen import teilnehmerliste

# "Pickling" / Serilization / Marshalling / Flattening
with open("teilnehmer.pickle", "wb") as datei:
    pickle.dump(teilnehmerliste, datei)


# "Unpickling" / Unserilization / Unmarshalling / De? Flattening
with open("teilnehmer.pickle", "rb") as datei:
    liste = pickle.load(datei)
print(liste)


