from p04_oop.m02_kalender import Kalender
from p04_oop.m03_uhr import Uhr

class KalenderUhr(Kalender, Uhr):
    def __init__(self, tag, monat, jahr, stunde, minute, sekunde):
        Kalender.__init__(self, tag, monat, jahr)
        Uhr.__init__(self, stunde, minute, sekunde)

    def __repr__(self):
        return Kalender.__repr__(self) + "  " + Uhr.__repr__(self)

    def naechsteSekunde(self):
        super().naechsteSekunde()
        if (self.stunde, self.minute, self.sekunde) == (0, 0, 0):
            super().naechsterTag()

if __name__ == "__main__":
    k = KalenderUhr(28, 2, 2000, 23, 59, 58)
    for i in range(10): # 10 mal wiederholen
        k.naechsteSekunde()
        print(k)
