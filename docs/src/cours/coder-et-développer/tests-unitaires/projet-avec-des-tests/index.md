---
layout: layout/post.njk
title: "Un programme avec des tests"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un projet informatique va toujours avoir 3 types de fichiers :

- le fichier à exécuter pour lancer notre programme, couramment appelé `main.py`{.fichier}. Ce fichier doit uniquement contenir des interaction avec l'utilisateur.
- Toutes les fonctions internes au programme, sont regroupées dans un fichier (ou un ensemble de fichiers)
- Tous les tests des fonctions internes au programme, sont regroupées dans un fichier (ou un ensemble de fichiers)


Par exemple, considérons un programme qui va chiffrer un message selon [le code de césar](https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage).


## Le projet

On commence par créer un dossier qui va contenir notre projet. Appelons le `chiffre_cesar`{.fichier}.

{% attention "**À retenir**" %}
Dans la mesure du possible, le nom des dossiers et des fichiers d'un projet informatiques :
- ne doivent contenir que des lettres **non accentuées**
- ne doivent contenir **pas** contenir d'espaces. On sépare les mots par des _underscore_ `_`
{% endattention %}

## Le programme principal

Le programme principal est le fichier que l'on va exécuter, on a coutume de l'appeler `main.py`{.fichier}

{% attention "**À retenir**" %}
Un projet informatique va contenir de nombreux fichiers, mais un seul sera le programme principal, celui que l'on exécutera avec la commande `python main.py`.
{% endattention %}

Dans notre cas, notre programme sera : 

fichier `main.py`{.fichier} :

```python
import texte
from chiffre import césar_chiffre, césar_déchiffre

entrée = input("Tapez une chaîne de caractères en français : ")
texte = texte.conversion(entrée)


clé = input("Tapez une lettre de l'alphabet (clé de chiffrement) : ")
chiffre = césar_chiffre(texte, clé)
déchiffre = césar_déchiffre(chiffre, clé)

print("Texte initial   :", texte)
print("Texte chiffré   :", chiffre)
print("Texte déchiffré :", déchiffre)

```

On voit que ce fichier demande des choses à un utilisateur et utilise deux importations (`texte`{.language-} et `chiffre`{.language-}) qui correspondent à nos fichiers de fonctions.

Pour exécuter le fichier, on utilise le terminal dans le dossier du projet :

```shell
$> python main.py
Tapez une chaîne de caractères en français : Éléonore m'adore !           
Tapez une lettre de l'alphabet (clé de chiffrement) : F
Texte initial   : ELEONORE M'ADORE !
Texte chiffré   : JQJTSTWJ R'FITWJ !
Texte déchiffré : ELEONORE M'ADORE !

```

## Fichiers de fonctions

Les deux imports correspondent aux fichiers `texte.py`{.fichier} et `chiffre.py`{.fichier} qui sont **dans le même dossier** que notre programme principal.

Chaque fichier va contenir un ensemble de fonctions de buts similaires.

{% attention "**À retenir**" %}
Pour que l'import dans le fichier `main.py`{.fichier} se passe sans soucis, tous les fichiers de fonctions doivent se trouver dans le dossier du projet.
{% endattention %}


### Fonctions texte

Fichier `texte.py`{.fichier} :

```python
import unicodedata

def conversion(texte_avec_accent):
    liste_caractères_unicode = list(unicodedata.normalize('NFKD', texte_avec_accent))
    
    liste_caractères_simple = []
    for c in liste_caractères_unicode:
        if not unicodedata.combining(c):
            liste_caractères_simple.append(c)
        
    chaîne_sans_accent = ''.join(liste_caractères_simple)
    texte_en_majuscule = chaîne_sans_accent.upper()
    
    return texte_en_majuscule

```

Ce fichier continent une unique fonction dont le but est de convertir un texte écrit en français dans le même texte en majuscule et sans accents.


On voit que ce fichier dépend d'un module python nommé [unicodedata](https://docs.python.org/3/library/unicodedata.html), qui permet de gérer les chaînes de caractères Unicode. Essayez de comprendre comment fonctionne la fonction `conversion`{.language-}.

### Fonctions chiffre

Fichier `texte.py`{.fichier} :

```python
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def césar_chiffre(texte, cle):

    décalage = ALPHABET.index(cle)
    texteCesar = ""
    for x in texte:
        if x in ALPHABET:
            texteCesar += ALPHABET[(ALPHABET.index(x) + décalage) % 26]
        else:
            texteCesar += x

    return texteCesar


def césar_déchiffre(texte, cle):

    décalage = ALPHABET.index(cle)
    texteCesar = ""
    for x in texte:
        if x in ALPHABET:
            texteCesar += ALPHABET[(ALPHABET.index(x) - décalage) % 26]
        else:
            texteCesar += x

    return texteCesar

```

Les deux fonctions du fichiers `chiffre.py`{.fichier} sont là pour chiffrer et déchiffrer un message selon le code de César.

## Fichiers de tests

L'usage veut que l'on utilise un fichier de test par fichier de fonctions.

Pour que pytest puisse comprendre que ce sont des fichiers de textes, on fait commencer les noms de fichiers par `test_`{.fichier}

{% attention "**À retenir**" %}
Pour que l'import dans les fichiers de tests se passent sans soucis, tous les fichiers de tests doivent se trouver dans le dossier du projet.
{% endattention %}

### Tests des fonctions de texte

Fichier `test_texte.py`{.fichier} :

```python
from texte import conversion

def test_conversion():
    assert "ABC DE" == conversion("ÀBÇ dè")

```

### Tests des fonctions de chiffre

Fichier `test_chiffre.py`{.fichier} :

```python
from chiffre import césar_chiffre, césar_déchiffre

def test_césar_chiffre():
    assert "A B" == césar_chiffre("A B", "A")
    assert "D F" == césar_chiffre("B D", "C")
    assert "Z A" == césar_chiffre("A B", "Z")


def test_césar_déchiffre():
    assert "A B" == césar_déchiffre("A B", "A")
    assert "B D" == césar_déchiffre("D F", "C")
    assert "A B" == césar_déchiffre("Z A", "Z")

```

### Exécution des tests

On exécute nos tests dans le terminal :

```shell
python -m pytest
========================================== test session starts ===========================================
platform darwin -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0
rootdir: ./chiffre-césar
collected 3 items                                                                                        

test_chiffre.py ..                                                                                 [ 66%]
test_texte.py .                                                                                    [100%]

=========================================== 3 passed in 0.00s ============================================
```

Ouf, tout est ok.

{% attention "**À retenir**" %}
Prenez l'habitude de tester vos fichier en utilisant le terminal.
{% endattention %}

## Liste des fichiers du projet

Le projet final contient 5 fichiers :

- `chiffre.py`{.fichier}
- `main.py`{.fichier}
- `test_chiffre.py`{.fichier}
- `test_texte.py`{.fichier}
- `texte.py`{.fichier}

Qui se séparent en :

- un programme principal,
- deux fichiers de fonctions,
- deux fichiers de tests, un par fichier de fonctions.

{% info %}
Si vous regardez les fichiers du dossier du projet, vous vous rendrez compte qu'un dossier `__pycache__`{.fichier} a été ajouté. Il a éte créé par l'interpréteur lors de l'exécution du programme principal. Il ne fait pas parie du projet et sera recréé par l'interpréteur si vous le supprimez.
{% endinfo %}