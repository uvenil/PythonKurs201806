from p04_oop.m02_kalender import Kalender
from p04_oop.m03_uhr import Uhr

class KalenderUhr(Kalender, Uhr):
    def __init__(self, tag, monat, jahr, stunden, minuten, sekunden):
        Kalender.__init__(self, tag, monat, jahr)
        Uhr.__init__(self, stunden, minuten, sekunden)

    def __repr__(self):
        return Kalender.__repr__(self) + " " + Uhr.__repr__(self)

    def naechsteSekunde(self):
        super().naechsteSekunde()
        if(self.stunden, self.minuten, self.sekunden) == (0, 0, 0):
            super().naechsterTag()

if __name__ == "__main__":
    ku = KalenderUhr(31, 12, 1999, 23, 59, 59)
    print(ku)

    for i in range(10):  # 10 mal wiederholen
        ku.naechsteSekunde()
        print(ku)
