from datetime import date

from p01_kennenlernen import meinebibliothek
from p01_kennenlernen.meinebibliothek import alter

torsten = ["Torsten", "Aachen", date(1967, 1, 1), ["C"]]
michael = ["Michael", "Moormerland", date(1981, 1, 10), ["Javascript"]]
karpoo = ["Karpoo", "Düsseldorf", date(1969, 1, 1), ["ABAP"]]
carsten = ["Carsten", "Aachen", date(1971, 2, 3), ["Basic"]]
thomas = ["Thomas", "Bielefeld", date(1964, 10, 12), ["Pascal"]]
angela = ["Angela", "Lingen", date(1983, 12, 31), ["C", "Java"]]
jonas = ["Jonas", "Löhne", date(1997, 4, 4), []]
marco = ["Marco", "Bielefeld", date(1975, 6, 24), []]
roman = ["Roman", "Hannover", date(1984, 2, 28), []]
daniel = ["Daniel", "Bielefeld", date(1980, 1, 1), ["Python"]]

teilnehmerliste = [torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel]

# 1) Alle Teilnehmer, die jünger als 40 sind

# a) for-Schleife mit if-Anweisung
erg = []
for teilnehmer in teilnehmerliste:
    if alter(teilnehmer[2]) < 40:
        erg.append(teilnehmer)

print(erg)

# b) filter mit lambda
erg = list(filter(lambda teilnehmer: alter(teilnehmer[2]) < 40, teilnehmerliste))

# c) List Comprehension
erg = [teilnehmer for teilnehmer in teilnehmerliste if alter(teilnehmer[2]) < 40]
print(erg)

# 2) Vornamen der Teilnehmer, die jünger als 40 sind.
# a) for-Schleife mit if-Anweisung
erg = []
for teilnehmer in teilnehmerliste:
    if alter(teilnehmer[2]) < 40:
        erg.append(teilnehmer[0])

print(erg)

# Vorüberlegung zu b) map-Funktion:
celsius_temperaturen = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] # Durchschnittstemperaturen in Bielefeld nach Monat in °C
fahrenheit = map(lambda celsius: celsius_to_fahrenheit(celsius), celsius_temperaturen)

# b) filter mit lambda
erg = list(filter(lambda teilnehmer: alter(teilnehmer[2]) < 40, teilnehmerliste))

# c) List Comprehension
erg = [teilnehmer[0] for teilnehmer in teilnehmerliste if alter(teilnehmer[2]) < 40]
print(erg)