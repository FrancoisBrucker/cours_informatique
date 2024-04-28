import données
from données import profit


def glouton(produits, masse_totale):
    ordre = list(range(len(produits)))
    ordre.sort(key=lambda i: -produits[i]["prix"] / produits[i]["kg"])

    sac_a_dos = [0] * len(produits)

    for i in ordre:
        x = produits[i]
        if masse_totale >= x["kg"]:
            sac_a_dos[i] = 1
            masse_totale -= x["kg"]

    return sac_a_dos


def successeur(n):
    i = len(n) - 1

    while (i >= 0) and (n[i] == 1):
        n[i] = 0
        i -= 1

    if i >= 0:
        n[i] = 1


def énumération(produits, masse_totale):
    n = len(produits)
    kg = [x["kg"] for x in produits]
    prix = [x["prix"] for x in produits]

    affectation = [0] * n

    affectation_max = list(affectation)
    objectif_max = 0

    while affectation != [1] * n:
        successeur(affectation)

        if sum(x * y for x, y in zip(affectation, kg)) <= masse_totale:
            objectif_courant = sum(x * y for x, y in zip(affectation, prix))
            if objectif_courant > objectif_max:
                objectif_max = objectif_courant
                affectation_max = list(affectation)
    return affectation_max


print("Données :")
for x in données.EXEMPLE:
    print(x)

print()
print("Sac à dos glouton :")

sac_à_dos = glouton(données.EXEMPLE, 20)

for i in range(len(sac_à_dos)):
    print(sac_à_dos[i], données.EXEMPLE[i]["nom"])

print()
print("Profit :", profit(sac_à_dos, données.EXEMPLE))

print()
print("Sac à dos optimal par énumération :")

sac_à_dos = énumération(données.EXEMPLE, 20)

for i in range(len(sac_à_dos)):
    print(sac_à_dos[i], données.EXEMPLE[i]["nom"])

print()
print("Profit :", profit(sac_à_dos, données.EXEMPLE))
