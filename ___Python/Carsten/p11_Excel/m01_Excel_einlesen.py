import pandas as pd
import xlrd
import xlsxwriter
from p01_kennenlernen import meinebibliothek


df = pd.read_excel("O:\___Python\personen.xlsx") # importieren von excel nach python mit datumsangabe in Timestamp
print(df)
print()

df1 = pd.to_datetime(df["Geburtsdatum"]) # umwandeln von Timestamp in datetime
print(df1)
print()

alter = []
for geburtstag in df1: #verwenden der bereits gebauten Altersberechnung
    alter.append(meinebibliothek.alter(geburtstag))

durchschnittsalter = sum(alter) / len(alter) # ermitteln des Durchschnittsalters
print ("Durchschnittsalter ", durchschnittsalter)
print()

df["Alter"] = alter # hinzufügen des berechneten Alters in die aus Excel eingelesene Tabelle
print(df)

writer = pd.ExcelWriter("O:\___Python\personen_bearbeitet.xlsx", engine="xlsxwriter") # erstellen eines Excel-"Writers" mit XlsxWriter

df.to_excel(writer, sheet_name='Sheet1') # konvertieren des dataframe in ein XlsxWriter Excel Objekt

writer.save() # schließen des Pandas Excel-"Writer" und exportieren des Excel-Dokuments
