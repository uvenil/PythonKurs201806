def ausgabe(liste, ende="\n", erstezeile=""):
    print(erstezeile)
    for element in liste:
        print(element, end=ende)


def ausgabe2(liste, **kwargs):
    ende = "\n" if "ende" not in kwargs else kwargs["ende"]
    erstezeile = "" if "erstezeile" not in kwargs else kwargs["erstezeile"]

    print(erstezeile)
    for element in liste:
        print(element, end=ende)

einkaufsliste = ["Milch", "Eier", "Bier"]
ausgabe(einkaufsliste)
ausgabe(einkaufsliste, " ")
print()
ausgabe(einkaufsliste, " ", "Meine Einkaufsliste:")

###


ausgabe2(einkaufsliste)
ausgabe2(einkaufsliste,ende = " ")
print()
ausgabe2(einkaufsliste, erstezeile = "Meine Einkaufsliste:")
