import random

r = random.Random()
# 1) PI annähern
for i in range(1000):
    x, y =r.uniform(0, 1), r.uniform(0, 1)
    if (x**2 + y**2) ** <= 1:
        c +=1

print(4 * c /n)


# 2) Check ob zwei Polynome gleic sind

def p1(x):
    return x ** 2 + 7 * x

def p2 (x):
    return (x + 3) * (x + 4)

def sindGleich(p1, p2):
    n = 10** 20
    x = r.randint(-n, n)
    return  p1(x)

sindGleich


# 3) Check, ob eine Zahl eine Prinzahl ist