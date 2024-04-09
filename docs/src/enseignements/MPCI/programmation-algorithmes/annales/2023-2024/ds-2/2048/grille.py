import pyglet


class Grille:
    def __init__(self, taille):
        self.fond = Carré(0, 0, taille)
        self.cases = []

        bord = (taille // 100) * 4
        taille_carré = (taille - 5 * bord) // 4

        for ligne in range(4):
            self.cases.append([])
            for colonne in range(4):
                self.cases[ligne].append(
                    vide(
                        bord + (bord + taille_carré) * colonne,
                        bord + (bord + taille_carré) * ligne,
                        taille_carré,
                    )
                )

    def intérieur(self, x, y):
        for i in range(4):
            for j in range(4):
                if self.cases[i][j].intérieur(x, y):
                    return (i, j)

    def draw(self):
        self.fond.draw()
        for ligne in self.cases:
            for case in ligne:
                case.draw()


class Carré:
    def __init__(self, x, y, taille):
        self.rectangle = pyglet.shapes.Rectangle(
            x,
            y,
            taille,
            taille,
            (185, 173, 161),
        )

    def draw(self):
        self.rectangle.draw()

    def intérieur(self, x, y):
        if (self.rectangle.x <= x <= self.rectangle.x + self.rectangle.width) and (
            self.rectangle.y <= y <= self.rectangle.y + self.rectangle.height
        ):
            return True
        return False


def vide(x, y, taille):
    return Case(1, x, y, taille)


class Case(Carré):
    def __init__(self, valeur, x, y, taille):
        super().__init__(x, y, taille)
        self.valeur = valeur
        self.neuf = False

        self.label = pyglet.text.Label(
            str(valeur),
            font_size=40,
            color=(0, 0, 0, 255),
            x=x + taille // 2,
            y=y + taille // 2,
            anchor_x="center",
            anchor_y="center",
        )
        self.mise_à_jour(valeur)

    def mise_à_jour(self, valeur):
        self.valeur = valeur
        self.label.text = str(valeur)

        if valeur == 1:
            self.rectangle.color = (202, 193, 181, 255)
        elif valeur == 2:
            self.rectangle.color = (238, 228, 218, 255)
        elif valeur == 4:
            self.rectangle.color = (237, 224, 200, 255)
        elif valeur == 8:
            self.rectangle.color = (242, 177, 121, 255)
        elif valeur == 16:
            self.rectangle.color = (245, 149, 99, 255)
        elif valeur == 32:
            self.rectangle.color = (246, 124, 95, 255)
        elif valeur == 64:
            self.rectangle.color = (246, 94, 59, 255)
        elif valeur == 128:
            self.rectangle.color = (237, 207, 114, 255)
        elif valeur == 256:
            self.rectangle.color = (237, 204, 97, 255)
        elif valeur == 512:
            self.rectangle.color = (237, 200, 80, 255)
        elif valeur == 1024:
            self.rectangle.color = (237, 197, 63, 255)
        elif valeur == 2048:
            self.rectangle.color = (237, 194, 46, 255)

    def incrémente(self):
        if self.valeur < 2048:
            self.mise_à_jour(self.valeur * 2)
            self.neuf = True

    def décrémente(self):
        if self.valeur > 1:
            self.mise_à_jour(self.valeur // 2)

    def fini(self):
        pass
        # aucune case de libre
        # chaque voisin a une valeur differente

    def draw(self):
        super().draw()
        if self.valeur > 1:
            self.label.draw()
