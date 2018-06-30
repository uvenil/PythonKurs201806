# Aufgabe:
# http://exercism.io/exercises/python/isbn-verifier/readme

# (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0

# Prüfe, ob isbn eine gültige ISBN-Nummer ist

def verify(isbn):
    sum = 0
    i = 10
    for c in isbn:
        try:
            z = int(c)
        except:
            if (c == "X" and i == 1):
                z = 10
            else:
                continue
        sum += z * i
        i -= 1
        if (i == 0):
            return (sum % 11 == 0)

def test():
    testisbn = "3-598-21508-8"
    testisbn2 = "3-598-21507-X"

    test = verify(testisbn)
    test2 = verify(testisbn2)
    print(test)
    print(test2)

test()

# Methode String.isdigit