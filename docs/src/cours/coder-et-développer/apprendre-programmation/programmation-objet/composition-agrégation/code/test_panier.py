from panier import Panier, Item


def test_init():
    panier = Panier()
    assert panier is not None


def test_montre_panier_vide():
    panier = Panier()
    assert panier.montre_panier() == tuple()


def test_ajoute():
    panier = Panier()
    panier.ajoute(Item("macbook", 1000))
    assert panier.montre_panier() == (Item("macbook", 1000),)


def test_supprime_dans_panier():
    panier = Panier()
    panier.ajoute(Item("macbook", 1000))
    panier.supprime(Item("macbook", 1000))

    assert panier.montre_panier() == tuple()

def test_item_eq():
    assert Item("macbook", 1000) == Item("macbook", 1000)
    assert Item("Rolex", 1000) != Item("macbook", 1000)
    assert Item("Rolex", 10000) != Item("Rolex", 1000)