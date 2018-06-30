

import pandas as pd
import xlrd

pfad = "O:\___Python"
# df = pd.read("O:\___Python"+"\personen.xlsx")
xl = pd.ExcelFile("O:\___Python"+"\personen.xlsx")

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Tabelle1')
print(df1)
