class Kalender(object):
    # Woerterbuch waere Overkill, da Werte gleich die Worte sind, deswegen Tupel (wie Liste, aber nicht veraenderbar)
    tageProMonat = (None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) #None ist nur Platzhalter, damit Monat dem Index entspricht

    def __init__(self, tag, monat, jahr):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr

    def schaltjahr(self):
        return self.jahr % 400 == 0 or (self.jahr % 100 != 0 and self.jahr % 4 == 0) # Wenn Rest 0

    def naechsterTag(self): #Methode
        self.tag += 1

        # if self.schaltjahr() and self.monat == 2:
        #     korrektur = 1
        # else:
        #     korrektur = 0

        korrektur = 1 if self.schaltjahr() and self.monat == 2 else 0 #ternary operator

        if self.tag > Kalender.tageProMonat[self.monat] + korrektur:
            self.tag = 1
            self.monat += 1
            if self.monat > 12:
                self.monat = 1
                self.jahr += 1

    def __repr__(self):
        return "%02i.%02i.%04i" % (self.tag, self.monat, self.jahr)

# Fuehre das aus, wenn dieses Skript ausgefuehrt wird (nicht, wenn KalenderUhr gestartet wird), nur zum Test
if __name__ == "__main__":
    k = Kalender(20, 2, 2000)
    for i in range(10): # 10 mal wiederholen; range() ist eingebaute Funktion
        k.naechsterTag()
        print(k)