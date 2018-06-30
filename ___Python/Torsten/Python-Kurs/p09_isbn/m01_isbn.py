# Aufgabe:
# http://exercism.io/exercises/python/isbn-verifier/readme

# Prüfe, ob isbn eine gültige ISBN-Nummer ist
import re

def verify(isbn):
    if len(isbn) < 10:
        return False

    check_digit = isbn[-1] # letzte Stelle der Eingabe
    if check_digit == "X":
        check_digit = 10
    elif check_digit.isdigit():
        check_digit = int(check_digit) # gültige Prüfziffer ist 0, 1, 2, ..., 9 oder X
    else:
        return False

    pre = isbn[:-1] # entferne die letzte Stelle der Eingabe
    pre = pre.replace("-", "") # entferne Bindestriche
    if len(pre) != 9:
        return False

    pre = re.sub('[^0-9]', '', pre) # behalte nur Ziffern
    if len(pre) != 9:
        return False

    sum = 0
    for i in range(9):
        sum += int(pre[i]) * (10 - i)
    sum += check_digit

    return sum % 11 == 0