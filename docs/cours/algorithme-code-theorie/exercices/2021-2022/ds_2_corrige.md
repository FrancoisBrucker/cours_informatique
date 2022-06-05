---
layout: page
title:  "corrigé DS 2 : projet de code"
category: cours
tags: code python
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [exercices]({% link cours/algorithme-code-theorie/exercices/index.md %}) / [2021-2022]({% link cours/algorithme-code-theorie/exercices/2021-2022/index.md %}) / [corrige DS 2 : projet de code]({% link cours/algorithme-code-theorie/exercices/2021-2022/ds_2_corrige.md %})
{: .chemin}


Un corrigé possible, sans tests, de la partie obligatoire du DS.

```python
import random

import pyglet
from pyglet.window import key

W_X = 640
W_Y = 480

GAUCHE = (-1, 0)
HAUT = (0, 1)
DROITE = (1, 0)
BAS = (0, -1)
STOP = (0, 0)

DELTA_SCORE = 1


class Snake:
    SIZE = 20
    
    def __init__(self):
        self.snake = []

        for i in range(10):
            self.snake.append(
                pyglet.shapes.Rectangle(
                    (16) * Snake.SIZE, (12 - i) * Snake.SIZE, Snake.SIZE, Snake.SIZE, color=(0xFF, 0xFF, 0xFF)
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
                0, pyglet.shapes.Rectangle(x, y, Snake.SIZE, Snake.SIZE, color=(0xFF, 0xFF, 0xFF))
            )
        else:
            for cell in self.snake:
                cell.x, x = x, cell.x
                cell.y, y = y, cell.y

    def recouvre(self):
        for i in range(1, len(self.snake)):
            if (self.snake[0].x == self.snake[i].x) and (self.snake[0].y == self.snake[i].y):
                return True
        return False
    
    def draw(self):
        for cell in self.snake:
            cell.draw()


class Bonus:
    DELTA = 5
    SIZE = 40
    
    def __init__(self):
        self.bonus = []
        self.delta = 0
    
    
    def update(self, dt, taille_x, taille_y):
        self.delta += dt

        if self.delta >= Bonus.DELTA:
            self.delta -= Bonus.DELTA
            self.bonus.append(
                pyglet.shapes.Circle(
                    random.randint(Bonus.SIZE, taille_x - Bonus.SIZE),
                    random.randint(Bonus.SIZE, taille_y - Bonus.SIZE),
                    Bonus.SIZE,
                    color=(0x00, 0xFF, 0x00),
                )
            )
    
    def intersection(self, rectangle):
        x = rectangle.x
        y = rectangle.y
        largeur = rectangle.width
        hauteur = rectangle.height

        for i in range(len(self.bonus)):
            x2, y2 = self.bonus[i].x, self.bonus[i].y
            r = self.bonus[i].radius

            if (
                self._dist2(x, y, x2, y2) <= r**2
                or self._dist2(x + largeur, y, x2, y2) <= r**2
                or self._dist2(x, y + hauteur, x2, y2) <= r**2
                or self._dist2(x + largeur, y + hauteur, x2, y2) <= r**2
            ):
                del self.bonus[i]
                return True

        return False

    def _dist2(self, x1, y1, x2, y2):
        return (x1 - x2) ** 2 + (y1 - y2) ** 2
    
    
    def draw(self):
        for bonus in self.bonus:
            bonus.draw()
        
        
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

if __name__ == "__main__":
    window = Fenetre()

    pyglet.app.run()
    print("c'est fini !")

```