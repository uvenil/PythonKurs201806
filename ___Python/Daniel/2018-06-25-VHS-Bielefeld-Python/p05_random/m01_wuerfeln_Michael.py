# Lösung Michael

import random

r = random.Random()
def wuerfeln():
    return r.randint(1,6)

def muenzwurf():
    return r.randint(0, 1)

# print(wuerfeln())



# print(d)

# 1) Lottozahlen (6/49)
z = []
while(len(z) < 6):
    t = r.randint(1, 49)
    if (not t in z):
        z.append(t)
# print(sorted(z))

# 2) wuerfeln2, fair, mit funktion muenzwurf
# [0, 1] => [1, 2, 3, 4, 5, 6]
def wuerfeln2():
    w = [1, 2, 3, 4, 5, 6]
    while len(w) > 1:
        leerWert = 0
        if (not len(w) % 2 == 0):
            w.append(leerWert)
            s = w
        #print("---")
        #print("w = " + str(w))
        m = muenzwurf()
        links = round(m * len(w)/2)
        rechts = links + round(len(w)/2)
        #print(str(links) + " - " + str(rechts))
        w = w[links : rechts]
        if (len(w) == 1 and w[0] == leerWert):
            w = s
    return w[0]

def wuerfeln3():
    binaer = 1
    for i in range(3):
        binaer += 2 ** i * muenzwurf()
    if binaer > 6:
        return wuerfeln3()
    return binaer

def wuerfeln4():    # beste Lösung
    while True:
        wuerfel = 1
        for i in range(3):
            wuerfel += 2 ** i * muenzwurf()
        if wuerfel < 7:
            break
    return wuerfel

print(wuerfeln2())
print()
print(wuerfeln3())

d = {}
for i in range(100000):
    augenzahl = wuerfeln4()
    if augenzahl in d:
        d[augenzahl] += 1
    else:
        d[augenzahl] = 1

print(sorted(d.items(), key=lambda tupel: tupel[0]))
