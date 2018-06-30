from datetime import date

class Teilnehmer(object):
    # Definieren einer Konstruktormethode
    def __init__(self, vorname, ort, geburtsdatum, sprachen):
        self.vorname = vorname
        self.ort = ort
        self.geburtsdatum = geburtsdatum
        self.sprachen = sprachen

    # for 2b) sich selbst repraesentieren
    def __repr__(self):
        return "%s %s %s %s" % (self.vorname, self.ort, self.geburtsdatum, self.sprachen)

    def alter(self):
        heute = date.today()
        jahre = heute.year - self.geburtsdatum.year
        if (self.geburtsdatum.month, self.geburtsdatum.day) > (heute.month, heute.day): #Tupelvergleich, hatte die Person dieses Jahr noch nicht Geburtstag?
            jahre -= 1 # Kurzform für: jahre = jahre -1
        return jahre

# Objekte Instanz der Klasse Teilnehmer
torsten = Teilnehmer("Torsten", "Aachen", date(1967, 1, 1), ["C"])
michael = Teilnehmer("Michael", "Moormerland", date(1981, 1, 10), ["Javascript"])
karpoo = Teilnehmer("Karpoo", "Düsseldorf", date(1969, 1, 1), ["ABAP"])
carsten = Teilnehmer("Carsten", "Aachen", date(1971, 3, 3), ["Basic"])
thomas = Teilnehmer("Thomas", "Bielefeld", date(1964, 10, 12), ["Pascal"])
angela = Teilnehmer("Angela", "Lingen", date(1983, 12, 31), ["C", "Java"])
jonas = Teilnehmer("Jonas", "Löhne", date(1997, 4, 4), [])
marco = Teilnehmer("Marco", "Bielefeld", date(1975, 6, 24), [])
roman = Teilnehmer("Roman", "Hannover", date(1984, 2, 28), [])
daniel = Teilnehmer("Daniel", "Bielefeld", date(1980, 1, 1), ["Python"])

teilnehmerliste = [torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel]

print(marco.vorname)    # Attribut
print(marco.alter())    # Methode (Man fragt)

# 1) Durchschnittsalter
#altersangaben = []
#for teilnehmer in teilnehmerliste:

# a) List Comprehension
altersliste = [teilnehmer.alter() for teilnehmer in teilnehmerliste]
print(sum(altersliste) / len(altersliste))

# b) Map
altersliste = list(map(lambda teilnehmer: teilnehmer.alter(), teilnehmerliste))
print(sum(altersliste) / len(altersliste))


# 2a) Alle Vornamen der Teilnehmer aus Bielefeld
bielefelder = [teilnehmer.vorname for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(bielefelder)


# 2b) Alle Teilnehmer aus Bielefeld
bielefelder = [teilnehmer for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(bielefelder)


# 3) Durchscnittsalter aller Bielefelder
durchschnittsalterliste = [teilnehmer.alter() for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(sum(durchschnittsalterliste) / len(durchschnittsalterliste))


# 4) Vornamen der Teilnehmer, die am meisten Programmiersprachen sprechen
laengen = [len(teilnehmer.sprachen) for teilnehmer in teilnehmerliste]
print(laengen)
m = max(laengen)
vornamen = [teilnehmer.vorname for teilnehmer in teilnehmerliste if m == len(teilnehmer.sprachen)]
print(vornamen)

# 5) Alle Teilnehmer aufsetigend sortiert nach Vornamen
sortiert = sorted(teilnehmerliste, key=lambda teilnehmer: teilnehmer.vorname)
print(sortiert)

# 7) Alle Teilnehmer aufsteigend sortiert nach Alter und dann Vorname
sortiert = sorted(teilnehmerliste, key=lambda teilnehmer: (teilnehmer.alter(), teilnehmer.vorname))
print(sortiert)