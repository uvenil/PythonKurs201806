from p04_oop.m02_kalender import Kalender
from p04_oop.m03_uhr import Uhr


class Kalenderuhr(Kalender, Uhr):
    def __init__(self, tag, monat, jahr, stunde, minute, sekunde, darstellung):
        Kalender.__init__(self, tag, monat, jahr) # Kein SUPER, weil die Funktion in jeder Klasse enthalten ist.
        Uhr.__init__(self, stunde, minute, sekunde, darstellung)

    def __repr__(self):
        return Kalender.__repr__(self) + " " + Uhr.__repr__(self)

    def naechsteSekunde(self):
        super().naechsteSekunde() # SUPER(), weil die Funktion in beider Klassen nur ein mal vorkommt.
        if(self.stunde, self.minute, self.sekunde) == (0, 0, 0):
            super().naechsterTag()



if __name__ == "__main__":
    k = Kalenderuhr(31, 12, 1999, 11, 59, 58, 12)

    for i in range(10):
        k.naechsteSekunde()
        print(k)