dictionary = {"Tisch": "table",
              "Stuhl": "chair",
              "Schreibtisch": "Desk"}

# 1) Wert aus einem Dictionary via Schlüssel ausgeben
print(dictionary["Stuhl"])

deutsch = input("Deutsches Wort:")
print("Du hast eingegeben:", deutsch)


# 1 LBYL (Look Before You Leap)
if deutsch in dictionary:
    englisch = dictionary[deutsch]
    print("Englisch:", englisch)
else:
    print("Unbekanntes Wort!")

#2 Try & Catch
try:
    englisch = dictionary[deutsch]
    print("Englisch:", englisch)
except KeyError:
    print("Unbekanntes Wort!")