import statistics
from datetime import date

from p01_kennenlernern import meinebibliothek

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

teilnehmerliste = [torsten, michael, karpoo , carsten, thomas, angela, jonas, marco, roman, daniel]

# 0) Anzahl Teilnehmer?
anzahl = len(teilnehmerliste)
print(anzahl)

# 1) Alle Teilnehmer
for teilnehmer in teilnehmerliste: # Schleife, lies
    print(teilnehmer)

print()

# 2) Alle Teilnehmer aus Bielefeld
for teilnehmer in teilnehmerliste: # Schleife, lies
    if teilnehmer[1] == "Bilefeld":
        print(teilnehmer)

print()

# if (a, b) < (c, d)
# 3) Alter
geburtsdatum = date(2000, 12, 1)
print(meinebibliothek.alter(geburtsdatum))
print()


# 4)
altersangaben = []
for teilnehmer in teilnehmerliste:
    altersangaben.append(meinebibliothek.alter(teilnehmer[2]))

print(altersangaben)
print()

# 5)
durchschnitt = sum(altersangaben) / len(altersangaben)
print(durchschnitt)
print(statistics.mean(altersangaben))
print()

# 6)
print(statistics.median(altersangaben))