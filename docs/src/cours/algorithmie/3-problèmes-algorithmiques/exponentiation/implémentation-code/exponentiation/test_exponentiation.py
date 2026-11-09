from exponentiation import puissance_naif, puissance_rapide


def test_puissance_naif_nombre_1():
    assert puissance_naif(1, 4) == 1


def test_puissance_naif_exposant_1():
    assert puissance_naif(4, 1) == 4


def test_puissance_naif_cas_general():
    assert puissance_naif(2, 4) == 16


def test_puissance_naif_cas_nombre_0():
    assert puissance_naif(0, 4) == 0


def test_puissance_naif_cas_exposant_0():
    assert puissance_naif(4, 0) == 1


def test_puissance_rapide_nombre_1():
    assert puissance_rapide(1, 4) == 1


def test_puissance_rapide_exposant_1():
    assert puissance_rapide(4, 1) == 4


def test_puissance_rapide_cas_general():
    assert puissance_rapide(2, 4) == 16


def test_puissance_rapide_cas_nombre_0():
    assert puissance_rapide(0, 4) == 0


def test_puissance_rapide_cas_exposant_0():
    assert puissance_rapide(4, 0) == 1
