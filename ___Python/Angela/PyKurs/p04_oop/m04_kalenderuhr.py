from p04_oop.m02_kalender import Kalender
from p04_oop.m03_uhr import Uhr


class KalenderUhr(Kalender, Uhr):   # alle Eigenschaften und Methoden werden vererbt
    def __init__(self, tag, monat, jahr, stunde, minute, sekunde):
        Kalender.__init__(self, tag, monat, jahr)
        Uhr.__init__(self, stunde, minute, sekunde)     # Oberklasse benennen

    def __repr__(self):
        return Kalender.__repr__(self) + " " + Uhr.__repr__(self)

    def naechsteSekunde(self):  #Methode ueberschreiben
        super().naechsteSekunde()               # super ruft die naechste Version in der Hierachie auf
        if (self.stunde, self.minute, self.sekunde) == (0, 0, 0):   #Mitternacht
            super().naechsterTag()

if __name__ == "__main__":
    k = KalenderUhr(31, 12, 1999, 23, 59, 58)
    for i in range(10):
        k.naechsteSekunde()
        print(k)