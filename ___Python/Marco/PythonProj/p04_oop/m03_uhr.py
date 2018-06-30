
class Uhr(object):

    def __init__(self, stunde, minute, sekunde):
        self.stunde = stunde
        self.minute = minute
        self.sekunde = sekunde

    def naechsteSekunde(self):
        self.sekunde += 1
        if self.sekunde > 59:
            self.sekunde = 0
            self.minute += 1
            if self.minute > 59:
                self.minute = 0
                self.stunde +=1
                if self.stunde > 23:
                    self.stunde = 0


    def __repr__(self):
        return "%02i:%02i:%02i" % (self.stunde, self.minute, self.sekunde) # % = Platzhalter i = ganze Zahlen 02=2 Stellen wenn eine leer dann 0

if __name__ == "__main__":

    u = Uhr(0, 0, 1)
    for i in range(10):
        u.naechsteSekunde()
        print(u)

