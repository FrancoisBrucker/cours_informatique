import données
from données import profit


def glouton(aliments, masse_totale):
    ordre = list(range(len(aliments)))
    ordre.sort(key=lambda i: -aliments[i]["prix"] / aliments[i]["kg"])

    sac_a_dos = [0] * len(aliments)

    for i in ordre:
        x = aliments[i]
        if masse_totale >= x["kg"]:
            sac_a_dos[i] = 1
            masse_totale -= x["kg"]

    return sac_a_dos

print("Données :")
for x in données.EXEMPLE:
    print(x)

print()
print("Sac à dos fractionnel optimal :")

sac_à_dos = glouton(données.EXEMPLE, 20)

for i in range(len(sac_à_dos)):
    print(sac_à_dos[i], données.EXEMPLE[i]["nom"])

print()
print("Profit :", profit(sac_à_dos, données.EXEMPLE))
