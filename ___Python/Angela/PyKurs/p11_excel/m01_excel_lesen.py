from datetime import datetime, date
import xlrd
from xlrd import xldate_as_tuple


def open_file(path):
    book = xlrd.open_workbook(path)
    print(book.nsheets)
    print(book.sheet_names())
    sheet = book.sheet_by_index(0)
    for i in range(sheet.nrows):
        values = []
        for k in range(sheet.ncols):
            values.append(sheet.cell(i, k).value)
        print(values)
    date_tupel = xlrd.xldate_as_datetime(1, 0)  # datemode – 0: 1900-based, 1: 1904-based
    print(date_tupel)




    # date_value = xldate_as_tuple(sheet.cell(i, k).value, book.datemode)
    # print(date(*date_value[:3]))




print(open_file("O:\___Python\Angela\Personen.xlsx"))