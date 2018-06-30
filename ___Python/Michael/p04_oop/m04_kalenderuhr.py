from p04_oop.m02_kalender import Kalender
from p04_oop.m03_uhr import Uhr


class KalenderUhr(Kalender, Uhr):
    pass
    def __init__(self, tag, monat, jahr, stunde, minute, sekunde):
        Kalender.__init__(self, tag, monat, jahr)
        Uhr.__init__(self, stunde, minute, sekunde)

    def __repr__(self):
        # Kalender.__repr__(self)
        # Uhr.__repr__(self)

    # def __str__(self):
        return "%02i.%02i.%04i" % (self.tag, self.monat, self.jahr) + " - " + "%02i.%02i.%02i" % (self.stunde, self.minute, self.sekunde)

    def naechsteSekunde(self):
        super().naechsteSekunde()
        # if (self.stunde == 0 and self.minute == 0 and self.sekunde == 0):
        if (self.stunde, self.minute,  self.sekunde) == (0, 0, 0):
            super().naechsterTag()


if __name__ == "__main__":
    ku = KalenderUhr(28, 2, 2000, 23, 59, 59)
    print(ku)
    for i in range(10):
        ku.naechsteSekunde()
        print(ku)
