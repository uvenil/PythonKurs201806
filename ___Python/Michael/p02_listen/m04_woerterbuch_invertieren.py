d = {"Tisch": "table",
     "Stuhl": "chair",
     "Schreibtisch": "desk"
    }

# Ziel: Weiteres Wörterbuch aufbauen, das englische Begriffe als Schlüssel enthält

print(d.items())
print()

# 1. Ansatz:
l = []
for tupel in d.items():
    l.append((tupel[1], tupel[0]))

print(l)
e = dict(l)
print(e)
print()

# 1b. Ansatz:
l = []
for key, value in d.items():
    l.append((value, key))

print(l)
e = dict(l)
print(e)
print()

# 2. Ansatz:
# l = [] # List Comprehension
l = [(tupel[1], tupel[0]) for tupel in d.items()]
print(l)
e = dict(l)
print(e)
print()

#3. Ansatz:
e = {}
for key, value in d.items():
    e[value] = key

print(e)
print()
