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

# 1) Alle Teilnehmer, die jünger als 40

# a) for-Schleife mit if-Anwendung
junge = []
for teilnehmer in  teilnehmerliste:
    if (meinebibliothek.alter(teilnehmer[2]) < 40):
        junge.append(teilnehmer)
print(junge)
print(len(junge))

# b) filter mit lambda
junge = list(filter(lambda teilnehmer: meinebibliothek.alter(teilnehmer[2]) < 40, teilnehmerliste))
print(junge)
print(len(junge))

# c) List Comprehension
junge = [teilnehmer for teilnehmer in teilnehmerliste if meinebibliothek.alter(teilnehmer[2])<40]
print(junge)
print(len(junge))

# 2) Vornamen der Teilnehmer, die jünger als 40 sind
jungevorn = [teilnehmer[0] for teilnehmer in teilnehmerliste if meinebibliothek.alter(teilnehmer[2])<40]
print(jungevorn)
print(len(jungevorn))



# b) filter mit lambda
junge = list(filter(lambda teilnehmer: meinebibliothek.alter(teilnehmer[2]) < 40, teilnehmerliste))
print(junge)
print(len(junge))

