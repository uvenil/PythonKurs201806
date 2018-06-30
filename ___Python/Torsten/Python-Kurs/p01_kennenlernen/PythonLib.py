from datetime import date

# 1) Berechnung des Alters; Geburtdatum wird übergeben
def alter(geburtsdatum):
    heute = date.today()
    jahre = heute.year - geburtsdatum.year
    if (geburtsdatum.month, geburtsdatum.day) > (heute.month, heute.day):
        jahre -= 1
    return(jahre)

def celsius_nach_fahrenheit(celsius):
    return celsius * 1.8 + 32