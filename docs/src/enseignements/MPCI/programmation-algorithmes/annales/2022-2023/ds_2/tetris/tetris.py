import random

import pyglet
from pyglet.window import key
from pyglet import shapes

from grille import Grille
import utils
from tetrominos import TETROMINOS

WINDOW_LARGEUR = 800
WINDOW_HAUTEUR = 600

DIMENSION_CASE = 25
NOMBRE_LIGNES = 20
NOMBRE_COLONNES = 10
GRILLE_X = (WINDOW_LARGEUR - NOMBRE_COLONNES * DIMENSION_CASE) // 2
GRILLE_Y = (WINDOW_HAUTEUR - NOMBRE_LIGNES * DIMENSION_CASE) // 2

FPS = 60
GRAVITÉ = 1
SOFT_DROP = 20
LOCK_DELAY = 1 / 2


class Tetris(pyglet.window.Window):
    def __init__(self):
        super().__init__(WINDOW_LARGEUR, WINDOW_HAUTEUR, "Tetris")

        self.grille = Grille(
            GRILLE_X,
            GRILLE_Y,
            NOMBRE_LIGNES,
            NOMBRE_COLONNES,
            DIMENSION_CASE,
            (127, 0, 234),
        )
        # x, y = self.grille.lc_vers_xy(10, 0)
        # self.grille.cases[10][0] = shapes.Rectangle(
        #     x,
        #     y,
        #     DIMENSION_CASE,
        #     DIMENSION_CASE,
        #     (127, 0, 234),
        # )
        # x, y = self.grille.lc_vers_xy(10, 9)
        # self.grille.cases[10][9] = shapes.Rectangle(
        #     x,
        #     y,
        #     DIMENSION_CASE,
        #     DIMENSION_CASE,
        #     (127, 0, 234),
        # )
        # x, y = self.grille.lc_vers_xy(19, 5)
        # self.grille.cases[19][5] = shapes.Rectangle(
        #     x,
        #     y,
        #     DIMENSION_CASE,
        #     DIMENSION_CASE,
        #     (127, 0, 234),
        # )

        self.nouveau_tetromino()  # crée self.tetromino
        self.vitesse = GRAVITÉ

        pyglet.clock.schedule_interval(self.update, 1 / FPS)
        self.accumulateur = 0

    def on_draw(self):
        self.clear()
        self.grille.draw()
        self.tetromino.draw()

    def update(self, dt):
        self.accumulateur += dt

        if not self.déplacement_bas():
            if self.accumulateur >= LOCK_DELAY:
                self.accumulateur = 0

                for i in range(self.tetromino.nombre_lignes):
                    for j in range(self.tetromino.nombre_colonnes):
                        if self.tetromino.cases[i][j] != None:
                            l, c = self.tetromino_vers_grille(i, j)
                            self.grille.cases[l][c] = self.tetromino.cases[i][j]

                self.grille.supprime_ligne()
                self.nouveau_tetromino()
        else:
            if self.accumulateur * self.vitesse >= 1:
                self.tetromino.déplace(1, 0)
                self.accumulateur = 0

    def on_key_press(self, symbol, modifiers):
        i, j = self.grille.xy_vers_lc(self.tetromino.x, self.tetromino.y)
        if symbol == key.SPACE:
            if self.déplacement_bas():
                while self.déplacement_bas():
                    self.tetromino.déplace(1, 0)
                self.accumulateur = 0
        elif symbol == key.LEFT:
            if self.déplacement_gauche():
                self.tetromino.déplace(0, -1)
                self.accumulateur = 0
        elif symbol == key.RIGHT:
            if self.déplacement_droite():
                self.tetromino.déplace(0, 1)
                self.accumulateur = 0
        elif symbol == key.DOWN:
            self.vitesse = SOFT_DROP
        elif symbol == key.UP:
            if self.rotation():
                self.tetromino.rotation()
                self.accumulateur = 0

    def on_key_release(self, symbol, modifiers):
        if symbol == key.DOWN:
            self.vitesse = GRAVITÉ

    def nouveau_tetromino(self):
        x, y = self.grille.lc_vers_xy(2, 3)

        self.tetromino = TETROMINOS[random.randrange(len(TETROMINOS))](x, y, self.grille.dimension_case)
        if self.tetromino.nombre_colonnes == 4:
            self.tetromino.déplace(0, 1)
        # self.tetromino = Grille(
        #     x,
        #     y,
        #     3,
        #     3,
        #     self.grille.dimension_case,
        #     (255, 255, 255),
        # )
        # x, y = self.tetromino.lc_vers_xy(0, 1)
        # self.tetromino.cases[0][1] = shapes.Rectangle(
        #     x,
        #     y,
        #     self.grille.dimension_case,
        #     self.grille.dimension_case,
        #     (255, 255, 255),
        # )
        # x, y = self.tetromino.lc_vers_xy(1, 1)
        # self.tetromino.cases[1][1] = shapes.Rectangle(
        #     x,
        #     y,
        #     self.grille.dimension_case,
        #     self.grille.dimension_case,
        #     (255, 255, 255),
        # )
        # self.tetromino.quadrillage = []

    def tetromino_vers_grille(self, i, j):
        x, y = self.tetromino.lc_vers_xy(i, j)
        l, c = self.grille.xy_vers_lc(x, y)

        return l, c
    
    def déplacement_bas(self):
        for j in range(self.tetromino.nombre_colonnes):
            i = self.tetromino.nombre_lignes - 1
            while i >= 0:
                if self.tetromino.cases[i][j] != None:
                    l, c = self.tetromino_vers_grille(i, j)

                    if (
                        l >= self.grille.nombre_lignes - 1
                        or self.grille.cases[l + 1][c] != None
                    ):
                        return False

                    i = -1
                else:
                    i -= 1
        return True

    def déplacement_gauche(self):
        for i in range(self.tetromino.nombre_lignes):
            j = 0
            while j < self.tetromino.nombre_colonnes:
                if self.tetromino.cases[i][j] != None:
                    l, c = self.tetromino_vers_grille(i, j)

                    if c <= 0 or self.grille.cases[l][c - 1] != None:
                        return False

                    j = self.tetromino.nombre_colonnes
                else:
                    j += 1
        return True

    def déplacement_droite(self):
        for i in range(self.tetromino.nombre_lignes):
            j = self.tetromino.nombre_colonnes - 1
            while j >= 0:
                if self.tetromino.cases[i][j] != None:
                    l, c = self.tetromino_vers_grille(i, j)

                    if (
                        c >= self.grille.nombre_colonnes - 1
                        or self.grille.cases[l][c + 1] != None
                    ):
                        return False

                    j = -1
                else:
                    j -= 1
        return True

    def rotation(self):
        rotation_test = utils.rotation(self.tetromino.cases)
        for i in range(self.tetromino.nombre_lignes):
            for j in range(self.tetromino.nombre_colonnes):
                l, c = self.tetromino_vers_grille(i, j)

                if rotation_test[i][j] != None and self.grille.cases[l][c] != None:
                    return False
        return True
