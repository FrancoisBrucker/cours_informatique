from fonctions import (
    cases_noires,
    cases_noires_mono_ligne,
    taille_minimale,
    verif_ligne,
)

cle_l = [[2], [3, 1], [4], [4], [1, 1]]
cle_c = [[1], [5], [4], [2], [4]]


def test_cases_noires():
    cle_l = [[2], [3, 1], [4], [4], [1, 1]]

    assert cases_noires(cle_l) == 16
    assert cases_noires_mono_ligne(cle_l) == 16


def test_taille_minimale():
    assert taille_minimale([3, 5, 2]) == 12


def test_verif_ligne():
    assert not verif_ligne([[1, 0, 1]], [[2]], 0)
    assert not verif_ligne([[1, 0]], [[2]], 0)
    assert not verif_ligne([[0]], [[1]], 0)
