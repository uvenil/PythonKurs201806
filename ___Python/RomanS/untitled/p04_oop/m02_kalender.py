class Kalender(object):
    tageProMonat = (None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    #print(sum(tageProMonat))

    def __init__(self, tag, monat, jahr):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr

    def schaltjahr(self):
        return self.jahr % 400 == 0 or (self.jahr % 100 != 0 and self.jahr % 4 == 0)

    def naechsterTag(self):
        self.tag +=1

        korrektur = 1 if self.schaltjahr() and self.monat == 2 else 0  #ternary operator

        if self.tag > Kalender.tageProMonat[self.monat] + korrektur:
            self.tag = 1
            self.monat +=1
            if self.monat > 12:
                self.jahr +=1
                self.monat =1
    def __repr__(self):
        return "%02i.%02i.%04i" % (self.tag, self.monat, self.jahr)

if __name__ == "__main__":

    k = Kalender(30, 12, 2017)
    for i in range (10):    # 10 mal wiederholen
        k.naechsterTag()
        print(k)