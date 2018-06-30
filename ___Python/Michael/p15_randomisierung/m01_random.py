import random
import math

# 1)

def montecpi():
    runden = 1000000
    radius = 1000000
    piZaehler = 0
    for i in range(runden):
        x = random.randint(1, radius)
        y = random.randint(1, radius)
        k = math.sqrt(radius ** 2 - x ** 2) # y-Wert für Kreispunkt an x
        if (y <= k):
            piZaehler += 1

    return piZaehler / runden * 4

print(montecpi())
print()

# 2)

def p1(x):
    return x ** + 7 *x

def p2(x):
    return (x + 3) * (x + 4)

def sindGleich(p1, p2):
    for i in range(100):
        r = random.randint(1, 100000)
        v1 = p1(r)
        v2 = p2(r)
        if not v1 == v2:
            return False

    return True

print(sindGleich(p1, p2))


# 3)
def primzahl(z):
    for i in range(1000000):
        r = random.randint(2, z - 1)
        if (z % r == 0):
            return False

    return True

# print(primzahl(7))
# print(primzahl(263))
print(primzahl(24574754745848753837356875863))