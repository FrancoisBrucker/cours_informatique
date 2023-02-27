class Grille:
    def __init__(self, lignes, colonnes):
        self.nombre_colones = colonnes
        self.matrice = ['∿'] * lignes * colonnes

    def tirer(self, ligne, colonne):
        if (0 <= colonne < self.nombre_colones) and (
            0 <= ligne * self.nombre_colones + colonne < len(self.matrice)
        ):
            self.matrice[ligne * self.nombre_colones + colonne] = "o"

    def __str__(self):
        colonne = 0
        grille = ""

        for case in self.matrice:
            grille += case

            colonne += 1
            if colonne == self.nombre_colones:
                grille += "\n"
                colonne = 0

        return grille[:-1]  # suppression du dernier "\n" inutile

    def ajoute(self, bateau):
        min_ligne = bateau.ligne
        min_colonne = bateau.colonne

        if bateau.vertical:
            max_ligne = min_ligne + (bateau.longueur - 1)
            max_colonne = min_colonne
        else:
            max_ligne = min_ligne
            max_colonne = min_colonne + (bateau.longueur - 1)

        nombre_lignes = len(self.matrice) / self.nombre_colones

        if (0 <= min_ligne <= max_ligne < nombre_lignes) and (
            0 <= min_colonne <= max_colonne < self.nombre_colones
        ):
            for i in range(bateau.longueur):
                if bateau.vertical:
                    ligne = min_ligne + i
                    colonne = min_colonne
                else:
                    ligne = min_ligne
                    colonne = min_colonne + i

                self.matrice[ligne * self.nombre_colones + colonne] = "⛵"
