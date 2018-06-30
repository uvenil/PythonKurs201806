# Wörterbuch (Dictionary, Hashtabelle, Hashtable, Hashmap, associative Array)
dic_wb1 = {"Tisch": "table",
         "Stuhl": "chair",
         "Schreibtisch": "desk"}

for wort in dic_wb1:
    print(dic_wb1[wort])

# Aus einem Wörterbuch einen Wert anhand des Schlüssels ermitteln
#print(wbuch["Stuhl"])

deutsch = input("Deutsches Wort?:")
print("Du hast eingegeben: "+ deutsch)
# Fehlerbehandlung Ansatz1 (Look Before You Leap)
if deutsch in dic_wb1:
    english = dic_wb1[deutsch]
    print("English: " + english)
else:
    print('Keine Überstzung vorhanden')

# Fehlerbehandlung Ansatz2 (it's easier to ask for forgiveness than for Permission)
try:
    english = dic_wb1[deutsch]
    print('English: ' + english)
except KeyError:
    print('Keine Übersetzung vorhanden (exception)')

eingabe = " *Stuhl* "
# Leerzeichen entfernen
eingabe = eingabe.strip(" ")
print(eingabe)

