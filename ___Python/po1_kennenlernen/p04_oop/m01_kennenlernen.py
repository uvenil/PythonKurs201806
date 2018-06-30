import statistics
from datetime import date

class Teilnehmer(object):
    # Konstruktormethode
    def __init__(self, vorname, ort, geburtsdatum, sprachen):
        self.vorname = vorname
        self.ort = ort
        self.geburtsdatum = geburtsdatum
        self.sprachen = sprachen

    # respresentation method
    def __repr__(self):
        return "%s %s %s %s" % (self.vorname, self.ort, self.geburtsdatum, self.sprachen)

    def alter(self):
        heute = date.today()
        jahre = heute.year - self.geburtsdatum.year
        if (self.geburtsdatum.month, self.geburtsdatum.day) > (heute.month, heute.day): # hatte die Person dieses Jahr noch nicht geburtstag?
            jahre -= 1 #jahre = jahre - 1

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

teilnehmerliste =[torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel] # Zuweisung

print(carsten.ort)
print(carsten.alter())

# 1) Durchschnittsalter

# a) List Comprehension
altersliste = [teilnehmer.alter() for teilnehmer in teilnehmerliste]
print(sum(altersliste) / len(altersliste))

# b) Map
altersliste = list(map(lambda teilnehmer: teilnehmer.alter(), teilnehmerliste))
#print(sum(altersliste) / len(altersliste))

# 2a) Alle Vornamen der Teilnehmer aus Bielefeld
ausbielefeld = [teilnehmer.vorname for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(ausbielefeld)

# 2b) Alle Teilnehmer aus Bielefeld
ausbielefeld = [teilnehmer for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(ausbielefeld)

# 3) Durchschnittsalter aller Bielefelder
ausbielefeld = [teilnehmer.alter() for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(sum(ausbielefeld) / len(ausbielefeld))

mittelwert = statistics.mean([teilnehmer.alter() for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"])
print(mittelwert)

# 4) Vornamen der Teilnehmer, die die meisten Programiersprachen sprechen?
laengen = [len(teilnehmer.sprachen) for teilnehmer in teilnehmerliste]
print(laengen)
m = max(laengen)
vornamen = [teilnehmer.vorname for teilnehmer in teilnehmerliste if m == len(teilnehmer.sprachen)]
print(vornamen)

# 5) Alle Teilnehmer sortiert nach Vorname
sortiert = sorted(teilnehmerliste, key=lambda teilnehmer: teilnehmer.vorname)
print(sortiert)

# 6) Alle Teilnehmer aufsteigend sortiert nach Alter und dann Vorname
sortiert = sorted(teilnehmerliste, key=lambda teilnehmer: (teilnehmer.alter(), teilnehmer.vorname))
print(sortiert)