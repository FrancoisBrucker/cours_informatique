import pyglet

LONGUEUR = 50
HAUTEUR = 20
VITESSE = 500


class Vaisseau:
    def __init__(self, sol, largeur_fenetre):
        self.vitesse = VITESSE
        self.max = largeur_fenetre

        self.forme = pyglet.shapes.Rectangle(
            (largeur_fenetre - LONGUEUR) // 2,
            sol,
            LONGUEUR,
            HAUTEUR,
            color=(0x47, 0xB6, 0xFF),
        )

    def bouge(self, dt, direction):
        if direction == 0:
            return

        new_x = self.forme.x + direction * dt * self.vitesse

        if new_x < 0:
            new_x = 0
        elif new_x + self.forme.width > self.max:
            new_x = self.max - self.forme.width

        self.forme.x = new_x

    def draw(self):
        self.forme.draw()

    def collision(self, bille):
        dist_x = min(
            (bille.forme.x - self.forme.x) ** 2,
            (bille.forme.x - self.forme.x - self.forme.width) ** 2,
        )
        dist_y = min(
            (bille.forme.y - self.forme.y) ** 2,
            (bille.forme.y - self.forme.y - self.forme.height) ** 2,
        )

        if (self.forme.x <= bille.forme.x <= self.forme.x + self.forme.width) and (
            self.forme.y <= bille.forme.y <= self.forme.y + self.forme.height
        ):
            return True
        elif self.forme.x <= bille.forme.x <= self.forme.x + self.forme.width:
            return dist_y < bille.forme.radius**2
        elif self.forme.y <= bille.forme.y <= self.forme.y + self.forme.height:
            return dist_x < bille.forme.radius**2
        else:
            return dist_x + dist_y < bille.forme.radius**2
