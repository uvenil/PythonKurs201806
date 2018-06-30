# 1) pi annähern über random
import random
import math
r = random.random

inside = 0
total = 100000

for i in range (0, total):
    x = r()
    y = r()
    if (math.sqrt(x ** 2 + y ** 2) <= 1):
        inside += 1

pi = 4 * inside/total
print(pi)


# 2) Check, ob zwei Polynome gleich sind

def p1(x):
    return x ** 2 + 7 * x

def p2(x):
    return (x + 3) * (x + 4)

# 3) check, ob eine Zahl eine Primzahl ist

def isprime(n):
    if (n == 2):
        return True
    if (n == 3):
        return True
    if (n % 2 == 0):
        return False
    if (n % 3 == 0):
        return False

    i = 5
    w = 2

    while (i*i <= n):
        if (n % i == 0):
            return False
        i += w
        w = 6 - w

    return True

print(isprime(1110))