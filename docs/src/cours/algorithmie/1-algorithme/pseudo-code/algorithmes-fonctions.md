---
layout: layout/post.njk
title: Algorithmes et fonctions

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le pseudo-code permet d'écrire des algorithmes de façon claire et sans ambiguïtés.

## Algorithme

{% definition %}
Un **_algorithme_** est une suite d'instructions de pseudo-code qui, a partir de paramètres d'entrées de type déterminé, rend une sortie de type déterminé. En pseudocode comme un bloc :

```pseudocode
algorithme <nom>(<nom paramètre>: <type paramètre>, ...) → <type de sortie>
    # ... instructions

    rendre <objet>
```

Il est défini avec :

- son nom,
- ses paramètres (0, 1 ou plusieurs séparés par des virgules) et son type de retour
- la dernière instruction d'un algorithme est l'instruction `rendre <objet>`{.language-}

{% enddefinition %}

Considérons par exemple la description de  l'algorithme de recherche d'un élément dans une liste :

```text
Nom : recherche
Entrées :
    T : un tableau d'entiers
    x : un entier
Sortie :
    un booléen
Programme :
    parcourir chaque élément de t jusqu'à trouver un élément dont la valeur est égale à la valeur de x.
    Si on trouve un tel élément, rendre "Vrai"
    Sinon rendre "Faux"
```

En pseudo-code, cela va donner ça :

<div id="problème-recherche"></div>

```pseudocode
algorithme recherche(T: []int,
                     x: int      # entier recherché dans t
                    ) → bool:    # Vrai si x est dans t

    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux
```

La definition du bloc algorithme (jusqu'aux `:`{.language-}) est constitué :

1. du mot-clé `algorithme`{.language-} qui détermine la nature du bloc
2. du nom de l'algorithme : `recherche`{.language-}
3. puis ses 3 paramètres d'entrées. Chaque paramètre est décrit par son nom suivit de son type. 
4. enfin, le type de sortie de l'algorithme qu'on fait précéder d'une flèche.

Si on a besoin d'information supplémentaire pour qu'un lecteur puisse mieux comprendre le pseudo-code on peut ajouter des commentaires en les faisant commencer par un `#`{.language-}.  Ne mettez pas trop de commentaires, normalement le pseudo-code et le nom des variables doit suffire. On a ici juste décrit ce que fait l'algorithme avec ses paramètres d'entrées.

{% lien %}
La description des types de paramètres est reprise du format python : <https://docs.python.org/fr/3.13/library/typing.html>{.externe}
{% endlien %}

Tout algorithme se termine par un retour d'un objet (de même type que son type de sortie) avec l'instruction `rendre`{.language-}. Cette instruction est la dernière qu'exécutera l'algorithme ainsi l'algorithme suivant rendra **toujours** 42 :

```pseudocode
algorithme réponse() → entier: 

    rendre 42
    rendre 0    # ne sera jamais exécuté
```

Ne confondez pas le retour d'un algorithme et un affichage à l'écran. L'algorithme suivant rendra l'entier 0 :

```pseudocode
algorithme réponse() → entier: 

    affiche 42
    rendre 0    # ne sera jamais exécuté
```

L'affichage à l'écran est une **information donnée à l'utilisateur**, l'algorithme s'en fiche et fonctionne tout à fait sans.

{% retenir %}
Pour distinguer le retour de fonction d'un affichage supprimez tous les affichages de votre pseudo-code et il doit continuer de fonctionner.
{% endretenir %}

## Fonctions

Dans un programme, de nombreuses phases sont répétées à divers endroits du code (sommer ou multiplier des vecteurs 3D dans un moteur physique par exemple). Pour éviter de devoir replacer toutes ces instructions à chaque fois on définis des _sous-programmes_ réutilisables à volonté, appelés **_fonctions_**.

{% definition %}
Une **_fonction_** est un algorithme. Elle a ainsi :

- un nom
- des paramètres d'entrée
- une sortie
- des instructions, appelées **_corps de la fonction_**

Une fois définie, on peut l'appeler comme une instruction (sa sortie est affectée à la variable `sortie`{.language-} dans l'exemple ci-après) :

```pseudocode
sortie ← <nom fonction>(<paramètre 1>, ..., <paramètre n>)
```

{% enddefinition %}

### Appels de fonctions

On peut définir des fonctions puis les utiliser ensuite comme dans tout langage de programmation. Considérons l'algorithme de recherche :

```pseudocode
algorithme recherche(t: []int,
                     x: int
                    ) → bool:

    pour chaque e de t:
        si e == x:
            rendre Vrai
    rendre Faux
```

On peut utiliser le pseudo code de nom _recherche_ dans d'autres pseudo-code comme une fonction. Par exemple :

```pseudocode

ref T []int ← [1, 2, 6]
ref trouve ← recherche(t, 6)

affiche à l'écran trouve
```

Est un pseudo-code valide puisque `recherche`{.language-} est bien défini et utilisé correctement (le type de ses paramètres est correct).

{% retenir %}
- Les différentes exécutions de fonctions au sein d'un même algorithmes ne partagent pas leurs variables.
- Les paramètres sont **des variables** qui sont initialisées au début de l'exécution de la fonction.
- **Seuls** les objets peuvent être transmis.
{% endretenir %}

Dans l'exemple précédent, tout ce passe comme si on disposait de deux ordinateurs, un qui exécute le pseudo-code, l'autre la fonction `recherche`{.language-} :

1. le passage de l'ordinateur effectuant le pseudo-code à l'ordinateur exécutant l'algorithme `recherche`{.language-} se fait en affectant les paramètres de la fonction recherche (ce sont des variables) à des objets manipulés par le pseudo-code : ici un tableau valant `[1, 2, 3]`{.language-}
2. le passage de l'ordinateur effectuant l'algorithme `recherche`{.language-} à l'ordinateur exécutant le pseudo-code se fait par le retour de la fonction

Dans l'exemple précédent, la variable `e`{.language-} définie dans l'algorithme `recherche`{.language-} n'est pas visible depuis le pseudo-code. En revanche, l'objet booléen de retour est lui transmis au pseudo-code via l'instruction `rendre`{.language-pseudocode}.

### Pseudo-code avec fonctions

On peut aussi directement coder des fonctions dans un pseudo-code. Par exemple :

```pseudocode
fonction recherche(T: []int, x: int) → bool:

    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux

algorithme exorcisme(T: []int) → str:
    si recherche(t, 666):
        rendre "Aspergez votre ordinateur d'eau bénite. Vite !"
    sinon:
        rendre "Tout va bien, le tableau n'est pas possédé. Ouf."
```

{% exercice %}
Que va afficher l'exécution de l'algorithme suivant :

```pseudocode/
fonction affiche_double(e: entier) → ∅:

    ref x ← 2 * e
    affiche x

algorithme calculatrice() → ∅:

    ref x int

    x ← demande un entier à l'utilisateur
    affiche_double(x)
    affiche x
```

{% endexercice %}
{% details "corrigé" %}
L'entier `x`{.language-} de la fonction est indépendant de l'entier `x`{.language-} défini dans l'algorithme. L'exécution de l'algorithme affichera alors :

1. le double de l'entier demandé à l'utilisateur : exécution de la ligne 5 
2. l'entier demandé à l'utilisateur : exécution de la ligne 13

{% enddetails%}

### Tableaux et fonctions

{% retenir %}
Les objets sont communs à toutes les exécutions d'un même algorithmes. Ils peuvent passer d'une fonction à une autre via les variables.
{% endretenir %}

Par exemple :

```pseudocode
fonction modif(U: []int) → ∅:

    U[2] ← U[0] + U[1]

algorithme tableau() → ∅:

    ref T ← [3]int

    T[0] ← 1
    T[1] ← 2
    T[2] ← 0
    affiche T[2]
    modif(T)
    affiche T[2]
```

Va afficher 0 puis 3. En effet :

- lors de l'exécution de la fonction `modif`{.language-} la **variable** `U`{.language-} va être associée à l'**objet** tableau de l'algorithme : la variable `T`{.language-} de l'algorithme est différente de la variable `U`{.language-} de la fonction mais est associé au **même** objet.
- on associe à la variable d'indice 2 de l'objet tableau un nouvel entier valant 3 : on a modifié le tableau défini dans l'algorithme.

Les tableaux sont les seuls objets défini en pseudo-code qui peuvent être modifiés, ce n'est pas le cas ni des 5 types basiques ni des chaînes.

{% retenir %}
Vérifiez toujours très soigneusement vos algorithmes lorsque vous créez des tableaux que vous passez en paramètres de fonctions. Ils peuvent être modifiés par cette fonction !
{% endretenir %}

## <span id="type"></span>Signature d'un algorithme ou d'une fonction

Lorsque l'on défini un algorithme ou un pseudo-code on explicite le type des objets en entrées et en sortie :

{% definition %}
Une **_signature de fonction_** associe :

- son nom
- le type de chacun de ses paramètres
- le type de sortie

On le représente ainsi :

```pseudocode
<nom de l'algorithme>(<type premier paramètre>, ..., <type dernier paramètre>) → <type de sortie>
```

Ou, lorsque le nom des paramètre peut-être utile on pourra les ajouter ainsi :

```pseudocode
<nom de l'algorithme>(<nom premier paramètre>: <type premier paramètre>, ..., <nom dernier paramètre>: <type dernier paramètre>) → <type de sortie>
```

{% enddefinition %}

{% definition %}
Le **_type_** d'un algorithme est sa signature sans son nom.

{% enddefinition %}

Par exemple pour l'algorithme `recherche`{.language-} :

- sa signature est `recherche(T []int, x int) → bool`{.language-} ou `recherche([]int, int) → bool`{.language-}
- son type est `([]int, int) → bool`{.language-}

Associer un type à une fonction permet lui permet d'être associée à un nom comme tout autre objet. Par exemple, en supposant que la fonction `recherche`{.language-} soit définie :

```pseudocode
ref f ([]int, int) → bool

f ← recherche
affiche f([1, 2, 6], 6)

```

{% attention %}
Ne confondez pas `nom_algorithme`{.language-} qui est l'algorithme et `nom_algorithme(a, b)`{.language-} qui est le résultat de son exécution avec les paramètres `a`{.language-} et `b`{.language-}.
{% endattention %}

## Récursivité

Le fait que les variables et les noms définis dans les fonctions restent dans le cadre de la fonction actuellement exécutée nous donnent accès à la récursivité : Il suffit que notre pseudo-code s'appelle lui-même comme une fonction.

{% attention %}
Attention aux conditions d'arrêts pour garantir qu'une fonction ne s'appelle pas indéfiniment.
{% endattention %}

Par exemple l'algorithme suivant est une implémentation récursive de l'algorithme `recherche`{.language-} :

<span id="algorithme-recherche-rec"></span>

```pseudocode
algorithme recherche(T: []entier,
                     x: entier     # entier recherché dans t
                    ) → booléen:   # Vrai si x est dans t

    si T.longueur == 0:
        rendre Faux
    sinon si T[0] == x:
        rendre Vrai
    sinon:
        rendre recherche(T[1:], x)
```
