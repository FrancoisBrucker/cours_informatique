import random

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
        return "[sky_blue1]01234[/sky_blue1]"


class Jeton:
    def __init__(self, couleur):
        self.couleur = couleur

    def __str__(self):
        if self.couleur == "R":
            return "[red]R[/red]"
        elif self.couleur == "V":
            return "[green]V[/green]"
        elif self.couleur == "B":
            return "[blue]B[/blue]"
        elif self.couleur == "J":
            return "[yellow]J[/yellow]"
        elif self.couleur == "U":
            return "[violet]U[/violet]"
        elif self.couleur == "X":
            return "[grey93]X[/grey93]"
        elif self.couleur == "O":
            return "[grey23]O[/grey23]"

        else:
            return " "
