import random

r= random.Random()

def wuerfeln():
    return r.randint(1, 6) # Augenzahl zwischen 1 und 6

def muenzwurf():
    return r.randint(0,1) # 0 = Kopf, 1 = Zahl

print(wuerfeln())

d = {}
for i in range(10000):
    augenzahl = wuerfeln()
    if augenzahl in d:
        d[augenzahl] += 1
    else:
        d[augenzahl] = 1

print(d)

# 1) Lottozahlen 6 aus 49 ermitteln ==> [2,7,13,17,19,42]
def kugel():
    return r.randint(1, 49) # Anzahl Kugeln 1 bis 49
#Lösung a
zahlen = []
d = {}
kugeln = 0
while kugeln < 6:
    ziehung = kugel() # Menge der gezogenen Kugeln
    if ziehung not in d: #diese Kugel wurde zuvor noch nicht gezogen
        d[ziehung] =1
        zahlen.append(ziehung) # Kugel darf nich nochmal gezogen werden deshalb nach ziehung
        kugeln += 1
print (sorted(zahlen))

# Lösung b
urne = list(range(1, 50)) # urne = [1,2,3..., 49]
lottoziehung = []
for i in range(6):
    ziehung = urne.pop(r.randint(0, len(urne) - 1))
    lottoziehung.append(ziehung)
print(sorted(lottoziehung))

# Lösung c
lottoziehung = r.sample(range(1, 50), 6)
print(sorted(lottoziehung))

# 2) Schreibe eine Funktion wuerfeln2, die fair würfelt.
# bei der Implementierung darf nur die Funktion muenzwurf benutzt werden
