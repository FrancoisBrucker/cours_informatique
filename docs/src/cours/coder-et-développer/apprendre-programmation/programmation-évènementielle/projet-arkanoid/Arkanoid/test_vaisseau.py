from vaisseau import Vaisseau, LONGUEUR
from bille import Bille


def test_position_initiale():
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


def test_collision_trop_gauche():
    vaisseau = Vaisseau(50, 480)
    bille = Bille(50, 480 - 50, 640)

    bille.forme.y = vaisseau.forme.y + vaisseau.forme.height // 2
    bille.forme.x = vaisseau.forme.x - 2 * bille.forme.radius

    assert not vaisseau.collision(bille)


def test_collision_trop_droite():
    vaisseau = Vaisseau(50, 480)
    bille = Bille(50, 480 - 50, 640)

    bille.forme.y = vaisseau.forme.y + vaisseau.forme.height // 2
    bille.forme.x = vaisseau.forme.x + vaisseau.forme.width + 2 * bille.forme.radius

    assert not vaisseau.collision(bille)


def test_collision_trop_haut():
    vaisseau = Vaisseau(50, 480)
    bille = Bille(50, 480 - 50, 640)

    bille.forme.y = vaisseau.forme.y + vaisseau.forme.height + 2 * bille.forme.radius
    bille.forme.x = vaisseau.forme.x + vaisseau.forme.width // 2

    assert not vaisseau.collision(bille)


def test_collision():
    vaisseau = Vaisseau(50, 480)
    bille = Bille(50, 480 - 50, 640)

    bille.forme.y = vaisseau.forme.y + vaisseau.forme.height // 2
    bille.forme.x = vaisseau.forme.x + vaisseau.forme.width // 2

    assert vaisseau.collision(bille)
