from p01_kennenlernen import meinebibliothek

celsius_temperaturen = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] # Durchschnittstemperatur in Bielefeld nach Monaten
# Aufgabe: Neue Liste fahrenheit erzeugen, die die Temperaturen in Fahrenheit enthält.

# Lösung (1) for-Schleife
fahrenheit = []
for temperatur in celsius_temperaturen:
    fahrenheit.append(temperatur * 1.8 + 32)

print(fahrenheit)

# Lösung (2) List Comprehension
fahrenheit = [temperatur * 1.8 + 32 for temperatur in celsius_temperaturen]
print(fahrenheit)

# Aufgabe: Neue Liste fahrenheit mit Temperaturen in Fahrenheit >= 15 °C

fahrenheit = [temperatur * 1.8 + 32 for temperatur in celsius_temperaturen if temperatur >= 15]
print(fahrenheit)

fahrenheit = [meinebibliothek.celsius_to_fahrenheit(temperatur) for temperatur in celsius_temperaturen if temperatur >= 15]
print(fahrenheit)