def ausgabe(liste, seperator="\n", erstezeile=""):
    print(erstezeile)
    for element in liste:
        print(element, end=seperator)

def ausgabe2(liste, **kwargs):
    seperator = "\n" if "ende" not in kwargs else kwargs["ende"]
    erstezeile = " " if "erstezeile" not in kwargs else kwargs["erstezeile"]
    print(erstezeile)
    for element in liste:
        print(element, end=seperator)

einkaufsliste = ["Milch", "Einer", "Bier"]
ausgabe(einkaufsliste)
ausgabe(einkaufsliste, " ")
print()
ausgabe(einkaufsliste, " ", "Meine Einkaufsliste")