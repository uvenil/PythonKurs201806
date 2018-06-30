import random

r = random.Random()

def wuerfeln():
    return r.randint(1, 6) # Augenzahl zwischen 1 und 6

def muenzwurf():
    return r.randint(0, 1)

def wuerfeln_lz():
    return r.randint(1, 49)

d = {}
for i in range(10000):
    augenzahl = wuerfeln()
    if augenzahl in d:
        d[augenzahl] +=1
    else:
        d[augenzahl] = 1
print(d)

# 1) Lottozahlen 6 aus 49 ermitteln

kugeln = 0
menge = set()
lottoziehung = []
while kugeln < 6:
    ziehung = wuerfeln_lz()
    if ziehung not in menge:
        lottoziehung.append(ziehung)
        menge.add(ziehung)
        kugeln +=1
print(sorted(lottoziehung))

# Lösung 2
urne = list(range(1, 50))
lottoziehung = []
for i in range(6):
    ziehung = urne.pop(r.randint(0, len(urne)) - 1)
    lottoziehung.append(ziehung)
print(sorted(lottoziehung))

# lösung 3
lottoziehung = r.sample(range(1, 50), 6)
print(sorted(lottoziehung))

# 2) Schreibe eine Funktion wuerfeln2, die fair würfeln2, die fair würfelt mit der Funktion münzwurf

# wl2 = {}
# i1 = 0
# i2 = 0
#
#     while i1 < 3:
#         i2 += muenzwurf()*i1
#     if i2 in [1,6]:
#         if i2 in wl2:
#             wl2[i2] += 1
#         else:
#             wl2[i2] = 1






