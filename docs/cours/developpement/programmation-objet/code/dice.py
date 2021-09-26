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


if __name__ == "__main__":
    # d = Dice()
    # print(d.get_position())

    # d2 = Dice(4)
    # print(d2.get_position())

    # d.set_position(6)
    # print(d.get_position())

    # d2.roll()
    # print(d2.get_position())

    tapis = []
    for i in range(5):
        tapis.append(Dice())

    print("======")
    for d in tapis:
        print(d.get_position())

    for d in tapis:
        d.roll()

    print("======")
    for d in tapis:
        print(d.get_position())
