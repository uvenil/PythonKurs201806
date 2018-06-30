from mmap import mmap,ACCESS_READ
from xlrd import open_workbook

excel_wb = open_workbook('O:/___Python/personen.xlsx')
excel_sheet = excel_wb.sheet_by_index(0)


list_excel = []
for i in range(1,3):
    list_excel.append(excel_sheet.cell(i,0))
    print(list_excel)





# with open('simple.xls','rb') as f:
# print open_workbook(
# file_contents=mmap(f.fileno(),0,access=ACCESS_READ)
# )
# aString = open('simple.xls','rb').read()
# print open_workbook(file_contents=aString