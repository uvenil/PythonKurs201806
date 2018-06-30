import statistics

from p01_kennenlernen import meinebibliothek

celsius = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3]
print("Durschnitt", statistics.mean(celsius))
print("Median", statistics.median(celsius))
print()

# Aufgabe: Neue Liste fahrenheit erzeugen, die die Temperatur in Fahrenheit umrechnen soll
# Lösung 1: mit for-Schleife arbeiten
fahrenheit = []
for monat in celsius:
    fahrenheit.append(monat * 1.8 + 32)

print(fahrenheit)
print()

# Lösung 2: List Comprehension
fahrenheit = [monat * 1.8 + 32 for monat in celsius]
print(fahrenheit)
print()

#Aufgbe: Neue Liste fahrenheit mit Temperaturen in Fahrenheit >= 15°C
fahrenheit = [meinebibliothek.celsius_to_fahrenheit(monat) for monat in celsius if monat >= 15]
print(fahrenheit)
print()

