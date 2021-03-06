celsius_temperaturen = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] #Durchschnittstemperaturen in Bilefeld nach Monat

#def mindestens15(temperatur):
#    return temperatur >= 15

mindestens15 = lambda temperatur: temperatur >= 15 # entspricht der o.g. Funktion def mindestens15(temperatur):

def zwischen5und10(temperatur):
    return 5 <= temperatur and temperatur <= 10


print(*filter(mindestens15, celsius_temperaturen))
print(list(filter(lambda temperatur: temperatur >= 15, celsius_temperaturen)))
print(*filter(zwischen5und10, celsius_temperaturen))
print(list(filter(lambda temperatur: 5 <= temperatur and temperatur <= 10, celsius_temperaturen)))
