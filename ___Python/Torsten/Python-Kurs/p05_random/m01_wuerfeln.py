import random

r = random.Random()

def wuerfeln():
    return r.randint(1, 6)

def muenzwurf():
    return r.randint(0, 1) # 0 > Kopf, 1 > Zahl

def kugel():
    return r.randint(1, 49)

def lottoziehung(anzahl):
    zahl = r.randint(1, 49)
    if zahl not in ziehung:
        ziehung.append(zahl)
        anzahl += 1

    if anzahl != 6:
        lottoziehung(anzahl)


d = {}
for i in range(100000):
    augenzahl = wuerfeln()

    if augenzahl in d:
        d[augenzahl] += 1
    else:
        d[augenzahl] = 1

print("Würfel klassisch:",d)


# 1) Lottozahlen ermittel für '6 aus 49'
# Ansatz A: WHILE
anzahl = 0
ziehung = []

while anzahl < 6:
    zahl = r.randint(1, 49)
    if zahl not in ziehung:
        ziehung.append(zahl)
        anzahl += 1

print("While-Schleife:",sorted(ziehung))


# Ansatz B: Rekursiv
anzahl = 0
ziehung = []
lottoziehung(anzahl)

print("Rekursiv:",sorted(ziehung))


# Ansatz C:
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


# Ansatz D: "Lottofee"
urne = list(range(1, 50)) # urne = [1, 2, 3, ..., 49]
lottoziehung = []
for i in range(6):
    ziehung = urne.pop(r.randint(0, len(urne)) - 1)
    lottoziehung.append(ziehung)

print(sorted(lottoziehung))


# Ansatz E: Geeignete Methode aus random benutzen
lottoziehung = r.sample(range(1, 50), 6)
print(sorted(lottoziehung))



# 2) Schreibe eine Funktion wuerfeln2, die fair würfelt.
#    Bei der Implementierung darf nur die Funktion muenzwurf verwendet werden.

# würfeln mit Münzwurf

# Dual    Dez
# 0 0 0   0
# 1 0 0   1
# 0 1 0   2
# 1 1 0   3
# 0 0 1   4
# 1 0 1   5
# 0 1 1   6
# 1 1 1   7

def wuerfeln2():
    while True:
        i_dual = 1  # Zähler Dual-Code
        i_augenzahl = 0
        while i_dual <= 4:
            i_augenzahl += muenzwurf() * i_dual
            i_dual *= 2 # Zähler Dual-Code multipliziert mit 2 (1,2,4...)
        if 0 < i_augenzahl < 7:
            break
    return i_augenzahl

dict_mw ={}
i_schleife = 0  # Schleifenzaehler
while i_schleife < 100000:
    i_augenzahl = wuerfeln2()
    if i_augenzahl in dict_mw:
        dict_mw[i_augenzahl] += 1
    else:
        dict_mw[i_augenzahl] = 1
    i_schleife += 1

print("Münzwurf: "+str(dict(sorted(dict_mw.items()))))