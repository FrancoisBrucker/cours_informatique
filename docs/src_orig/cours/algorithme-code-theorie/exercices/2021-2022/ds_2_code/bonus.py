import random

import pyglet


class Bonus:
    DELTA = 5
    SIZE = 40

    def __init__(self):
        self.bonus = []
        self.delta = 0

    def update(self, dt, taille_x, taille_y):
        self.delta += dt

        if self.delta >= Bonus.DELTA:
            self.delta -= Bonus.DELTA
            self.bonus.append(
                pyglet.shapes.Circle(
                    random.randint(Bonus.SIZE, taille_x - Bonus.SIZE),
                    random.randint(Bonus.SIZE, taille_y - Bonus.SIZE),
                    Bonus.SIZE,
                    color=(0x00, 0xFF, 0x00),
                )
            )

    def intersection(self, rectangle):
        x = rectangle.x
        y = rectangle.y
        largeur = rectangle.width
        hauteur = rectangle.height

        for i in range(len(self.bonus)):
            x2, y2 = self.bonus[i].x, self.bonus[i].y
            r = self.bonus[i].radius

            if (
                self._dist2(x, y, x2, y2) <= r**2
                or self._dist2(x + largeur, y, x2, y2) <= r**2
                or self._dist2(x, y + hauteur, x2, y2) <= r**2
                or self._dist2(x + largeur, y + hauteur, x2, y2) <= r**2
            ):
                del self.bonus[i]
                return True

        return False

    def _dist2(self, x1, y1, x2, y2):
        return (x1 - x2) ** 2 + (y1 - y2) ** 2

    def draw(self):
        for bonus in self.bonus:
            bonus.draw()
