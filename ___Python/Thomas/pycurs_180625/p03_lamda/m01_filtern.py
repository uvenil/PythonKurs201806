temp_celsius = [0.7, 2.1, 4.2, 8.2, 12.5, 15.6, 16.9, 16.3, 13.6, 9.5, 4.6, 2.3] #Durschnittstemperaturen Bielefeld

# Alle Temperaturen >= 15
list_tc1 = []
list_tc1 = [temp1 for temp1 in temp_celsius]
print(list_tc1)