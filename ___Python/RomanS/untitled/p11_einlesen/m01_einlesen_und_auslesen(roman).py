# Datei einlesen und ausgeben der Werte

import xlrd
import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd

from xlrd import open_workbook,xldate_as_tuple
import xlrd


DATA_FILE = "O:/___Python/personen.xlsx"

# Read Excel data
def read_excel_file(filename):
    book = xlrd.open_workbook(filename, encoding_override = "utf-8")
    sheet = book.sheet_by_index(0)
    x_data = [sheet.cell(i, 0).value for i in range(1, sheet.ncols+1)]
    y_data = [sheet.cell(i, 1).value for i in range(1, sheet.ncols+1)]
#    z_data = [sheet.cell(i, 2).value for i in range(1, sheet.ncols+1)]
    z_data = [xldate_as_tuple(sheet.cell(i, 2).value, book.datemode) for i in range(1, sheet.ncols+1)]  #"%10s"



   # year, month, day = xlrd.xldate_as_tuple(ms_date_number, book.datemode)
   # py_date = datetime.datetime(year, month, day)



#    if z_data.ctype ==3:
#        ms_date_number = z_data
   # z_data = xldate_as_tuple(z_data, book.datemode)
    #format = z_data.format("dd.mm.yyyy")
    #z_date.write('A2', z_data, format)

    #return x_data, y_data, z_date
    return x_data, y_data, z_data

x_data, y_data, z_data = read_excel_file(DATA_FILE)
print(x_data,y_data,z_data)