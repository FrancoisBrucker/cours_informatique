import random

import pyglet
from pyglet.window import key, mouse

from grille import Grille


class DeuxMilleQuaranteHuit(pyglet.window.Window):
    def __init__(self):
        super().__init__(800, 800, "2048")

        self.grille = Grille(800)

    def on_draw(self):
        self.grille.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.DOWN:
            di, dj = (-1, 0)
            lignes = [0, 1, 2, 3]
            colonnes = [0, 1, 2, 3]
        elif symbol == key.UP:
            di, dj = (1, 0)
            lignes = [3, 2, 1, 0]
            colonnes = [0, 1, 2, 3]
        elif symbol == key.LEFT:
            di, dj = (0, -1)
            lignes = [0, 1, 2, 3]
            colonnes = [0, 1, 2, 3]
        elif symbol == key.RIGHT:
            di, dj = (0, 1)
            lignes = [0, 1, 2, 3]
            colonnes = [3, 2, 1, 0]
        else:
            return

        a_bougé = False

        for i in range(4):
            for j in range(4):
                self.grille.cases[i][j].neuf = False

        for _ in range(3):
            for i in lignes:
                for j in colonnes:
                    if self.grille.cases[i][j].valeur == 1:
                        continue

                    if (not (0 <= i + di < 4)) or (not (0 <= j + dj < 4)):
                        continue

                    if self.grille.cases[i + di][j + dj].valeur == 1:
                        self.grille.cases[i + di][j + dj].mise_à_jour(
                            self.grille.cases[i][j].valeur
                        )
                        self.grille.cases[i][j].mise_à_jour(1)
                        self.grille.cases[i][j].neuf = False
                        self.grille.cases[i + di][j + dj].neuf = False
                        a_bougé = True
                    elif (
                        (self.grille.cases[i + di][j + dj].valeur
                        == self.grille.cases[i][j].valeur)
                        and (not self.grille.cases[i + di][j + dj].neuf)
                        and (not self.grille.cases[i][j].neuf)
                    ):
                        self.grille.cases[i + di][j + dj].incrémente()
                        self.grille.cases[i + di][j + dj].neuf = True
                        self.grille.cases[i][j].mise_à_jour(1)

                        self.grille.cases[i][j].neuf = False
                        a_bougé = True

        cases_libres = []
        for i in lignes:
            for j in colonnes:
                if self.grille.cases[i][j].valeur == 1:
                    cases_libres.append(self.grille.cases[i][j])

        if a_bougé and len(cases_libres):
            case = random.choice(cases_libres)
            case.incrémente()

            if random.random() > 0.8:
                case.incrémente()

    def on_mouse_press(self, x, y, button, modifiers):
        case = self.grille.intérieur(x, y)
        if case is None:
            return
        i, j = case

        if button & mouse.LEFT:
            self.grille.cases[i][j].incrémente()
        elif button & mouse.RIGHT:
            self.grille.cases[i][j].décrémente()


window = DeuxMilleQuaranteHuit()
print(window.get_size())

pyglet.app.run()
print("c'est fini !")
