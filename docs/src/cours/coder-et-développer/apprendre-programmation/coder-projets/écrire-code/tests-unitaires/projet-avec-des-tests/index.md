---
layout: layout/post.njk
title: "Un projet avec des tests"

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

Du point de vue de python un projet est un dossier qui va contenir les différents fichiers python. Appelons le `chiffre_cesar`{.fichier}.

{% attention2 "**À retenir**" %}
Dans la mesure du possible, le nom des dossiers et des fichiers d'un projet informatiques :
- ne doivent contenir que des lettres **non accentuées**
- ne doivent contenir **pas** contenir d'espaces. On sépare les mots par des _underscore_ `_`
{% endattention2 %}


Téléchargez le projet :

{% faire %}
1. Téléchargez le fichier [chiffre-cesar.zip](./chffre-cesar.zip){.interne} qui contient l'ensemble des fichiers du projet,
2. décompressez le fichier,
3. ouvrez le dossier dans vscode.
{% endfaire %}

## Le programme principal

Le programme principal est le fichier que l'on va exécuter, on a coutume de l'appeler `main.py`{.fichier}

{% attention2 "**À retenir**" %}
Un projet informatique va contenir de nombreux fichiers, mais un seul sera le programme principal, celui que l'on exécutera avec la commande `python main.py`.
{% endattention2 %}

Dans notre cas, notre programme est : 

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

Exécutez le projet :

{% faire %}
Ouvrez un terminal dans vscode, vous devriez être dans le dossier du projet : exécutez le programme en exécutant la commande `python main.py`.

{% endfaire %}

## Fichiers de fonctions

Les deux imports du programme principal correspondent aux fichiers `texte.py`{.fichier} et `chiffre.py`{.fichier} qui sont **dans le même dossier** que notre programme principal. Ces deux fichiers contiennent toutes les fonctions nécessaire à l'exécution du programme principal.

{% attention2 "**À retenir**" %}
Pour que l'import dans le fichier `main.py`{.fichier} se passe sans soucis, tous les fichiers de fonctions doivent se trouver dans le dossier du projet.
{% endattention2 %}

Chaque fichier va contenir un ensemble de fonctions de buts similaires.

### Fonctions texte

Fichier `texte.py`{.fichier} :

```python
import unicodedata


def conversion(texte_avec_accent):
    liste_glyphes_unicode = list(unicodedata.normalize("NFKD", texte_avec_accent))

    liste_caractères = []
    for c in liste_glyphes_unicode:
        if not unicodedata.combining(c):
            liste_caractères.append(c)
    
    chaîne_sans_accent = "".join(liste_caractères)
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

{% attention2 "**À retenir**" %}
Pour que l'import dans les fichiers de tests se passent sans soucis, tous les fichiers de tests doivent se trouver dans le dossier du projet.
{% endattention2 %}

On exécute nos tests dans un terminal dont le dossier courant est le dossier du projet :

```shell
python -m pytest
============================= test session starts ==============================
platform darwin -- Python 3.14.2, pytest-9.0.1, pluggy-1.6.0
rootdir: ./chffre-cesar
collected 8 items                                                              

test_chiffre.py .....                                                    [ 62%]
test_texte.py ...                                                        [100%]

============================== 8 passed in 0.04s ===============================
```

Ouf, tout est ok.

{% attention2 "**À retenir**" %}
Prenez l'habitude de tester vos fichier en utilisant le terminal.
{% endattention2 %}

Exécutons les tests du projet :

{% faire %}
Ouvrez un terminal dans vscode, vous devriez être dans le dossier du projet : exécutez les tests en exécutant la commande `python -m pytest`.

{% endfaire %}

Ce que l'on teste est dépendant de chaque développeur : si les tests passent il doit être convaincu que son code est fonctionnel.

{% attention2 "**À retenir**" %}
C'est au développeur des fonctions de créer des tests pour elles de tel sorte que s'ils passent il soit persuadé que son code est sans bug (si un bug est découvert plus tard, il suffit de rajouter un test qui le montre puis corriger le code).
{% endattention2 %}


### Tests des fonctions de texte

Fichier `test_texte.py`{.fichier} :

```python
from texte import conversion


def test_conversion_minuscules_vers_majuscule():
    assert "ABCDE" == conversion("abcde")


def test_conversion_avec_espaces():
    assert "AB CD" == conversion("ab cd")


def test_conversion_avec_accents():
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