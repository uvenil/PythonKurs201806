import pandas as pd
import xlsxwriter as ew
from datetime import date

torsten = ["Torsten", "Aachen"]
michael = ["Michael", "Moormerland"]
karpoo = ["Karpoo", "Düsseldorf"]
carsten = ["Carsten", "Aachen"]
thomas = ["Thomas", "Bielefeld"]
angela = ["Angela", "Lingen"]
jonas = ["Jonas", "Löhne"]
marco = ["Marco", "Bielefeld"]
roman = ["Roman", "Hannover"]
daniel = ["Daniel", "Bielefeld"]

teilnehmerliste =[torsten, michael, karpoo, carsten, thomas, angela, jonas, marco, roman, daniel] # Zuweisung

# Create a Pandas dataframe from the data.
#df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
teilnehmerexcel = []
for teilnehmer in teilnehmerliste: # Schleife, lies: "für jeden teilnehmer in der liste teilnehmerliste wiederhole:"
    teilnehmerexcel.append(teilnehmer)


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('teilnehmerliste.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
teilnehmerexcel.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()