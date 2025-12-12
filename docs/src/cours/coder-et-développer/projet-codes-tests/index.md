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

On va ajouter des tests aux fonctions [du sujet sans les tests](../projet-codes/syracuse-sujet){.interne}. Chaque développeur va avoir d'autres tests, ce n'est pas un problème. Il faut juste être honnête avec soit-même et est moralement sur que si ses tests passent le code est correct.

S'il s'avère que l'on trouve a posteriori un bug pas de problème on rajoute un test et on le corrige. Comme le test reste : le bug ne pourra jamais revenir après une modification du code.

{% exercice %}
Quels sont les tests qui vous permettraient d'avoir confiance dans le code de la fonction `syracuse`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

J'aime tester :

- les cas limites
- un cas général

Il faut de plus s'assurer que les tests passent par tous les blocs de code.

Ici on peut par exemple tester les cas limites pair et impair (2 et 1), et un cas général (42 et 111 par exemple).
{% enddetails %}

{% exercice %}
Codez vos tests pour la fonction `syracuse`{.language-}.
{% endexercice %}
{% details "corrigé" %}

Fichier `test_syracuse.py`{.fichier} :

```python
from syracuse import syracuse

def test_syracuse_pair():
    assert syracuse(2) == 1


def test_syracuse_impair():
    assert syracuse(1) == 4

def test_syracuse_cas_général():
    assert syracuse(42) == 21
    assert syracuse(111) == 334


```

{% enddetails %}

{% exercice %}
Quels sont les tests qui vous permettraient d'avoir confiance dans le code de la fonction `suite`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

Comme pour la fonction `syracuse`{.language-}, tester le cas limite (1) et un cas général (5) me suffit.

{% enddetails %}

{% exercice %}
Codez vos tests pour la fonction `suite`{.language-}.
{% endexercice %}
{% details "corrigé" %}

Fichier `test_syracuse.py`{.fichier} :

```python
from syracuse import syracuse, suite

# ...

def test_suite_u_0_1():
    assert suite(1) == [1]


def test_suite_u_0_5():
    assert suite(5) == [5, 16, 8, 4, 2, 1]

```

{% enddetails %}

## <span id="pendu"></span>Jeu du pendu

Ajoutez des tests aux fonctions [du sujet sans les tests](../projet-codes/pendu-sujet){.interne}.

{% exercice %}
Que testeriez vous pour vérifier que la fonction `est_une_lettre`{.language-} fonctionne ? Implémentez ces tests.
{% endexercice %}
{% details "corrigé" %}

Pour tester la fonction `est_une_lettre(lettre, mot)`{.language-} vous pourrez vérifier un cas ou la lettre est trouvé et un cas où elle ne l'est pas :

- `est_une_lettre("i", "victoire")`{.language-} doit rendre `True`{.language-}
- `est_une_lettre("e", "la disparition")`{.language-} doit rendre `False`{.language-}

Fichier `test_pendu.py`{.fichier}

```python
from pendu import est_une_lettre


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

{% exercice %}
Que testeriez vous pour vérifier que la fonction `caractères`{.language-} fonctionne ? Implémentez ces tests.

{% endexercice %}
{% details "corrigé" %}

Pour tester la fonction `caractères(lettre, mot)`{.language-} on peut reprendre nos tests précédents pour cette fonction et ainsi vérifier que :
  
- `caractères("i", "victoire")`{.language-} doit rendre `[1, 5]`{.language-}
- `caractères("e", "la disparition")`{.language-} doit rendre `[]`{.language-}

Fichier `test_pendu.py`{.fichier}

```python
from pendu import est_une_lettre, caractères

# ...

def test_caractères():
    assert [1, 5] == caractères("i", "victoire")
    assert [] == caractères("e", "la disparition")

```

{% enddetails %}

{% exercice %}
Que testeriez vous pour vérifier que la fonction `découvre`{.language-} fonctionne ? Implémentez ces tests.
{% endexercice %}
{% details "corrigé" %}
Pour tester la fonction `découvre(mot_caché, lettre, positions)`{.language-}, j'essaie de vérifier ce qu'il se passe si :

- il suffit de rajouter des lettres : `découvre("......", "r", [1, 2, 5])`{.language-} doit rendre `".rr..r"`{.language-}
- ajouter des lettres à un mot partiellement découvert : `découvre("erre.r", "u", [4])`{.language-} doit rendre `"erreur"`{.language-}
- ne pas ajouter des lettres : `découvre("erre.r", "u", [])`{.language-} doit rendre `"erre.r"`{.language-}

Remarquez que nos tests doivent toujours être _plausible_ et donc utiliser des paramètres que l'on pourrait réellement utiliser, ici de vrais mots.

Fichier `test_pendu.py`{.fichier}

```python
from pendu import est_une_lettre, caractères, découvre, caché

# ...

def test_découvre():
    assert ".rr..r" == découvre("......", "r", [1, 2, 5])
    assert "erreur" == découvre("erre.r", "u", [4])
    assert "erre.r" == découvre("erre.r", "u", [])

```

{% enddetails %}

{% exercice %}
Que testeriez vous pour vérifier que la fonction `caché`{.language-} fonctionne ? Implémentez ces tests.
{% endexercice %}
{% details "corrigé" %}

Même pattern que d'habitude cas limite et cas général :

- `caché("")`{.language-} doit rendre `""`{.language-}
- `caché("anticonstitutionnellement")`{.language-} doit rendre `"........................."`{.language-}

Fichier `test_pendu.py`{.fichier}

```python
from pendu import est_une_lettre, caractères, découvre, caché

# ...

def test_caché():
    assert "" == caché("")
    assert "........................." == caché("anticonstitutionnellement")

```

{% enddetails %}

## <span id="compte-caractere"></span>Le compte est bon

Notez qu'on ne teste jamais les programmes `main.py`{.fichier} car ils nécessitent un utilisateur et on veut que nos tests soient automatisés.
{% exercice %}
Ajoutez des tests aux fonctions `donne_prochain_indice`{.language-}, `compte_caractère`{.language-} et `donne_max_doublon`{.language-} [du sujet sans les tests](../projet-codes/compte-caractere-sujet){.interne}.
{% endexercice %}
{% details "corrigé" %}

J'applique toujours le même pattern : j'essaie de faire un test par cas et s'il y a des boucles un cas limite et un cas général. Ce qui pourrait donner ici :

- Pour tester la fonction `donne_prochain_indice(chaîne:str, indice:int) -> int`{.language-} vous pourrez vérifier que :
  - `donne_prochain_indice("bxaaxaaaxax", 4)`{.language-} rende 8
  - `donne_prochain_indice("bxaaxaaaxax", 0)`{.language-} rende `None`{.language-}
- Pour tester la fonction `compte_caractère(chaîne: str, indice: int) -> int`{.language-}  vous pourrez vérifier que :
  - Un caractère non présent dans la chaîne
  - Un caractère présent plusieurs fois dans la chaîne
- Pour tester la fonction `donne_max_doublon(chaîne: str) -> str`{.language-}   vous pourrez tester avec une chaîne admettant plusieurs caractères répétés un nombre différent de fois.

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

A vous sans aide ! L'exercice ici est de trouver à partir du code les tests les plus simples possible permettant d'être confiant dans notre code.

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
