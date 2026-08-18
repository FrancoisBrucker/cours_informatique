import random

class Dé:
    def __init__(self):
        self.position = 1 

    def lancer(self):
        self.position = random.randrange(1, 6 + 1)
    
    def texte(self):
        if self.position == 1:
            return "⚀"
        elif self.position == 2:
            return "⚁"
        elif self.position == 3:
            return "⚂"
        elif self.position == 4:
            return "⚃"
        elif self.position == 5:
            return "⚄"
        else:
            return "⚅"

