def enfant_gauche(x):
    return x[1]


def change_enfant_gauche(x, nouveau):
    x[1] = nouveau


def enfant_droit(x):
    return x[2]


def change_enfant_droit(x, nouveau):
    x[2] = nouveau


def valeur(x):
    return x[0]


def change_valeur(x, nouveau):
    x[0] = nouveau


def hauteur(noeud):
    if noeud is None:
        return 0
    return max(hauteur(enfant_gauche(noeud)), hauteur(enfant_droit(noeud))) + 1


def nombre(noeud):
    if noeud is None:
        return 0
    return nombre(enfant_gauche(noeud)) + nombre(enfant_droit(noeud)) + 1

racine_1 = [42, [12, [6, None, None], [5, None, None]], [3, [1, None, None], None]]
racine_2 = [42, [12, [3, None, None], [1, None, None]], [6, [5, None, None], None]]

print("hauteur : ", hauteur(racine_1), " - nombre : ", nombre(racine_1))
