from doppelganger import doppelganger_entrée, doppelganger_valide, doppelganger_naif, doppelganger_tri, doppelganger_bool, doppelganger_optimal


def test_valeurs_doppelganger_valide():
    assert not doppelganger_valide([0, 0])
    assert not doppelganger_valide([1, 2])
    assert doppelganger_valide([1, 2, 2])


def test_valeurs_doppelganger_entrée():
    for _ in range(10):
        T = doppelganger_entrée(10)
        assert doppelganger_valide(T)


def test_doppelganger_naif():
    assert doppelganger_naif([1, 1, 2]) == 1


def test_doppelganger_trie():
    assert doppelganger_tri([1, 2, 1]) == 1
    assert doppelganger_tri([1, 2, 2]) == 2


def test_doppelganger_bool():
    assert doppelganger_bool([1, 2, 2]) == 2


def test_doppelganger_optimal():
    assert doppelganger_optimal([1, 2, 2]) == 2
