class Panier:
    def __init__(self):
        self.stock = tuple()

    def ajoute(self, fruit):
        temp = list(self.stock)
        temp.append(fruit)

        self.stock = tuple(temp)

    def montre_panier(self):
        return self.stock

    def supprime(self, fruit):
        temp = list(self.stock)
        temp.remove(fruit)

        self.stock = tuple(temp)        


# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/

if __name__ == "__main__":
    panier = Panier()

    print(panier.montre_panier())

    panier.ajoute("pomme")

    print(panier.montre_panier())

    panier.ajoute("pomme")
    panier.ajoute("poire")

    print(panier.montre_panier())

    panier.supprime("pomme")
    print(panier.montre_panier())
