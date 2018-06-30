from datetime import date

class Teilnehmer(object):
    def __init__(self, vorname, ort, geburtsdatum, sprachen): # Konstruktormethode
        self.vorname = vorname #Attribute
        self.ort = ort
        self.geburtsdatum = geburtsdatum
        self.sprachen = sprachen

    def __repr__(self): #Representation method
        return "%s %s %s %s" % (self.vorname, self.geburtsdatum, self.ort, self.sprachen)

    def my_repr(self): #individuelle Representation method
        return "%s %s %s" % (self.vorname, self.geburtsdatum, self.ort)


    def alter(self):
        heute = date.today()
        jahre = heute.year-self.geburtsdatum.year
        #   Pos 0               Pos 1                   Pos 2       Pos 3
        if (self.geburtsdatum.month, self.geburtsdatum.day) >= (heute.month, heute.day): # tuple Vergleich Pos0 Pos2 wenn gleich dann Vergleich Pos1 Pos3
            jahre -= 1 # Kurzform für: jahre = jahre -1
        return jahre



#Erzeugung Instanz
torsten = Teilnehmer("Torsten", "Aachen", date(1967, 1,1), ["C"])
michael = Teilnehmer("Michael", "Moormerland", date(1981, 1, 10), ["Javascript"])
karpoo = Teilnehmer("Karpoo", "Düsseldorf", date(1969, 1,1), ["ABAP"])
carsten = Teilnehmer("Carsten", "Aachen", date(1971, 2, 3), ["Basic"])
thomas = Teilnehmer("Thomas", "Bielefeld", date(1964, 10, 12), ["Pascal"])
angela = Teilnehmer("Angela", "Lingen", date(1983, 12, 31), ["C", "Java"])
jonas = Teilnehmer("Jonas", "Löhne", date(1997, 4, 4), [])
marco = Teilnehmer("Marco", "Bielefeld", date(1975, 6, 24), [])
roman = Teilnehmer("Roman", "Hannover", date(1984, 2, 28), [])
daniel = Teilnehmer("Daniel", "Bielefeld", date(1980, 1, 1), ["Python"])

teilnehmerliste = [torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel]

print(carsten.ort)
print(marco.vorname)
print(marco.alter())

# Durchschnittsalter

# a) List Comprehension
altersliste = [teilnehmer.alter() for teilnehmer in teilnehmerliste]
print(sum(altersliste)/len(teilnehmerliste))

# b) Map
altersliste = list(map(lambda teilnehmer: teilnehmer.alter(), teilnehmerliste))
print(sum(altersliste) / len(altersliste))

# Alle Teilnehmer aus Bielefeld
selectlist = [teilnehmer.vorname for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(selectlist)

# Alle Teilnehmer aus Bielefeld
selectlist = [teilnehmer for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(selectlist)

# Durchscnittsalter aller Bielefelder
selectlist = [teilnehmer.alter() for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(sum(selectlist) /len(selectlist))

# Welche Teilnehmer sprechen die meisten Programmiersprachen

selectlist1 = [len(teilnehmer.sprachen) for teilnehmer in teilnehmerliste]
print(selectlist1)
maxlist1 = max(selectlist1) #Maximum nicht im nächsten Ausdruck ermitteln -> Laufzeit!!!
selectlist2 = [teilnehmer.vorname for teilnehmer in teilnehmerliste if maxlist1 == len(teilnehmer.sprachen)]
print(selectlist2)

# Alle Teilnehmer aufsteigend sortiert nach Vornamen
selectlist3 = sorted(teilnehmerliste, key=lambda teilnehmer: teilnehmer.vorname)
print(selectlist3)

# Alle Teilnehmer aufsteigend sortiert nach Ort und Vornamen
selectlist3 = sorted(teilnehmerliste, key=lambda teilnehmer: (teilnehmer.ort, teilnehmer.vorname))
print(selectlist3)

# Teilnehmerliste mit my_repr ausgeben
print(list(map(lambda teilnehmer: teilnehmer.my_repr(), teilnehmerliste)))
