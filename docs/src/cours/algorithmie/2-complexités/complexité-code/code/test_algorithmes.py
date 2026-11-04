from algorithmes import recherche

def test_recherche_OUI():
    T = list(range(10))

    assert recherche(T, 0)
    assert recherche(T, 5)
    assert recherche(T, 9)

def test_recherche_NON():
    T = list(range(10))

    assert not recherche(T, -1)
    assert not recherche(T, 10)
