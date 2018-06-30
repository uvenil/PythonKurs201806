# Aufgabe:
# http://exercism.io/exercises/python/isbn-verifier/readme

# Prüfe, ob isbn eine gültige ISBN-Nummer ist
def verify(isbn):
    x = [None]
    for i in isbn:
        try:
            i = int(i)
            x.append(i)
        except ValueError:
            if isbn[-1] == "X" and i == "X":
                i = 10
                x.append(i)
    print(x)
    if len(x) == 11 and (x[1] * 10 + x[2] * 9 + x[3] * 8 + x[4] * 7 + x[5] * 6 + x[6] * 5 + x[7] * 4 + x[8] * 3 + x[9] * 2 + x[10] * 1) % 11 == 0:
        return True
    else:
        return False

isbn = "3-598-2X507-9"
print(verify(isbn))

