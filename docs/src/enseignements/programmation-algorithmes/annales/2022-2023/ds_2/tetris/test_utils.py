from utils import xy_vers_lc, lc_vers_xy, rotation


def test_xy_vers_lc():
    assert (2, 0) == xy_vers_lc(275, 50, 275, 50, 25, 3)
    assert (0, 1) == xy_vers_lc(300, 100, 275, 50, 25, 3)


def test_lc_vers_xy():
    assert (275, 50) == lc_vers_xy(2, 0, 275, 50, 25, 3)
    assert (300, 100) == lc_vers_xy(0, 1, 275, 50, 25, 3)


def test_rotation():
    matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrice_rotation = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    assert matrice_rotation == rotation(matrice)