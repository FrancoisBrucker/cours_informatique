def xy_vers_lc(x, y, origine_grille_x, origine_grille_y, dimension_case, nombre_lignes_grille):
    ligne = nombre_lignes_grille - 1 - (y - origine_grille_y) // dimension_case
    colonne = (x - origine_grille_x) // dimension_case

    return (ligne, colonne)


def lc_vers_xy(ligne, colonne, origine_grille_x, origine_grille_y, dimension_case, nombre_lignes_grille):
    x = origine_grille_x + dimension_case * colonne
    y = origine_grille_y + dimension_case * (nombre_lignes_grille - 1 - ligne)

    return (x, y)


def rotation(matrice):
    nombre_lignes = len(matrice)
    nombre_colonnes = len(matrice[0])

    matrice_rotation = []
    for i in range(nombre_lignes):
        ligne = []
        for j in range(nombre_colonnes):
            ligne.append(None)
        matrice_rotation.append(ligne)

    for i in range(nombre_lignes):
        for j in range(nombre_colonnes):
            matrice_rotation[j][nombre_colonnes - 1 - i] = matrice[i][j]

    return matrice_rotation
