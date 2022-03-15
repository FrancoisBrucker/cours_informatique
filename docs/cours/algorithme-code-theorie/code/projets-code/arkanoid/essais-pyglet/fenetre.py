from turtle import update
import pyglet
from pyglet.window import key


class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super(HelloWorldWindow, self).__init__(400, 200, "texte", resizable=True)

        self.label = pyglet.text.Label(
            "Hello, world!",
            x=self.width // 2,
            y=self.height // 2,
            anchor_x="center",
            anchor_y="center",
        )
        self.dx = 0
        self.dy = 0

        pyglet.clock.schedule_interval(self.update, 0.5)

    def update(self, dt):
        if self.dx != 0 or self.dy != 0:
            self.label = pyglet.text.Label(
                "Hello, world!",
                x=max(min(self.label.x + self.dx, self.width), 0),
                y=max(min(self.label.y + self.dy, self.height), 0),
                anchor_x="center",
                anchor_y="center",
            )

    def on_resize(self, width, height):
        super().on_resize(width, height)

        self.label = pyglet.text.Label(
            "Hello, world!",
            x=width // 2,
            y=height // 2,
            anchor_x="center",
            anchor_y="center",
        )

    def on_key_press(self, symbol, modifiers):
        delta = 10
        if symbol == key.UP:
            self.dy = delta
        elif symbol == key.DOWN:
            self.dy = -delta
        elif symbol == key.LEFT:
            self.dx = -delta
        elif symbol == key.RIGHT:
            self.dx = +delta

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.dy = 0
        elif symbol == key.DOWN:
            self.dy = 0
        elif symbol == key.LEFT:
            self.dx = 0
        elif symbol == key.RIGHT:
            self.dx = 0

    def on_draw(self):
        print("draw:", self.get_size())
        self.clear()
        self.label.draw()


window = HelloWorldWindow()
print(window.get_size())

pyglet.app.run()
print("c'est fini !")
