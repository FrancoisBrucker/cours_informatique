import pyglet


class Snake:
    SIZE = 20

    def __init__(self):
        self.snake = []

        for i in range(10):
            self.snake.append(
                pyglet.shapes.Rectangle(
                    (16) * Snake.SIZE,
                    (12 - i) * Snake.SIZE,
                    Snake.SIZE,
                    Snake.SIZE,
                    color=(0xFF, 0xFF, 0xFF),
                )
            )

        self.augmente_taille = 0

    def position(self):
        return self.snake[0].x, self.snake[0].y

    def deplace(self, direction):
        x = self.snake[0].x + Snake.SIZE * direction[0]
        y = self.snake[0].y + Snake.SIZE * direction[1]

        if self.augmente_taille > 0:
            self.augmente_taille -= 1
            self.snake.insert(
                0,
                pyglet.shapes.Rectangle(
                    x, y, Snake.SIZE, Snake.SIZE, color=(0xFF, 0xFF, 0xFF)
                ),
            )
        else:
            for cell in self.snake:
                cell.x, x = x, cell.x
                cell.y, y = y, cell.y

    def recouvre(self):
        for i in range(1, len(self.snake)):
            if (self.snake[0].x == self.snake[i].x) and (
                self.snake[0].y == self.snake[i].y
            ):
                return True
        return False

    def draw(self):
        for cell in self.snake:
            cell.draw()
