satz = "Fischers Fritze fischt frische Fische"
# Häufigkeit Buchstabe e

# 1. Ansatz: for-schleife und Zähler
zaehler = 0
for zeichen in satz:
    if zeichen == "e":
        zaehler += 1
print (zaehler)

# Häufigkeit der Buchstaben im Satz
dic_m03 = {}
for zeichen in satz:
    if zeichen in dic_m03:
        dic_m03[zeichen] += 1
    else:
        dic_m03[zeichen] = 1
print("Dictonray unsortiert "+str(dic_m03))
print("")

# Sortieren nach Häufigkeit
dic_m03 = sorted(dic_m03.items(), key=lambda tupel: tupel[1], reverse=True)
print("Dictonray sortiert   "+str(dict(dic_m03)))
