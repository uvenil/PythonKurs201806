# Wörterbuch/Dictionary (Schlüssel-Wert-Paare), Hashtabelle/Hashtable/Hashmap, assoziatives Feld/associative Array

d = {"Tisch": "table",
     "Stuhl": "chair",
     "Schreibtisch": "desk"
    }

print(d["Stuhl"])

deutsch = input("Deutsches Wort? ")
print("Du hast eingegeben: " + deutsch)

# Ansatz 1: LBYL (Look before you leap)
if deutsch in d:
    english = d[deutsch]
    print("Englisch: " + english)
else:
    print("Keine Übersetzung vorhanden!")

# Ansatz 2: EAFP (it´s Easier to Ask for Forgiveness than for Permission
try:
    english = d[deutsch]
except KeyError:
    print("Keine Übersetzung vorhanden!")

# 1)
eingabe = " Stuhl "
eingabe = eingabe.strip()
print(eingabe)

# 2)