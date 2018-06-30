from datetime import date


class Teilnehmer(object):
    # Konstruktormethode
    def __init__(self, vorname, ort, geburtsdatum, sprachen):
        self.vorname = vorname
        self.ort = ort
        self.geburtsdatum = geburtsdatum
        self.sprachen = sprachen

    def __repr__(self): # representation mathod %s = string
        return "%s %s %s %s" % (self.vorname, self.ort, self.geburtsdatum, self.sprachen) # damit sich objekt sich selbst darstellen kann


    def alter(self):
        heute = date.today()
        jahre = heute.year - self.geburtsdatum.year
        if (self.geburtsdatum.month, self.geburtsdatum.day) >= (heute.month, heute.day):  # hatte die Person diese Jahr noch nicht Geburtstag?
            jahre -= 1  # Kurzform für: jahre = jahre - 1
        return jahre

torsten = Teilnehmer("Torsten", "Aachen", date(1967, 1, 1), ["C"])
michael = Teilnehmer ("Michael", "Moormerland", date(1981, 1, 10), ["Javescript"])
karpoo = Teilnehmer("Karpoo", "Düsseldorf", date(1969, 1, 1), ["ABAP"])
carsten = Teilnehmer("Carsten", "Aachen", date(1971, 2, 3), ["Basic"])
thomas = Teilnehmer("Thomas", "Bielefeld", date(1964, 10, 12), ["Pascal"])
angela = Teilnehmer("Angela", "Lingen", date(1983, 12, 31), ["C","Java"])
jonas = Teilnehmer("Jonas", "Löhne", date(1997, 4, 4), [])
marco = Teilnehmer("Marco", "Bielefeld", date(1975, 6, 24), [])
roman = Teilnehmer("Roman", "Hannover", date(1984, 2, 28), [])
daniel = Teilnehmer("Daniel", "Bielefeld", date(1980, 1, 1), ["Python"])

teilnehmerListe = [torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel]

print(marco.alter()) #Methode
print(marco.vorname) #Eigenschaft

# 1) Durchschnittsalter
# a) List Comprehension
altersliste = [teilnehmer.alter() for teilnehmer in teilnehmerListe]
print(sum(altersliste) / len(altersliste))

# b) Map
altersliste = list(map(lambda teilnehmer: teilnehmer.alter(), teilnehmerListe))
print(sum(altersliste) / len(altersliste))

# 2a) Alle Vornamen der Teilnehmer aus Bielefeld
teilnehmerBielefeld = [teilnehmer.vorname for teilnehmer in teilnehmerListe if teilnehmer.ort == "Bielefeld"]
print(teilnehmerBielefeld)

# 2b) Alle Teilnehmer aus Bielefeld
teilnehmerBielefeld = [teilnehmer for teilnehmer in teilnehmerListe if teilnehmer.ort == "Bielefeld"]
print(teilnehmerBielefeld)


# 3) Durchschnittsalter aller Bielefeld
alterBielefelder = [teilnehmer.alter() for teilnehmer in teilnehmerListe if teilnehmer.ort == "Bielefeld"]
print (sum(alterBielefelder) / len(alterBielefelder))

# 4) Vorname der Teilnehmer, die am meisten Programmiersprachen sprechen
anzahlsprachen = [len(teilnehmer.sprachen) for teilnehmer in teilnehmerListe]
m = max(anzahlsprachen)
vornamen = [teilnehmer.vorname for teilnehmer in teilnehmerListe if m == len(teilnehmer.sprachen)]
print (vornamen)

# 5) Alle Teilnehmer sortiert nach Vornamen aufsteigend
sortiert = sorted(teilnehmerListe, key=lambda teilnehmer: teilnehmer.vorname)
print(sortiert)

# 6) Alle Teilnehmer sortiert nach Alter und dann nach Vorname
sortiert = sorted(teilnehmerListe, key=lambda teilnehmer: (teilnehmer.alter(), teilnehmer.vorname))
print(sortiert)
