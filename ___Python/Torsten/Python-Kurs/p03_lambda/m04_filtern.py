temperaturenGC = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] #Durchschnittstemp. in Bielefeld
print("Temperaturen in °C:", temperaturenGC)

#def mindestens15(temperatur):
#    return temperatur>= 15

mindesten15 = lambda temperatur: temperatur >= 15


#def zwischen5und10(temperatur):
#    return 5 <= temperatur and temperatur <= 10


def filtern (liste, kriterium):
    gefiltert = []

    for item in liste:
        if kriterium(item):
            gefiltert.append(item)

    return(gefiltert)


print(filtern(temperaturenGC, mindesten15))
print(filtern(temperaturenGC,lambda temperatur: temperatur >= 15))
print(filtern(temperaturenGC,lambda temperatur: 5 <= temperatur and temperatur <= 10))