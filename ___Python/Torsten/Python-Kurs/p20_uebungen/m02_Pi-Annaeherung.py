import random

from math import sqrt


# Ansatz 1:
r = random.Random()
n = 1000000
innerhalb = 0

for i in range(n):
    (x, y) = (r.uniform(-1, 1), r.uniform(-1, 1))

    radius = sqrt(x**2 + y**2)

    if radius <= 1:
        innerhalb += 1

print(4 * innerhalb / n)


# Ansatz 2:

def p1(x):
    return x ** 2 + 7 * x + 12

def p2(x):
    return (x + 3) * (x + 4)

def sindGleich(p1, p2):
    n = 10 ** 20
    x = r.randint(-n, n)
    return p1(x) == p2(x)

print(sindGleich(p1, p2))


