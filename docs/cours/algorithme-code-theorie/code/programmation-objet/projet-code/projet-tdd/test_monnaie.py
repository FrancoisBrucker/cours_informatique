from monnaie import Dollar, Franc


def test_multiplication_dollar():
    cinq = Dollar(5)

    assert Dollar(10) == cinq * 2
    assert Dollar(15) == cinq * 3


def test_multiplication_franc():
    cinq = Franc(5)

    assert Franc(10) == cinq * 2
    assert Franc(15) == cinq * 3


def test_egalite_dollar():
    assert Dollar(5) == Dollar(5)


def test_egalite_franc():
    assert Franc(5) == Franc(5)


def test_non_egalite_dollar():
    assert Dollar(5) != Dollar(6)


def test_non_egalite_franc():
    assert Franc(5) != Franc(6)


def test_franc_dollar():
    assert Franc(1) != Dollar(1)
