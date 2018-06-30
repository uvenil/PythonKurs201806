class Uhr(object):

    # Konstruktor
    def __init__(self, stunden, minuten, sekunden):
        self.sekunden = sekunden
        self.minuten = minuten
        self.stunden = stunden

    def __repr__(self):
        return "%02i:%02i:%02i" % (self.stunden, self.minuten, self.sekunden)

    def naechsteSekunde(self):
        self.sekunden += 1

        if self.sekunden > 59:
            self.sekunden = 0
            self.minuten += 1
            if self.minuten > 59:
                self.minuten = 0
                self.stunden += 1
                if self.stunden > 23:
                    self.stunden = 0

if __name__ == "__main__":
    u = Uhr(23, 59, 58)

    for i in range(10):  # 10 mal wiederholen
        u.naechsteSekunde()
        print(u)