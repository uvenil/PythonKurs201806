import pandas as pd
from datetime import date, datetime, time
import xlrd
from xlrd import open_workbook, cellname, XL_CELL_TEXT, xldate_as_tuple, xldate_as_datetime

file_location = "O:\___Python\personen.xlsx"

book = open_workbook("O:\___Python\personen.xlsx")

#print(book.nsheets)

#for sheet_index in range(book.nsheets):
#   print(book.sheet_by_index(sheet_index))

sheet = book.sheet_by_index(0)
#print(book.sheet_names())
#print(sheet.ncols)
#print(sheet.nrows)

# for row_index in range(sheet.nrows):
#     for col_index in range(sheet.ncols):
#         print(sheet.cell(row_index,col_index).value)


cell = sheet.cell(0, 0)


for i in range(sheet.ncols-1):
    print(sheet.cell_value(1, i))


date_value = xldate_as_tuple(sheet.cell(1,2).value, book.datemode)

print(datetime(*date_value))