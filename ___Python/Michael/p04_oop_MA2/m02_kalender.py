class Kalender(object):
    tagepromonat = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, tag, monat, jahr):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr

    def naechsterTag(self):
        self.tag += 1

        korrektur = 1 if self.schal

        if self.tag > Kalender.tagepromonat[self.monat]: # TODO: nicht alle Monate haben 31 Tage
            self.tag = 1
            self.monat += 1
            if self.monat > 12:
                self.monat = 1
                self.jahr += 1

    def __repr__(self):
        return "%02i.%02i.%04i" % (self.tag, self.monat, self.jahr)


k = Kalender(26, 2, 1999)

print(sum(Kalender.tagepromonat))


for i in range(10): # 10 mal wiederholen
    k.naechsterTag()
    print(k)
