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

        sac_à_dos_fractionnel = borne_supérieure(
            solution_ouverte, produits, ordre, masse_totale
        )
        profit_sac_à_dos_fractionnel = profit(sac_à_dos_fractionnel, produits)

        if profit_sac_à_dos_fractionnel > profit_sac_à_dos:
            i = première_valeur_fractionnelle(sac_à_dos_fractionnel)
            if i is None:
                sac_à_dos = sac_à_dos_fractionnel
                profit_sac_à_dos = profit_sac_à_dos_fractionnel
            else:
                for v in [0, 1]:
                    nouvelle_solution_ouverte = list(solution_ouverte)
                    nouvelle_solution_ouverte[i] = v
                    if (
                        sum(
                            x["kg"]
                            for x, o in zip(produits, nouvelle_solution_ouverte)
                            if o == 1
                        )
                        <= masse_totale
                    ):
                        solutions_ouvertes_possibles.append(nouvelle_solution_ouverte)
    return sac_à_dos


def programmation_dynamique(produits, masse_totale):
    M = []
    S = []

    M.append([None] * (masse_totale+1))
    S.append([None] * (masse_totale+1))

    for j in range(masse_totale + 1):
        if produits[0]["kg"] > j:
            M[-1][j] = 0
            S[-1][j] = [0] * len(produits)
        else:
            M[-1][j] = produits[0]["prix"]
            S[-1][j] = [1] + [0] * (len(produits)-1)

    M.append([0] * (masse_totale+1))
    S.append([None] * (masse_totale+1))
    S[1][0] = [0] * len(produits)

    for i in range(1, len(produits)):
        print(S[0])
        for j in range(1, masse_totale + 1):
            if produits[i]["kg"] > j:
                M[-1][j] = M[-2][j]
                S[-1][j] = list(S[-2][j])
            elif M[-2][j] < M[-2][j - produits[i]["kg"]] + produits[i]["prix"]:
                M[-1][j] = M[-2][j - produits[i]["kg"]] + produits[i]["prix"]
                S[-1][j] = list((S[-2][j - produits[i]["kg"]]))
                S[-1][j][i] = 1
            else:
                M[-1][j] =M[-2][j]
                S[-1][j] =list(S[-2][j])
        M[0], M[1] = M[1], [0] * (masse_totale+1)
        S[0], S[1] = S[1], [None] * (masse_totale+1)
        S[1][0] = [0] * len(produits)

    return S[0][-1]


print("Données :")
for x in données.EXEMPLE:
    print(x)

print()
print("Sac à dos optimal (branch and bound) :")

sac_à_dos = branch_and_bound(données.EXEMPLE, 20)

for i in range(len(sac_à_dos)):
    print(sac_à_dos[i], données.EXEMPLE[i]["nom"])

print()
print("Profit :", profit(sac_à_dos, données.EXEMPLE))

print()
print("Sac à dos optimal (programmation dynamique) :")

sac_à_dos = programmation_dynamique(données.EXEMPLE, 20)

for i in range(len(sac_à_dos)):
    print(sac_à_dos[i], données.EXEMPLE[i]["nom"])

print()
print("Profit :", profit(sac_à_dos, données.EXEMPLE))
