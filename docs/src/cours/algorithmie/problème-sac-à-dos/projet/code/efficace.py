import données
from données import profit

def borne_supérieure(ouverte, produits, ordre, masse_totale):
    sac_a_dos = [0] * len(produits)

    for i in ordre:
        x = produits[i]

        if ouverte[i] == 1:
            sac_a_dos[i] = 1
            masse_totale -= x["kg"]

    for i in ordre:
        if ouverte[i] != -1:
            continue

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


def première_valeur_fractionnelle(sac_à_dos):
    for i in range(len(sac_à_dos)):
        if 0 < sac_à_dos[i] < 1:
            return i
    return None


def branch_and_bound(produits, masse_totale):
    ordre = list(range(len(produits)))
    ordre.sort(key=lambda i: -produits[i]["prix"] / produits[i]["kg"])

    n = len(produits)

    sac_à_dos = [0] * n
    profit_sac_à_dos = 0

    solution_ouverte = [-1] * n
    solutions_ouvertes_possibles = [solution_ouverte]

    while solutions_ouvertes_possibles:
        solution_ouverte = solutions_ouvertes_possibles.pop()

        sac_à_dos_fractionnel = borne_supérieure(solution_ouverte, produits, ordre, masse_totale)
        profit_sac_à_dos_fractionnel = profit(sac_à_dos_fractionnel, produits) 

        print(solution_ouverte, sac_à_dos_fractionnel, profit_sac_à_dos_fractionnel)

        if profit_sac_à_dos_fractionnel > profit_sac_à_dos:
            i = première_valeur_fractionnelle(sac_à_dos_fractionnel)
            if i is None:
                sac_à_dos = sac_à_dos_fractionnel
                profit_sac_à_dos = profit_sac_à_dos_fractionnel
            else:
                for v in [0, 1]:
                    nouvelle_solution_ouverte = list(solution_ouverte)
                    nouvelle_solution_ouverte[i] = v
                    if (sum(x["kg"] for x, o in zip(produits, nouvelle_solution_ouverte) if o == 1) <= masse_totale):
                        solutions_ouvertes_possibles.append(nouvelle_solution_ouverte)
    return sac_à_dos


print("Données :")
for x in données.EXEMPLE:
    print(x)

print()
print("Sac à dos optimal :")

sac_à_dos = branch_and_bound(données.EXEMPLE, 20)

for i in range(len(sac_à_dos)):
    print(sac_à_dos[i], données.EXEMPLE[i]["nom"])

print()
print("Profit :", profit(sac_à_dos, données.EXEMPLE))
