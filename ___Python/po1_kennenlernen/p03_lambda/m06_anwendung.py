from datetime import date
from p01_kennenlernen import meinebibliothek

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

teilnehmerliste =[torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel] # Zuweisung

# 1) Alle Teilnehmer die jünger als 40 sind

# a) for-Schleife mit if-Anweisung
teilnehmerunter40 = []
for check in teilnehmerliste:
    if meinebibliothek.alter(check[2]) < 40:
        teilnehmerunter40.append(check)

print(teilnehmerunter40)
print()

# b) Filter mit lambda
print(list(filter(lambda teilnehmer: meinebibliothek.alter(teilnehmer[2]) < 40, teilnehmerliste)))
print()

# c) List Comprehension
teilnehmerunter40 = [teilnehmer for teilnehmer in teilnehmerliste if meinebibliothek.alter(teilnehmer[2]) < 40]
print(teilnehmerunter40)
print()

# 2) Vornamen der Teilnehmer, die jünger als 40 sind
# a) for-Schleife mit if-Anweisung
vornameteilnehmerunter40 = []
for check in teilnehmerliste:
    if meinebibliothek.alter(check[2]) < 40:
        vornameteilnehmerunter40.append(check[0])

print(vornameteilnehmerunter40)
print()
# b) Filter mit lambda
vornameteilnehmerunter40 = list(map(lambda teilnehmer: teilnehmer[0], filter(lambda teilnehmer: meinebibliothek.alter(teilnehmer[2]) < 40, teilnehmerliste)))
print(vornameteilnehmerunter40)
print()

# c) List Comprehension
vornameteilnehmerunter40 = [teilnehmer[0] for teilnehmer in teilnehmerliste if meinebibliothek.alter(teilnehmer[2]) < 40]
print(vornameteilnehmerunter40)
print()