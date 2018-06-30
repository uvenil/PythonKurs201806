# 1) Fakultät
# iterative Definition
# n! =1*2*...* (n-1) *n
# 5! =1*2*3*4*5
# 4! =1*2*3*4
# ...
# 1! = 1
# 0! = 1

# rekursive Definition
# n! = n*(n-1)!, für n>=1
# 0! =1

#rekursiv
def fak(n):
    if n == 0:
        return 1
    else:
        return n * fak(n-1)

print(fak(4))

#iterativ
def fak_iter(n):
    erg = 1
    for i in range(1, n+1):
        erg *= i
    return erg

print(fak(4))
