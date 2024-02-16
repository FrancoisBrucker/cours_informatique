from fonctions import compte_caractère, donne_prochain_indice, donne_max_doublon


def test_donne_prochain_indice():
    assert donne_prochain_indice("bxaaxaaaxax", 4) == 8
    assert donne_prochain_indice("bxaaxaaaxax", 0) == None


def test_compte_caractère():
    assert compte_caractère("bxaaxaaaxax", 0) == 1
    assert donne_prochain_indice("bxaaxaaaxax", 1) == 4

def test_donne_max_doublon():
    assert donne_max_doublon("bxaaxaaaxax") == 6

