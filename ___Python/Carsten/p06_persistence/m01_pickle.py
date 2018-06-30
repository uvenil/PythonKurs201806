import pickle

from p01_kennenlernen.m01_kennenlernen import teilnehmerliste

# "pickling"
with open("teilnehmer.pickle", "wb") as datei:
    pickle.dump(teilnehmerliste, datei)

# "unpickling"
with open("teilnehmer.pickle", "rb") as datei:
    liste = pickle.load(datei)

print(liste)

