import pytest
from compteur import Compteur


def test_constructeur():
    c = Compteur()
    assert isinstance(c, Compteur)


def test_assertion():
    with pytest.raises(AssertionError):
        c = Compteur(0)

def test_valeur_initiale():
    c = Compteur()
    assert c.valeur == 0 and c.pas == 1

    c = Compteur(3, 12)
    assert c.valeur == 12 and c.pas == 3

    c = Compteur(pas=3)
    assert c.valeur == 0 and c.pas == 3

    c = Compteur(valeur=12)
    assert c.valeur == 12 and c.pas == 1


def test_incrémente():
    c = Compteur()

    c.incrémente()
    assert c.valeur == 1

    c.incrémente()
    assert c.valeur == 2

def test_accesseur_mutateur():
    c = Compteur()

    c.pas = 42
    assert c.pas == 42

    with pytest.raises(AssertionError):
        c.pas = 0


def test_comparaisons():
    assert Compteur(valeur=1) == Compteur(valeur=1)
    assert Compteur(valeur=1) <= Compteur(valeur=1)
    
    assert Compteur(valeur=1) <= Compteur(valeur=2)
    assert Compteur(valeur=1) < Compteur(valeur=2)
