# 1) Fakultät

# iterative Definition
# n! = 1 * 2 * 3 * ... * (n-1) * n
# 5! = 1 * 2 * 3 * 4 * 5   (Lies: "5 Fakultät")
# 4! = 1 * 2 * 3 * 4
# 3! = 1 * 2 * 3
# 2! = 1 * 2
# 1! = 1
# 0! = 1

def fak_iter(n):
    erg = 1
    for i in range(1, n + 1):
        erg *= i
    return erg

print(fak_iter(4))


# rekursive Definition
# n! = n * (n - 1)!, für n >= 1     (in Teilprobleme auflösen, am Ende wieder zusammen setzen)
# 0! = 1                            (Abbruchbedingung)

def fak_rek(n):
    if n == 0:
        return 1
    else:
        return n * fak_rek(n - 1)

print(fak_rek(4))