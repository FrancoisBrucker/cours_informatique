from texte import conversion


def test_conversion_minuscules_vers_majuscule():
    assert "ABCDE" == conversion("abcde")


def test_conversion_avec_espaces():
    assert "AB CD" == conversion("ab cd")


def test_conversion_avec_accents():
    assert "ABC DE" == conversion("ÀBÇ dè")
