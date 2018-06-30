temperaturenGC = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] #Durchschnittstemp. in Bielefeld
print("Temperaturen in °C:", temperaturenGC)

# Alle Temperaturen, die >= 15°C

gefiltert = []

for temp in temperaturenGC:
    if temp >=15:
        gefiltert.append(temp)

print(gefiltert)