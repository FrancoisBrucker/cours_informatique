from dé import Dé, MIN_VALEUR, MAX_VALEUR, TapisVert


def test_init():
    assert isinstance(Dé(), Dé)


def test_position():
    assert Dé().position == 1
    assert Dé(position=3).position == 3


def test_lancer():
    assert MIN_VALEUR <= Dé().lancer().position <= MAX_VALEUR


def test_set_position():
    dé = Dé()

    dé.position = 4
    assert dé.position == 4

    dé.position = 12
    assert dé.position == MAX_VALEUR

    dé.position = -1
    assert dé.position == MIN_VALEUR


def test_get_position():
    dé = Dé()

    dé.position = 4
    assert dé.position == dé._position


def test_dé_str():
    assert str(Dé()) == "⚀"


def test_tapis_vert_creation():
    tapis_vert = TapisVert()

    for d in tapis_vert.dés:
        assert d.position == 1


def test_tapis_vert_modification():
    tapis_vert = TapisVert()
    tapis_vert.dés[2].position = 5

    assert tapis_vert.dés[2].position == 5


def test_tapis_vert_roll():
    tapis_vert = TapisVert()
    tapis_vert.lancer()

    for d in tapis_vert.dés:
        assert 1 <= d.position <= 6


def test_tapis_vert_nombre_positions():
    tapis_vert = TapisVert()

    assert [0, 5, 0, 0, 0, 0, 0] == tapis_vert.nombre_positions()

    tapis_vert.dés[2].position = 4

    assert [0, 4, 0, 0, 1, 0, 0] == tapis_vert.nombre_positions()


def test_tapis_vert_nb_des_identiques():
    tapis_vert = TapisVert()

    assert tapis_vert.nb_dés_valeurs_identiques(5)
    assert tapis_vert.nb_dés_valeurs_identiques(4)

    tapis_vert.dés[2].position = 4

    assert not tapis_vert.nb_dés_valeurs_identiques(5)
