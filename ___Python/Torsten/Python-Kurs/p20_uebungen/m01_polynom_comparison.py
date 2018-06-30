import random

def p1(x):
    return x**2 + - 3*x - 28

def p2(x):
    return (x + 4) * (x - 7)

def sindGleich(a, b):
    r = random.Random()
    for i in range(100000):
        zahl = r.randint(-100, 100)

        if a(zahl) != b(zahl):
            return False

    return True

print(sindGleich(p1, p2))