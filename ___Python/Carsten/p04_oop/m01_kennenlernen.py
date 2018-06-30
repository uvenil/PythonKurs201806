from datetime import date

class Teilnehmer(object):
    # Konstruktormethodik
    def __init__(self, vorname, ort, geburtsdatum, sprachen):
        self.vorname = vorname
        self.ort = ort
        self.geburtsdatum = geburtsdatum
        self.sprachen = sprachen

    def __repr__(self):
        return "%s %s" % (self.vorname, self.ort)

    def alter(self):
        heute = date.today()
        jahre = heute.year - self.geburtsdatum.year
        if (self.geburtsdatum.month, self.geburtsdatum.day) > (heute.month, heute.day) : # dieses Jahr noch nicht Geburtstag?
            jahre -= 1 # Kurzform jahre = jahre - 1
        return jahre

torsten = Teilnehmer("Torsten", "Aachen", date(1967, 1, 1), ["C"])
michael = Teilnehmer("Michael", "Moormerland", date(1981, 1, 10), ["Javascript"])
karpoo = Teilnehmer("Karpoo", "Düsseldorf", date(1969, 1, 1), ["ABAP"])
carsten = Teilnehmer("Carsten", "Aachen", date(1971, 2, 3), ["Basic"])
thomas = Teilnehmer("Thomas", "Bielefeld", date(1964, 10, 12), ["Pascal"])
angela = Teilnehmer("Angela", "Lingen", date(1983, 12, 31), ["C", "Java"])
jonas = Teilnehmer("Jonas", "Löhne", date(1997, 4, 4), [])
marco = Teilnehmer("Marco", "Bielefeld", date(1975, 6, 24), [])
roman = Teilnehmer("Roman", "Hannover", date(1984, 2, 28), [])
daniel = Teilnehmer("Daniel", "Bielefeld", date(1980, 1, 1), ["Python"])

teilnehmerliste = [torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel]

print(marco.vorname)
print(marco.alter())

#1) Durchschnittsalter

#s) List Comprehension
altersliste = [teilnehmer.alter() for teilnehmer in teilnehmerliste]
print(sum(altersliste)/len(altersliste))

#b) Map
altersliste = list(map(lambda teilnehmer: teilnehmer.alter(), teilnehmerliste))
print(sum(altersliste)/len(altersliste))

#2a) Alle Teilnehmer aus Bielefeld
Bielefelder = [teilnehmer.vorname for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(Bielefelder)

#2b) Alle Teilnehmer aus Bielefeld
Bielefelder = [teilnehmer for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(Bielefelder)


#3) Durchschnittsalter aller Bielefelder

Bielefelderalter = [teilnehmer.alter() for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(sum(Bielefelderalter)/len(Bielefelderalter))

#4) Welche Teilnehmer sprechen die meisten Programmiersprachen
maxsprachen = -1
for teilnehmer in teilnehmerliste:
    if len(teilnehmer.sprachen) > maxsprachen:
        maxsprachen = len(teilnehmer.sprachen)
print(maxsprachen)
sprachenmax = [teilnehmer.vorname for teilnehmer in teilnehmerliste if len(teilnehmer.sprachen) == maxsprachen]
print(sprachenmax)

maxsprachen = -1
programmiersprachen = [len(teilnehmer.sprachen) for teilnehmer in teilnehmerliste]
print(programmiersprachen)
maxsprachen = max(programmiersprachen)
sprachenmax = [teilnehmer.vorname for teilnehmer in teilnehmerliste if len(teilnehmer.sprachen) == maxsprachen]
print(sprachenmax)

#5) Alle Teilnehmer aufsteigend sortiert nach Vorname
sortiert = sorted(teilnehmerliste, key=lambda teilnehmer: teilnehmer.vorname)
print(sortiert)

#6) Alle Teilnehmer aufsteigend sortiert nach Ort, Vorname
sortiert = sorted(teilnehmerliste, key=lambda teilnehmer: (teilnehmer.ort, teilnehmer.vorname))
print(sortiert)
