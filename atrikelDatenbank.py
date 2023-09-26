# import artikel

# print(artikel.artikel1)

# artikel.artikel1["artikelNummer"] =54
# print(artikel.artikel1)

import os
import json

#print(os.listdir("./artikel"))
# ui = input("Was möchtest du sehen? (1) zeige alle Artikel")

def loadDict(filename):
    with open(filename+".json","r",encoding="utf-8") as f:
        loadedDict = json.load(f)
    return loadedDict

# if ui.startswith("1"):
fileNameList = os.listdir("./artikel")
artikelListe = []
for item in fileNameList:
    nameOhneEnde = "./artikel/"+item.removesuffix(".json")
    temp = loadDict(nameOhneEnde)
    artikelListe.append(temp)
    # print(temp)


kunden  = []
# if ui.startswith("1"):
fileNameList = os.listdir("./kunden")
for item in fileNameList:
    nameOhneEnde = "./kunden/"+item.removesuffix(".json")
    kunden.append(loadDict(nameOhneEnde))

einkauf = []

fileNameList = os.listdir("./einkauf")
for item in fileNameList:
    nameOhneEnde = "./einkauf/"+item.removesuffix(".json")
    einkauf.append(loadDict(nameOhneEnde))

filteredList = []
"""
identifier nummer
kundennummer
in allen Einkäufe suche nach kunde
"""

kunde = "24788"
for item in einkauf:
    if item["kunde"] == kunde:
        print(item)
        item["objekte"] = []
        for artikel in item["artikel"]:
            for a2 in artikelListe:
                #print(artikel,a2)
                if str(artikel) == str(a2["artikelNummer"]):
                    print(a2['artikelBezeichnung'])
                    item["objekte"].append(a2)
                    break
        filteredList.append(item)
print(filteredList[0])
