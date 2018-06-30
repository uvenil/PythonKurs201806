# Aufgabe:
# http://exercism.io/exercises/python/isbn-verifier/readme

isbn = []
# Trenner "-" entfernen
def trennerentf(isbn):
    for c in isbn:
        if c == int:
            isbn.append(int(c))
    return isbn

# Prüfe Länge mehr oder weniger als 10 Stellen
def pruefelaenge(isbn):
    if len(isbn) > 10:
        return False

# Prüfe, ob isbn eine gültige ISBN-Nummer ist
def verify(isbn):
    trennerentf(isbn)
    if not pruefelaenge(isbn) and ((isbn[0] * 10 + isbn[1] * 9 + isbn[2] * 8 + isbn[3] * 7 + isbn[4] * 6 + isbn[5] * 5 + isbn[6] * 4 + isbn[7] * 3 + isbn[7] * 2 + isbn[9] * 1) % 11 == 0):
        return True
    else:
        return False


if __name__ == '__main__':
    testisbn = [1, 2, '-', 4, 5, 6, 7, 8, 'A', 10]
    isbnresult = trennerentf(testisbn)
    print(isbnresult)