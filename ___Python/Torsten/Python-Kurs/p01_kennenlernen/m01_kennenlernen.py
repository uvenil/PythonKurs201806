import statistics
from datetime import date
from p01_kennenlernen import PythonLib

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

# 1) Anzahl Teilnehmer
anzahl = len(teilnehmerliste)
print("Anzahl: ", anzahl)


# 2) Alle Teilnehmer
for teilnehmer in teilnehmerliste:
    print(teilnehmer)

print()


# 2) Alle Teilnehmer aus Bielefeld
for teilnehmer in teilnehmerliste:
    if teilnehmer[1] == "Bielefeld":
        print(teilnehmer)

print()


# 3) Wie alt sind die einzelnen Teilnehmer
altersangaben = []
for teilnehmer in teilnehmerliste:
    alter = PythonLib.alter(teilnehmer[2])
    altersangaben.append(alter)
    print("Alter von", teilnehmer[0], "ist", alter)

print()
print(altersangaben)
print()


# 3) Wie hoch ist das Durchschnittsalter der Teilnehmer
summealter = 0
altersangaben = []

for teilnehmer in teilnehmerliste:
    alter = PythonLib.alter(teilnehmer[2])
    altersangaben.append(alter)

for alter in altersangaben:
    summealter += alter

durchschnittsalter = sum(altersangaben) / len(altersangaben)
#durchschnittsalter = summealter / len(altersangaben)
print("Durchschnittsalter:", durchschnittsalter)
print("Mean:", statistics.mean(altersangaben))
print("Median:", statistics.median(altersangaben))

print()