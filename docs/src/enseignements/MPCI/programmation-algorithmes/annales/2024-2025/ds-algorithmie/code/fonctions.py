def cases_noires(cle_l):
    total = 0
    for ligne in cle_l:
        for nombre in ligne:
            total += nombre
    return total


def cases_noires_mono_ligne(cle_l):
    return sum(sum(ligne) for ligne in cle_l)


def compatibles(cle_l, cle_c):
    return cases_noires(cle_l) == cases_noires(cle_c)


def taille_minimale(ligne):
    return sum(ligne) + len(ligne) - 1


def verif_ligne(sol, cle_l, i):
    nc = len(sol)

    i_bloc = 0
    taille = 0

    for j in range(nc):
        couleur_case = sol[i][j]
        if couleur_case == 1:
            taille = taille + 1
        if taille > 0 and (couleur_case == 0 or j + 1 == nc):
            if i_bloc < len(cle_l[i]) and taille == cle_l[i][i_bloc]:
                taille = 0
                i_bloc = i_bloc + 1
            else:
                return False
    return i_bloc == len(cle_l[i])
