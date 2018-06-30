import random

r = random.Random()
def wuerfeln():
    return r.randint(1, 6) # Augenzahl zwischen 1 und 6

def muenzwurf():
    return r.randint(0, 1) # 0 = Kopf, 1 = Zahl

def kugel():
    return r.randint(1, 49)

d = {}
for i in range(100000):
    augenzahl = wuerfeln()
    if augenzahl in d:
        d[augenzahl] += 1
    else:
        d[augenzahl] = 1

print(d)

# 1) Lottozahlen 6 aus 49 ermitteln ==> [2, 7, 13, 17, 19, 42]

# Lösung a)
kugeln = 0
menge = set() # Menge der bereits gezogenen Kugeln
lottoziehung = []
while kugeln < 6:
    ziehung = kugel()
    if ziehung not in menge: # Diese Kugel wurde zuvor noch nicht gezogen
        lottoziehung.append(ziehung)
        menge.add(ziehung) # Diese Kugel darf nicht noch einmal gezogen werden, deshalb landet sie in der Menge der zuvor gezogenen Kugeln
        kugeln += 1

print(sorted(lottoziehung))

# Lösung b) Ansatz "Lottofee"
urne = list(range(1, 50)) # urne = [1, 2, 3, ..., 49]
lottoziehung = []
for i in range(6):
    ziehung = urne.pop(r.randint(0, len(urne)) - 1)
    lottoziehung.append(ziehung)

print(sorted(lottoziehung))

# Lösung c) Geeignete Methode aus random benutzen
lottoziehung = r.sample(range(1, 50), 6)
print(sorted(lottoziehung))

# 2) Schreibe eine Funktion wuerfeln2, die fair würfelt.
# Bei der Implementierung darf nur die Funktion muenzwurf benutzt werden
