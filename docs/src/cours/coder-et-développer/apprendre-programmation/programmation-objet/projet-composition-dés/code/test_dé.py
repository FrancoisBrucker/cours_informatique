from dé import Dé, TapisVert


from dé import Dé


def test_init():
    assert isinstance(Dé(), Dé)


def test_position():
    assert Dé().position == 1
    assert Dé(position=4).position == 4


def test_lancer():
    dé = Dé()
    dé.lancer()
    assert Dé.MIN_VALEUR <= dé.position <= Dé.MAX_VALEUR


def test_str():
    dé = Dé()
    assert str(dé) == "⚀"
    dé.position = 4
    assert str(dé) == "⚃"


def test_tapis_vert_creation():
    tapis_vert = TapisVert()

    for d in tapis_vert.dés:
        assert d.position == 1


def test_tapis_vert_modification():
    tapis_vert = TapisVert()
    tapis_vert.dés[2].position = 5

    assert tapis_vert.dés[2].position == 5


def test_tapis_vert_lancer():
    tapis_vert = TapisVert()
    tapis_vert.lancer()

    for d in tapis_vert.dés:
        assert 1 <= d.position <= 6


def test_tapis_vert_nombre_positions():
    tapis_vert = TapisVert()

    assert [0, 5, 0, 0, 0, 0, 0] == tapis_vert._nombre_positions()

    tapis_vert.dés[2].position = 4

    assert [0, 4, 0, 0, 1, 0, 0] == tapis_vert._nombre_positions()


def test_tapis_vert_nb_des_identiques():
    tapis_vert = TapisVert()

    assert tapis_vert.nb_dés_valeurs_identiques(5)
    assert tapis_vert.nb_dés_valeurs_identiques(4)

    tapis_vert.dés[2].position = 4

    assert not tapis_vert.nb_dés_valeurs_identiques(5)
