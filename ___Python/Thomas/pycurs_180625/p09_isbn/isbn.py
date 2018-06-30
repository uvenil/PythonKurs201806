# Aufgabe:
# http://exercism.io/exercises/python/isbn-verifier/readme

# Prüfe, ob isbn eine gültige ISBN-Nummer ist
import re


def verify(isbn):

    print(isbn)
    list_isbn = []
    for chr_isbn in isbn:
        try:
            i_isbn = int(chr_isbn)
            if i_isbn in range(10):
                list_isbn.append(i_isbn)
        except ValueError:
            pass
        if len(list_isbn) == 10:
            i_cl = 10
            i_check_isbn = 0
            while i_cl > 0:
                i_check_isbn += list_isbn[i_cl-1]*i_cl
                i_cl -= 1
            if i_check_isbn % 11 == 0:
                return True
        else:
            return False
    return False

#if verify('3-598-21507-8'):
#    print('Richtig')
#else:
#    print('Falsch')

# def verify(isbn):
#     if len(isbn < 10):
#         return False
#     check_digit = isbn[-1]
#     if not(check_digit in range(0, 9) or check_digit == 'X'):
#         return False
#     if check_digit =='X':
#         check_digit = 10
#     else:
#         check_digit = int(check_digit)
#     pre = isbn[:-1] #entferne letzte Stelle
#     pre = re.sub('[^0-9]', '', pre)
#     print(pre)
#     if len(pre) !=9:
#         return False
#
#     sum = 0
#     for i in range(9):
#         sum += int(pre[i]* (10-i)
#     sum += check_digit
#
#     return sum % 11 == 0


print(verify('3-598-P1581-X'))