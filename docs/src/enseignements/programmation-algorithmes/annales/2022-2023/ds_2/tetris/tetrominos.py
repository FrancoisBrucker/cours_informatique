from pyglet import shapes

from grille import Grille


# class Tetromino(Grille):
#     def __init__(
#         self,
#         x,
#         y,
#         nombre_lignes,
#         nombre_colonnes,
#         cases_occupées,
#         dimension_case,
#         couleur,
#     ):
#         super().__init__(x, y, nombre_lignes, nombre_colonnes, dimension_case, couleur)
#         self.quadrillage = []

#         for i, j in cases_occupées:
#             x, y = self.lc_vers_xy(i, j)
#             self.cases[i][j] = shapes.Rectangle(
#                 x,
#                 y,
#                 dimension_case,
#                 dimension_case,
#                 couleur,
#             )


# class L(Tetromino):
#     def __init__(self, x, y, dimension_case):
#         couleur = (255, 191, 0)
#         super().__init__(
#             x, y, 3, 3, 
#             [(0, 2), (1, 0), (1, 1), (1, 2)], 
#             dimension_case, couleur
#         )


class L(Grille):
    def __init__(self, x, y, dimension_case):
        couleur = (255, 191, 0)

        super().__init__(x, y, 3, 3, dimension_case, couleur)
        self.quadrillage = []

        for i, j in [(0, 2), (1, 0), (1, 1), (1, 2)]:
            x, y = self.lc_vers_xy(i, j)
            self.cases[i][j] = shapes.Rectangle(
                x,
                y,
                dimension_case,
                dimension_case,
                couleur,
            )


class J(Grille):
    def __init__(self, x, y, dimension_case):
        couleur = (100, 149, 237)

        super().__init__(x, y, 3, 3, dimension_case, couleur)
        self.quadrillage = []

        for i, j in [(0, 0), (1, 0), (1, 1), (1, 2)]:
            x, y = self.lc_vers_xy(i, j)
            self.cases[i][j] = shapes.Rectangle(
                x,
                y,
                dimension_case,
                dimension_case,
                couleur,
            )


class T(Grille):
    def __init__(self, x, y, dimension_case):
        couleur = (153, 50, 204)

        super().__init__(x, y, 3, 3, dimension_case, couleur)
        self.quadrillage = []

        for i, j in [(0, 1), (1, 0), (1, 1), (1, 2)]:
            x, y = self.lc_vers_xy(i, j)
            self.cases[i][j] = shapes.Rectangle(
                x,
                y,
                dimension_case,
                dimension_case,
                couleur,
            )


class I(Grille):
    def __init__(self, x, y, dimension_case):
        couleur = (64, 224, 208)

        super().__init__(x, y, 4, 4, dimension_case, couleur)
        self.quadrillage = []

        for i, j in [(1, 0), (1, 1), (1, 2), (1, 3)]:
            x, y = self.lc_vers_xy(i, j)
            self.cases[i][j] = shapes.Rectangle(
                x,
                y,
                dimension_case,
                dimension_case,
                couleur,
            )


class O(Grille):
    def __init__(self, x, y, dimension_case):
        couleur = (223, 255, 0)

        super().__init__(x, y, 4, 4, dimension_case, couleur)
        self.quadrillage = []

        for i, j in [(1, 1), (1, 2), (2, 1), (2, 2)]:
            x, y = self.lc_vers_xy(i, j)
            self.cases[i][j] = shapes.Rectangle(
                x,
                y,
                dimension_case,
                dimension_case,
                couleur,
            )


class Z(Grille):
    def __init__(self, x, y, dimension_case):
        couleur = (222, 49, 99)

        super().__init__(x, y, 3, 3, dimension_case, couleur)
        self.quadrillage = []

        for i, j in [(0, 0), (0, 1), (1, 1), (1, 2)]:
            x, y = self.lc_vers_xy(i, j)
            self.cases[i][j] = shapes.Rectangle(
                x,
                y,
                dimension_case,
                dimension_case,
                couleur,
            )


class S(Grille):
    def __init__(self, x, y, dimension_case):
        couleur = (60, 179, 113)

        super().__init__(x, y, 3, 3, dimension_case, couleur)
        self.quadrillage = []

        for i, j in [(0, 1), (0, 2), (1, 0), (1, 1)]:
            x, y = self.lc_vers_xy(i, j)
            self.cases[i][j] = shapes.Rectangle(
                x,
                y,
                dimension_case,
                dimension_case,
                couleur,
            )


TETROMINOS = [L, J, T, I, O, Z, S]
