import random

r = random.Random()
Zahlen = 0
augenzahlen = []

def wuerfeln():
    return r.randint(1,6)

def muenzwurf():
    return r.randint(0,1)

def lottoziehen():
    return r.randint(1,49)


def wuerfeln2():
    augenzahl = 10
    while(augenzahl>6):
        würfe = []
        for i in range(3):
            würfe.append(muenzwurf())
        augenzahl = 1*würfe[0]+2*würfe[1]+4*würfe[2]+1
    return augenzahl

def wuerfeln3():
    augenzahl = 0
    würfe = []
    for i in range(3):
        würfe.append(muenzwurf())
        augenzahl = 1*würfe[0]+2*würfe[1]+4*würfe[2]+1
    return augenzahl

d = {}
for i in range(100000):
    augenzahl = wuerfeln2()
    if augenzahl in d:
        d[augenzahl] += 1
    else:
        d[augenzahl] = 1

print(d)

#1) Lottozahlen 6 aus 49 ermitteln (sortiert)
Zahlen = 0
Lottozahlen = []
while (Zahlen < 6):
    Lottozahl = lottoziehen()
    if Lottozahl in Lottozahlen:
        pass
    else:
        Lottozahlen.append(Lottozahl)
        Zahlen += 1
Lottozahlensortiert = sorted(Lottozahlen)
print(Lottozahlensortiert)


#2) Schreibe eine Funktion wuerfeln2, die fair wuerfelt
# Bei der Implementierung darf nur die Funktion muenzwurf benutzt werden

