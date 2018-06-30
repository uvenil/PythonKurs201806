import random

r = random.Random()
def wuerfeln():
    return r.randint(1, 6) # Augenzahl zw. 1 und 6

def muenzwurf():
    return r.randit(0, 1) # 0 = Kopf, 1 = Zahl

d = {}
for i in range(100000):
    augenzahl = wuerfeln()
    if augenzahl in d:
        d[augenzahl] += 1
    else:
        d[augenzahl] =1

print(d)

# 1) Lottozahlen 6 aus 49 ermitteln ==> [1, 2, 4, 40, 13, 7]

# Lösung a)

def kugel():
    return r.randint(1, 49) # Anzahl Kugeln 1 bis 49

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


# Lösung b) "Lottofee"
urne = list(range(1, 50)) # urne = [1, 2, ..., 49]
lottoziehung = []
for i in range(6):
    ziehung = urne.pop(r.randint(0, len(urne))-1)
    lottoziehung.append(ziehung)

print(sorted(lottoziehung))



