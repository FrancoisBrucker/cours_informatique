from panier import Panier


def test_init():
    panier = Panier()
    assert panier is not None


def test_montre_panier_vide():
    panier = Panier()
    assert panier.montre_panier() == tuple()


def test_ajoute():
    panier = Panier()
    panier.ajoute("pomme")
    assert panier.montre_panier() == ("pomme",)


def test_supprime_dans_panier():
    panier = Panier()
    panier.ajoute("pomme")
    panier.supprime("pomme")

    assert panier.montre_panier() == tuple()
