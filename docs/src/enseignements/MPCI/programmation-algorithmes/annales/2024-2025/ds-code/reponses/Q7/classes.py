import random


class Plateau:
    def __init__(self):
        self.piste = Piste()
        self.piste.melange()
        self.podium = Podium()
        self.pions = {"R": -1, "V": -1, "B": -1, "J": -1, "U": -1}

    def __str__(self):
        s = str(self.piste)
        s += " "
        s += str(self.podium)

        return s

    def deplace(self, couleur):
        if self.pions[couleur] is not None:  # pas encore le podium
            if self.pions[couleur] > -1:
                self.piste.jetons[self.pions[couleur]].pion = False

            self.pions[couleur] = self.piste.suivant(couleur, self.pions[couleur])

            if self.pions[couleur] is None:  # va sur le podium
                self.podium.ajoute(couleur)
            else:  # ajoute le pion sur le jeton
                self.piste.jetons[self.pions[couleur]].pion = True


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

    def suivant(self, couleur, position_initiale):
        for i in range(position_initiale + 1, len(self.jetons)):
            if self.jetons[i].couleur == couleur:
                return i
        return None

    def gauche_droite(self, position):
        g = position - 1
        d = position + 1
        while (g >= 0) and self.jetons[g].pion:
            g -= 1
        while (d < len(self.jetons)) and self.jetons[d].pion:
            d += 1

        if g < 0:
            g = None
        if d >= len(self.jetons):
            d = None

        return (g, d)

    def __str__(self):
        return "".join(str(x) for x in self.jetons)


class Podium:
    def __init__(self):
        self.places = [None, None, None, None, None]

    def ajoute(self, couleur):
        for i in range(len(self.places) - 1, -1, -1):
            if self.places[i] is None:
                self.places[i] = couleur
                return

    def __str__(self):
        s = "[sky_blue1]"
        for i in range(len(self.places)):
            if self.places[i] is None:
                s += str(i)
            elif self.places[i] == "R":
                s += "[red]R[/red]"
            elif self.places[i] == "V":
                s += "[green]V[/green]"
            elif self.places[i] == "B":
                s += "[blue]B[/blue]"
            elif self.places[i] == "J":
                s += "[yellow]J[/yellow]"
            elif self.places[i] == "U":
                s += "[violet]U[/violet]"
        s += "[/sky_blue1]"

        return s


class Jeton:
    def __init__(self, couleur):
        self.couleur = couleur
        self.pion = False

    def __str__(self):
        if self.couleur == "R":
            if self.pion:
                return "[red u]r[/red u]"
            else:
                return "[red]R[/red]"
        elif self.couleur == "V":
            if self.pion:
                return "[green u]v[/green u]"
            else:
                return "[green]V[/green]"
        elif self.couleur == "B":
            if self.pion:
                return "[blue u]b[/blue u]"
            else:
                return "[blue]B[/blue]"
        elif self.couleur == "J":
            if self.pion:
                return "[yellow u]j[/yellow u]"
            else:
                return "[yellow]J[/yellow]"
        elif self.couleur == "U":
            if self.pion:
                return "[violet u]u[/violet u]"
            else:
                return "[violet]U[/violet]"
        elif self.couleur == "X":
            return "[grey93]X[/grey93]"
        elif self.couleur == "O":
            return "[grey23]O[/grey23]"

        else:
            return " "


class Joueur:
    def __init__(self):
        self.jetons = {"R": 0, "V": 0, "B": 0, "J": 0, "U": 0, "X": 0, "O": 0}

    def points(self, podium):
        pts = 0
        for i in range(len(podium.places)):
            if podium.places[i] is not None:
                pts += i * self.jetons[podium.places[i]]
        pts += self.jetons["B"] * sum(
            [1 for x, y in self.jetons.items() if y > 0 and x != "B"]
        )
        return pts

    def __str__(self):
        return str(self.jetons)
