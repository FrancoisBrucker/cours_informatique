from monnaie import Dollar


def test_multiplication():
    cinq = Dollar(5)
    cinq.fois(2)

    assert 10 == cinq.montant
