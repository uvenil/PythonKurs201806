celsius = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3,] #Durchschinttstemperatur in Bielefed nach Monaten in C

def filtern(liste, grenze):
    gefiltert = []
    for element in liste:
        if element >= grenze:
            gefiltert.append(element)

    return gefiltert
print(filtern(celsius, 15))
print(filtern(celsius, 16))