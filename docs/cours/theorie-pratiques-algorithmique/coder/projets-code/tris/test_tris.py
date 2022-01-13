from tris import insertion, selection, colle, fusion, rapide


def test_insertion_croissant():
    tab = [1, 2, 3]
    insertion(tab)

    assert tab == [1, 2, 3]


def test_insertion_decroissant():
    tab = [3, 2, 1]
    insertion(tab)

    assert tab == [1, 2, 3]


def test_selection_croissant():
    tab = [1, 2, 3]
    selection(tab)

    assert tab == [1, 2, 3]


def test_selection_decroissant():
    tab = [3, 2, 1]
    selection(tab)

    assert tab == [1, 2, 3]


def test_colle():
    assert colle([1, 4, 7], [0, 2, 3, 98]) == [0, 1, 2, 3, 4, 7, 98]


def test_fusion_fin():
    assert fusion([4]) == [4]


def test_fusion_avec_rec():
    assert fusion([1, 2, 0, 4, 3, 98, 7]) == [0, 1, 2, 3, 4, 7, 98]


def test_rapide_fin():
    assert rapide([4]) == [4]


def test_rapide_avec_rec():
    assert rapide([1, 2, 0, 4, 3, 98, 7]) == [0, 1, 2, 3, 4, 7, 98]
