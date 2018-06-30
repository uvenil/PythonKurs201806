from datetime import date

class Teilnehmer(object):
    # Konstruktormethode
    def __init__(self, vorname, ort, geburtsdatum, sprachen):
        self.vorname = vorname
        self.ort = ort
        self.geburtsdatum = geburtsdatum
        self.sprachen = sprachen

    def __repr__(self):
        return "%s %s %s %s" % (self.vorname, self.ort, self.geburtsdatum, self.sprachen)

    def alter(self):
        heute = date.today()
        jahre = heute.year - self.geburtsdatum.year
        if (self.geburtsdatum.month, self.geburtsdatum.day) > (
        heute.month, heute.day):  # hatte die Person dieses Jahr noch nicht Geburtstag?
            jahre -= 1  # Kurzform für: jahre = jahre - 1
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

teilnehmerliste = [torsten, michael, karpoo , carsten, thomas, angela, jonas, marco, roman, daniel]

print(marco.vorname)
print(marco.alter())

# 1) Durchschnittsalter

# a) List Comprehension
altersliste = [teilnehmer.alter() for teilnehmer in teilnehmerliste]
print(sum(altersliste) / len(altersliste))

# b) Map
altersliste = list(map(lambda teilnehmer: teilnehmer.alter(), teilnehmerliste))
print(sum(altersliste) / len(altersliste))
print()

# 2) Alle Vornamen der Teilnehmer aus Bielefeld
bielef = [teilnehmer.vorname for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld" ]
print(bielef)
print()

# 2b) Alle Vornamen der Teilnehmer aus Bielefeld
bielef = [teilnehmer for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld" ]
print(bielef)
print()

# 3) Durchschnittsalter aller Bielefelder
bielef = [teilnehmer.alter() for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld" ]
print(sum(bielef) / len(bielef))
print()

# 4) Vornamen der Teilnehmer, die am meisten Programmiersprachen sprechen
# sprachanz = [(teilnehmer.vorname, len(teilnehmer.sprachen)) for  teilnehmer in teilnehmerliste ]
# maxnamen = [tn[0] for tn in sprachanz if tn[1] == maxsprach]
maxsprach = max([len(teilnehmer.sprachen) for teilnehmer in teilnehmerliste ])
maxnamen = [ teilnehmer.vorname for teilnehmer in teilnehmerliste if len(teilnehmer.sprachen) == maxsprach]

# print(sprachanz)
print(maxsprach)
print(maxnamen)
print()

# 5) Ale Teilnehmer
sortiert = sorted(teilnehmerliste, key = lambda teilnehmer: teilnehmer.vorname)
print(sortiert)

'''
# 6) Ale Teilnehmer 
sortiert = sorted(teilnehmerliste, key = lambda teilnehmer: (teilnehmer.nachname, teilnehmer.vorname))
print(sortiert)
'''

# 7) Ale Teilnehmer
sortiert = sorted(teilnehmerliste, key = lambda teilnehmer: (teilnehmer.alter(), teilnehmer.vorname))
print(sortiert)
