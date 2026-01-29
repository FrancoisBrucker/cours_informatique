from chiffre import césar_chiffre, césar_déchiffre


def test_césar_chiffre_sans_décalage():
    assert "AB" == césar_chiffre("AB", "A")


def test_césar_chiffre_sans_décalage_avec_espaces():
    assert "A B" == césar_chiffre("A B", "A")


def test_césar_chiffre_décalage():
    assert "D F" == césar_chiffre("B D", "C")


def test_césar_chiffre_décalage_modulo():
    assert "Z A" == césar_chiffre("A B", "Z")


def test_césar_déchiffre():
    assert "A B" == césar_déchiffre("A B", "A")
    assert "B D" == césar_déchiffre("D F", "C")
    assert "A B" == césar_déchiffre("Z A", "Z")
