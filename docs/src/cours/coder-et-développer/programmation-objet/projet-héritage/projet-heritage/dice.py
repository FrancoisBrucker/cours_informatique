import random


class Dice:
    NOMBRE_FACES = 6

    def __init__(self, position=1):
        self.position = position

    def lancer(self):
        self.position = random.randint(1, self.NOMBRE_FACES)


class StatDice(Dice):
    def __init__(self, position=1):
        super().__init__(position)
        self.historique = []

    def lancer(self):
        self.position = random.randint(1, self.NOMBRE_FACES)
        super().lancer()
        self.historique.append(self.position)

    def moyenne(self):
        return sum(self.historique) / max(1, len(self.historique))


dice = StatDice()

for i in range(1000):
    dice.lancer()

print('1000 lancers :', dice.moyenne())
