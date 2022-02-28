import random


class Dice:
    def __init__(self, position=1):
        self._position = position

    def get_position(self):
        return self._position

    def set_position(self, nouvelle_position):
        self._position = nouvelle_position

    def roll(self):
        self._position = random.randint(1, 6)

        return self

    def __str__(self):
        return str(self.get_position())


class TapisVert:
    def __init__(self):
        temp = []
        for i in range(5):
            temp.append(Dice())

        self._dices = tuple(temp)

    def get_des(self):
        return self._dices

    def roll(self):
        for dice in self.get_des():
            dice.roll()

    def _positions(self):
        count = [0] * 7
        for dice in self.dices:
            count[dice.get_position()] += 1
        return count

    def _nb_des_identiques(self, nb_times):
        count = self._positions()

        for i in range(len(count)):
            if count[i] >= nb_times:
                return True
        return False

    def a_une_pair(self):
        return self._nb_des_identiques(2)

    def a_un_brelan(self):
        return self._nb_des_identiques(3)

    def a_un_carre(self):
        return self._nb_des_identiques(4)
    
    def a_une_double_paire(self):
        count = self._positions()
        nb_2 = 0
        for x in count:
            if x > 1:
                nb_2 += 1
        return nb_2 > 1
    
    def a_un_full(self):
        count = self._positions()
        nb_2 = 0
        nb_3 = 0
        for x in count:
            if x == 2:
                nb_2 += 1
            elif x == 3:
                nb_3 += 1
        return (nb_2 > 0) and (nb_3 > 0)
