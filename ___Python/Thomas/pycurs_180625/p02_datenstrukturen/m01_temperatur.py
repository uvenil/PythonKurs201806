celsius = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] #Durschnittstemperaturen Bielefeld

# Liste Umrechnung in Fahrenheit erzeugen (FOR-Schleife)
wertefahrenheit = []
for wertecelsius in celsius:
    wertefahrenheit.append(round((wertecelsius*1.8)+32, 2)) # F = C*1.8 + 32      C = (F-32)/1.8
print(wertefahrenheit)

# Liste Umrechnung in Fahrenheit erzeugen (LIST Comprehension)
print('Werte Fahrenheit')
wertefahrenheit = [wertecelsius * 1.8 +32 for wertecelsius in celsius]
print(wertefahrenheit)

# Liste Umrechnung in Fahrenheit mit Temperaturen in Celsius >= 15°C
print('Werte Fahrenheit (Celsius>=15°C)')
wertefahrenheit = [wertecelsius* 1.8 +32 for wertecelsius in celsius if wertecelsius >= 15]
print(wertefahrenheit)

