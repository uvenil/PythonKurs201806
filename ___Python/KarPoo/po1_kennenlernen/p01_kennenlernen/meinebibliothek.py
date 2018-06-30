from datetime import date

# Funktion alter mit einem Parameter geburtsdatum
def alter(geburtsdatum):
    heute = date.today()
    jahre = heute.year - geburtsdatum.year
    if (geburtsdatum.month, geburtsdatum.day) > (heute.month, heute.day): # hatte die Person dieses Jahr noch nicht geburtstag?
        jahre -= 1 #jahre = jahre - 1
    else:
        jahre = jahre

    return jahre

# Funktion celsius nach fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32.0