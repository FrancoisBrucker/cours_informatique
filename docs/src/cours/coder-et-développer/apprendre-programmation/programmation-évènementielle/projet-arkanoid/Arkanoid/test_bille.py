from bille import Bille


def test_position_initiale():
    bille = Bille(50, 480 - 50, 640)

    assert bille.forme.x == 640 // 2
    assert bille.forme.y == (480 - 50 + 50) // 2


def test_bouge():
    bille = Bille(50, 480 - 50, 640)
    bille.vitesse = (2, 5)

    bille.bouge(2)

    assert bille.forme.x == 640 // 2 + 2 * 2
    assert bille.forme.y == (480 - 50 + 50) // 2 + 2 * 5


def test_bouge_retour_haut():

    bille = Bille(50, 480 - 50, 640)
    bille.vitesse = (0, -5)
    bille.forme.y = 51

    bille.bouge(1)

    assert bille.forme.x == 640 // 2
    assert bille.forme.y == (480 - 50 + 50) // 2


def test_rebondit_x_droite():
    bille = Bille(50, 480 - 50, 640)
    bille.vitesse = (75, 25)
    bille.forme.x = 641

    bille.bouge(1)

    assert bille.forme.x == 640
    assert bille.vitesse == (-75, 25)


def test_rebondit_x_gauche():
    bille = Bille(50, 480 - 50, 640)
    bille.vitesse = (-75, 25)
    bille.forme.x = -1

    bille.bouge(1)

    assert bille.forme.x == 0
    assert bille.vitesse == (75, 25)


def test_rebondit_y_haut():
    bille = Bille(50, 480 - 50, 640)
    bille.vitesse = (75, 25)
    bille.forme.y = 480 - 50 + 1

    bille.bouge(1)

    assert bille.forme.y == 480 - 50
    assert bille.vitesse == (75, -25)
