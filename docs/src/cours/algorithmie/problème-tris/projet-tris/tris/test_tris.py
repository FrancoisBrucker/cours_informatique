from tris import insertion, sélection, bulles, combiner, fusion, rapide


def test_insertion_croissant():
    tab = [1, 2, 3]
    insertion(tab)

    assert tab == [1, 2, 3]


def test_insertion_décroissant():
    tab = [3, 2, 1]
    insertion(tab)

    assert tab == [1, 2, 3]


def test_selection_croissant():
    tab = [1, 2, 3]
    sélection(tab)

    assert tab == [1, 2, 3]


def test_selection_décroissant():
    tab = [3, 2, 1]
    sélection(tab)

    assert tab == [1, 2, 3]

def test_bulles_croissant():
    tab = [1, 2, 3]
    bulles(tab)

    assert tab == [1, 2, 3]


def test_bulles_décroissant():
    tab = [3, 2, 1]
    bulles(tab)

    assert tab == [1, 2, 3]

def test_combiner():
    assert combiner([1, 4, 7], [0, 2, 3, 98]) == [0, 1, 2, 3, 4, 7, 98]


def test_fusion_fin():
    assert fusion([4]) == [4]


def test_fusion_avec_rec():
    assert fusion([1, 2, 0, 4, 3, 98, 7]) == [0, 1, 2, 3, 4, 7, 98]


def test_rapide_fin():
    assert rapide([4]) == [4]


def test_rapide_avec_rec():
    assert rapide([1, 2, 0, 4, 3, 98, 7]) == [0, 1, 2, 3, 4, 7, 98]
