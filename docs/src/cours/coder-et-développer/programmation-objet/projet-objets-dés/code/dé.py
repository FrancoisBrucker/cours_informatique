import random

class Dé:
    def __init__(self):
        self.position = 1 

    def lancer(self):
        self.position = random.randrange(1, 6 + 1)

