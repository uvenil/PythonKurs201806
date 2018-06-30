import statistics

from xlrd import open_workbook, xldate_as_datetime

from p01_kennenlernen.m01_kennenlernen import geburtsdatum
from p01_kennenlernen.meinebibliothek import alter

book = open_workbook("O:\___Python\personen.xlsx")

sheet = book.sheet_by_index(0)
print(sheet)

nrows = sheet.nrows
ncols = sheet.ncols

for i in range (1, nrows):
    row_slice = sheet.row_slice(i, 0, ncols)
    for cell in row_slice:
        print(cell.value, end=" ")

print()

birthdates = [xldate_as_datetime(sheet.row_slice(i, 0, ncols)[2].value, False) for i in range(1, nrows)]
print(birthdates)

altersangaben = [alter(geburtsdatum) for geburtstag in birthdates]
print(altersangaben)

print(statistics.mean(altersangaben))
