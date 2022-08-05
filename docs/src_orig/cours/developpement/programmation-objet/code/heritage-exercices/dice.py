import random


class Dice:
    NUMBER_FACES = 6

    def __init__(self, position=1):
        self._position = position

    def get_position(self):
        return self._position

    def set_position(self, new_position):
        self._position = new_position

    def roll(self):
        self.set_position(random.randint(1, self.NUMBER_FACES))


class StatDice(Dice):
    def __init__(self, position=1):
        super().__init__(position)
        self._memory = [0] * (self.NUMBER_FACES + 1)

    @property
    def memory(self):
        return tuple(self._memory)

    def set_position(self, new_position):
        super().set_position(new_position)
        self._memory[new_position] += 1

    def stats(self):
        n_roll = max(1, sum(self._memory))

        return [x / n_roll for x in self._memory]

    def mean(self):
        n_roll = max(1, sum(self._memory))
        valeur = 0
        for i in range(len(self._memory)):
            valeur += i * self._memory[i]
        return valeur / n_roll


d = StatDice()

for i in range(10000):
    d.roll()

print(d.memory)
print(d.stats())
print(d.mean())
