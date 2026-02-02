from point_fixe import lièvre_tortue, mu


def test_lièvre_tortue():
    T = [6, 1, 3, 2, 6, 4, 5]
    assert 4 == lièvre_tortue(T)


def test_mu():
    T = [6, 1, 3, 2, 6, 4, 5]
    assert 6 == mu(T)
