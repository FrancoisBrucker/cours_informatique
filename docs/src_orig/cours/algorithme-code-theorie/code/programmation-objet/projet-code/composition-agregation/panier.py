class Panier:
    def __init__(self):
        self.stock = []

    def ajoute(self, fruit):
        self.stock.append(fruit)

    def montre_panier(self):
        return tuple(self.stock)

    def supprime(self, fruit):
        self.stock.remove(fruit)
