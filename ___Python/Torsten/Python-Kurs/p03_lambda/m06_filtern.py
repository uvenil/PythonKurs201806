from datetime import date
from p01_kennenlernen import PythonLib
from p01_kennenlernen.PythonLib import celsius_nach_fahrenheit

temperaturenGC = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] #Durchschnittstemp. in Bielefeld
print("Temperaturen in °C:", temperaturenGC)


daniel = ["Daniel", "Bielefeld", date(1980,1,1), ["Python"]]
torsten = ["Torsten", "Aachen", date(1967,1,1,), ["C"]]
michael = ["Michael", "Moormerland", date(1981,1,10), ["Javascript"]]
karpoo = ["Karpoo", "Düsseldorf", date(1969,1,1), ["APAP"]]
carsten = ["Carsten", "Aachen", date(1971,2,3), ["Basic"]]
thomas = ["Thomas", "Bielefeld", date(1964,10,12), ["Pascal"]]
angela = ["Angela", "Lingen", date(1983,12,31), ["C", "Java"]]
jonas = ["Jonas", "Löhne", date(1997,4,4), []]
marco = ["Marco", "Bielefeld", date(1975,6, 24), []]
roman = ["Roman", "Hanover", date(1984,2,27), [""]]

teilnehmerliste = [daniel, torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman]

# 1) Alle Teilnehmer, die jünger als 40 sind in einer neuen Liste
# 1a) for-Schleife mit if-Anweisung

result = []
for item in teilnehmerliste:
    if PythonLib.alter(item[2]) < 40:
        result.append(item)

print(result)

result = []
for item in teilnehmerliste:
    if PythonLib.alter(item[2]) < 40:
        result.append(item[0])

print(result)


# 1b) filter-Funktion (lambda)

result = list(filter(lambda teilnehmer: PythonLib.alter(teilnehmer[2]) < 40, teilnehmerliste))
print(result)

# Vorüberlegung MAP-Funktion
temperaturenGC = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] #Durchschnittstemp. in Bielefeld
print("Temperaturen in °C:", temperaturenGC)
result = list(map(lambda celsius: celsius_nach_fahrenheit(celsius), temperaturenGC))
print(result)

result = list(map(lambda  teilnehmer: teilnehmer[0],filter(lambda teilnehmer: PythonLib.alter(teilnehmer[2]) < 40, teilnehmerliste)))
print(result)


# 1c) List-Comprehension

result = [item for item in teilnehmerliste if PythonLib.alter(item[2]) < 40]
print(result)