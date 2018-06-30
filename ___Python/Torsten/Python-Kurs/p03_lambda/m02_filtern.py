temperaturenGC = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] #Durchschnittstemp. in Bielefeld
print("Temperaturen in °C:", temperaturenGC)

def filtern (liste, kriterium):
    gefiltert = []

    for item in liste:
        if item >= kriterium:
            gefiltert.append(item)

    return(gefiltert)

print(filtern(temperaturenGC,15))
print(filtern(temperaturenGC,8))