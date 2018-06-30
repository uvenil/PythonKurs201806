# 1) PI annähern




# 2) Check ob zwei polynomegleich sind




# 3) Check ob Zahl eine Primzahl ist
import random

r = random.Random()

def division():
    return r.randint(1, a+1) # Zufallszahl zw 1 und Eingabe

a = int(input())
print(a)

ergebnisse=[]
for i in range(int(a/10), int(a/2)):  # Min und max Anzahl für Divisionen
    ergebnisse.append(a % division())
    #ergebnisse2 = ergebnisse([1] , [-2])
    if 0 in ergebnisse:
        print(a, "Ist eine Primzahl")
    else:
        print(a, "Ist keine Primzahl")

    print(ergebnisse)




#for n in range(1, a+1):


        #ergebnisliste erstellen
       # alle elemente außer 1. und letztes prüfen ob a/element integer ist

