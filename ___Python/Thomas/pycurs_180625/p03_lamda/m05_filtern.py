temp_celsius = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] #Durschnittstemperaturen Bielefeld

# Funktion
# def mindestens15(temperatur):
#     return temperatur >=15 # Boolean temp>=15 -> TRUE
# umgewandelt in lambda
# mindestens15 = lambda temperatur: temperatur >= 15


def zwischen5und10(temperatur):
    return (5 <= temperatur and temperatur <=10)

print(list(filter(lambda temperatur: temperatur >= 15, temp_celsius)))
print(list(filter(lambda temperatur: 5 <= temperatur and temperatur <=10, temp_celsius)))
print(list(filter(zwischen5und10, temp_celsius)))