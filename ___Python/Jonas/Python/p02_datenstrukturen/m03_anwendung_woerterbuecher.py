satz = "Fischers Fritze fischt frische Fische"
# 1Häufigkeit des Buchstabens e

# Ansatz 1) for-Schleife und Zähler anzahl
zaehler = 0
for zeichen in satz:
    if zeichen == "e":
        zaehler += 1
print (zaehler)

# 2 Häufigkeitsverteilung der buchstaben im satz
d = {}
for zeichen in satz:
    if zeichen in d:
        d[zeichen] += 1
    else:
        d[zeichen] = 1

print(d)

try:
    d[zeichen] += 1
except KeyError:
    d[zeichen] = 1

print(d)

# 3 Sortieren nach Häufigkeit
print(sorted(d)) #Lambdas
print(sorted(d.items(), key=lambda tupel: tupel[1], reverse=True))
