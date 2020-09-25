from figures_des import contient_une_paire, compte_valeur, \
     contient_une_double_paire, contient_un_brelan, contient_un_carre, contient_un_full


def test_contient_une_paire_une_paire():
    assert contient_une_paire([1, 2, 3, 4, 1])


def test_contient_une_paire_pas_de_paire():
    assert not contient_une_paire([1, 2, 3, 4, 5])


def test_contient_une_paire_un_brelan():
    assert contient_une_paire([2, 2, 3, 4, 2])


def test_contient_une_paire_un_full():
    assert contient_une_double_paire([2, 2, 3, 3, 3])


def test_compte_valeur():
    assert compte_valeur([1, 2, 3, 1, 2]) == {1: 2, 2: 2, 3: 1}


def test_contient_un_brelan_un_brelan():
    assert contient_un_brelan([3, 2, 3, 4, 3])


def test_contient_un_brelan_une_double_paire():
    assert not contient_un_brelan([1, 1, 2, 2, 3])


def test_contient_un_carre_un_carre():
    assert contient_un_carre([3, 2, 3, 3, 3])


def test_contient_un_carre_un_brelan():
    assert not contient_un_brelan([1, 2, 3, 4, 1])


def test_contient_une_double_paire_une_double_paire():
    assert contient_une_double_paire([1, 4, 3, 4, 1])


def test_contient_une_bouble_paire_un_carre():
    assert not contient_une_double_paire([1, 1, 1, 1, 5])


def test_contient_un_full_oui():
    assert contient_un_full([1, 1, 2, 2, 2])


def test_contient_un_full_non():
    assert not contient_un_full([1, 1, 3, 2, 2])


def test_contient_un_full_six_des():
    assert contient_un_full([1, 1, 1, 2, 2, 2])
