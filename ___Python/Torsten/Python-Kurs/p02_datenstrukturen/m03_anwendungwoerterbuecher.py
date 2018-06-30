satz = "Unsere Seminare sind anerkannt als Arbeitnehmerweiterbildung (Bildungsurlaub) nach dem AWbG für NRW. Angestellte und Arbeiter/Innen in NRW haben nach dem AWbG Anspruch auf fünf Tage Bildungsurlaub im Jahr."

# Häufigkeit von Buchstaben
d = {}
for zeichen in satz:
    if zeichen in d:
        d[zeichen] += 1
    else:
        d[zeichen] = 1

print(d)

# Sortieren nach Häufigkeit
print(sorted(d.items(), key = lambda tupel: tupel[1], reverse = True))