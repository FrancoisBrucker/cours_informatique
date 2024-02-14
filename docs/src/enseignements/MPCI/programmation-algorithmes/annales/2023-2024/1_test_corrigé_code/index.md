---
layout: layout/post.njk

title:  "Corrigé Test 1 : code"
authors:
    - François Brucker
---

## Barème

Une note sur 4 répartie comme suit :

- 1 point de note de style répartit en :
  - 1/4 point si trois fichiers utilisés : `main.py`{.language-} pour le programme principal, `fonctions.py`{.language-} pour le code des fonctions utilisées dans le programme principal et `test_fonctions.py`{.language-} pour les tests des fonctions de `fonctions.py`{.language-}
  - 1/4 point pour le choix de noms de variables explicites
  - 1/4 point si les tests passent et/ou sont cohérent avec le code
  - 1/4 point si black a été utilisé pour que le code soit agréable à lire
- 1 point pour la question 1 répartit en :
  - 1/3 point pour la gestion du `while`{.language-}
  - 1/3 point pour l'utilisation de la fonction `find`{.language-} ou du recodage de sa fonctionnalité
  - 1/3 point pour le reste (`input`{.language-}, ...)
- 1 point pour la question 2 répartit en :
  - 1/3 point pour le code de la fonction
  - 1/3 point pour les tests de la fonction
  - 1/3 point pour l'utilisation de la fonction dans le programme principal (ou à minima la fonctionnalité utilisée)
- 1 point pour la question 3 répartit en :
  - 1/3 point pour le code de la fonction
  - 1/3 point pour les tests de la fonction
  - 1/3 point pour l'utilisation de la fonction dans le programme principal (ou à minima la fonctionnalité utilisée)

La question 4 n'a été abordée par personne.

La note sur $20$ finale est obtenue en multipliant la note sur 4 par $5$

{% note "**Objectif du test**" %}

En 15 minutes :

- **un élève *normal*** doit parvenir à faire la première question sans le `while`{.language-} et le code/test de la deuxième question. Ce qui lui permet d'avoir 2.333333 points sur 4, soit 11.66666/20
- **un bon élève** doit parvenir à réussir les 2 premières questions. Ce qui lui permet d'avoir 3/4 et donc 15/20
- **un très bon élève** fait plus que les 2 premières questions.

{% endnote %}

La ventilation des notes est :

|note/4   | ≤1 | ]1, 1.5]   | ]1.5, 2]   | ]2, 2.25]    | ]2.25, 2.5] | ]2.5,2.75]  | ]2.75, 3] | ]3, 3.5]     | >3.5|
|note/20  |≤4.2| [5.2, 6.7] | [8.3, 10]  | [10.4, 11.3] | [11.7, 12.5]| [12.9, 13.8]| [14.2, 15]| [15.4, 17.1] | 18.3|
|---------|----|------------|------------|--------------|-------------|-------------|-----------|--------------|-----|
|nombre   | 4  |  3         |  8         |  6           |  9          | 6           | 4         |  4           |  1  |
|rang min | 42 | 39         | 31         | 25           | 16          | 10          | 6         |  2           |  1  |
| # <     |  0 |  4         |  7         | 15           | 21          | 30          | 36        | 40           |  44 |

- moyenne : 11.1/20 (2.22/4)
- écart-type : 3.57/20 (0.71/4)
- médiane : 11.67/20 (2.33/4)

Je suis globalement content de vous, vous avez globalement tous travaillé pour le test et la plupart des notes en dessous de 10 sont dues à un manque d'expérience. Quelques notes sont cependant préoccupantes et il faudra vraiment travailler sa production de code et comprendre comment tout ceci fonctionne ensemble.

## Erreurs fréquemment rencontrées

Je n'ai pas vraiment eu d'erreurs surprenantes. Ce sont des erreurs de débutant et elles sont de deux types :

- une mauvaise compréhension des mécanismes : ça se travaille et vient avec l'expérience
- croire que l'on peut produire du code de qualité et qui marche sans l'exécuter : l'humilité s'apprend aussi avec l'expérience

### Recoder des fonctions

La majorité d'entre vous n'avez pas lu la documentation de la méthode `find`. Du coup vous l'avez recodé, le plus souvent avec des erreurs...

Vous ne perdez pas de temps à comprendre et lire de la documentation. Votre code sera plus clair, plus facile à utiliser et avec moins de bug si vous utilisez les fonctions et méthodes que python met à votre disposition. Apprendre à lire de la documentation vous fera gagner un temps fou !

{% note %}
Pour lire une documentation, en particulier savoir quels sont les paramètres d'une fonction lisez [cette partie du cours](/cours/coder-et-développer/bases-python/fonctions-méthodes/#paramètres).
{% endnote %}

Enfin, on utilise les fonctions testées dans le programme principal. On vous demande de coder des fonctions (et de les tester), ce n'est pas pour rien... Utilisez les !

### Ne pas exécuter son code

De nombreuses erreurs auraient pu être évitées si vous aviez exécuté votre code : programme principal et surtout tests ! L'interpréteur et surtout `pytest` sont meilleurs que l'esprit humain pour voir rapidement les erreurs : cela plante ou rend un résultat incohérent.

Pour que cela fonctionne, il faut faire en sorte de **toujours** pouvoir exécuter votre code :

- écrire **une** ligne du programme principal puis l'exécuter
- écrire **une** fonction puis son test à la fois puis exécuter les tests.

Loin de vous ralentir cela vous fera repérer et corriger rapidement les erreurs. Entraînez vous et vous verrez.

### Ne pas utiliser black pour écrire du code agréable à lire

Cette erreur est inexcusable. Black est accessible à partir d'un raccourci clavier et fonctionne parfaitement. Cela rendra votre code plus lisible pour vous et pour le correcteur.

### Utiliser le typage des fonctions

Préférez définir vos fonctions sans le typage :

- on préfèrera écrire ça : `def donne_prochain_indice(chaine, indice):`{.language-} puis le reste de la définition de la fonction
- à ça : `def donne_prochain_indice(chaine: str, indice: int) -> int:`{.language-} qui est plus lourd et n'apporte pas grand chose à la lisibilité.

Le typage a bien sur son utilité dans la documentation ou lorsque l'on veut définir précisément les paramètres (pour un test par exemple), mais dans le code où la fonction va être utilisée tout de suite après c'est inutile et rend la définition plus dure à lire.

### Erreurs rares

Mais qu'il faut tout de suite arrêter de faire :

- pas de `from fonctions import *` dans le programme principal car on ne sait pas ce qu'on importe
- les commentaires ne se font pas avec `""" ..."""`. Les commentaires en python s'écrivent avec `#`. Si l'on veut commenter plusieurs lignes à la fois vscode a une commande pour cela : `menu édition > afficher/masquer le commentaire de ligne`. On l'utilise tellement souvent qu'il y a souvent un raccourci clavier en plus.

## Corrigé

### Question 1

Fichier `main.py`{.fichier} :

```python
chaine_entrée = ""

while chaine_entrée != "sortie":
    chaine_entrée = input("Entre une chaine de caractères : ")
    caractère_entrée = input("Entre un caractère : ")

    index_caractère = chaine_entrée.find(caractère_entrée)
    print("Premier index du caractère :", index_caractère)
```

### Question 2

#### `fonctions.py`{.fichier}

```python
def donne_prochain_indice(chaine, indice):
    possible_suivant = chaine.find(chaine[indice], indice + 1)

    if possible_suivant > -1:
        return possible_suivant
    return None

```

#### `test_fonctions.py`{.fichier}

```python
from fonctions import donne_prochain_indice


def test_donne_prochain_indice():
    assert donne_prochain_indice("bxaaxaaaxax", 4) == 8
    assert donne_prochain_indice("bxaaxaaaxax", 0) == None
```

#### `main.py`{.fichier}

On ajoute à la fin du fichier `main.py`{.fichier} les lignes suivantes, dans le bloc `while`{.language-} :

```python
    if index_caractère == -1:
        print("Il n'apparait pas")
    elif donne_prochain_indice(chaine_entrée, index_caractère) != None:
        print("Il apparait plusieurs fois")
    else:
        print("Il apparait une fois")
```

### Question 3

#### `fonctions.py`{.fichier}

```python
def compte_caractère(chaine, indice):
    compte = 0

    while indice != None:
        compte += 1
        indice = donne_prochain_indice(chaine, indice)

    return compte
```

#### `test_fonctions.py`{.fichier}

```python
from fonctions import compte_caractère 


def test_compte_caractère():
    assert compte_caractère("bxaaxaaaxax", 0) == 1
    assert donne_prochain_indice("bxaaxaaaxax", 1) == 4
```

#### `main.py`{.fichier}

On ajoute à la fin du fichier `main.py`{.fichier} les lignes suivantes, dans le bloc `while`{.language-} :

```python
    if index_caractère > -1:
        print("caractère apparait", compte_caractère(chaine_entrée, index_caractère), "fois.")
```

### Question 4

#### `fonctions.py`{.fichier}

```python
def donne_max_doublon(chaine):
    nombre_max = 0

    for i in range(len(chaine)):
        nombre_max = max(nombre_max, compte_caractère(chaine, i))

    return nombre_max
```

#### `test_fonctions.py`{.fichier}

```python
from fonctions import donne_max_doublon


def test_donne_max_doublon():
    assert donne_max_doublon("bxaaxaaaxax") == 6
```

#### `main.py`{.fichier}

On ajoute à la fin du fichier `main.py`{.fichier} les lignes suivantes, dans le bloc `while`{.language-} :

```python
    if index_caractère > -1:
        if index_caractère == donne_max_doublon(chaine_entrée):
            print("c'est le max !")
```

### Fichiers complets

#### `fonctions.py`{.fichier}

```python
def donne_prochain_indice(chaine, indice):
    possible_suivant = chaine.find(chaine[indice], indice + 1)

    if possible_suivant > -1:
        return possible_suivant
    return None


def compte_caractère(chaine, indice):
    compte = 0

    while indice != None:
        compte += 1
        indice = donne_prochain_indice(chaine, indice)

    return compte


def donne_max_doublon(chaine):
    nombre_max = 0

    for i in range(len(chaine)):
        nombre_max = max(nombre_max, compte_caractère(chaine, i))

    return nombre_max

```

#### `test_fonctions.py`{.fichier}

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

#### `main.py`{.fichier}

```python
from fonctions import donne_prochain_indice, compte_caractère, donne_max_doublon

chaine_entrée = ""

while chaine_entrée != "sortie":
    chaine_entrée = input("Entre une chaine de caractères : ")
    caractère_entrée = input("Entre un caractère : ")

    index_caractère = chaine_entrée.find(caractère_entrée)
    print("Premier index du caractère :", index_caractère)

    if index_caractère == -1:
        print("Il n'apparait pas")
    elif donne_prochain_indice(chaine_entrée, index_caractère) != None:
        print("Il apparait plusieurs fois")
    else:
        print("Il apparait une fois")

    if index_caractère > -1:
        print("caractère apparait", compte_caractère(chaine_entrée, index_caractère), "fois.")

        if index_caractère == donne_max_doublon(chaine_entrée):
            print("c'est le max !")

```
