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

{% note2 "**Définition**" %}
Un **_algorithme_** est une suite d'instructions de pseudo-code qui, a partir de paramètres d'entrées de type déterminé, rend une sortie de type déterminé.

{% endnote2 %}

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
algorithme recherche(T: [entier],
                     x: entier     # entier recherché dans t
                    ) → booléen:   # Vrai si x est dans t

    e := entier
    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux
```

Le programme est un bloc. La definition du bloc (jusqu'aux `:`{.language-}) est constitué :

1. du mot-clé `algorithme`{.language-} qui détermine la nature du bloc
2. suit le du nom du programme
3. puis ses paramètres d'entrées entre parenthèses. Chaque paramètre est décrit par son nom suivit de son type
4. enfin, le type de sortie de l'algorithme qu'on fait précéder d'une flèche.

Si on a besoin d'information supplémentaire pour qu'un lecteur puisse mieux comprendre le pseudo-code on peut ajouter des commentaires en les faisant commencer par un `#`{.language-}.  Ne mettez pas trop de commentaires, normalement le pseudo-code et le nom des variables doit suffire. On a ici juste décrit ce que fait l'algorithme avec ses paramètres d'entrées.

{% lien %}
La description des types de paramètres est reprise du format python : <https://docs.python.org/fr/3.13/library/typing.html>
{% endlien %}

Tout algorithme se termine par un retour d'un objet (de même type que son type de sortie) avec l'instruction `rendre`{.language-}. Cette instruction est la dernière qu'exécutera l'algorithme ainsi l'algorithme suivant rendra **toujours** 42 :

```pseudocode
algorithme réponse() → entier: 

    rendre 42
    rendre 0    # ne sera jamais exécuté
```

Ne cofondez pas le retour d'un algorithme et un affichage à l'écran. L'algorithme suivant rendra l'entier 0 :

```pseudocode
algorithme réponse() → entier: 

    affiche 42
    rendre 0    # ne sera jamais exécuté
```

L'affichage à l'écran est une **information donnée à l'utilisateur**, l'algorithme s'en fiche et fonctionne tout à fait sans.

{% attention2 "**À retenir**" %}
Pour distinguer le retour de fonction d'un affichage supprimez tous les affichages de votre pseudo-code et il doit continuer de fonctionner.
{% endattention2 %}


Terminons par un petit exercice :

<span id="algorithme-nombre-occurrences"></span>

{% exercice %}
Adaptez le pseudo code de l'algorithme `recherche(T: [entier], x: entier) → booléen`{.language-} précédent pour créer l'algorithme :

```pseudocode
nombre(T: [entier], x: entier) → entier
```

Cet algorithme  rend le nombre de fois où `x`{.language-} est présent dans `T`{.language-}
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme nombre(T: [entier], x: entier) → entier:
    nb := entier
    nb ← 0

    e := entier
    pour chaque e de T:
        si e == x:
            nb ← nb + 1
    rendre nb
```

{% enddetails %}

## Fonctions

Dans un programme, de nombreuses phases sont répétées à divers endroits du code (sommer ou multiplier des vecteurs 3D dans un moteur physique par exemple). Pour éviter de devoir replacer toutes ces instructions à chaque fois on définis des _sous-programmes_ réutilisables à volonté, appelés **_fonctions_**.

{% note2 "**Définition**" %}
Une fonction est un programme. Elle a ainsi :

- un nom
- des paramètres d'entrée
- une sortie
- des instructions, appelées **_corps de la fonction_**

Une fois définie, on peut l'appeler comme une instruction (sa sortie est affectée à la variable `sortie`{.language-} dans l'exemple ci-après) :

```pseudocode
sortie ← nom_fonction(entrée_1, ..., entrée_n)
```

{% endnote2 %}

### Appels de fonctions

On peut définir des fonctions puis les utiliser ensuite comme dans tout langage de programmation. Considérons l'algorithme de recherche :

```pseudocode
algorithme recherche(t: [entier],
                     x: entier
                    ) → booléen:

    e := entier
    pour chaque e de t:
        si e == x:
            rendre Vrai
    rendre Faux
```

On peut utiliser le pseudo code de nom _recherche_ dans d'autres pseudo-code comme une fonction. Par exemple :

```pseudocode

t := [entier]{longueur: 3}
t ← [1, 2, 6]

trouve := booléen
trouve ← recherche(t, 6)
affiche à l'écran trouve
```

Est un pseudo-code valide puisque `recherche`{.language-} est bien défini et utilisé correctement (le type de ses paramètres est correct).

{% attention2 "**À retenir**" %}
- Les différentes exécutions de fonctions au sein d'un même algorithmes ne partagent pas leurs variables.
- Les paramètres sont des variables qui sont initialisées au début de l'exécution de la fonction.
- Seuls les objets peuvent être transmis.
{% endattention2 %}

Dans l'exemple précédent, la variable `e`{.language-} définie dans la fonction `recherche`{.language-} n'est pas visible depuis l'algorithme. En revanche, l'objet booléen de retour est lui transmis à l'algorithme via l'instruction `rendre`{.language-pseudocode}.

### Pseudo-code avec fonctions

On peut aussi directement coder des fonctions dans un pseudo-code. Par exemple :

```pseudocode
fonction recherche(t: [entier],
                   x: entier
                  ) → booléen:

    e := entier
    pour chaque e de t:
        si e == x:
            rendre Vrai
    rendre Faux

algorithme exorcisme(t: [entier]
                    ) → chaîne:

    si recherche(t, 666):
        rendre "Aspergez votre ordinateur d'eau bénite. Vite !"
    sinon:
        rendre "Tout va bien, le tableau n'est pas possédé. Ouf."
```

{% exercice %}
Que va afficher l'exécution de l'algorithme suivant :

```pseudocode/
fonction affiche_double(e: entier) → ∅:

    x := entier
    x ← 2 * e
    affiche x

algorithme calculatrice() → ∅:

    x := entier

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

{% attention2 "**À retenir**" %}
Les objets sont communs à toutes les exécutions d'un même algorithmes. Ils peuvent passer d'une fonction à une autre via les variables.
{% endattention2 %}

Par exemple :

```pseudocode
fonction modif(U: [entier]) → ∅:

    U[2] ← U[0] + U[1]

algorithme tableau() → ∅:

    T := [entier]
    T ← [entier]{longueur: 3}

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

{% attention2 "**À retenir**" %}
Vérifiez toujours très soigneusement vos algorithmes lorsque vous créez des tableau que vous passez en paramètres de fonctions. Ils peuvent être modifiés par cette fonction !
{% endattention2 %}

## <span id="type"></span>Type d'un algorithme ou d'une fonction

Lorsque l'on défini un algorithme ou un pseudo-code on explicite le type des objets en entrées et en sortie :

{% note2 "**Définition**" %}
Une **_signature de fonction_** associe :

- son nom
- le type de chacun de ses paramètres
- le type de sortie

On le représente ainsi :

```pseudocode
nom_de_l_algorithme(type_premier_paramètre, ..., type_dernier_paramètre) → type_de_sortie
```

Ou, lorsque le nom des paramètre peut-être utile on pourra les ajouter ainsi :

```pseudocode
nom_de_l_algorithme(nom_premier_paramètre: type_premier_paramètre, ..., nom_premier_paramètre: type_dernier_paramètre) → type_de_sortie
```

{% endnote2 %}

{% note2 "**Définition**" %}
Le **_type_** d'un algorithme est sa signature sans son nom.

{% endnote2 %}

Par exemple pour l'algorithme `recherche`{.language-} :

- sa signature est `recherche([entier], entier) → booléen`{.language-}
- son type est `([entier], entier) → booléen`{.language-}

{% note %}
Lorsque le nom des paramètres est significatif, on les ajoutera à la signature. On écrira par exemple `division(dividende: réel, diviseur: réel) → réel`{.language-} plutôt que `division(réel, réel) → réel`{.language-} qui ne nous permet pas directement d'utiliser la fonction.
{% endnote %}

Associer un type à une fonction permet lui permet d'être associée à un nom comme tout autre objet. Par exemple, en supposant que la fonction `recherche`{.language-} soit définie :

```pseudocode
f := ([entier], entier) → booléen

f ← recherche
affiche f([1, 2, 6], 6)

```

{% attention %}
Ne confondez pas `nom`{.language-} qui est l'algorithme et `nom(a, b)`{.language-} qui est le résultat de son exécution avec les paramètres `a`{.language-} et `b`{.language-}.
{% endattention %}

## Récursivité

Le fait que les variables et les noms définies dans les fonctions restent dans le cadre de la fonction actuellement exécuté nous donnent accès à la récursivité : Il suffit que notre pseudo-code s'appelle lui-même comme une fonction.

{% attention %}
Attention aux conditions d'arrêts pour garantir qu'une fonction ne s'appelle pas indéfiniment.
{% endattention %}

Par exemple l'algorithme suivant est une implémentation récursive de l'algorithme `recherche`{.language-} :

<span id="algorithme-recherche-rec"></span>

```pseudocode
algorithme recherche(T: [entier],
                     x: entier     # entier recherché dans t
                    ) → booléen:   # Vrai si x est dans t

    si T.longueur == 0:
        rendre Faux
    sinon si T[0] == x:
        rendre Vrai
    sinon:
        rendre recherche(T[1:], x)
```
