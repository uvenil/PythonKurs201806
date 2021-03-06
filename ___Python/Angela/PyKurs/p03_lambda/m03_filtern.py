celsius_temperaturen = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] # Durchschnittstemperatur in Bielefeld nach Monaten

def mindestens15(temperatur):
    return temperatur >= 15

def zwischen5und10(temperatur):
    return 5 <= temperatur and temperatur <= 10

def filtern(liste, kriterium):
    gefiltert = []
    for element in liste:
        if kriterium(element):
            gefiltert.append(element)
    return gefiltert

print(filtern(celsius_temperaturen, mindestens15)) # Funktion mitgeben
print(filtern(celsius_temperaturen, zwischen5und10))