def borne_inférieure(ouverte, produits, masse_totale):
    pass


def borne_supérieure(ouverte, produits, masse_totale):
    pass


def première_valeur_fractionnelle(sac_à_dos):
    for i in range(len(sac_à_dos)):
        if 0 < sac_à_dos[i] < 1:
            return i
    return None


def branch_and_bound(produits, masse_totale):
    n = len(produits)

    ouverte = [-1] * n
    borne_inf, solution_inf = borne_inférieure(ouverte, produits, masse_totale)
    possibles = []

    i = première_valeur_fractionnelle(solution_max)
    if i is not None:
        ouverte_1 = list(ouverte)
        ouverte_1[i] = 1

        ouverte_0 = list(ouverte)
        ouverte_0[i] = 0

        possibles.append(ouverte_1)
        possibles.append(ouverte_0)

    while possibles:
        ouverte = possibles.pop()

        possible_borne_max, possible_solution_max = borne_supérieure(
            ouverte, produits, masse_totale
        )
        possible_borne_inf, possible_solution_inf = borne_inférieure(
            ouverte, produits, masse_totale
        )
        if possible_borne_max > borne_inf:
            if borne_inf < possible_borne_inf:
                borne_inf, solution_inf = possible_borne_inf, possible_solution_inf

            i = première_valeur_fractionnelle(possible_solution_max)
            if i is None:
                if borne_inf < possible_borne_max:
                    borne_inf, solution_inf = possible_borne_max, possible_solution_max
            else:
                ouverte_1 = list(ouverte)
                ouverte_1[i] = 1

                ouverte_0 = list(ouverte)
                ouverte_0[i] = 0

                possibles.append(ouverte_1)
                possibles.append(ouverte_0)

    sac_à_dos = solution_inf
    return sac_à_dos
