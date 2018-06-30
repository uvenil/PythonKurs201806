# Wörterbuch/Dictionary, Hashtabelle/Hashtable/Hashmap, assoziatives Array

d = {"Tisch": "table",
     "Stuhl": "chair",
     "Schreibtisch": "desk"}

# Ziel: weiteres Wörterbuch aufbauen, das als Schlüssel englische Begriffe enthält

# 1. Ansatz
l = []
for tupel in d.items():
    l.append((tupel[1], tupel[0]))

print(l)
e = dict(l)
print(e["chair"])

#2. Ansatz
l =[]
l = [((tupel[1]), tupel[0]) for tupel in d.items()]

print(l)
e = dict(l)
print(e["table"])


#3. Ansatz
e = {}
for key, value in d.items():
    e[value] = key

print(e["desk"])

