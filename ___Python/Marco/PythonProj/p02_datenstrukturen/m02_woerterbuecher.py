# Wörterbuch/Dictionary (Paare von Schlüsseln und Werten), Hashtabelle/Hashtable/Hashmap, assoziatives Feld/accociative Array

d = {"Tisch": "table",
     "Stuhl": "chair",
     "Schreibtisch": "desk"}

# Aus einem Wörterbuch einen Wert anhand eines Schlüssels ermitteln:
# print(d["Stuhl"])

deutsch = input ("Deutsches Wort?")
print("Du hast eingegeben: " + deutsch)

#  Ansatz 1: LBYL (Look before you leap)
if deutsch in d: #Prüfe, ob der Schlüssel im Wörterbuch d vorhanden ist
    english = d[deutsch]
    print("English: "+ english)
else:
    print("Keine Übersetzung vorhanden.")

# Ansatz 2: EAFPL (it´s easier to ask for forgivness than for permission)
try:
    english = d[deutsch]
    print("English: "+ english)
except KeyError:
    print("Keine Übersetzung vorhanden.")

    #######

    eingabe = " Stuhl "
# 1) Führende/Nachfolgende Leerzeichen entfernen
eingabe = eingabe.strip(" ")
print(eingabe)

# 2) Alle Nichtbuchstaben entfernen: reguläre Ausdrücke
