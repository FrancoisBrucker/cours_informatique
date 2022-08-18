
import json

f = open("ODSEN_GENERAL.json", "r")
data_brut = json.load(f)
f.close()

donnees = data_brut["results"]

for attr in donnees[0]:
    print(attr, donnees[0][attr])

actif = 0
for x in donnees:
    if x["Etat"] != "ANCIEN":
        actif += 1
print("nombre de sénateurs :", actif)