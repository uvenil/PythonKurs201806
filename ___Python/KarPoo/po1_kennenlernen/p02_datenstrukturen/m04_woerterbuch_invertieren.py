# Wörterbuch/Dictionary (Paare von Schlüsseln und Werten), Hashtabelle/Hashtable/Hashmap, assoziatives Feld/associative Array

d = {"Tisch": "table",
     "Stuhl": "chair",
     "Schreibtisch": "desk"}

print(d.items())
print()

# Ziel: Weiteres Wörterbuch aufbauen, das als Schlüssel englische Begriffe enthält.

# 1. Ansatz:
l = []
for tupel in d.items():
    l.append((tupel[1], tupel[0]))

print(l)
e = dict(l)
print(e["chair"])
print()

# 2. Ansatz:
l = [((tupel[1], tupel[0])) for tupel in d.items()] #List Comprehension

print(l)
e = dict(l)
print(e["chair"])
print()

# 3. Ansatz:
e = {}
for key, value in d.items():
    e[value] = key

print(e.items())
print(e["chair"])
print()