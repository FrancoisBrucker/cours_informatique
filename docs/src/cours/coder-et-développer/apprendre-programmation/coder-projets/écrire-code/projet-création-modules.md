---
layout: layout/post.njk

title: "Projet : création de modules"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Pour ce projet, on va suivre [les consignes du tutoriel vscode et python](../../outils/éditeur-vscode/python/){.interne} :

1. vous avez créé un projet avec vscode
2. tous les fichiers que vous créez sont dans le dossier du projet
3. vous exécutez le code en utilisant le triangle vert

Ces consignes précédentes assurent que **vous exécutez votre code python à partir du dossier contenant votre projet**.

{% info %}
On va reprendre les différents [exercices de code](../../../concepts/projet-codes/){.interne} pour les transformer en un projet python exécutable avec vscode.
{% endinfo %}

## <span id="syracuse"></span>Syracuse

{% faire %}

1. Commencez par créer le dossier `syracuse`{.fichier} dans un explorateur de fichier
2. dans vscode, choisissez : "_fichier > ouvrir le dossier..._" puis naviguez jusqu'à votre dossier `syracuse`{.fichier}. On vous demande si vous faites confiances aux auteurs, puisque c'est vous dites oui.
3. créez un fichier `main.py`{.fichier} contenant uniquement la ligne `print("bonjour")`{.language-}

Exécutez le fichier main avec vscode et le terminal pour vérifier que tout fonctionne.
{% endfaire %}
{% faire %}
Supprimez le contenu du fichier `main.py`{.fichier} (mais pas le fichier en lui-même) qui n'était là que pour un test de fonctionnement.
{% endfaire %}

Tout est prêt pour coder :

{% exercice %}
Reprenez [l'exercice syracuse du projet de code](../../../concepts/projet-codes/#syracuse){.interne} et faites en sorte que :

- le fichier `main.py`{.fichier}  contienne uniquement la partie exécution du programme,
- le fichier `syracuse.py`{.fichier} contienne les diverses fonctions (un fichier à tout à fait le droit de s'appeler comme le répertoire qui le contient)

{% endexercice %}
{% details "corrigé" %}
Fichier `syracuse.py`{.fichier} :

```python
def syracuse(x):
    if x % 2 == 0:
        return x / 2
    else:
        return 3 * x + 1


def suite(u_0):
    sortie = [u_0]

    u_n = u_0
    while u_n != 1:
        u_n = syracuse(u_n)
        sortie.append(u_n)

    return sortie

```

Fichier `main.py`{.fichier} :

```python
from syracuse import suite

sortie_utilisateur = input("Donnez un entier : ")

u_0 = int(sortie_utilisateur)

print("suite de Syracuse associée : ", suite(u_0))

```

{% enddetails %}

## <span id="pendu"></span>Pendu

{% faire %}

1. Commencez par créer le dossier `jeu_du_pendu`{.fichier} dans un explorateur de fichier
2. dans vscode, choisissez : "_fichier > ouvrir le dossier..._" puis naviguez jusqu'à votre dossier `jeu_du_pendu/`{.fichier}. On vous demande si vous faites confiances aux auteurs, puisque c'est vous dites oui.
3. créez un fichier `main.py`{.fichier} contenant uniquement la ligne `print("bonjour")`{.language-}

Exécutez le fichier main avec vscode et le terminal pour vérifier que tout fonctionne.
{% endfaire %}
{% faire %}
Supprimez le contenu du fichier `main.py`{.fichier} (mais pas le fichier en lui-même) qui n'était là que pour un test de fonctionnement.
{% endfaire %}

Tout est prêt pour coder :

{% exercice %}
Reprenez [l'exercice du jeu du pendu du projet de code](../../../concepts/projet-codes/#pendu){.interne} et faites en sorte que :

- le fichier `main.py`{.fichier}  contienne uniquement la partie exécution du programme,
- le fichier `pendu.py`{.fichier} contienne les diverses fonctions.

{% endexercice %}

{% details "corrigé" %}
Fichier `pendu.py`{.fichier} :

```python
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

Fichier `main.py`{.fichier} :

```python
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

{% enddetails %}

## <span id="compte-caractère"></span>Le compte est bon

{% faire %}

1. Commencez par créer le dossier `compte_caractère`{.fichier} dans un explorateur de fichier
2. dans vscode, choisissez : "_fichier > ouvrir le dossier..._" puis naviguez jusqu'à votre dossier `compte_caractère/`{.fichier}. On vous demande si vous faites confiances aux auteurs, puisque c'est vous dites oui.
3. créez un fichier `main.py`{.fichier} contenant uniquement la ligne `print("bonjour")`{.language-}

Exécutez le fichier main avec vscode et le terminal pour vérifier que tout fonctionne.
{% endfaire %}
{% faire %}
Supprimez le contenu du fichier `main.py`{.fichier} (mais pas le fichier en lui-même) qui n'était là que pour un test de fonctionnement.
{% endfaire %}

Tout est prêt pour coder :

{% exercice %}
Reprenez [l'exercice du jeu du compte du projet de code](../../../concepts/projet-codes/#compte-caractère){.interne} et faites en sorte que :

- le fichier `main.py`{.fichier}  contienne uniquement la partie exécution du programme,
- le fichier `fonctions.py`{.fichier} contienne les diverses fonctions.

{% endexercice %}

{% details "corrigé" %}
Fichier `fonctions.py`{.fichier} :

```python
def donne_prochain_indice(chaîne, indice):
    possible_suivant = chaîne.find(chaîne[indice], indice + 1)

    if possible_suivant > -1:
        return possible_suivant
    return None


def compte_caractère(chaîne, indice):
    compte = 0

    while indice != None:
        compte += 1
        indice = donne_prochain_indice(chaîne, indice)

    return compte


def donne_max_doublon(chaîne):
    nombre_max = 0
    caractère_max = ""

    for i in range(len(chaîne)):
        compte_i = compte_caractère(chaîne, i)
        if compte_i > nombre_max:
            nombre_max = compte_i
            caractère_max = chaîne[i]

    return caractère_max

```

Fichier `main.py`{.fichier} :

```python
from fonctions import donne_prochain_indice, compte_caractère, donne_max_doublon

chaîne_entrée = ""

while chaîne_entrée != "sortie":
    chaîne_entrée = input("Entre une chaîne de caractères : ")
    caractère_entrée = input("Entre un caractère : ")

    index_caractère = chaîne_entrée.find(caractère_entrée)
    print("Premier index du caractère :", index_caractère)

    if index_caractère == -1:
        print("Il n’apparaît pas")
    elif donne_prochain_indice(chaîne_entrée, index_caractère) != None:
        print("Il apparaît plusieurs fois")
    else:
        print("Il apparaît une fois")

    if index_caractère > -1:
        nombre = compte_caractère(chaîne_entrée, index_caractère)
        print("Le caractère apparaît", nombre, "fois.")

        if nombre == donne_max_doublon(chaîne_entrée):
            print("c'est le max !")

```

{% enddetails %}