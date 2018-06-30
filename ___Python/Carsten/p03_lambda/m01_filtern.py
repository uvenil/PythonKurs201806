celsius = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3]

# Alle Temperaturen größer gleich 15
gefiltert = []
for month in celsius:
    if month >= 15:
        gefiltert.append(month)

print(gefiltert)

