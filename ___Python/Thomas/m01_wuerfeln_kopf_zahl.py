import random

r = random.Random()

def wuerfeln():
    return r.randint(1, 6) # Augenzahl zwischen 1 und 6

def muenzwurf():
    return r.randint(0, 1)

# wuerfeln mit Augenzahl zwischen 1 und 6
d = {}
for i in range(100000):
    augenzahl = wuerfeln()
    if augenzahl in d:
        d[augenzahl] +=1
    else:
        d[augenzahl] = 1

print("Würfeln:  "+str(dict(sorted(d.items())))+'\n')

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