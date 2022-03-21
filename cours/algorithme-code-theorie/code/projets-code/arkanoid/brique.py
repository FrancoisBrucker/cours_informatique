import pyglet

LONGUEUR = 40
HAUTEUR = 20


class Brique:
    def __init__(self, x, y):
        self.forme = pyglet.shapes.Rectangle(
            x,
            y,
            LONGUEUR,
            HAUTEUR,
            color=(0xFA, 0x5E, 0x4A),
        )

    def draw(self):
        self.forme.draw()

    def collision(self, bille):
        if (bille.forme.x < self.forme.x - bille.forme.radius):
            return False

        if (bille.forme.x > self.forme.x + self.forme.width + bille.forme.radius):
            return False

        if (bille.forme.y < self.forme.y - bille.forme.radius):
            return False

        if (bille.forme.y > self.forme.y + self.forme.height + bille.forme.radius):
            return False

        return True
