import random

r = random.Random()

# 1) PI annähern
n = 100000
c = 0
for i in range(n):
    x, y = r.uniform(0, 1), r.uniform(0, 1)
    if (x**2 + y**2) ** 0.5 <= 1:
        c += 1

print(4 * c / n)

# 2) Check, ob zwei Polynome gleich sind

def p1(x):
    return x ** 2 + 7 * x + 12

def p2(x):
    return (x + 3) * (x + 4)

def sindGleich(p1, p2):
    n = 10 ** 20
    x = r.randint(-n, n)
    return p1(x) == p2(x)

print(sindGleich(p1, p2))

# 3) Check, ob eine Zahl eine Primzahl ist
