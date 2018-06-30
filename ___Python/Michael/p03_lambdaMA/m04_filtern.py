celsius_temperaturen = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] # Durchschnittstemperaturen in Bielefeld nach Monat in °C

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

print(filtern(celsius_temperaturen, lambda temperatur: temperatur >= 15))
print(filtern(celsius_temperaturen, lambda temperatur: 5 <= temperatur and temperatur <= 10))

# Alle Temperaturen <= 15:
