celsius = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] # Avg. Temp in °C

# Alle Temperaturen >= 15°C:

gefiltert = []
for temperatur in celsius:
    if temperatur >= 15:
        gefiltert.append(temperatur)
print(gefiltert)
print()
print("End of Program")