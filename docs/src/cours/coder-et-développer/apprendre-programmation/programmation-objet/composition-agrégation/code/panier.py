class Panier:
    def __init__(self):
        self.stock = tuple()

    def ajoute(self, fruit):
        self.stock = self.stock + (fruit,)

    def montre_panier(self):
        return self.stock

    def supprime(self, fruit):
        stock_temporaire = list(self.stock)
        stock_temporaire.remove(fruit)
        self.stock = tuple(stock_temporaire)

class Item:
    def __init__(self, nom, prix):
        self._nom = nom
        self._prix = prix


    def __eq__(self, other):
        return self._nom == other._nom and self._prix == other._prix

    def __repr__(self):
        return f"Item({self._nom}, {self._prix})"

    def __str__(self):
        return f"Un item de nom {self._nom} valant {self._prix} euros."
