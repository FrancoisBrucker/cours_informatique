from pendu import est_une_lettre, caractères, découvre, caché


def test_est_une_lettre():
    assert est_une_lettre("i", "victoire")
    assert not est_une_lettre("e", "la disparition")


def test_caractères():
    assert [1, 5] == caractères("i", "victoire")
    assert [] == caractères("e", "la disparition")


def test_découvre():
    assert ".rr..r" == découvre("......", "r", [1, 2, 5])
    assert "erreur" == découvre("erre.r", "u", [4])
    assert "erre.r" == découvre("erre.r", "u", [])


def test_caché():
    assert "" == caché("")
    assert "........................." == caché("anticonstitutionnellement")
