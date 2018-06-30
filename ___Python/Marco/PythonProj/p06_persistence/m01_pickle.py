import pickle

from p01.m_01 import teilnehmerliste

# pickling
with open("teilnehmer.pickles", "wb") as datei:
    pickle.dump(teilnehmerliste, datei)

#unpickling
with open ("teinehmer.pickle", "rb") as datei:
    liste = pickle.load(datei)

print(liste)
