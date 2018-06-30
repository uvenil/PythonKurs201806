import random

r = random.Random()       #Modul random mit Klasse Random, r=Wuerfel
def wuerfeln():
    return r.randint(1, 6)

def lotto():
    return r.randint(1, 49)

def muenzwurf():
    return r.randint(0, 1)  # 0 = Kopf, 1 = Zahl

def wuerfeln2():
    return muenzwurf()

print(wuerfeln())

# Test auf Wahrscheinlichkeitsverteilung
d = {}
for i in range(100000):
    augenzahl = wuerfeln()
    if augenzahl in d:
        d[augenzahl] += 1
    else:
        d[augenzahl] = 1

print(d)

# 1) Lottozahlen 6 aus 49 ermitteln

# Lösung a)
l = []
kugel = 0
while kugel < 6:
    lottozahl = lotto()
    if not lottozahl in l:
        l.append(lottozahl)
        kugel += 1

print(sorted(l))


# Lösung b)

urne = list(range(1, 50))   # urne = [1, 2, ..., 49]
lottoziehung = []
for i in range(6):
    ziehung = urne.pop(r.randint(0, len(urne)) - 1)
    lottoziehung.append(ziehung)

print(sorted(lottoziehung))


# Lösung c) Geeignete Methode aus random benutzen
lottoziehung = r.sample(range(1, 50), 6)

print(sorted(lottoziehung))




# 2) Schreibe eine Funktion wuerfeln2, die fair wuerfelt.
# Bei der Implementierung darf nur die Funktion muenzwurf benutzt werden


def wuerfeln2():
    binaer = 1
    for i in range(3):
        binaer += 2 ** i * muenzwurf()
    if binaer > 6:
        return wuerfeln2()
    return binaer