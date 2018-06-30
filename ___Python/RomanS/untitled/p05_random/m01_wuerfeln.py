import random

r = random.Random()

def wuerfeln():
   return r.randint(1,6) # Augenzahl zw 1 und 6


def muenzwurf():
    return r.randint(0,1) # 0 = Kopf, 1 = Zahl


print(wuerfeln())

d={}
for i in range (10000):
    augenzahl = wuerfeln()
    if augenzahl in d:
        d[augenzahl] +=1
    else:
        d[augenzahl] = 1

print(d)

# 1) Lottozahlen ermitteln 6 aus 49
# Lösung a)
def kugel():
    return r.randint(1, 49) # Anzahl Kugeln 1 bis 49
kugeln=0
menge = set()
lottoziehung = []
while kugeln <6:
    ziehung=kugel()
    if ziehung not in menge: # Diese Kugel wurde zuvor noch nicht gezogen
            lottoziehung.append(ziehung)
            menge.add(ziehung) # Diese Kugel darf nicht noch einmal gezogen werden
            kugeln +=1
print(sorted(lottoziehung))

# Lösung b) Ansatz "Lottofee"
urne = list(range(1, 50)) # urne = [1, 2, 3, ..., 49]
lottoziehung=[]
for i in range (6):
    ziehung = urne[r.randint(0, len(urne)) -1 ]
    lottoziehung.append(ziehung)

print(sorted(lottoziehung))


# Unsere Lösung
"""
zahlen = []
d = {}
kugeln = 0
while kugeln < 6:
    ziehung = kugel()
    if ziehung not in d:
        d[ziehung] =1
        zahlen.append(ziehung)
        kugeln += 1
print (sorted(zahlen))
"""

# 2) Schreibe eine Funktion würfeln2, die fair würfelt



# Bei der Implementierung darf nur die Funktion muenzwurf benutzt werden