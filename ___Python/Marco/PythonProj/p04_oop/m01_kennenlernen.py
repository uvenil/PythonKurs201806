from datetime import date

from p01.m_01 import teilnehmer


class Teilnehmer(object):
    # Konstruktormethode
    def __init__ (self, vorname, ort, geburtsdatum, sprachen):
        self.vorname = vorname
        self.ort = ort
        self.geburtsdatum = geburtsdatum
        self.sprachen = sprachen


    def __repr__(self):
        return "%s %s %s" % (self.vorname, self.ort, self.geburtsdatum)




    def alter(self) -> object:
        heute = date.today()
        jahre = heute.year - self.geburtsdatum.year
        if (self.geburtsdatum.month, self.geburtsdatum.day) > (heute.month, heute.day):  # hatte die Person dieses Jahr noch nicht Geburtstag
            jahre -= 1  # Kurzform für jahre = jahre - 1
        return jahre

torsten = Teilnehmer("Torsten", "Aachen", date(1967, 1, 1), ["C"])
michael = Teilnehmer("Michael", "Moormerland", date(1981, 10, 1), ["Javascript"])
karpoo = Teilnehmer("Karpoo", "Düsseldorf", date(1969, 1, 1), ["ABAP"])
carsten = Teilnehmer("Carsten", "Aachen", date(1971, 1, 1), ["Basic"])
thomas = Teilnehmer("Thomas", "Bielefeld", date(1964, 1, 1), ["Pascal"])
angela = Teilnehmer("Angela", "Lingen", date(1983, 1, 1), ["c", "Java"])
jonas = Teilnehmer("Jonas", "Löhne", date(1997, 4, 4), [])
marco = Teilnehmer("Marco", "Bielefeld", date(1975, 6, 24), [])
roman = Teilnehmer("Roman", "Hannover", date(1984, 2, 28), [])
daniel = Teilnehmer("Daniel", "Bielefeld", date(1980, 1, 1), ["Python"])

teilnehmerliste = [torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel] #Zuweisung

# 0) Durchschnittsalter
#  print(daniel.vorname) # marco[0]
print(daniel.alter()) # alter(marco[0])

# 1) Durchschnittsalter

# b) list comprehension
altersliste = [teilnehmer.alter() for teilnehmer in teilnehmerliste]
print(sum(altersliste) / len(altersliste))

# b) map
altersliste = list(map(lambda teilnehmer: teilnehmer.alter(), teilnehmerliste))
print(sum(altersliste) / len(altersliste))

#) 2) Alle Teilnehmer aus Bielefeld
bielefelder = [teilnehmer for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(bielefelder)

#) 2a) Alle Teilnehmer aus Bielefeld
bielefelder = [teilnehmer.vorname for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(bielefelder)


#) 3) Durchschnittsalter aller Bielefelder
durchschnitt = [teilnehmer.alter () for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(sum(durchschnitt)/len(durchschnitt))

# 4) Vorname der Teilnehmer, die am meisten Sprachen können
laengen = [len(teilnehmer.sprachen) for teilnehmer in teilnehmerliste]
print(laengen)
m = max(laengen)
vornamen = [teilnehmer.vorname for teilnehmer in teilnehmerliste if m == len(teilnehmer.sprachen)]
print(vornamen)

# 5) Alle Teilnehmer sortiert nach Vornamen aufsteigend
sortiert = sorted(teilnehmerliste, key=lambda teilnehmer: teilnehmer.vorname)
print(sortiert)

# 7 Alle Teilnehmer aufsteigend sortiert nach Alter und dann Vorname
sortiert = sorted(teilnehmerliste, key=lambda teilnehmer: (teilnehmer.alter(), teilnehmer.vorname))
print(sortiert)










