celsius = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] # Avg. Temp in °C

def min15(temperatur):
    return temperatur >= 15

def zw5und10(temperatur):
    return 5 <= temperatur and temperatur <=10

def filtern(liste, kriterium):
    gefiltert = []
    for element in liste:
        if kriterium(element):
            gefiltert.append(element)

    return gefiltert


print(filtern(celsius, lambda temperatur: temperatur >=15))
print(filtern(celsius, lambda temperatur: 5 <= temperatur and temperatur <=10))


print()
print("End of Program")