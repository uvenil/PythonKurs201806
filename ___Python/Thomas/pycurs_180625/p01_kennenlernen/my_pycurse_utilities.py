from datetime import date

# Funktion alter mit einem Parameter geburtsdatum
def alter(geburtsdatum):
    heute = date.today()
    jahre = heute.year-geburtsdatum.year
    #   Pos 0               Pos 1                   Pos 2       Pos 3
    if (geburtsdatum.month, geburtsdatum.day) >= (heute.month, heute.day): # tuple Vergleich Pos0 Pos2 wenn gleich dann Vergleich Pos1 Pos3
        jahre -= 1 # Kurzform für: jahre = jahre -1
    return(jahre)

def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def fahrenheit_to_celsius(fahrenheit):
    return ((fahrenheit - 32)/1.8)
