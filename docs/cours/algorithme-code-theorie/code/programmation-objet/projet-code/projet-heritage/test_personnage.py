from personnage import Personnage, Magicien, Guerriere


def test_init():
    perso = Personnage(10, 4)

    assert perso.get_vie() == 10 and perso.attaque == 4


def test_get_set_vie():
    perso = Personnage(10, 4)
    perso.set_vie(2)
    assert perso.get_vie() == 2


def test_taper():
    perso = Personnage(10, 4)
    perso2 = Personnage(8, 2)

    perso.se_faire_taper(perso2)

    assert perso.get_vie() == 8 and perso2.get_vie() == 8


def test_magicien():
    perso = Personnage(10, 4)
    mago = Magicien(3, 2, 1)

    mago.lancer_sort(perso)

    assert perso.get_vie() == 9


def test_guerriere_bloquage_100():
    xena = Guerriere(12, 4, 100)
    perso = Personnage(10, 4)
    xena.se_faire_taper(perso)

    assert xena.get_vie() == 12


def test_guerriere_bloquage_0():
    xena = Guerriere(12, 4, 0)
    perso = Personnage(10, 4)
    xena.se_faire_taper(perso)

    assert xena.get_vie() == 8
