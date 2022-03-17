from vaisseau import Vaisseau, LONGUEUR


def test_initial_position():
    vaisseau = Vaisseau(50, 480)

    assert vaisseau.forme.x == (480 - LONGUEUR) // 2
    assert vaisseau.forme.y == 50


def test_bouge_droite():
    vaisseau = Vaisseau(50, 480)
    vaisseau.forme.x = 0

    vaisseau.vitesse = 10

    vaisseau.bouge(2, +1)

    assert vaisseau.forme.x == 20


def test_bouge_gauche():
    vaisseau = Vaisseau(50, 480)
    vaisseau.forme.x = 100

    vaisseau.vitesse = 10

    vaisseau.bouge(2, -1)

    assert vaisseau.forme.x == 80


def test_bouge_negatif():
    vaisseau = Vaisseau(50, 480)
    vaisseau.forme.x = 1
    vaisseau.vitesse = 10

    vaisseau.bouge(1, -1)

    assert vaisseau.forme.x == 0


def test_bouge_depasse_taille():
    vaisseau = Vaisseau(50, 480)
    vaisseau.forme.x = 479 - LONGUEUR
    vaisseau.vitesse = 10

    vaisseau.bouge(1, +1)

    assert vaisseau.forme.x == 480 - LONGUEUR
