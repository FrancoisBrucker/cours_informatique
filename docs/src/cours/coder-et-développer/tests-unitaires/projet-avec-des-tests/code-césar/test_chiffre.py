from chiffre import césar_chiffre, césar_déchiffre

def test_césar_chiffre():
    assert "A B" == césar_chiffre("A B", "A")
    assert "D F" == césar_chiffre("B D", "C")
    assert "Z A" == césar_chiffre("A B", "Z")


def test_césar_déchiffre():
    assert "A B" == césar_déchiffre("A B", "A")
    assert "B D" == césar_déchiffre("D F", "C")
    assert "A B" == césar_déchiffre("Z A", "Z")
