d = {"Tisch": "table",
     "Stuhl": "chair",
     "Schreibtisch": "desk"}

# Ziel: Weiteres Wörterbuch aufbauen, das als Schlüssel englische Begriffe enthält.

# 1. Ansatz:
l = []
for tupel in d.items():
    l.append((tupel[1], tupel[0]))

# 2. Ansatz:
l = [] # List Comprehension

print(l)
e = dict(l)
print(e["chair"])

# 3. Ansatz:
e = {}
for key, value in d.items():
    e[value] = key
