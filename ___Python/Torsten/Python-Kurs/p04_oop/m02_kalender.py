class Kalender (object):
    tageProMonat = (None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, tag, monat, jahr):
        self.tag = tag
        self.monat = monat
        self.jahr= jahr

    def schaltjahr(self):
        return self.jahr% 400 == 0 or (self.jahr % 100 != 0 and self.jahr % 4 == 0)

    def __repr__(self):
        return "{:02}.{:02}.{:04}".format(self.tag, self.monat, self.jahr)

    def naechsterTag(self):
        self.tag += 1

        korrektur = 1 if self.schaltjahr() and self.monat == 2 else 0

        if self.tag > Kalender.tageProMonat[self.monat] + korrektur:
            self.tag = 1
            self.monat += 1
            if self.monat > 12:
                self.monat = 1
                self.jahr += 1


if __name__ == "__main__":
    k = Kalender(27, 2, 1999)

    for i in range(10):
        k.naechsterTag()
        print(k)
