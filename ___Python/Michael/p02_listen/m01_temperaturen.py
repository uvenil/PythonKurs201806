from p01_kennenlernern import meinebibliothek
from p01_kennenlernern.meinebibliothek import celsius_to_fahrenheit

celsius_temperaturen = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] # Durchschnittstemperaturen in Bielefeld nach Monat in °C
# Aufgabe: Neue Liste fahrenheit erzeugen, die die Temperaturen in Fahrenheit enthält.

# °F = °C * 1,8 + 32

# 1)
fahrenheit = []
for temp in celsius:
    fahr = celsius_to_fahrenheit(temp)
    fahrenheit.append(fahr)

print(fahrenheit)
print()

# 2) List Comprehension
fahrenheit = [celsius_to_fahrenheit(temperatur) for temperatur in celsius]
print(fahrenheit)
print()

# 3) List Comprehension
fahrenheit = [meinebibliothek.celsius_to_fahrenheit(temperatur) for temperatur in celsius if temperatur > 15]
print(fahrenheit)
print()
