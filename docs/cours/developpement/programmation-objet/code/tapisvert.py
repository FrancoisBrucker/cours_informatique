from dice import Dice


class TapisVert:
    def __init__(self):
        temp = []
        for i in range(5):
            temp.append(Dice())
        self._dices = tuple(temp)

    def get_des(self):
        return self._dices

    def roll(self):
        for dice in self._dices:
            dice.roll()

    def somme(self):
        s = 0
        for d in self._dices:
            s += d.get_position()
        return s


if __name__ == "__main__":


    tv = TapisVert()

    for d in tv.get_des():
        print(d.get_position())
    print('-----')
    print(tv.somme())
    print('=====')

    tv.roll()
    for d in tv.get_des():
        print(d.get_position())
    print('-----')
    print(tv.somme())
    print('=====')
