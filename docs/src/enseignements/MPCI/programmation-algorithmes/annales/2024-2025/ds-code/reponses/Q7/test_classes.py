from classes import Jeton, Piste, Podium


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


def test_piste_gauche_droite():
    piste = Piste()
    piste.jetons = [Jeton("V"), Jeton("R"),  Jeton("J"), Jeton("R")]

    assert piste.gauche_droite(0) == (None, 1)
    assert piste.gauche_droite(3) == (2, None)  
    assert piste.gauche_droite(2) == (1, 3)
    piste.jetons[1].pion = True
    assert piste.gauche_droite(2) == (0, 3)
    piste.jetons[0].pion = True
    assert piste.gauche_droite(2) == (None, 3)


def test_podium_ajoute():
    podium = Podium()

    podium.ajoute("V")
    assert podium.places == [None, None, None, None, "V"]
    podium.ajoute("R")
    assert podium.places == [None, None, None, "R", "V"]
