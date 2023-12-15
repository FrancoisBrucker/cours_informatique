import pyglet
from pyglet import shapes
from pyglet.window import mouse


class Formes(pyglet.window.Window):
    def __init__(self):
        super().__init__(640, 480, "formes")

        self.rectangle = shapes.Rectangle(200, 200, 200, 200, color=(0xF5, 0x83, 0x18))
        self.circle = shapes.Circle(0, 0, 50, color=(0xFF, 0, 0))
        self.circle.opacity = 128

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT and (
            (self.circle.x - x) ** 2 + (self.circle.y - y) ** 2
            <= self.circle.radius ** 2
        ):
            self.circle.x += dx
            self.circle.y += dy

    def on_draw(self):
        self.clear()

        self.rectangle.draw()
        self.circle.draw()


forme = Formes()

pyglet.app.run()
print("c'est fini !")
