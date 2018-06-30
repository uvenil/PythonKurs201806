import random

r = random.Random()

def wuerfeln():
    return r.randint(1, 6)

def lottozahl():
    return r.randint(1, 49)

def muenzwurf():
    return r.randint(0, 1)


#def wuerfeln2():
    #    wurfreihe = []

    #    for i in range(3):
    #   augenzahl = wuerfeln()
    #    wurfreihe[i] = augenzahl

    # 0, 0, 0, 0 = 1
    #    if (wurfreihe[0] == 0) and (wurfreihe[1] == 0) and (wurfreihe[2] == 0) and (wurfreihe[3] == 0):
    #       return 1
    # 0, 0, 0, 1 = 2
    #    elif (wurfreihe[0] == 0) and (wurfreihe[1] == 0) and (wurfreihe[2] == 0) and (wurfreihe[3] == 1):
    #       return 2
    # 0, 0, 1, 0 = 3
    #   elif (wurfreihe[0] == 0) and (wurfreihe[1] == 0) and (wurfreihe[2] == 1) and (wurfreihe[3] == 0):
    #       return 3
    # 0, 0, 1, 1 = 4
    #    elif (wurfreihe[0] == 0) and (wurfreihe[1] == 0) and (wurfreihe[2] == 1) and (wurfreihe[3] == 1):
    #       return 4
    # 0, 1, 0, 0 = 5
    #    elif (wurfreihe[0] == 0) and (wurfreihe[1] == 1) and (wurfreihe[2] == 0) and (wurfreihe[3] == 0):
    #       return 5
    # 0, 1, 0, 1 = 6
    #   elif (wurfreihe[0] == 0) and (wurfreihe[1] == 1) and (wurfreihe[2] == 0) and (wurfreihe[3] == 1):
#       return 6


d = {}
for i in range(10000):
    augenzahl = wuerfeln()
    if augenzahl in d:
        d[augenzahl] += 1
    else:
        d[augenzahl] = 1

print(d)

# 1a) Lottozahlen 6 aus 49 ermitteln
lottoreihe = [0, 0, 0, 0, 0, 0]

e = {}
i = 0
while i <= (len(lottoreihe) - 1):
    zahl = lottozahl()
    if zahl not in e:
        e[zahl] = 1
        lottoreihe[i] = zahl
        i = i + 1

print(e)
print(lottoreihe)

# 1b) Lottozahlen 6 aus 49 ermitteln
kugeln = 0
menge = set() # Menge der bereits gezogenen Kugeln
lottoziehung = []
while kugeln < 6:
    ziehung = lottozahl()
    if ziehung not in menge: # Diese Kugeln ist noch nicht gezogen
        lottoziehung.append(ziehung)
        menge.add(ziehung)
        kugeln += 1

print(sorted(lottoziehung))

# 1c) Ansatz Lottofee
urne = list(range(1, 50))
lottoziehung2 = []
for i in range(6):
    ziehung = urne.pop(r.randint(0, len(urne)) -1)
    lottoziehung2.append(ziehung)

print(sorted(lottoziehung2))

# 2) Schreibe eine Funktion wuerfeln2, die fair würfelt
# Bei der Implementierung darf nur die Funktion muenzwurf benutzt werden
#f = {}
#for i in range(10000):
#    augenzahl = wuerfeln2()
#    if augenzahl in f:
#        f[augenzahl] += 1
#    else:
#        f[augenzahl] = 1

#print(f)

