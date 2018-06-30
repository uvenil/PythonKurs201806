from p01_kennenlernen import meinebibliothek

celsius_temperaturen = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] #Durchschnittstemperaturen in Bilefeld nach Monat

# Aufgabe: Neue Liste fahrenheit erzeugen, die die Temperaturen in Fahrenheit enthält.
fahrenheit = []

# Lösung 1) for-Schleife
for temperatur in celsius_temperaturen: # fahrenheit entspricht i = 0; celsius entspricht i < celsius.lenght; i++ entfällt
    fahrenheit.append(meinebibliothek.celsius_to_fahrenheit(temperatur)) #

print(fahrenheit)
print()

# Lösung 2) List Comprehension
fahrenheit = [temperatur * 1.8 + 32.0 for temperatur in celsius_temperaturen]

print(fahrenheit)
print()

# Aufgabe: Neue Liste mit Temperaturen in fahrenheit, aber nur über 15C
fahrenheit = [temperatur * 1.8 + 32.0 for temperatur in celsius_temperaturen if temperatur >= 15.0]

print(fahrenheit)
print()

