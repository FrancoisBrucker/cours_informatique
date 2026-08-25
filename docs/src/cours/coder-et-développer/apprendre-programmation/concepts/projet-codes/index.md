---
layout: layout/post.njk

title: "On s'entraîne à coder de petits projets"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Quelques exercices pour se mettre le code dans les pattes. Pour chacun des projets vous ferez 2 fichiers :

- le programme principal de nom `main.py`{.language-} qui sera exécuté
- le fichier contenant les différentes fonctions appelées dans le programme principal. Son nom doit être en relation avec son contenu.

Chaque sujet contient son corrigé, mais faites dans l'ordre :

{% faire "**Pour chaque sujet**" %}

1. faites tous les exercices
2. regardez les erreurs courantes et corriger si besoin votre projet
3. comparez votre code au corrigé

{% endfaire %}

## <span id="syracuse"></span>Syracuse

On essaye d'écrire un programme qui teste la [conjecture de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) pour des entiers.

### Questions

{% exercice %}
Écrivez une fonction `syracuse`{.language-} telle que :

- **entrée** : un entier $x$
- **sortie** :
  - $x/2$ si $x$ est pair
  - $3x + 1$ si $x$ est impair

{% endexercice %}
{% info %}
En utilisant le fait que le modulo s'écrit `%`{.language-} en python.
{% endinfo %}
{% details "corrigé" %}

```python
def syracuse(x):
    if x % 2 == 0:
        return x / 2
    else:
        return 3 * x + 1

```
{% enddetails %}
{% exercice %}
Vérifiez que le code fonctionne en demandant à l'utilisateur de taper un nombre et rend la suite de Syracuse de ce nombre.

- vous supposerez que l'utilisateur ne se trompe pas (pas besoin de gérer ses erreurs potentielles)
- vous utiliserez [la fonction `input()`{.language-}](https://docs.python.org/fr/3.13/library/functions.html#input) qui rend une chaîne de caractères tapée par l'utilisateur
- `int(x)`{.language-} est l'entier représenté par la chaîne de caractère `x`{.language-}.

{% endexercice %}
{% details "corrigé" %}

```python
def syracuse(x):
    if x % 2 == 0:
        return x / 2
    else:
        return 3 * x + 1


sortie_utilisateur = input("Donnez un entier : ")
n = int(sortie_utilisateur)

print("suite de Syracuse associée : ", syracuse(n))

```
{% enddetails %}

{% exercice %}
Écrivez une fonction qui rend tous les éléments de la suite de Syracuse associée à un nombre

- **entrée** : un entier $x$
- **sortie** : les élément de la suite de Syracuse associée à $x$

La suite de Syracuse est définie telle que :

- $u_0 =x$
- $u_{n+1} = \mbox{syracuse}(u_n)$
- on s'arrête lorsque $u_n =1$
{% endexercice %}
{% details "corrigé" %}

```python
def suite(u_0):
    sortie = [u_0]

    u_n = u_0
    while u_n != 1:
        u_n = syracuse(u_n)
        sortie.append(u_n)

    return sortie

```


{% enddetails %}

{% exercice %}
Écrivez le programme qui demande à l'utilisateur de taper un nombre et rend la suite de Syracuse de ce nombre.

- vous supposerez que l'utilisateur ne se trompe pas (pas besoin de gérer ses erreurs potentielles)
- vous utiliserez [la fonction `input()`{.language-}](https://docs.python.org/fr/3.13/library/functions.html#input) qui rend une chaîne de caractères tapée par l'utilisateur
- `int(x)`{.language-} est l'entier représenté par la chaîne de caractère `x`{.language-}.

{% endexercice %}
{% details "corrigé" %}

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

print("suite de Syracuse associée : ", suite(int(input("Donnez un entier : ")))) 

```

Je me suis amusé pour traiter l'entrée faite par un utilisateur. Comprenez :

- pourquoi ça fonctionne,
- pourquoi on préfère ne pas faire comme ça dans de vrais programmes
 
{% enddetails %}

### Erreurs courantes à éviter

Après un input vous aurez **toujours** une chaîne de caractère. Il faut la convertir dans ce que va demander vos fonctions, ici des entiers.

Ne faites **PAS** de conversion de type dans vos fonctions. Si elles demandent des entrées entiers supposez que c'est le cas (par de `int(x) % 2` par exemple dans la fonction `syracuse`). Tôt ou tard ce genre chose va vous sauter à la figure car un jour vous votre programme va planter sans que vous compreniez pourquoi ni où est le soucis.

## <span id="pendu"></span>Jeu du pendu

On essaye d'écrire un programme qui joue au [jeu du pendu](https://fr.wikipedia.org/wiki/Pendu_(jeu)).

### Questions

{% exercice %}
Écrire la fonction `est_une_lettre(lettre, mot)`{.language-} telle que :

- **paramètres d'entrée** :
  1. `lettre`{.language-} un caractère
  2. `mot`{.language-} une chaîne de caractères
- **sortie** :
  - si au moins une des lettres de `mot`{.language-} et `lettre`{.language-}, la fonction rend `True`{.language-}
  - sinon, la fonction rend `False`{.language-}
- **exemples** :
  - `est_une_lettre("i", "victoire")`{.language-} doit rendre `True`{.language-}
  - `est_une_lettre("e", "la disparition")`{.language-} doit rendre `False`{.language-}

{% endexercice %}
{% details "corrigé" %}

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

{% enddetails %}
{% exercice %}
Écrire la fonction `caractères(lettre, mot)`{.language-} telle que :

- **paramètres d'entrée** :
  1. `lettre`{.language-} un caractère
  2. `mot`{.language-} une chaîne de caractères
- **sortie** :
  - une liste $L$ contenant tous les indices des caractères de `mot`{.language-} qui valent `lettre`{.language-}. Cette liste doit être triée par ordre croissant.
- **exemples** :
  - `caractères("i", "victoire")`{.language-} doit rendre `[1, 5]`{.language-}
  - `caractères("e", "la disparition")`{.language-} doit rendre `[]`{.language-}

{% endexercice %}
{% details "corrigé" %}

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


{% enddetails %}
{% exercice %}
Écrire la fonction `découvre(mot_caché, lettre, positions)`{.language-} telle que :

- **paramètres d'entrée** :
  1. `mot_caché`{.language-} une chaîne de caractères
  2. `lettre`{.language-} un caractère
  3. `positions`{.language-} une liste d'entiers rangés par ordre croissant
- **sortie** :
  - la chaîne de caractères `mot_caché`{.language-} où les indices correspondants aux entiers de `positions`{.language-} sont remplacés par `lettre`{.language-}
- **exemples** :
  - `découvre("......", "r", [1, 2, 5])`{.language-} doit rendre `".rr..r"`{.language-}
  - `découvre("erre.r", "u", [4])`{.language-} doit rendre `"erreur"`{.language-}
  - `découvre("erre.r", "u", [])`{.language-} doit rendre `"erre.r"`{.language-}

{% endexercice %}
{% details "corrigé" %}

La fonction que j'attends est :

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

{% enddetails %}
{% exercice %}
Écrire la fonction `caché(mot)`{.language-} telle que :

- **paramètres d'entrée** :
  1. `mot`{.language-} une chaîne de caractères
- **sortie** :
  - une chaîne de caractères composée uniquement de `"."`{.language-} et de longueur égale à celle de `mot`{.language-}
- **exemples** :
  - `caché("anticonstitutionnellement")`{.language-} doit rendre `"........................."`{.language-}
  - `caché("")`{.language-} doit rendre `""`{.language-}

{% endexercice %}
{% details "corrigé" %}

En utilisant la multiplications des chaînes de caractères, la fonction est triviale :

```python
def caché(mot):
    return "." * len(mot)
```

{% enddetails %}
{% exercice %}
Créez le programme permettant de jouer au pendu jusqu'à ce que le mot à trouver ne contienne plus de `"."`{.language-}
{% endexercice %}
{% details "corrigé" %}

Une proposition de programme principal :

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

### Erreurs courantes à éviter

#### Description d'une fonction

La description d'une fonction (entre `"""`{.language-}) est inutile. Le code **doit** se suffire à lui-même pour être lisible et compris. Si ce n'est pas le cas, c'est que vous avez mal codé !

La description de chaque fonction n'est utile que si vous faire une bibliothèque (une suite de fonctions qui devront être utilisées par d'autres sans qu'ils aient à connaître leurs codes). Ici, vous faite du code qui sera exécuté ou utilisé par vous et les autres membres de l'équipe de développement (ou le correcteur, ici moi) : la description ou les commentaires **doivent** être inutiles : faites du code lisible.

#### Listes

On préférera toujours utiliser `L.append(i)`{.language-} plutôt que `L = L + [i]`{.language-} car `append`{.language-} est une méthode en $\mathcal{O}(1)$ opérations alors `+` crée une nouvelle liste et est donc en $\mathcal{O}(n)$ où $n$ est la taille de la liste `L`{.language-}.

#### Comparaison de booléens

On ne teste pas si un booléen est vrai ou faux, on utilise directement sa valeur.

- On écrit : `assert est_une_lettre("i", "victoire")`{.language-}
- ~~On écrit pas `assert est_une_lettre("i", "victoire") == True`{.language-}~~

En effet, les deux formes sont équivalentes puisque une comparaison avec `==`{.language-} rend `True`{.language-} ou `False`{.language-} mais la seconde est plus compacte et moins redondante.

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

#### Variable différent d'une chaîne de caractère

Ne confondez pas la variable ou le paramètre d'une fonction `x`{.language-} avec une chaîne de caractères contenant le caractère x, notée `'x'`{.language-}.


## <span id="compte-caractère"></span>Le compte est bon

Le programme consiste à demander à l'utilisateur une chaîne de caractères et un caractère. On cherchera à savoir combien de fois apparaît le caractère dans la chaîne. On va créer le programme en ajoutant petit à petit des fonctionnalités au programme.

### Questions

{% exercice %}

Créer un programme permettant d'exécuter les 4 étapes de l'algorithme suivant :

1. Demander à l'utilisateur une chaîne de caractères que l'on nommera `chaîne_entrée`{.language-} (en utilisant [la fonction `input([prompt: str]) -> str`{.language-}](https://docs.python.org/fr/3/library/functions.html#input))
2. Demander à l'utilisateur un caractère que l'on nommera `caractère_entrée`{.language-} (vous ne ferez aucune vérification de type)
3. Afficher à l'écran le plus petit indice (ou -1) de `chaîne_entrée`{.language-} valant `caractère_entrée`{.language-} (vous pourrez utiliser [la méthode `find`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.find) des chaînes de caractères)
4. Retournez à l'étape 1. de cet algorithme à part si `chaîne_entrée`{.language-} valait `"sortie"`{.language-}


{% endexercice %}
{% details "corrigé" %}

Programme :

```python
chaîne_entrée = ""

while chaîne_entrée != "sortie":
    chaîne_entrée = input("Entre une chaîne de caractères : ")
    caractère_entrée = input("Entre un caractère : ")

    index_caractère = chaîne_entrée.find(caractère_entrée)
    print("Premier index du caractère :", index_caractère)
```

{% enddetails %}

On veut savoir si le caractère `caractère_entrée`{.language-} apparaît plusieurs fois dans la chaîne `chaîne_entrée`{.language-}. Comme on connaît déjà le premier indice où il apparaît, on cherche s'il apparaît aussi plus tard.

{% exercice %}

Créer la fonction `donne_prochain_indice(chaîne:str, indice:int) -> int`{.language-} qui rend :

- Le plus petit indice $j$ strictement plus grand que le paramètre `indice`{.language-} tel que `chaîne[j] == chaîne[indice]`{.language-},
- `None`{.language-} si cet indice n'existe pas.

{% endexercice %}
{% details "corrigé" %}

```python
def donne_prochain_indice(chaîne, indice):
    possible_suivant = chaîne.find(chaîne[indice], indice + 1)

    if possible_suivant > -1:
        return possible_suivant
    return None

```

{% enddetails %}
{% exercice %}
Dans l'étape 3. de l'algorithme du programme principal, **utilisez la fonction que vous venez de coder** pour ajouter un affichage qui indique si `caractère_entrée`{.language-} apparaît plusieurs fois dans `chaîne_entrée`{.language-} ou pas.
{% endexercice %}
{% info %}
L'étape 3. du programme principal sera alors constitué de deux actions :

- Afficher à l'écran le plus petit indice (ou -1) de `chaîne_entrée`{.language-} valant `caractère_entrée`{.language-} (vous pourrez utiliser [la méthode `find`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.find) des chaînes de caractères) (***question 1***)
- Afficher si `caractère_entrée`{.language-} est présent plus d'une fois dans `chaîne_entrée`{.language-} (***question 2***)
{% endinfo %}

{% details "corrigé" %}

On ajoute à la fin du programme les lignes suivantes, dans le bloc `while`{.language-} :

```python
while chaîne_entrée != "sortie":

    # ...

    if index_caractère == -1:
        print("Il n'apparaît pas")
    elif donne_prochain_indice(chaîne_entrée, index_caractère) != None:
        print("Il apparaît plusieurs fois")
    else:
        print("Il apparaît une fois")
```


{% enddetails %}

On veut finalement savoir combien de fois apparaît `caractère_entrée`{.language-} dans la chaîne `chaîne_entrée`{.language-}. Comme on connaît sa première position grace à la question 1 et qu'on peut connaître la suivante grace  à la question 2, on va terminer le boulot et compter combien de fois apparaît `caractère_entrée`{.language-} dans `chaîne_entrée`{.language-}.


{% exercice %}
Créer la fonction `compte_caractère(chaîne: str, indice: int) -> int`{.language-} qui rend le nombre de fois où le caractère `chaîne[indice]`{.language-} est présent dans le paramètre `chaîne`{.language-}

{% endexercice %}
{% details "corrigé" %}

```python
def compte_caractère(chaîne, indice):
    compte = 0

    while indice != None:
        compte += 1
        indice = donne_prochain_indice(chaîne, indice)

    return compte
```


{% enddetails %}



{% exercice %}
Dans l'étape 3. du programme, **utilisez la fonction que vous venez de coder** pour ajouter un affichage qui indique le nombre de fois où  `caractère_entrée`{.language-} apparaît dans `chaîne_entrée`{.language-}.

{% endexercice %}
{% info %}
L'étape 3. du programme sera alors constitué de trois actions :

- Afficher à l'écran le plus petit indice (ou -1) de `chaîne_entrée`{.language-} valant `caractère_entrée`{.language-} (vous pourrez utiliser [la méthode `find`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.find) des chaînes de caractères) (***question 1***)
- Afficher à l'écran si `caractère_entrée`{.language-} est présent plus d'une fois dans `chaîne_entrée`{.language-} (***question 2***)
- Afficher à l'écran le nombre de fois où  `caractère_entrée`{.language-} apparaît dans `chaîne_entrée`{.language-} (***question 3***)
{% endinfo %}
{% details "corrigé" %}

On ajoute à la fin du programme les lignes suivantes, dans le bloc `while`{.language-} :

```python
while chaîne_entrée != "sortie":

    # ...
    

    if index_caractère > -1:
        nombre = compte_caractère(chaîne_entrée, index_caractère)
        print("Le caractère apparaît", nombre , "fois.")
```


{% enddetails %}


Cerise sur le gateau, on cherche à savoir si `caractère_entrée`{.language-} est le caractère qui apparaît le plus de fois dans `chaîne_entrée`{.language-}.


{% exercice %}
Créer la fonction  `donne_max_doublon(chaîne: str) -> int`{.language-} qui rend le nombre maximum de fois où apparaît un même caractère dans `chaîne`{.language-}.

{% endexercice %}
{% details "corrigé" %}

```python
def donne_max_doublon(chaîne):
    nombre_max = 0

    for i in range(len(chaîne)):
        nombre_max = max(nombre_max, compte_caractère(chaîne, i))

    return nombre_max
```

{% enddetails %}

{% exercice %}

Dans l'étape 3. de l'algorithme du programme principal, **utilisez la fonction que vous venez de coder** pour  ajouter un affichage qui le nombre maximum de répétition d'un caractère, et affichez un message de victoire si `caractère_entrée`{.language-} réalise ce maximum.

{% endexercice %}
{% info %}
L'étape 3. du programme principal sera alors constitué de quatre actions :

- Afficher à l'écran le plus petit indice (ou -1) de `chaîne_entrée`{.language-} valant `caractère_entrée`{.language-} (vous pourrez utiliser [la méthode `find`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.find) des chaînes de caractères) (***question 1***)
- Afficher à l'écran si `caractère_entrée`{.language-} est présent plus d'une fois dans `chaîne_entrée`{.language-} (***question 2***)
- Afficher à l'écran le nombre de fois où  `caractère_entrée`{.language-} apparaît dans `chaîne_entrée`{.language-} (***question 3***)
- Afficher à l'écran  le nombre maximum de répétition d'un caractère, et affichez un message de victoire si `caractère_entrée`{.language-} réalise ce maximum. (***question 4***)
{% endinfo %}

{% details "corrigé" %}

On ajoute à la fin du programme les lignes suivantes, dans le bloc `while`{.language-} :

```python
while chaîne_entrée != "sortie":

    # ...
    
    if index_caractère > -1:
        nombre = compte_caractère(chaîne_entrée, index_caractère)
        print("Le caractère apparaît", nombre, "fois.")

        if nombre == donne_max_doublon(chaîne_entrée):
            print("c'est le max !")
```

{% enddetails %}
{% exercice %}

Jouez au pendu avec votre programme !
{% endexercice %}
{% details "corrigé" %}

Le programme complet est :

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

### Erreurs courantes à éviter

Attention aux erreurs de débutant :

- une mauvaise compréhension des mécanismes : ça se travaille et vient avec l'expérience
- croire que l'on peut produire du code de qualité et qui marche sans l'exécuter : l'humilité s'apprend aussi avec l'expérience

#### Recoder des fonctions

La majorité d'entre vous n'avez pas lu la documentation de la méthode `find`{.language-}. Du coup vous l'avez recodé, le plus souvent avec des erreurs...

Vous ne perdez pas de temps à comprendre et lire de la documentation. Votre code sera plus clair, plus facile à utiliser et avec moins de bug si vous utilisez les fonctions et méthodes que python met à votre disposition. Apprendre à lire de la documentation vous fera gagner un temps fou !

{% note %}
Pour lire une documentation, en particulier savoir quels sont les paramètres d'une fonction lisez [cette partie du cours](/cours/coder-et-développer/bases-python/fonctions-méthodes/#paramètres).
{% endnote %}

Enfin, on utilise les fonctions testées dans le programme principal. On vous demande de coder des fonctions (et de les tester), ce n'est pas pour rien... Utilisez les !

#### Utiliser le typage des fonctions

Préférez définir vos fonctions sans le typage :

- on préférera écrire ça : `def donne_prochain_indice(chaîne, indice):`{.language-} puis le reste de la définition de la fonction
- à ça : `def donne_prochain_indice(chaîne: str, indice: int) -> int:`{.language-} qui est plus lourd et n'apporte pas grand chose à la lisibilité.

Le typage a bien sur son utilité dans la documentation ou lorsque l'on veut définir précisément les paramètres (pour un test ou en algorithmie par exemple), mais dans le code où la fonction va être utilisée tout de suite après c'est inutile et rend la définition plus dure à lire.

#### Erreurs rares

Mais qu'il faut tout de suite arrêter de faire :

- pas de `from fonctions import *` dans le programme principal car on ne sait pas ce qu'on importe
- les commentaires ne se font pas avec `""" ..."""`. Les commentaires en python s'écrivent avec `#`. Si l'on veut commenter plusieurs lignes à la fois vscode a une commande pour cela : `menu édition > afficher/masquer le commentaire de ligne`. On l'utilise tellement souvent qu'il y a souvent un raccourci clavier en plus.
