from fonctions import bonjour


def test_bonjour():
    assert bonjour("monde") == "bonjour monde !"
