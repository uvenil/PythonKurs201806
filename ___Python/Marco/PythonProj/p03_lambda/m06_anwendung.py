from datetime import date

from p01 import meinebib
from p01.meinebib import alter

torsten = ["Torsten", "Aachen", date(1967, 1, 1), ["C"]]
michael = ["Michael", "Moormerland", date(1981, 10, 1), ["Javascript"]]
karpoo = ["Karpoo", "Düsseldorf", date(1969, 1, 1), ["ABAP"]]
carsten = ["Carsten", "Aachen", date(1971, 1, 1), ["Basic"]]
thomas = ["Thomas", "Bielefeld", date(1964, 1, 1), ["Pascal"]]
angela = ["Angela", "Lingen", date(1983, 1, 1), ["c", "Java"]]
jonas = ["Jonas", "Löhne", date(1997, 4, 4), []]
marco = ["Marco", "Bielefeld", date(1975, 6, 24), []]
roman = ["Roman", "Hannover", date(1984, 2, 28), []]
daniel = ["Daniel", "Bielefeld", date(1980, 1, 1), ["Python"]]

teilnehmerliste = [torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel] #Zuweisung

# Alle Teilnehmer, die jünger als 40 sind

# a) for-Schleife mit if-Anweisung

# b) filter mit Lambda

# c) List Comprehension


# a) for-Schleife mit if-Anweisung
ergebnis = [] # Liste
for teilnehmer in teilnehmerliste:
    if alter(teilnehmer [2]) >= 40:
        ergebnis.append(teilnehmer)

print(ergebnis)

# b) filter mit Lambda
ergebnis = list(filter(lambda teilnehmer: alter(teilnehmer[2]) < 40, teilnehmerliste))


# c) List Comprehension
ergebnis = [teilnehmer for teilnehmer in teilnehmerliste if alter(teilnehmer [2]) < 40]
print(ergebnis)










