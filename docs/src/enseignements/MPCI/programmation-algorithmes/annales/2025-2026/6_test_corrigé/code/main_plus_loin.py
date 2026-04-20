from fractran import Fractran, Fraction, Facteur

#  Les deux programmes fonctionnent de la même manière : on ne garde de la sortie que des entiers satisfaisant une 
#  condition.
#  Cette condition s'exprime de la forme :
#  - `n == Facteur([2, 3]).nombre(Facteur([2, 3]).décomposition(n))` pour Fibonacci
#  - `n == Facteur([2]).nombre(Facteur([2]).décomposition(n))` pour les nombres premiers
#
#  Elle exprime le fait que la sortie n est égale à une décomposition de la forme :
#
# - n = 2^i*3^j pour Fibonacci
# - n = 2^i pour les nombres premiers



print("Fibonacci rend les couples (F(n), F(n+1)) :")
fibonacci = [
    Fraction(23, 95),
    Fraction(57, 23),
    Fraction(17, 39),
    Fraction(130, 17),
    Fraction(11, 14),
    Fraction(35, 11),
    Fraction(19, 13),
    Fraction(1, 19),
    Fraction(35, 2),
    Fraction(13, 7),
    Fraction(7, 1),
]

sortie_brute = Fractran(fibonacci).suite(3, 1000)
sortie = []
for n in sortie_brute:
    if n == Facteur([2, 3]).nombre(Facteur([2, 3]).décomposition(n)):
        sortie.append(Facteur([2, 3]).décomposition(n))

print(sortie)

print("Nombres premiers :")
crible = [
    Fraction(17, 91),
    Fraction(78, 85),
    Fraction(19, 51),
    Fraction(23, 38),
    Fraction(29, 33),
    Fraction(77, 29),
    Fraction(95, 23),
    Fraction(77, 19),
    Fraction(1, 17),
    Fraction(11, 13),
    Fraction(13, 11),
    Fraction(15, 14),
    Fraction(15, 2),
    Fraction(55, 1),
]

sortie_brute = Fractran(crible).suite(3, 100000)
sortie = []
for n in sortie_brute:
    if n == Facteur([2]).nombre(Facteur([2]).décomposition(n)):
        sortie.append(Facteur([2]).décomposition(n)[0])

print(sortie)
