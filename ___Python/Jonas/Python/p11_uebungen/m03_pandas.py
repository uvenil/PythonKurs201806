import pandas
import pandas as pd

from p01_kennenlernen.meinebibliothek import alter

df = pd.read_excel ("O:\___Python\personen.xlsx")
print(df)

geburtstage = df["Geburtsdatum"]


print(geburtstage)

altersangaben = [alter(pd.to_datetime(geburtstag)) for geburtstag in geburtstage]
print(altersangaben)

