import random


class Plateau:
    def __init__(self):
        self.piste = Piste()
        self.piste.melange()
        self.podium = Podium()

    def __str__(self):
        s = str(self.piste)
        s += " "
        s += str(self.podium)

        return s


class Piste:
    def __init__(self):
        self.jetons = []
        for couleur in ("R", "V", "B", "J", "U"):
            for i in range(9):
                self.jetons.append(Jeton(couleur))
        for couleur in ("X", "O"):
            for i in range(5):
                self.jetons.append(Jeton(couleur))

    def melange(self):
        random.shuffle(self.jetons)

    def __str__(self):
        return "".join(str(x) for x in self.jetons)


class Podium:
    def __str__(self):
        return "01234"


class Jeton:
    def __init__(self, couleur):
        self.couleur = couleur

    def __str__(self):
        return self.couleur
