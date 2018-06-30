d = {"Tisch": "table",
     "Stuhl": "chair",
     "Schreibtisch": "desk"}

# Ziel: Weiteres Woerterbuch aufbauen, das als Schluessel englische Begriffe enthaelt
# print(d.items())

# 1. Ansatz
l = []
for tupel in d.items():
    l.append((tupel[1], tupel[0]))

print(l)
e = dict(l)
print(e["chair"])

# 2. Ansatz
l = [(tupel[1], tupel[0]) for tupel in d.items()] # List Comprehension

print(l)
e = dict(l)
print(e["chair"])

# 3. Ansatz
e = {}
for key, value in d.items():
    e[value] = key