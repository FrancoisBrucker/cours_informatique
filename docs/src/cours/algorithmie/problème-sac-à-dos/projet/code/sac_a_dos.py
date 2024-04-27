def glouton(aliments, masse_totale):
    aliments.sort(key=lambda x: -x["prix"] / x["kg"])
    sac_a_dos = []

    for i in range(len(aliments)):
        p, k, nom = aliments[i]

        if masse_total >= k:
            sac_a_dos.append(nom)
            masse_totale -= k

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
