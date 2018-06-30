from p01_kennenlernen import meinebibliothek
from p01_kennenlernen.meinebibliothek import celsius_to_fahrenheit

celsius = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3,] #Durchschinttstemperatur in Bielefed nach Monaten in C
# Aufgabe: neue Liste Fahrenheit erzeugen, die die Temperaturen in Fahrenheit enthält.

# Lösung 1) for-Schleife
fahrenheit = []
for temperatur in celsius:
    fahrenheit.append(temperatur * 1.8 + 32)

print(fahrenheit)
print()

#Lösung 2) List Comprehension
fahrenheit = [temperatur * 1.8 + 32 for temperatur in celsius]
print(fahrenheit)
print()

# Aufgabe: neue Liste fahrenheit mit Temperaturen in fahrenheit >= 15°C
fahrenheit = [temperatur * 1.8 + 32 for temperatur in celsius if temperatur >= 15]
print(fahrenheit)

fahrenheit = [meinebibliothek.celsius_to_fahrenheit(temperatur) for temperatur in celsius if temperatur >= 15]
print(fahrenheit)