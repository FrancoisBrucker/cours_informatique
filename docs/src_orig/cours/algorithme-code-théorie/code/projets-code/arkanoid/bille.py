import pyglet

RAYON = 5


class Bille:
    def __init__(self, hauteur_sol, hauteur_plafond, largeur_fenetre):
        self.vitesse = (0, 0)

        self.min_y = hauteur_sol
        self.max_y = hauteur_plafond
        self.min_x = 0
        self.max_x = largeur_fenetre

        self.forme = pyglet.shapes.Circle(
            x=(self.max_x + self.min_x) // 2,
            y=(self.max_y + self.min_y) // 2,
            radius=RAYON,
            color=(0xB3, 0xCE, 0xDC),
        )

    def bouge(self, dt):
        x = self.forme.x + dt * self.vitesse[0]
        y = self.forme.y + dt * self.vitesse[1]

        if y < self.min_y:
            x = (self.max_x + self.min_x) // 2
            y = (self.max_y + self.min_y) // 2
            self.vitesse = (0, 0)
        elif y > self.max_y:
            y = self.max_y
            self.vitesse = (self.vitesse[0], -self.vitesse[1])

        if x < self.min_x:
            x = self.min_x
            self.vitesse = (-self.vitesse[0], self.vitesse[1])
        elif x > self.max_x:
            x = self.max_x
            self.vitesse = (-self.vitesse[0], self.vitesse[1])

        self.forme.x = x
        self.forme.y = y

    def draw(self):
        self.forme.draw()
