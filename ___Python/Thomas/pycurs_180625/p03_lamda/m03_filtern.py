temp_celsius = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] #Durschnittstemperaturen Bielefeld


def mindestens15(temperatur):
    return temperatur >=15 # Boolean temp>=15 -> TRUE

def zwischen5und10(temperatur):
    return (5 <= temperatur and temperatur <=10)

# Alle Temperaturen >= 15
def filtern(liste, kriterium):
    gefiltert = []
    for element in liste:
        if kriterium(element): # Funktion wird übergeben !!
            gefiltert.append(element)
    return gefiltert

print(filtern(temp_celsius, mindestens15))
print(filtern(temp_celsius, zwischen5und10))