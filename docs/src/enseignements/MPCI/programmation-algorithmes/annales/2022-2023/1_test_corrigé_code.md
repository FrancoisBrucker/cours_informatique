---
layout: layout/post.njk

title:  "Corrigé Test 1 : code"
authors:
    - François Brucker
---


## Barème

Une note sur 5 répartie comme suit :

1. sur 1 point (.5 pour le code et .5 pour les tests)
2. sur 1 point (.5 pour le code et .5 pour les tests)
3. sur 1 point (.5 pour le code et .5 pour les tests)
4. sur 1 point (.5 pour le code et .5 pour les tests)
5. sur 1 point

La note sur $20$ finale est obtenue en multipliant la note sur 5 par $6$

{% note "**Objectif du test**" %}

En 15 minutes :

* **un élève *normal*** doit parvenir à faire parfaitement les 2 premières questions. Ce qui lui permet d'avoir 2/5, soit 12/20
* **un bon élève** doit parvenir à réussir les 3 premières questions. Ce qui lui permet d'avoir 3/5 et donc 18/20
* **un très bon élève** fait plus que les 3 premières questions.
{% endnote %}

La ventilation des notes est :

|note/5 | 0 | 0.5  | 1   | 1.25| 1.5 | 1.75 | 2 | 2.25 | 2.5 | 2.75 | 3 | 3.5 | 4 | 5 |
|note/20| 0 | 3    | 6   | 7.5 | 9   | 10.5 | 12| 13.5 | 15  | 16.5 | 18| 21  | 24| 30|
|-------|---|------|-----|-----|-----|------|---|------|-----|------|---|-----|---|---|
|nombre | 3 |  5   |  10 |  1  |  1  | 1    | 12|  1   |  1  | 1    | 4 | 1   | 1 | 1 |
|rang   | 41| 36   | 26  | 25  | 24  | 23   | 11|  10  | 9   |  8   | 4 | 3   | 2 | 1 |
| # <   |  0|  3   |  8  | 18  | 19  |20    | 21| 33   |  34 | 35   | 36| 40  | 41| 42|

* moyenne : 10.2/20 (1.7/5)
* écart-type : 6.57/20 (1.09/5)
* médiane : 12/20 (2/5)

## Erreurs fréquemment rencontrées

{% attention %}
Beaucoup d'entres vous sont venus sans réelle préparation au test. Cela se ressent dans les notes (la moité des élèves ont moins de dix et un quart moins de six) !
{% endattention %}

Vous **devez** préparer chaque test pour obtenir une note correcte (12 ou plus). Le cours est en ligne, il y a des annales et les profs — très sympas — répondent à vos questions en direct ou par mail.

Outre le manque de préparation, j'ai vu beaucoup de code ou de tests qui ne s'exécutent manifestement pas. Votre code **doit** être exécutable sinon le correcteur peut penser que vous tentez de l'enfumer et ça le force à modifier votre code pour le faire fonctionner, en particulier pour lancer les tests (ce qui le rend irritable et moins enclin à être bienveillant).

Enfin, cela masque les fonctions ou les tests qui sont corrects !

{% note %}
Du code est fait pour être exécuté donc vous devez vous assurer que :

* le code rendu est exécutable
* vos tests sont exécutables avec pytest (on peut tolérer un test qui rate si vous expliquez que vous n'avez pas eu le temps de corriger le bug)

Pour cela, vous **devez** lancer régulièrement vos tests **pendant** le test.

{% endnote %}

Ci-après quelques remarques plus ponctuelles

### Trop lent

Vous prenez globalement  bien trop de temps à écrire des algorithmes simples. La première question est une application directe du S1 et la seconde ne devrait pas vous prendre plus de 5min. Presque tout le monde aurait du arriver à la question 3, ce qui est loin d'être le cas.

Pour vous améliorer en code, relisez le cours [coder en python]({{ "/cours/utiliser-python"  }}) qui vous donnent toutes les bases nécessaire pour... coder en python.

Enfin, les tests à effectuer vous étaient donnés dans l'énoncé sous la forme d'exemples, il vous suffisait de les reprendre en utilisant le formalisme vu lors du [projet pourcentage]({{ "/cours/algorithme-code-théorie/code/projet-pourcentages" | url }}).

### Format des tests

Les tests **doivent** être fait comme dans le [projet pourcentages]({{ "/cours/algorithme-code-théorie/code/projet-pourcentages" | url }}) ! Il faut donc :

* un fichier de test séparé du code et un fichier de test par fichier de code. Le nom de ce fichier doit s'appeler `test_[nom du fichier de code à tester].py`{.fichier}
* pourvoir l'exécuter avec `python -m pytest` dans un terminal (utilisez le nom de l'interpréteur python que vous avez, voir [ce tutoriel]({{ "/tutoriels/vsc-python" }}#quel-python))

En particulier :

{% attention %}

* afficher un résultat à l'écran avec la commande `print`{.language-} n'est **pas** un test
* faire un assert sans fonction de test n'est **pas** un test
* une fonction de test n'a **pas** de paramètres.

{% endattention %}

Chaque test **doit** commencer par `test_`{.language-} suivi du nom de la fonction à tester. S'il y a plusieurs tests pour une même fonction, on ajoute ce que le test teste :

```python
def test_[nom de la fonction à tester]_[ce que ça teste]():
    # ...
```

{% info %}
Ici, différentier les 2 tests proposés par fonction n'était pas évident. Regrouper les 2 tests en une seule fonction comme je le fais dans le corrigé était légitime.
{% endinfo %}

### Misc

Quelques remarques sur des erreurs ou lourdeurs que j'ai vu chez certains. Essayez d'y faire attention pour vos prochains codes et rendus.

#### Nom des fichiers

Il vous faut a priori 2 fichiers :

* un pour le code, que vous pouvez appeler `pendu.py`{.fichier}, ou `code.py`{.fichier}
* un pour tester le code qui s'appelle comme le nom du fichier de code précédé de `test_`{.fichier}. Donc `test_pendu.py`{.fichier} ou `test_code.py`{.fichier} selon le nom de votre fichier de code.

#### Description d'une fonction

La description d'une fonction (entre `"""`{.language-}) est inutile. Le code **doit** se suffire à lui-même pour être lisible et compris. Si ce n'est pas le cas, c'est que vous avez mal codé !

La description de chaque fonction n'est utile que si vous faire une bibliothèque (une suite de fonctions qui devront être utilisées par d'autres sans qu'ils aient à connaître leurs codes). Ici, vous faite du code qui sera  exécuté ou utilisé par vous et les autres membres de l'équipe de développement (ou le correcteur, ici moi) : la description ou les commentaires **doivent** être inutiles : faites du code lisible.

#### Listes

On préférera toujours utiliser `L.append(i)`{.language-} plutôt que `L = L + [i]`{.language-} car `append`{.language-} est une méthode en $\mathcal{O}(1)$ opérations alors `+` crée une nouvelle liste et est donc en $\mathcal{O}(n)$ où $n$ est la taille de la liste `L`{.language-}.

#### Comparaison de booléens

On ne teste pas si un booléen est vrai ou faux, on utilise directement sa valeur.

* On écrit : `assert est_une_lettre("i", "victoire")`{.language-}
* ~~On écrit pas `assert est_une_lettre("i", "victoire") == True`{.language-}~~

En effet,  les deux formes sont équivalentes  puisque une comparaison avec `==`{.language-} rend `True`{.language-} ou `False`{.language-} mais la seconde est plus compacte et moins redondante.

De même (vu souvent), à la place d'écrire :

```text
Si f() == Vrai alors:
    return Vrai
sinon:
    return Faux
```

écrivez :

```text
return f()
```

#### Import

Deux fautes de style reviennent assez souvent :

* `from truc import *`{.language-}
* `import contrôle as ctr`{.language-}

Ne faites aucune des deux, c'est [Bad Karma](https://www.youtube.com/watch?v=2dRIHt2SJHE) (et c'est très très mal !) : ça vous sautera à la figure tôt ou tard.

{% attention "**Pourquoi c'est mal**" %}

* `from truc import *`{.language-} : **on ne sais pas ce que l'on importe**. Le traçage des fonctions n'est pas clair et tôt ou tard ça va vous sauter à la figure en important des choses que vous ne voulez pas importer
* `import contrôle as ctr`{.language-}. Je ne vois pas l'avantage de cette chose. Vous vous tirez au moins 3 fois une balle dans le pied :
  1. **Ce n'est pas plus court**. Car, pourquoi ne pas avoir écrit `import contrôle as c`{language-} ? C'est **encore** plus court... On gagne carrément 2 caractères à chaque utilisation du module ! De quoi finir à 12h14 à la place de 12h15 (royal !).. Ou tant qu'à gagner des lettres autant directement renommer le fichier `contrôle.py`{fichier} en `ctr.py`{.fichier}. On aurait eu encore moins de choses à écrire (juste `import ctr`{language-}, soit carrément 12 caractères de moins !)
  2. **c'est moins lisible**. Vous devez pouvoir lire votre code sans avoir besoin de réfléchir aux significations des variables. Votre esprit doit être concentré sur la compréhension de l'algorithmie. Vous gagnez 10 microsecondes à l'écriture (et encore, voir ci-après) mais vous perdez 2 secondes à chaque lecture pour vous rappeler la signification de `ctr`{.language-}.
  3. **vous empêchez votre éditeur de vous aider** avec la complétion automatique qui rend un nom explicite est plus facile à comlpèter qu'une abréviation.
  
{% endattention %}

#### Variable différent d'une chaîne de caractère

Je ne l'ai vu qu'une fois mais je préfère prévenir. Ne confondez pas la variable ou le paramètre d'une fonction `x`{.language-} avec une chaîne de caractères contenant le caractère x, notée `'x'`{.language-}.

## Corrigé de la question 1. Fonction `est_une_lettre(lettre, mot)`{.language-}

### tests de `est_une_lettre(lettre, mot)`{.language-}

Commençons par les tests. Ils vous étaient donnés dans l'énoncé. Il suffisait de les écrire. Par exemple :

```python
def test_est_une_lettre():
    assert est_une_lettre("i", "victoire")
    assert not est_une_lettre("e", "la disparition")
```

{% info %}
Pas besoin d'écrire `assert est_une_lettre("i", "victoire") == True`{.language-}, c'est équivalent à `assert est_une_lettre("i", "victoire")`{.language-}.
{% endinfo %}

### fonction `est_une_lettre(lettre, mot)`{.language-}

Plusieurs possibilités. Commençons par la plus simple, que **tout le monde** devrait arriver à faire, c'est une retranscription directe d'un algorithme du cours :

```python
def est_une_lettre(lettre, mot):
    for c in mot:
        if lettre == c:
            return True
    return False
```

On pouvait aussi utiliser le mot clé `in`{.language-} de python (supposé connu de tous), pour une solution écrite en 30 secondes chrono :

```python
def est_une_lettre(lettre, mot):
    if lettre in mot:
        return True
    else:
        return False
```

Notez que la version précédente est identique à la version ci-dessous, bien plus élégante :

```python
def est_une_lettre(lettre, mot):
    return lettre in mot
```

## Corrigé de la question 2. Fonction `caractères(lettre, mot)`{.language-}

### tests de `caractères(lettre, mot)`{.language-}

Encore une fois les tests étaient donnés. Il suffisait de les re-écrire :

```python
def test_caractères():
    assert [1, 5] == caractères("i", "victoire")
    assert [] == caractères("e", "la disparition")
```

### fonction `caractères(lettre, mot)`{.language-}

```python
def caractères(lettre, mot):
    position = []

    for i in range(len(mot)):
        if mot[i] == lettre:
            position.append(i)

    return position
```

On utilise ici la fonction `range`{.language-} pour itérer sur les indices du tableau plutôt que sur ses valeurs.

Encore une fois, **tout le monde** devrait arriver à faire cette fonction d'une seule traite, sans réfléchir.

## Corrigé de la question 3. Fonction `découvre(mot_caché, lettre, positions)`{.language-}

### tests de `découvre(mot_caché, lettre, positions)`{.language-}

Comme d'habitude, les tests étaient donnés dans l'énoncé :

```python
def test_découvre():
    assert ".rr..r" == découvre("......", "r", [1, 2, 5])
    assert "erreur" == découvre("erre.r", "u", [4])
    assert "erre.r" == découvre("erre.r", "u", [])

```

### fonction `découvre(mot_caché, lettre, positions)`{.language-}

La fonction que j'attendais est :

```python
def découvre(mot_caché, lettre, positions):
    mot = ""

    for i in range(len(mot_caché)):
        if i in positions:
            mot += lettre
        else:
            mot += mot_caché[i]

    return mot
```

Sa complexité est en $\mathcal{O}(n\cdot m)$ avec $n$ et $m$ les longueurs de la chaîne `mot_caché`{.language-} et de la liste `positions`{.language-} respectivement (pourquoi ?).

En utilisant les caractéristiques de la liste `positions`{.language-} trié par ordre croissant, on aurait pu forger la fonction ci-dessous de complexité $\mathcal{O}(n)$ (pourquoi est-ce que ça marche ?):

```python
def découvre(mot_caché, lettre, positions):
    mot = ""

    if len(positions) == 0:
        return mot_caché

    pos = 0
    for i in range(len(mot_caché)):
        if i == positions[pos]:
            mot += lettre
            pos = min(pos + 1, len(positions) - 1)
        else:
            mot += mot_caché[i]

    return mot

```

## Corrigé de la question 4. Fonction `caché(mot)`{.language-}

Comme toujours, les tests vous étaient donnés dans l'énoncé :

```python
def test_caché():
    assert "" == caché("")
    assert "........................." == caché("anticonstitutionnellement")
```

En utilisant la multiplications des chaînes de caractères, la fonction est triviale :

```python
def caché(mot):
    return "." * len(mot)
```

## Corrigé de la question 5. Programme principal

Une proposition de programme principal :

```python
    mot_à_trouver = "table"
    mot_caché = caché(mot_à_trouver)

    print("mot à trouver :", mot_caché)
    nombre_essai = 0

    while est_une_lettre(".", mot_caché):
        lettre = input("Donnez une lettre : ")
        mot_caché = découvre(mot_caché, lettre, caractères(lettre, mot_à_trouver))
        print("mot à trouver :", mot_caché)

        nombre_essai += 1

    print("Victoire !, vous avez gagné en", nombre_essai, "essais.")
```

## Fichiers finaux

### `pendu.py`{.fichier}

```python#
def est_une_lettre(lettre, mot):
    return lettre in mot


def caractères(lettre, mot):
    position = []

    for i in range(len(mot)):
        if mot[i] == lettre:
            position.append(i)

    return position


def découvre(mot_caché, lettre, positions):
    mot = ""

    for i in range(len(mot_caché)):
        if i in positions:
            mot += lettre
        else:
            mot += mot_caché[i]

    return mot


def caché(mot):
    return "." * len(mot)

```

### `test_pendu.py`{.fichier}

```python#
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

### `main.py`{.fichier}

```python#
from pendu import caché, est_une_lettre, découvre, caractères


mot_à_trouver = "table"
mot_caché = caché(mot_à_trouver)


print("mot à trouver :", mot_caché)
nombre_essai = 0

while est_une_lettre(".", mot_caché):
    lettre = input("Donnez une lettre : ")
    mot_caché = découvre(mot_caché, lettre, caractères(lettre, mot_à_trouver))
    print("mot à trouver :", mot_caché)

    nombre_essai += 1

print("Victoire !, vous avez gagné en", nombre_essai, "essais.")

```
