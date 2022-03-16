import pyglet
from pyglet.window import key


class Fenetre(pyglet.window.Window):
    def __init__(self):
        super().__init__(640, 480, "Arkanoid")

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

    def on_mouse_press(self, x, y, button, modifiers):
        print("press:", x, y, button)

        if (abs(self.label.x - x) <= self.label.content_width / 2) and (
            abs(self.label.y - y) <= self.label.content_height / 2
        ):
            print("clique dans le label")

    def on_mouse_release(self, x, y, button, modifiers):
        print("release:", x, y, button)

        if (abs(self.label.x - x) <= self.label.content_width / 2) and (
            abs(self.label.y - y) <= self.label.content_height / 2
        ):
            print("relâcher le bouton dans le label")

    def on_mouse_motion(self, x, y, dx, dy):
        if (abs(self.label.x - x) <= self.label.content_width / 2) and (
            abs(self.label.y - y) <= self.label.content_height / 2
        ):
            if (abs(self.label.x - (x - dx)) > self.label.content_width / 2) or (
                abs(self.label.y - (y - dy)) > self.label.content_height / 2
            ):
                print("entre dans label")
        else:
            if (abs(self.label.x - (x - dx)) <= self.label.content_width / 2) and (
                abs(self.label.y - (y - dy)) <= self.label.content_height / 2
            ):
                print("sort du label")

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
        # print("draw:", self.get_size())
        self.clear()
        self.label.draw()


window = HelloWorldWindow()
print(window.get_size())

pyglet.app.run()
print("c'est fini !")
