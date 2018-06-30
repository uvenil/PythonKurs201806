# Wörterbuch (Dictionary, Hashtabelle, Hashtable, Hashmap, associative Array)
dic_wbde = {"Tisch": "table",
         "Stuhl": "chair",
         "Schreibtisch": "desk"}
print(dic_wbde)
print("")
# 1. Ansatz
dic_wbed = {}
for wort in dic_wbde:
    dic_wbed[(dic_wbde[wort])] = wort
print(dic_wbed)
print("")

# 2. Ansatz
dic_wbed = [(wort[1],wort[0]) for wort in dic_wbde.items()]
print(dict(dic_wbed))