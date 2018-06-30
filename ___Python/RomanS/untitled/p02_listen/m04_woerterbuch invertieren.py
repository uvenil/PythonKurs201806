d = {"Tisch": "table",
    "Stuhl": "chair",
    "Schreibtisch": "desk"}

# Ziel: Weiteres Dict aufbauen, das als Schlüssel (Key) englische Begriffe enthält.

print()
print("Start")
print(d.items())  # Ausgabe erzeugt die TUPEL ('Tisch', 'table'), ('Stuhl', 'chair'), ('Schreibtisch', 'desk')

# 1.) Ansatz:

l = []
for tupel in d.items():
    l.append((tupel[1], tupel[0]))

print(l)

e = dict(l)
print(e["chair"])

# 2. Ansatz: List Comprehension ???
#l=[]
#print(l)
#e=dict(l)
#print(e["chair"])


# 3. Ansatz:
for key, value in d.items():
    e[value] = key



print()
print("End of Program")
