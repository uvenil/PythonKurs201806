def mittelwert(liste):
    return sum(liste)/len(liste)

def mittelwert2(*liste):
    return sum(liste)/len(liste)


print(mittelwert([3, 4, 5]))
print(mittelwert2(3, 4, 5))

def ausgabe(Liste, ende="\n"):
    for element in Liste:
        print(element, end=ende)

def ausgabe2(Liste, **kwargs):
    ende = "\n" if "ende" not in kwargs else kwargs["ende"]
    erstezeile = " " if "erstezeile" not in kwargs else kwargs["erstezeile"]
    print(erstezeile)
    for element in Liste:
        print(element, end=ende)

einkaufsliste = ["Milch", "Eier", "Bier"]
ausgabe(einkaufsliste)
ausgabe(einkaufsliste, " ")
print()

ausgabe2(einkaufsliste)

print()
ausgabe2(einkaufsliste, erstezeile = "asdf" )