celsius = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] # Avg. Temp in °C
print(celsius)


# 1) Lösung mit for-Schleife
fh = []
for temp in celsius:
    fh.append((temp*1.8) + 32)
print(fh)

print()

# 2) Lösung mit List comprehension

fh = [temperatur *1.8+32 for temperatur in celsius]
print(fh,"comprehension")

print()

# 3) Filtern nach Temps >= 15°C
filtered=[]
for temp in celsius:
    if temp >=15:
        filtered.append(temp*1.8+32)
print(filtered)

print()


# 4) Filtern nach Temps >= 15°C, Compreh
filtered=[]
filtered = [temp *1.8+32 for temp in celsius if temp>=15]
print(filtered, "Filtered Compreh")

print()

