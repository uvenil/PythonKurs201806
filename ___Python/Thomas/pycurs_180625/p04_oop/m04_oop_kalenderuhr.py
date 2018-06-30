from p04_oop.m02_oop_kalender import Kalender
from p04_oop.m03_oop_uhr import Uhr

class KalenderUhr(Kalender, Uhr): #vererben
    def __init__(self, tag, monat, jahr, stunde, minute, sekunde):
        Kalender.__init__(self, tag, monat, jahr)
        Uhr.__init__(self, stunde, minute, sekunde)

    def __repr__(self):
        return  Kalender.__repr__(self) + " " + Uhr.__repr__(self)

    def naechste_sekunde(self):
        super().naechste_sekunde()
        # python3 äquivalent Uhr.naechste_sekunde(self)
        # python2 aquivalent super(KalenderUhr, self).naechste_sekunde()
        if (self.stunde, self.minute, self.sekunde) == (0, 0, 0): #Mitternacht -> Kalender Tag + 1
            super().naechsterTag()

if __name__ == "__main__":
    k = KalenderUhr(31, 12, 1999, 23, 59, 58)
    for i in range(10): # 10 mal wiederholen
        k.naechste_sekunde()
        print(k)
