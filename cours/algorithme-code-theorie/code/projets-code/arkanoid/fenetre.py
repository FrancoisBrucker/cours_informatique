import pyglet
from pyglet.window import key

from vaisseau import Vaisseau


class Fenetre(pyglet.window.Window):
    def __init__(self):
        super().__init__(640, 480, "Arkanoid")

        self.score = pyglet.text.Label(
            "0000",
            x=630,
            y=470,
            anchor_x="right",
            anchor_y="top",
        )

        self.vie = pyglet.text.Label(
            "2",
            x=10,
            y=10,
            anchor_x="left",
            anchor_y="bottom",
        )

        self.sol = pyglet.shapes.Line(0, 50, 640, 50, color=(0xFF, 0xFF, 0xFF))

        self.vaisseau = Vaisseau(50, 640)

        self.direction = 0  # -1 (gauche) ; 0 (immobile) ; 1 (droite)
        pyglet.clock.schedule_interval(self.update, 1 / 60)

    def update(self, dt):
        self.vaisseau.bouge(dt, self.direction)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.direction += -1
        elif symbol == key.RIGHT:
            self.direction += 1

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.direction -= -1
        elif symbol == key.RIGHT:
            self.direction -= 1

    def on_draw(self):
        self.clear()
        self.score.draw()
        self.vie.draw()
        self.sol.draw()

        self.vaisseau.draw()
