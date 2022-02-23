from pytest import approx
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


def test_plus_est_une_Somme():
    somme = monnaie.dollar(5) + monnaie.dollar(2)

    assert somme.gauche == monnaie.dollar(5)
    assert somme.droite == monnaie.dollar(2)


def test_conversion_addition():
    somme = monnaie.dollar(5) + monnaie.dollar(2)
    banque = monnaie.Banque()
    conversion = banque.conversion(somme, "USD")

    assert monnaie.dollar(7) == conversion


def test_banque_conversion_monnaie_identique():
    banque = monnaie.Banque()
    assert monnaie.dollar(1) == banque.conversion(monnaie.dollar(1), "USD")


def test_banque_conversion_monnaie_differente():
    banque = monnaie.Banque()
    assert monnaie.franc(1) == banque.conversion(monnaie.dollar(2), "CHF")


def test_banque_change_identique():
    assert 1 == monnaie.Banque().change("USD", "USD")


def test_banque_change_CHF_dollar():
    assert 2 == monnaie.Banque().change("CHF", "USD")
    assert 0.5 == approx(monnaie.Banque().change("USD", "CHF"))


def test_somme_conversion_deux_monnaies():
    assert monnaie.franc(2) == monnaie.Banque().conversion(
        monnaie.dollar(2) + monnaie.franc(1), "CHF"
    )


def test_somme_de_somme():
    banque = monnaie.Banque()
    expression = monnaie.dollar(1) + (monnaie.franc(2) + monnaie.dollar(1))
    assert monnaie.franc(3) == banque.conversion(expression, "CHF")


def test_somme_de_somme_2():
    banque = monnaie.Banque()
    expression = (monnaie.dollar(1) + monnaie.franc(2)) + monnaie.dollar(1)
    assert monnaie.franc(3) == banque.conversion(expression, "CHF")


def test_mult_de_somme():
    banque = monnaie.Banque()

    expression = (monnaie.franc(2) + monnaie.dollar(1)) * 4
    assert monnaie.franc(10) == banque.conversion(expression, "CHF")
