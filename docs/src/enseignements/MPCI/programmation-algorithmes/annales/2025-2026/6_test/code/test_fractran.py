from fractran import Fraction, Fractran, Facteur


def test_Fraction_init():
    assert Fraction(1, 2).numérateur == 1
    assert Fraction(1, 2).dénominateur == 2


def test_Fraction_est_entier():
    assert Fraction(1, 2).est_entier(2)
    assert not Fraction(1, 3).est_entier(2)


def test_Fraction_valeur():
    assert Fraction(3, 2).valeur(4) == 3 * (4 // 2)


def test_Facteur_init():
    assert Facteur([2, 3, 7]).facteurs == [2, 3, 7]


def test_Facteur_nombre():
    assert Facteur([2, 3, 7]).nombre([1, 2]) == (2 ** 1) * (3 ** 2)
    assert Facteur([2, 3, 7]).nombre([1, 2, 3]) == (2 ** 1) * (3 ** 2) * (7 ** 3)


def test_Facteur_décomposition():
    assert Facteur([2, 3, 7]).décomposition(1) == [0, 0, 0]
    assert Facteur([2, 3, 7]).décomposition(2**3 * 3**2 * 7) == [3, 2, 1]


def test_Fractran_init():
    assert isinstance(Fractran([Fraction(3, 2)]), Fractran)


def test_Fractran_run_une_fraction():
    assert Fractran([Fraction(3, 2)]).run(2**3 * 3**7) == 3**10


def test_Fractran_run_plusieurs_fractions():

    programme = [Fraction(3, 10), Fraction(4, 3)]

    assert Fractran(programme).run(14) == 14
    assert Fractran(programme).run(15) == 8


def test_Fractran_suite():

    programme = [Fraction(3, 10), Fraction(4, 3)]

    assert Fractran(programme).suite(14, 10) == [14]
    assert Fractran(programme).suite(15, 10) == [15, 20, 6, 8]
