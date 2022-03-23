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
        dist_x = min((bille.forme.x - self.forme.x) ** 2, (bille.forme.x - self.forme.x - self.forme.width) ** 2)
        dist_y = min((bille.forme.y - self.forme.y) ** 2, (bille.forme.y - self.forme.y - self.forme.height) ** 2)

        if (self.forme.x <= bille.forme.x <= self.forme.x + self.forme.width):
            return dist_y < bille.forme.radius ** 2
        elif (self.forme.y <= bille.forme.y <= self.forme.y + self.forme.height):
            return dist_x < bille.forme.radius ** 2
        else:
            return dist_x + dist_y < bille.forme.radius ** 2