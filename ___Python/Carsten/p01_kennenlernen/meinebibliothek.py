from datetime import date


# Funktion Alter mit einem Parameter
def alter(geburtsdatum):
    heute = date.today()
    jahre = heute.year - geburtsdatum.year
    if (geburtsdatum.month, geburtsdatum.day) > (heute.month, heute.day) : # dieses Jahr noch nicht Geburtstag?
        jahre -= 1 # Kurzform jahre = jahre - 1
    return jahre

def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32
