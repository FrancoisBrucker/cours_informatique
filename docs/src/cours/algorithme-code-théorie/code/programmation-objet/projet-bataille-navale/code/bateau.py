class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    @property
    def positions(self):
        pos = []
        for i in range(self.longueur):
            if self.vertical:
                v, h = i, 0
            else:
                v, h = 0, i
            pos.append((self.ligne + v, self.colonne + h))

        return pos

    def coulé(self, grille):
        min_ligne = self.ligne
        min_colonne = self.colonne

        if self.vertical:
            max_ligne = min_ligne + (self.longueur - 1)
            max_colonne = min_colonne
        else:
            max_ligne = min_ligne
            max_colonne = min_colonne + (self.longueur - 1)

        nombre_lignes = len(grille.matrice) / grille.nombre_colones

        if (0 <= min_ligne <= max_ligne < nombre_lignes) and (
            0 <= min_colonne <= max_colonne < grille.nombre_colones
        ):
            for i in range(self.longueur):
                if self.vertical:
                    ligne = min_ligne + i
                    colonne = min_colonne
                else:
                    ligne = min_ligne
                    colonne = min_colonne + i

                if grille.matrice[ligne * grille.nombre_colones + colonne] != "o":
                    return False

            return True
        return False
