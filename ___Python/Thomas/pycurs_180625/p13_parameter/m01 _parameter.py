def ausgabe(liste, ende="\n"):
    for element in liste:
        print(element, end=ende)

einkaufsliste = ["Milch", "Eier", "Bier"]
print(einkaufsliste)


def ausgabe2(liste, **kwargs):
    ende = "\n" if "ende" not in kwargs else kwargs["ende"]
    erstezeile = "\n" if "erstezeile" not in kwargs else kwargs["erstezeile"]
    print(erstezeile)
    for element in liste:
        print(element, end=ende)


einkaufsliste = ["Milch", "Eier", "Bier"]
ausgabe2(einkaufsliste, erstezeile = "Meine Einkaufsliste")


def mittelwert(liste):
    return sum(liste)/ len(liste)

def mittelwert2(liste):
    return sum(liste)/ len(liste)

print(mittelwert([3,4,5]))
#print(mittelwert2(3,4,5))