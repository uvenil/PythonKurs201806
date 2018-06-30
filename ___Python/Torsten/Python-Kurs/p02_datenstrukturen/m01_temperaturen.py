from p01_kennenlernen import PythonLib

temperaturenGC = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] #Durchschnittstemp. in Bielefeld
print("Temperaturen in °C:", temperaturenGC)

durchschnittstemperaturGC = sum(temperaturenGC) / len(temperaturenGC)
print("Durchschnittstemperatur in °C:", durchschnittstemperaturGC)

print()

# 1) Neue Liste mit °F-Temperaturen erzeugen
# A - FOR-Schleife
temperaturenGF = []
for temperatur in temperaturenGC:
    temperaturenGF.append(temperatur * 1.8 + 32)

print("Temperaturen in °F:", temperaturenGF)
durchschnittstemperaturGF = sum(temperaturenGF) / len(temperaturenGF)
print("Durchschnittstemperatur in °F:", durchschnittstemperaturGF)


# B - List Comprehension
temperaturenGF = [temperatur * 1.8 + 32 for temperatur in temperaturenGC]
print("Temperaturen in °F:", temperaturenGF)


# 2) Neue Liste Fahrenheit mit > 15°C(!)
# A - FOR-Schleife
temperaturenGF = []
for temperatur in temperaturenGC:
    if temperatur >= 15:
        temperaturenGF.append(PythonLib.celsius_nach_fahrenheit(temperatur))

print("Temperaturen in °F:", temperaturenGF)

# B - List Comprehension
temperaturenGF = [temperatur * 1.8 + 32 for temperatur in temperaturenGC if temperatur >= 15]
print("Temperaturen in °F:", temperaturenGF)
