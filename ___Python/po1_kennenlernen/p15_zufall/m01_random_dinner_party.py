# 3) Check ob Zahl eine Primzahl ist
eingabe = input("Zahl: ")

def modexp(m, e, n):
    if e==0:
        return 1
    if e%2==1:
        return modexp(m, e-1, n)*m % n
    else:
        return modexp(m, e//2, n)**2 % n

# Fermat-Test
def isCompositeFermat(n):
    n = int(eingabe)
    return modexp(2, n-1, n) != 1

if isCompositeFermat(eingabe) is True:
    print(eingabe + " ist keine Primzahl")
else:
    print(eingabe + " ist eine Primzahl")