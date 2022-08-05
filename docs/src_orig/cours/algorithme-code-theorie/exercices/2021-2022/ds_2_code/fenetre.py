import pyglet
from pyglet.window import key

from snake import Snake
from bonus import Bonus

W_X = 640
W_Y = 480

GAUCHE = (-1, 0)
HAUT = (0, 1)
DROITE = (1, 0)
BAS = (0, -1)
STOP = (0, 0)

DELTA_SCORE = 1


class Fenetre(pyglet.window.Window):
    def __init__(self):
        super().__init__(W_X, W_Y, "Snake")

        self.score = pyglet.text.Label(
            "0",
            x=W_X,
            y=W_Y,
            anchor_x="right",
            anchor_y="top",
        )
        self.chrono = 0

        self.snake = Snake()

        self.bonus = Bonus()

        self.mort = False
        self.direction = STOP
        self.direction_stockee = HAUT
        pyglet.clock.schedule_interval(self.update, 1 / 10)

    def update(self, dt):
        if self.direction == STOP:
            return

        self.snake.deplace(self.direction)
        self._check_mort()

        if self.mort:
            return

        self._check_sur_un_bonus()

        self._score_update(dt)
        self.bonus.update(dt, W_X, W_Y)

    def _check_mort(self):
        x, y = self.snake.position()

        if x < 0:
            self.mort = True
            self.direction = STOP
        elif x + Snake.SIZE > W_X:
            self.mort = True
            self.direction = STOP

        if y < 0:
            self.mort = True
            self.direction = STOP
        elif y + Snake.SIZE > W_Y:
            self.mort = True
            self.direction = STOP

        if self.snake.recouvre():
            self.mort = True
            self.direction = STOP

    def _check_sur_un_bonus(self):
        if self.bonus.intersection(self.snake.snake[0]):
            self.score.text = str(int(self.score.text) + 5)
            self.snake.augmente_taille += 5

    def _score_update(self, dt):
        self.chrono += dt

        if self.chrono >= DELTA_SCORE:
            self.chrono -= DELTA_SCORE
            self.score.text = str(int(self.score.text) + 1)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            if self.direction == STOP:
                self.direction = self.direction_stockee
            else:
                self.direction_stockee = self.direction
                self.direction = STOP

        if self.direction == STOP:
            return

        if symbol == key.UP and self.direction != BAS:
            self.direction = HAUT
        elif symbol == key.RIGHT and self.direction != GAUCHE:
            self.direction = DROITE
        elif symbol == key.LEFT and self.direction != DROITE:
            self.direction = GAUCHE
        elif symbol == key.DOWN and self.direction != HAUT:
            self.direction = BAS

    def on_key_release(self, symbol, modifiers):
        pass

    def on_draw(self):
        self.clear()

        self.score.draw()
        self.snake.draw()
        self.bonus.draw()
