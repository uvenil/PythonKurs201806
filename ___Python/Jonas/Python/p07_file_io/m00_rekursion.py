#Probleme in Teilprobleme unterteilen und so weiter
# 1) Fakultät
#iterative Definition
# n! = 1*2*3 ... * (n-1) * n
# 5! = 1*2*3*4*5(lise "5 fakultät")
# 4! = 1*2*3*4
# 1! = 1
# 0! = 1

#rekursive Definition:
# n! = n * (n-1)! für n >= 1
# 0! = 1

def fak(n): #rekursiv
    if n == 0:
        return 1
    else :
        return n * fak(n - 1)

print(fak(4))

def fak_iter(n): #iterativ
    erg = 1
    for i in range(1, n + 1): # +1 weil obergrenze nicht zählt
        erg *= i

    return erg

print(fak_iter(4))