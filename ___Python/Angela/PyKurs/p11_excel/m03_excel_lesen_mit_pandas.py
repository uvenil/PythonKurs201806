from datetime import date
import pandas as pd

def alter(datumsangbe):
    heute = date.today()
    jahre = heute.year - datumsangbe.year
    if (datumsangbe.month, datumsangbe.day) > (heute.month, heute.day):
        jahre -= 1
    return jahre

df = pd.read_excel("O:\___Python\Angela\Personen.xlsx")     # data frame
print("Spaltennamen:")
print(df)
datumslist = []
alterslist = []
for i in df.index:
    vorname = df['Vorname']
    ort = df['Ort']
    datum= df['Geburtsdatum']
    print(vorname[i], ort[i], datum[i]) # TODO: Nur Datum
    daten = datumslist.append(datum[i])
    alters = alterslist.append(alter(datum[i]))

# print(datumslist)
# print(alterslist)
print(" ")
print("Durchschnittsalter:")
print(sum(alterslist) / len(alterslist))