from carte import Carte
from deck import Deck, jeu32


def test_deck_creation():
    deck = Deck()
    assert isinstance(deck, Deck)


def test_deck_vide():
    deck = Deck()
    assert len(deck.cartes) == 0


def test_ajoute():
    deck = Deck()
    deck.ajoute(Carte(Carte.VALEURS.As, Carte.COULEURS.Carreau))
    assert len(deck.cartes) == 1


def test_pioche():
    deck = Deck()
    deck.ajoute(Carte(Carte.VALEURS.As, Carte.COULEURS.Carreau))
    assert len(deck.cartes) == 1
    assert Carte(Carte.VALEURS.As, Carte.COULEURS.Carreau) == deck.pioche()
    assert len(deck.cartes) == 0

def test_melange():
    deck = Deck()
    deck.ajoute(Carte(Carte.VALEURS.As, Carte.COULEURS.Carreau))
    deck.mélange()
    
    assert deck.cartes[0] == Carte(Carte.VALEURS.As, Carte.COULEURS.Carreau)


def test_jeu32():
    deck = jeu32()
    assert len(deck.cartes) == 32