import num

def test_nombre():
    assert num.nombre("Aé") == 65 + 233

def test_somme_digit():
    assert num.somme_digit(65) == 11

def test_chiffre_associé():
    assert num.chiffre_associe("Aé") == 1