from datetime import date

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

teilnehmerliste = [torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel] # Zuweisung

# 0) Anzahl Teilnehmer?
anzahl = len(teilnehmerliste)
print(anzahl)

# 1) Alle Teilnehmer
for teilnehmer in teilnehmerliste: # Schleife, lies: "für jeden teilnehmer in der liste teilnehmerliste wiederhole:"
    print(teilnehmer)

print()

# 2) Alle Teilnehmer aus Bielefeld
for teilnehmer in teilnehmerliste:
    if teilnehmer[1] == "Bielefeld": # == ist ein Vergleichsoperator (hier: auf Gleichheit)
        print(teilnehmer)

print()

# 3) Alter ermitteln
geburtsdatum = date(2000, 3, 1)
heute = date.today()
jahre = heute.year - geburtsdatum.year
if (geburtsdatum.month, geburtsdatum.day) > (heute.month, heute.day): # hatte die Person dieses Jahr noch nicht Geburtstag?
    jahre -= 1 # Kurzform für: jahre = jahre - 1
print(jahre)
