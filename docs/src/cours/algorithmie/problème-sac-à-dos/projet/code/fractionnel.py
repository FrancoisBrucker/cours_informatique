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


print("Données :")
for x in données.EXEMPLE:
    print(x)

print("Sac à dos fractionnel optimal :")
profit = 0

for x in sac_a_dos_fractionnel(données.EXEMPLE, 20):
    print(x)
    profit += données.prix(x[0]) * x[1]
print("Profit :", profit)
