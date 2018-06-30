import pickle

from p01_kennenlernen.m01_kennenlernen import teilnehmerListe


# pickling / serialization / marshalling / flattening
with open("teilnehmer.pickle", "wb") as datei:
    pickle.dump(teilnehmerListe, datei)

# unpickling / deserialization / unmarshalling
with open("teilnehmer.pickle", "rb") as datei:
    liste = pickle.load(datei)

print(liste)