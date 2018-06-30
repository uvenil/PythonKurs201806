# Wörterbuch/Dictionary (Paare von Schlüsseln und Werten), Hashtabelle/Hashtable/Hashmap, assoziatives Feld/ associative Array

d = {"Tisch": "table",
     "Stuhl": "chair",
     "Schreibtisch": "desk"}

# Aus einem Wörterbuch einen Wert anhand eines Schlüssels ermitteln
# print(d["Stuhl"])

deutsch = input("Deutsches Wort?")
print("Du hast eingegeben: " + deutsch)

# Ansatz 1: LBYL Look before you leap
if deutsch in d: # Prüfe, ob der schlüssel deutsch in Wörterbuch d vorhanden ist
    english = d[deutsch]
    print("English: " + english)
else:
    print("Keine Übersetzung vorhanden")

# Ansatz 2: EAFP It´s earsier to ask for forgiveness than for permission
try:
    english = d[deutsch]
    print("English: " + english)
except KeyError:
    print("Keine Übersetzung vorhanden")

#######

eingabe = " Stuhl "
# 1)führende/nachfolgende Leerzeichen entfernen
eingabe = eingabe.strip(" ")
print(eingabe)

# 2) alle Nichtbuchstaben entfernen: reguläre Ausdrücke
