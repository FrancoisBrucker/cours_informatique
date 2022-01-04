
def puissance_naif(nombre, exposant):
    résultat = 1
    compteur = exposant
    while compteur > 0:
        résultat *= nombre
        compteur -= 1
    return résultat


def puissance_rapide(nombre, exposant):
    resultat = 1
    compteur = exposant

    while compteur > 0:
        if compteur % 2 != 0:
            resultat *= nombre
            compteur -= 1
        else:
            nombre *= nombre
            compteur /= 2

    return resultat
