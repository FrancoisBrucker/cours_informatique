---
layout: layout/post.njk

title:  "Corrigé Test 1 : code"
authors:
    - François Brucker
---


## Barème

La note est sur 5.

1. code + test
2. code + test
3. code + test
4. code + test
5. code

La ventilation des notes est :

|note  | 0.5  | 1   | 1.5 | 2   | 2.5 | 3 | 3.5 | 4 | 5 | 6 |
-------|------|-----|-----|-----|-----|---|-----|---|---|---|
|nombre|      |     |     |     |     |   |     |   |   |   |
|rang  |      |     |     |     |     |   |     |   |   |   |

## Erreurs fréquemment rencontrées

{% attention %}
Beaucoup sont venus sans réel préparation au test. Cela se ressent avec les notes ! Vous **devez** préparer chaque test pour obtenir une note correct. Il y a des annales et le sujet du test vous est donné.
{% endattention %}

### Trop lent

Vous prenez bien trop de temps à écrire des algorithmes simples ! La première question est une application directe du cours et la seconde ne devrait pas vous prendre plus de 5min. Presque tout le monde aurait du arriver à la question 3, ce qui est loin d'être le cas.

### Les tests

Les tests **doivent** être fait comme dans le [projet pourcentage]({{ "/cours/algorithme-code-théorie/code/projet-pourcentage" | url }}) ! Il faut donc :

* un fichier de test séparé du code
* pourvoir l'exécuter avec pytest
* afficher un résultat à l'écran n'est **pas** un test.

En plus, les tests vous étaient donné dans l'énoncé sous la forme des exemples, il vous suffisait de les reprendre.

Chaque test **doit** commencer par `test_`{.language-} suivi du nom de la fonction à test. S'il y a plusieurs tests pur une même fonction, on ajoute ce que le test teste. Ici, une seule fonction de test pour chaque fonction suffisait.

### Nom des fichiers

Il vous faut a priori 2 fichiers :

* un pour le code, que vous pouvez appeler `pendu.py`{.fichier}, ou `code.py`{.fichier}
* un pour tester le code qui s'appelle comme le nom du fichier de code précédé de `test_`{.fichier}. Donc `test_pendu.py`{.fichier} ou `test_code.py`{.fichier} selon le nom de votre fichier de code.

### Listes

On préfère `L.append(i)`{.language-} à `L = L + [i]`{.language-} car `append` est en $\mathcal{O}(1)$ opérations alors `+`crée une nouvelle liste et est donc en $\mathcal{O}(n)$ où $n$ est la taille de la liste.

### Comparaison de booléens

`assert est_une_lettre("i", "victoire") == True` est équivalent à ``assert est_une_lettre("i", "victoire")` puisque une comparaison avec `==` rend `True` ou `False`. Préférez donc la deuxième écriture plus compacte et moins redondante.

De même pour l'idiome :

```
Si f() == Vrai alors:
    return Vrai
sinon:
    return Faux
```

Qui s'écrit avantageusement :

```
return Vrai
```

## 1. fonction `est_une_lettre(lettre, mot)`{.language-}

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

## 2. fonction `caractères(lettre, mot)`{.language-}

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

## 3. fonction `découvre(mot_caché, lettre, positions)`{.language-}

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

## 4. fonction `caché(mot)`{.language-}

> TBD : fct + test

## 5. programme principal
