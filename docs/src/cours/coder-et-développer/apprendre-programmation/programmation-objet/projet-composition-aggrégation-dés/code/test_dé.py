from dé import Dé, TapisVert, MementoDé, MementoTapisVert


from dé import Dé


def test_init():
    assert isinstance(Dé(), Dé)


def test_valeur():
    assert Dé().valeur == 1
    assert Dé(valeur=4).valeur == 4


def test_lancer():
    dé = Dé()
    dé.lancer()
    assert Dé.MIN_VALEUR <= dé.valeur <= Dé.MAX_VALEUR


def test_str():
    dé = Dé()
    assert str(dé) == "⚀"
    dé.valeur = 4
    assert str(dé) == "⚃"


def test_tapis_vert_creation():
    tapis_vert = TapisVert()

    for d in tapis_vert.dés:
        assert d.valeur == 1


def test_tapis_vert_modification():
    tapis_vert = TapisVert()
    tapis_vert.dés[2].valeur = 5

    assert tapis_vert.dés[2].valeur == 5


def test_tapis_vert_lancer():
    tapis_vert = TapisVert()
    tapis_vert.lancer()

    for d in tapis_vert.dés:
        assert 1 <= d.valeur <= 6


def test_tapis_vert_nombre_valeurs():
    tapis_vert = TapisVert()

    assert [0, 5, 0, 0, 0, 0, 0] == tapis_vert._nombre_valeurs()

    tapis_vert.dés[2].valeur = 4

    assert [0, 4, 0, 0, 1, 0, 0] == tapis_vert._nombre_valeurs()


def test_tapis_vert_nb_des_identiques():
    tapis_vert = TapisVert()

    assert tapis_vert.nb_dés_valeurs_identiques(5)
    assert tapis_vert.nb_dés_valeurs_identiques(4)

    tapis_vert.dés[2].valeur = 4

    assert not tapis_vert.nb_dés_valeurs_identiques(5)

def test_mementoDé():
    dé = Dé()
    dé.valeur = 5
    memento = MementoDé(dé)
    dé.valeur = 1
    memento.restore()
    assert dé.valeur == 5


def test_mementoTapisVert():
    tapis_vert = TapisVert()
    for dé in tapis_vert.dés:
        dé.valeur = 5
    memento = MementoTapisVert(tapis_vert)
    for dé in tapis_vert.dés:
        dé.valeur = 1
    memento.restore()
    for dé in tapis_vert.dés:
        assert dé.valeur == 5
