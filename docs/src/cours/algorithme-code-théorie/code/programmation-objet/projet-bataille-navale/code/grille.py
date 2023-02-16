class Grille:
    def __init__(self, lignes, colonnes):
        self.matrice = []

        for l in range(lignes):
            self.matrice.append([])
            for c in range(colonnes):
                self.matrice[-1].append(".")

    def tirer(self, l, c):
        if (c < 1) or (c > len(self.matrice[0])) or (l < 1) or (l > len(self.matrice)):
            return
        self.matrice[l - 1][c - 1] = "o"

    def ajoute(self, bateau):
        min_ligne = bateau.ligne
        min_colonne = bateau.colonne

        if bateau.vertical:
            max_ligne = min_ligne + (bateau.longueur - 1)
            max_colonne = min_colonne
        else:
            max_ligne = min_ligne
            max_colonne = min_colonne + (bateau.longueur - 1)

        if (0 < min_ligne <= max_ligne <= len(self.matrice)) and (
            0 < min_colonne <= max_colonne <= len(self.matrice[0])
        ):
            for i in range(bateau.longueur):
                if bateau.vertical:
                    ligne = min_ligne - 1 + i
                    colonne = min_colonne - 1
                else:
                    ligne = min_ligne - 1
                    colonne = min_colonne - 1 + i

                self.matrice[ligne][colonne] = "X"
