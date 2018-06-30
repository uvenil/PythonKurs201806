import pandas as pd
#import xlrd
#'from p01_kennenlernen import my_pycurse_utilities
from p01_kennenlernen.my_pycurse_utilities import alter

excel_file = "O:/___python/thomas/personen_t.xlsx"
personen = pd.read_excel(excel_file)

excel_dict_liste = {}
excel_namen = []

excel_df = pd.read_excel(excel_file)
excel_df['Geburtsdatum'] = pd.to_datetime(excel_df['Geburtsdatum']).apply(lambda x: x.date())
excel_dict_imp = excel_df.to_dict()

excel_first_col = True
for values1 in excel_dict_imp.values():
    i_val1 = 0
    for values2 in values1.values():
        if excel_first_col:
            excel_dict_liste[values2] = []
            excel_namen.append(values2)
        else:
            excel_dict_liste[excel_namen[i_val1]].append(values2)
            i_val1 += 1
    excel_first_col = False

for namen in excel_dict_liste:
    datum = excel_dict_liste[namen]
    print(str(namen)+' '+str(excel_dict_liste[namen])+' '+str(alter(datum[1])))


