import monnaie


def test_multiplication():
    cinq = monnaie.dollar(5)

    assert monnaie.dollar(10) == cinq * 2
    assert monnaie.dollar(15) == cinq * 3


def test_egalite():
    assert monnaie.dollar(5) == monnaie.dollar(5)


def test_non_egalite_dollar():
    assert monnaie.dollar(5) != monnaie.dollar(6)


def test_franc_dollar():
    assert monnaie.franc(1) != monnaie.dollar(1)


def test_devise():
    assert "USD" == monnaie.dollar(1).devise
    assert "CHF" == monnaie.franc(1).devise
