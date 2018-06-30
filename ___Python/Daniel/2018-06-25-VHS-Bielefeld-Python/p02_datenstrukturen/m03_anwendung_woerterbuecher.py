satz = "Fischers Fritze fischt frische Fische"
# 1) Häufigkeit des Buchstabens e
# for-Schleife und Zähler anzahl
zaehler = 0
for zeichen in satz:
    if zeichen == "e":
        zaehler += 1

print(zaehler)

# 2) Häufigkeitsverteilung der Buchstaben im satz
d = {}
for zeichen in satz:
    if zeichen in d:
        d[zeichen] += 1
    else:
        d[zeichen] = 1

print(d)

# 3) Sortieren nach Häufigkeit
print(d.items())
print(sorted(d.items(), key=lambda tupel: tupel[1], reverse=True))


