from arbre_binaire import hauteur, nombre


racine_1 = [42, [12, [6, None, None], [5, None, None]], [3, [1, None, None], None]]
racine_2 = [42, [12, [3, None, None], [1, None, None]], [6, [5, None, None], None]]

print("hauteur : ", hauteur(racine_1), " - nombre : ", nombre(racine_1))
