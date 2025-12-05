---
layout: layout/post.njk

title: "On s'entraîne à coder de petits projets"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Or reprend [les exercices de code](../projet-codes/){.interne} et on leur ajoute des tests.

{% faire %}

- reprenez le code des exercices précédents
- ajoutez un fichier de tests s'appellant `test_fonctions.py`{.language-}

{% endfaire %}

Les corriges sont des **propositions** de tests, ce n'est pas la vérité :

{% attention "**À retenir**" %}
Les tests sont écrit par le développeur et leurs buts est qu'ils lui permettent d'être convaincu que le code fonctionne si les tests passent. Ce n'est pas une **preuve** mais permet de continuer à coder tranquillement.
{% endattention %}

## <span id="syracuse"></span>Syracuse

{% exercice %}
Ajoutez des tests aux fonctions [du sujet sans les tests](../projet-codes/syracuse-sujet){.interne}.
{% endexercice %}
{% details "corrigé" %}

Fichier `test_syracuse.py`{.fichier} :

```python
from syracuse import syracuse, suite

def test_syracuse_pair():
    assert syracuse(2) == 1


def test_syracuse_impair():
    assert syracuse(1) == 4


def test_suite_u_0_1():
    assert suite(1) == [1]


def test_suite_u_0_5():
    assert suite(5) == [5, 16, 8, 4, 2, 1]

```

{% enddetails %}

## <span id="pendu"></span>Jeu du pendu

{% exercice %}
Ajoutez des tests aux fonctions [du sujet sans les tests](../projet-codes/pendu-sujet){.interne}.

- Pour tester la fonction `est_une_lettre(lettre, mot)`{.language-} vous pourrez vérifier que :
  - `est_une_lettre("i", "victoire")`{.language-} doit rendre `True`{.language-}
  - `est_une_lettre("e", "la disparition")`{.language-} doit rendre `False`{.language-}

- Pour tester la fonction `caractères(lettre, mot)`{.language-} vous pourrez vérifier que :
  - `caractères("i", "victoire")`{.language-} doit rendre `[1, 5]`{.language-}
  - `caractères("e", "la disparition")`{.language-} doit rendre `[]`{.language-}

- Pour tester la fonction `découvre(mot_caché, lettre, positions)`{.language-} vous pourrez vérifier que :
  - `découvre("......", "r", [1, 2, 5])`{.language-} doit rendre `".rr..r"`{.language-}
  - `découvre("erre.r", "u", [4])`{.language-} doit rendre `"erreur"`{.language-}
  - `découvre("erre.r", "u", [])`{.language-} doit rendre `"erre.r"`{.language-}

- Pour tester la fonction `caché(mot)`{.language-} vous pourrez vérifier que :
  - `caché("anticonstitutionnellement")`{.language-} doit rendre `"........................."`{.language-}
  - `caché("")`{.language-} doit rendre `""`{.language-}

{% endexercice %}
{% details "corrigé" %}

Fichier `test_pendu.py`{.fichier}

```python/
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

```

{% enddetails %}

## <span id="compte-caractere"></span>Le compte est bon

{% exercice %}
Ajoutez des tests aux fonctions [du sujet sans les tests](../projet-codes/compte-caractere-sujet){.interne}.

- Pour tester la fonction `donne_prochain_indice(chaîne:str, indice:int) -> int`{.language-} vous pourrez vérifier que :
  - `donne_prochain_indice("bxaaxaaaxax", 4)`{.language-} rende 8
  - `donne_prochain_indice("bxaaxaaaxax", 0)`{.language-} rende `None`{.language-}
- Pour tester la fonction `compte_caractère(chaîne: str, indice: int) -> int`{.language-}  vous pourrez vérifier que :
  - Un caractère non présent dans la chaîne
  - Un caractère présent plusieurs fois dans la chaîne
- Pour tester la fonction `donne_max_doublon(chaîne: str) -> str`{.language-}   vous pourrez tester avec une chaîne admettant plusieurs caractères répétés un nombre différent de fois.

{% endexercice %}
{% details "corrigé" %}

Fichier `test_fonctions.py`{.fichier}

```python
from fonctions import compte_caractère, donne_prochain_indice, donne_max_doublon


def test_donne_prochain_indice():
    assert donne_prochain_indice("bxaaxaaaxax", 4) == 8
    assert donne_prochain_indice("bxaaxaaaxax", 0) == None


def test_compte_caractère():
    assert compte_caractère("bxaaxaaaxax", 0) == 1
    assert donne_prochain_indice("bxaaxaaaxax", 1) == 4

def test_donne_max_doublon():
    assert donne_max_doublon("bxaaxaaaxax") == 6

```

{% enddetails %}

## <span id="polynomes"></span>Somme et produits de polynômes

Uniquement des fonctions à créer.

{% exercice %}
Ajoutez des tests aux fonctions [du sujet sans les tests](../projet-codes/polynomes-sujet){.interne}.
{% endexercice %}
{% details "corrigé" %}

Fichier `test_polynôme.py`{.fichier}

```python

from polynome import valeur, somme, produit

def test_valeur_constante():
    assert valeur([1], 4) == 1 * 4 ** 0


def test_valeur_vide():
    assert valeur([], 4) == 0


def test_valeur_polynôme():
    assert valeur([1, 2, 3], 2) == 1 + 2 * 2 + 3 * 4


def test_somme_un_vide():
    assert somme([1, 2, 3], []) == [1, 2, 3]
    assert somme([], [1, 2, 3]) == [1, 2, 3]


def test_somme_égal():
    assert somme([1, 2, 3], [3, 2, 1]) == [4, 4, 4]


def test_somme_different():
    assert somme([1, 2, 3], [3]) == [4, 2, 3]
    assert somme([3], [1, 2, 3]) == [4, 2, 3]


def test_produit_longueur1():
    assert produit([1, 2, 3], [2]) == [2, 4, 6]
    assert produit([2], [1, 2, 3]) == [2, 4, 6]


def test_produit_égal():
    assert produit([2, 3], [3, 2]) == [6, 13, 6]

```

{% enddetails %}
