from datetime import date

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

# 0) Wieviel Teilnehmer hat der Kurs?
anzahl = len(teilnehmerliste)
print(anzahl)

# 1) Alle Teilnehmer
for teilnehmer in teilnehmerliste: # Schleife, lies: "für jeden teilnehmer in liste teilnehmerliste wiederhole:"
    print(teilnehmer)

print()

# 2) Alle Teilnehmer aus Bielefeld
for teilnehmer in teilnehmerliste:
    if teilnehmer [1] == "Bielefeld": # == Vergleichsoperator hier: auf Gleichheit
        print(teilnehmer)

print()

# 3) Alter ermitteln
geburtsdatum = date(2000, 12, 1)
print(m_datumsbib(geburtsdatum))

# 4) Für alle Teilnehmer das Alter ermitteln ==> [51,37,43,...]
altersangaben =[]
for teilnehmer in teilnehmerliste:
    altersangaben.append(m_datumsbib.alter(teilnehmer[2]))

print(altersangaben)
print()

# 5) Durchschnittliches Alter
durchschnitt = sum(altersangaben) / len(altersangaben)
print(durchschnitt)

# 6) Median der Altersangaben
print(statistics.median(altersangaben))

