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
        if (bille.forme.x < self.forme.x - bille.forme.radius):
            return False

        if (bille.forme.x > self.forme.x + self.forme.width + bille.forme.radius):
            return False

        if (bille.forme.y > self.forme.y + self.forme.height + bille.forme.radius):
            return False

        return True
