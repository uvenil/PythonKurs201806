d = {"Tisch": "table",
              "Stuhl": "chair",
              "Schreibtisch": "Desk"}

# 1) Werte und Schlüssel vertauschen
# Ansatz 1
e = {}
for key, value in d.items():
    e[value] = key

print(e)


# Ansatz 2
l = []
e = {}

for tupel in d.items():
    l.append((tupel[1], tupel[0]))

e = dict(l)
print(e)


# 3) List-Comprehension

e = {}
l = []
l = [(tupel[1], tupel[0]) for tupel in d.items()]
e = dict(l)
print(l)
print(e)

e = {}
e = dict([(value, key) for key, value in d.items()])

print(e)