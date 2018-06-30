#1) PI annähern
import random, math

random.seed()
treffer = 0

#z = input("Anzahl Durchlaeufe: ")
anzahl = 1000

for i in range(anzahl):
    x = random.random()
    y = random.random()
    z = math.sqrt(x ** 2 + y ** 2)
    if z < 1:
        treffer += 1

print("PI in Naeherung bei", anzahl, "Durchlaeufen: ", 4 * treffer / anzahl)
print("Abweichung: " + str(round(100 * abs(1 - (4 * treffer / anzahl) / math.pi), 2)) + "%")

#2) check, ob zwei Polynome gleich sind


def p1(x):
    return x ** 2 + 7 * x + 13

def p2(x):
    return (x + 3) * (x + 4)

def sindGleich(p1, p2):
    mehr = 0
    for i in range(anzahl):
        x = random.randint(0, 1)
        if p1(x) != p2(x):
            mehr += 1
    if mehr != 0:
        return False
    return True

gleich = sindGleich(p1, p2)
print()
print("Funktionen sind gleich: ", gleich)

#3) check, ob eine Zahl eine Primzahl ist
anzahl = 1000
Zahl = 98

for i in range(anzahl):
    x = random.randint(0, Zahl/2)
    print (x)
    if Zahl % x == 0:
        print(Zahl, "scheint keine Primzahl zu sein")
    else:
        print("nach ", i, " Versuchen, scheint es eine Primzahl zu sein !")
