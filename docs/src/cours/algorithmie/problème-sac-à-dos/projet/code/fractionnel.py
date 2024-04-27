import données


def sac_a_dos_fractionnel(produits, masse_totale):
    produits.sort(key=lambda x: -x["prix_kg"])

    sac_a_dos = []
    for x in produits:
        if masse_totale >= x["kg"]:
            sac_a_dos.append((x, 1))
            masse_totale -= x["kg"]
        elif masse_totale > 0:
            sac_a_dos.append((x, masse_totale / x["kg"]))
            masse_totale = 0
        else:
            break

    return sac_a_dos


def profit(sac):
    return sum(données.prix(produit) * fraction for produit, fraction in sac)


print("Données :")
for x in données.EXEMPLE:
    print(x)

print("Sac à dos fractionnel optimal :")

sac_à_dos = sac_a_dos_fractionnel(données.EXEMPLE, 20)

for x in sac_à_dos:
    print(x)

print("Profit :", profit(sac_à_dos))
