class Uhr (object):

    def __init__(self, stunde, minute, sekunde, darstellung):
        self.sekunde = sekunde
        self.minute = minute
        self.stunde= stunde
        self.darstellung = darstellung

    def __repr__(self):
            return "{:02d}:{:02d}:{:02d}".format(self.stunde, self.minute, self.sekunde)

    def naechsteSekunde(self):
        self.sekunde += 1

        if self.sekunde > 59:
            self.sekunde = 0
            self.minute += 1
            if self.minute > 59:
                self.minute = 0
                self.stunde += 1
                if self.stunde > self.darstellung - 1:
                    self.stunde = 0
                    self.minute = 0
                    self.sekunde = 0


if __name__ == "__main__":
    u = Uhr(00, 00, 1, 24)

    for i in range(10):
        u.naechsteSekunde()
        print(u)
