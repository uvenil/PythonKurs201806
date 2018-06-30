from datetime import date

from p01_kennenlernen import meinebibliothek
from p01_kennenlernen.meinebibliothek import celsius_to_fahrenheit

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

#1) Alle Teilnehmer, die jünger als 40 sind

#a) for-Schleife mit if-Anweisung
Listekleiner40=[]
for teilnehmer in teilnehmerliste:
    if meinebibliothek.alter(teilnehmer[2]) < 40:
        Listekleiner40.append(teilnehmer[0])

print(Listekleiner40)

# Vorüberlegung
celsius = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3]
fahrenheit = map(lambda celsiuse: celsius_to_fahrenheit(celsiuse), celsius)

#b) filter mit Lambda
erg = list(map(lambda teilnehmer: teilnehmer[0], filter(lambda teilnehmer: meinebibliothek.alter(teilnehmer[2]) < 40, teilnehmerliste)))

print(erg)
#c) List Comprehension
Listekleiner40 = [teilnehmer[0] for teilnehmer in teilnehmerliste if meinebibliothek.alter(teilnehmer[2]) < 40]

print(Listekleiner40)

#d) Vornamen der Teilnehmer, die jünger als 40 sind
