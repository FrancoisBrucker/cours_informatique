import math


class Fraction:
    def __init__(self, dénominateur, numérateur):
        self.dénominateur = dénominateur
        self.numérateur = numérateur

    def __str__(self):
        return str(self.dénominateur) + "/" + str(self.numérateur)

    def réduit(self):
        q = math.gcd(self.dénominateur, self.numérateur)
        return Fraction(self.dénominateur / q, self.numérateur / q)

    def __eq__(self, other):
        x = self.réduit()
        y = other.réduit()

        return (x.dénominateur == y.dénominateur) and (x.numérateur == y.numérateur)


def test_str():
    assert str(Fraction(3, 4)) == "3/4"
