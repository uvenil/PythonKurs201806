from datetime import date
import statistics
import math

class Teilnehmer(object):
    #Konstruktormethode
    def __init__(self, vorname, ort, geburtsdatum, sprachen):
        self.vorname = vorname
        self.ort = ort
        self.geburtsdatum = geburtsdatum
        self.sprachen = sprachen

        # representation method
    def __repr__(self):
        return "%s %s %s %s" % (self.vorname, self.ort, self.geburtsdatum, self.sprachen)
        # return self.vorname + " " + self.ort + " " + str(self.geburtsdatum) + " " + str(self.sprachen)

    def alter(self):
        heute = date.today()
        jahre = heute.year - self.geburtsdatum.year
        if (self.geburtsdatum.month, self.geburtsdatum.day) > (heute.month, heute.day):  # Wenn Monate kleiner oder gleich sind, vergleiche die Tage, hatte diese Pers diese Jahr schon Geb.?
            jahre -= 1          # Kurzform für jahre = jahre - 1
        return jahre

torsten = Teilnehmer("Torsten",     "Aachen",       date(1967,1,1),     ["C"])
michael = Teilnehmer("Michael",     "Moormerland",  date(1981,1,10),    ["Python"])
karpoo = Teilnehmer("Karpoo",      "Düsseldorf",   date(1969,1,1),     ["ABAP"])
carsten = Teilnehmer("Carsten",     "Aachen",       date(1971,2,3),     ["Basic"])
thomas = Teilnehmer("Thomas",      "Bielefeld",    date(1964,10,12),   ["Pascal"])
angela = Teilnehmer("Angela",      "Lingen",       date(1983,12,31),   ["C", "Java"])
jonas = Teilnehmer("Jonas",       "Löhne",        date(1997,4,4),     [])
marco = Teilnehmer("Marco",       "Bielefeld",    date(1975,6,24),    [])
roman = Teilnehmer("Roman",       "Hannover",     date(1984,2,28),    [])
daniel = Teilnehmer("Daniel",      "Bielefeld",    date(1980,1,1),     ["Python"])

teilnehmerliste = [torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel]

print(marco.vorname)
print(marco.alter())

# 1) Durschnittsalter

# a) List Comprehension
altersliste = [teilnehmer.alter() for teilnehmer in teilnehmerliste]
print(sum(altersliste)/len(altersliste))

# b) Map
altersliste = list(map(lambda teilnehmer:teilnehmer.alter(), teilnehmerliste))
print(sum(altersliste)/len(altersliste))

# 2a) Alle Vornamen der Teilnehmer aus Bielefeld

bfelder = [teilnehmer.vorname for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(bfelder)

# 2b) Alle  Teilnehmer aus Bielefeld
bfelder = [teilnehmer.ort for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(bfelder)


# 3) Durschnittsalter aller Bielefelder

bfelderalter = round(statistics.mean(list([teilnehmer.alter() for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"])),2)
print("Durschnittsalter = ", bfelderalter)


# 4) Welche Teilnehmer sprechen am meisten Programmiersprachen, Vornamen
laenge = [len(teilnehmer.sprachen) for teilnehmer in teilnehmerliste]
print(laenge)
m = max(laenge)
vornamen = [teilnehmer.vorname for teilnehmer in teilnehmerliste if max(laenge) == len(teilnehmer.sprachen)]
print(vornamen)

# 5) Alle Teilnehmer aufsteigend sortiert nach Vorname
sortiert = sorted(teilnehmerliste, key=lambda teilnehmer: teilnehmer.vorname)
print(sortiert)

# 6) Alle Teilnehmer aufsteigend sortiert nach nachname dann Vorname
#sortiert = sorted(teilnehmerliste, key=lambda teilnehmer: teilnehmer.vorname)
#print(sortiert)

# 7) Alle Teilnehmer aufsteigend sortiert nach alter dann Vorname
sortiert = sorted(teilnehmerliste, key=lambda teilnehmer: (teilnehmer.alter(), teilnehmer.vorname))
print(sortiert)

