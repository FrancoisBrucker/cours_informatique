from classes import Jeton, Piste


def test_jeton():
    jeton = Jeton("R")
    assert jeton.couleur == "R"


def test_piste():
    piste = Piste()

    couleurs = {"R": 0, "V": 0, "B": 0, "J": 0, "U": 0, "X": 0, "O": 0}
    for x in piste.jetons:
        assert isinstance(x, Jeton)
        couleurs[x.couleur] += 1
    assert couleurs == {"R": 9, "V": 9, "B": 9, "J": 9, "U": 9, "X": 5, "O": 5}


def test_piste_melange():
    piste = Piste()

    assert len(piste.jetons) == 9 * 5 + 5 * 2
    piste.melange()
    assert len(piste.jetons) == 9 * 5 + 5 * 2
