from fractran import Fractran, Fraction, Facteur

facteurs = Facteur([2, 3, 5])

print("Somme :")
somme = [Fraction(3, 2)]
for i in range(10):
    for j in range(10):
        retour = Fractran(somme).run(facteurs.nombre([i, j]))  # on exécute un programme Fractran avec les nombres de la forme 2^i * 3 ^j
        décomposition = facteurs.décomposition(retour)         # on ne garde du retour du programme Fractran que la puissance de sa décomposition en nombre premiers pour 2, 3 et 5
        print(i, "+", j, "=", décomposition[1], "(retour =", retour, "; décomposition =", décomposition, ")")

        #  pour le programme :
        #  Si    entrée = 2^i * 3^j 
        #  alors sortie = 3^{i+j}


print("Produit :")
produit = [
    Fraction(455, 33),
    Fraction(11, 13),
    Fraction(1, 11),
    Fraction(3, 7),
    Fraction(11, 2),
    Fraction(1, 3),
]
for i in range(10):
    for j in range(10):
        retour = Fractran(produit).run(facteurs.nombre([i, j])) # on exécute un programme Fractran avec les nombres de la forme 2^i * 3 ^j
        décomposition = facteurs.décomposition(retour)
        print(i, "*", j, "=", décomposition[2], "(retour =", retour, "décomposition =", décomposition, ")")

        #  pour le programme :
        #  Si    entrée = 2^i * 3^j 
        #  alors sortie = 5^{i*j}
