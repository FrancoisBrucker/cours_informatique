import données


def sac_a_dos_fractionnel(produits, masse_totale):
    ordre = list(range(len(produits)))
    ordre.sort(key=lambda i: -produits[i]["prix"] / produits[i]["kg"])

    sac_a_dos = [0] * len(produits)

    for i in ordre:
        x = produits[i]
        if masse_totale >= x["kg"]:
            sac_a_dos[i] = 1
            masse_totale -= x["kg"]
        elif masse_totale > 0:
            sac_a_dos[i] = masse_totale / x["kg"]
            masse_totale = 0
        else:
            break

    return sac_a_dos


def profit(sac, produits):
    return sum(fraction * produit["prix"] for fraction, produit in zip(sac, produits))


print("Données :")
for x in données.EXEMPLE:
    print(x)

print("Sac à dos fractionnel optimal :")

sac_à_dos = sac_a_dos_fractionnel(données.EXEMPLE, 20)

for i in range(len(sac_à_dos)):
    print(sac_à_dos[i], données.EXEMPLE[i]["nom"])

print("Profit :", profit(sac_à_dos, données.EXEMPLE))
