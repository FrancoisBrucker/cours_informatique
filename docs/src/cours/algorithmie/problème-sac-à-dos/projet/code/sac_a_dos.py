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


def énumération(produits, K):
    kg = [x["kg"] for x in produits]
    prix = [x["prix"] for x in produits]
    n = len(produits)

    sac_à_dos = [0] * n

    sac_à_dos_max = list(sac_à_dos)
    sac_à_dos_profit_max = 0

    while sac_à_dos != [1] * n:
        successeur(sac_à_dos)

        if sum(x * y for x, y in zip(sac_à_dos, kg)) <= K:
            profit = sum(x * y for x, y in zip(sac_à_dos, prix))
            if profit > sac_à_dos_profit_max:
                sac_à_dos_profit_max = profit
                sac_à_dos_max = list(sac_à_dos)

    return sac_à_dos_max


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
