class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=True):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def touché(self, ligne, colonne):
        if self.vertical:
            if self.colonne == colonne and (
                self.ligne <= ligne <= self.ligne + self.longueur - 1
            ):
                return True
            else:
                return False
        else:
            if self.ligne == ligne and (
                self.colonne <= colonne <= self.colonne + self.longueur - 1
            ):
                return True
            else:
                return False

    def coulé(self, grille):
        min_ligne = self.ligne
        min_colonne = self.colonne

        if self.vertical:
            max_ligne = min_ligne + (self.longueur - 1)
            max_colonne = min_colonne
        else:
            max_ligne = min_ligne
            max_colonne = min_colonne + (self.longueur - 1)

        if not ((0 < min_ligne <= max_ligne <= len(grille.matrice)) and (
            0 < min_colonne <= max_colonne <= len(grille.matrice[0])
        )):
            return False
        
        for i in range(self.longueur):
            if self.vertical:
                ligne = min_ligne - 1 + i
                colonne = min_colonne - 1
            else:
                ligne = min_ligne - 1
                colonne = min_colonne - 1 + i

            if grille.matrice[ligne][colonne] != "o":
                return False

        return True
