from datetime import date

class Teilnehmer(object):
    def __init__(self, vorname, ort, geburtsdatum, sprachen):
        self.vorname = vorname
        self.ort = ort
        self.geburtsdatum = geburtsdatum
        self.sprachen = sprachen

    def __repr__(self):
        return "{} {}".format(self.vorname, self.ort)

    def alter(self):
        heute = date.today()
        jahre = heute.year - self.geburtsdatum.year
        if (self.geburtsdatum.month, self.geburtsdatum.day) > (heute.month, heute.day):
            jahre -= 1
        return (jahre)

torsten = Teilnehmer("Torsten", "Aachen", date(1967,1,1,), ["C"])
daniel = Teilnehmer("Daniel", "Bielefeld", date(1980,1,1), ["Python"])
michael = Teilnehmer("Michael", "Moormerland", date(1981,1,10), ["Javascript"])
karpoo = Teilnehmer("Karpoo", "Düsseldorf", date(1969,1,1), ["APAP"])
carsten = Teilnehmer("Carsten", "Aachen", date(1971,2,3), ["Basic", "C"])
thomas = Teilnehmer("Thomas", "Bielefeld", date(1964,10,12), ["Pascal"])
angela = Teilnehmer("Angela", "Lingen", date(1983,12,31), ["C", "Java"])
jonas = Teilnehmer("Jonas", "Löhne", date(1997,4,4), [])
marco = Teilnehmer("Marco", "Bielefeld", date(1975,6, 24), [])
roman = Teilnehmer("Roman", "Hanover", date(1984,2,27), [""])

teilnehmerliste = [daniel, torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman]


print(marco.vorname)
print(marco.alter())

# 1) Durchschnittsalter

altersliste = [teilnehmer.alter() for teilnehmer in teilnehmerliste]
print("Durchschnittsalter:", sum(altersliste) /( len(altersliste)))

altersliste = list(map(lambda teilnehmer: teilnehmer.alter(), teilnehmerliste))
print("Durchschnittsalter:", sum(altersliste) /( len(altersliste)))

# 2a) Alle Vornamen der Teilnehmer aus Bielefeld
teilnehmerbielefeld = [teilnehmer.vorname for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(teilnehmerbielefeld)

# 2b) Alle Teilnehmer aus Bielefeld
teilnehmerbielefeld = [teilnehmer for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print(teilnehmerbielefeld)

# 3) Durchschnittsalter aller Teilnehmer aus Bielefeld
teilnehmeralterbielefeld = [teilnehmer.alter() for teilnehmer in teilnehmerliste if teilnehmer.ort == "Bielefeld"]
print("Durchschnittsalter (Bielefelder):", sum(teilnehmeralterbielefeld) / (len(teilnehmeralterbielefeld)))

# 4) Vornamen der Teilnehmer, die am meisten Sprachen beherrschen
d = [len(teilnehmer.sprachen) for teilnehmer in teilnehmerliste]
maxsprachen = max(d)
teilnehmermaxsprachen = [teilnehmer.vorname for teilnehmer in teilnehmerliste if len(teilnehmer.sprachen) == maxsprachen]
print("Teilnehmer mit max. Anzahl(",maxsprachen, ") Sprachen:", teilnehmermaxsprachen)

# 5) Alle Teilnehmer nach Vornamen aufsteigend
sortiert = sorted(teilnehmerliste, key=lambda teilnehmer: teilnehmer.vorname)
print("Teilnehmer sortiert nach Vornamen:", sortiert)

# 5) Alle Teilnehmer nach Ort und Vornamen aufsteigend
sortiert = sorted(teilnehmerliste, key=lambda teilnehmer: (teilnehmer.ort, teilnehmer.vorname))
print("Teilnehmer sortiert nach Ort und Vornamen:", sortiert)

print("________________")


# 6) Generator für die Eigenschaften aller Personen

def showProperties(obj):
    for item in obj:
        yield "\n{}".format(item)

        for key, value in item.__dict__.items():
            yield "{}: {}".format(key.capitalize(), value)

f = showProperties(teilnehmerliste)

for x in f:
    print(x)

print()

f = showProperties(teilnehmerliste)
l = []
for x in f:
    l.append(x)
print(l)

