def donne_prochain_indice(chaine, indice):
    possible_suivant = chaine.find(chaine[indice], indice + 1)

    if possible_suivant > -1:
        return possible_suivant
    return None


def compte_caractère(chaine, indice):
    compte = 0

    while indice != None:
        compte += 1
        indice = donne_prochain_indice(chaine, indice)

    return compte


def donne_max_doublon(chaine):
    nombre_max = 0

    for i in range(len(chaine)):
        nombre_max = max(nombre_max, compte_caractère(chaine, i))

    return nombre_max
