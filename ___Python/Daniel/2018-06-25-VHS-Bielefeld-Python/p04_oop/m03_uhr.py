class Uhr(object):
    def __init__(self, stunde, minute, sekunde):
        self.sekunde = sekunde
        self.minute = minute
        self.stunde = stunde

    def naechsteSekunde(self):
        self.sekunde += 1

        if self.sekunde >= 60:
            self.sekunde = 0
            self.minute += 1
            if self.minute >= 60:
                self.minute = 0
                self.stunde += 1
                if self.stunde >= 24:
                    self.stunde = 0

    def __repr__(self):
        return "%02i:%02i:%02i" % (self.stunde, self.minute, self.sekunde)

if __name__ == "__main__":
    k = Uhr(23, 59, 58)
    for i in range(10): # 10 mal wiederholen
        k.naechsteSekunde()
        print(k)
