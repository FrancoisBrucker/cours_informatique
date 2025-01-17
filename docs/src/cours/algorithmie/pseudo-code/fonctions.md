---
layout: layout/post.njk
title: Fonctions

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Dans un programme, de nombreuses phases sont répétées à divers endroits du code (sommer ou multiplier des vecteurs 3D dans un moteur physique par exemple). Pour éviter de devoir replacer toutes ces instructions à chaque fois on définis des _sous-programmes_ réutilisables à volonté, appelés **_fonctions_**.

{% note "**Définition**" %}
Une fonction est un programme. Elle a ainsi :

- un nom
- des paramètres d'entrée
- une sortie
- des instructions, appelées **_corps de la fonction_**

Une fois définie, on peut l'appeler comme une instruction (sa sortie est affectée à la variable `sortie`{.language-} dans l'exemple ci-après) :

```pseudocode
sortie ← nom(entrée_1, ..., entrée_n)
```

{% endnote %}

## Fonctions et algorithmes

### Appels de fonctions

On peut définir des fonctions puis les utiliser ensuite comme dans tout langage de programmation. Considérons l'algorithme de recherche :

```pseudocode
algorithme recherche(t: [entier],
                     x: entier
                    ) → booléen:

    pour chaque e de t:
        si e == x:
            rendre Vrai
    rendre Faux
```

On peut utiliser le pseudo code de nom _recherche_ dans d'autres pseudo-code comme une fonction. Par exemple :

```pseudocode
t ← [1, 2, 6]
trouve ← recherche(t, 6)
affiche à l'écran trouve
```

Est un pseudo-code valide puisque `recherche`{.language-} est bien défini et utilisé correctement (le type de ses paramètres est correct).

### Pseudo-code avec fonctions

On peut aussi directement coder des fonctions dans un pseudo-code. Par exemple :

```pseudocode
fonction recherche(t: [entier],
                    x: entier
                    ) → booléen:

    pour chaque e de t:
        si e == x:
            rendre Vrai
    rendre Faux

algorithme exorcisme(t: [entier]
                    ) → str:

    si recherche(t, 666):
        rendre "Aspergez votre ordinateur d'eau bénite. Vite !"
    sinon:
        rendre "Tout va bien, le tableau n'est pas possédé. Ouf."
```

### Signature d'une fonction

Lorsque l'on défini un algorithme ou un pseudo-code on explicite le type des objets en entrées et en sortie, comme on l'a fait pour l'algorithme recherche.

Lorsque l'on code une fonction en python on a pas toujours l'habitude (ni le besoin) de le faire, mais on peut le spécifier en utilisant **_les signatures de fonctions_**, qui correspond juste à la description de son bloc :

{% note "**Définition**" %}
Une signature de fonction associe :

- son type à chaque paramètre (précédé d'un `:`)
- le type de sortie (précédé d'un `->`)
  {% endnote %}
  {% info %}
  Par exemple, la signature de la fonction recherche est :

```pseudocode
recherche(t: [entier], x: entier) -> booléen
```

{% endinfo %}

### Variables locales

Il est important de voir que lorsque l'on exécute une fonction, les variables qu'elle crée existeront dans un espace à elle, pas dans celui du pseudo-code appelant. Le code suivant affichera 4 et pas 6 qui est dernière valeur prise par la variable `e`{.language-} de la fonction `recherche`{.language-} :

```pseudocode
e ← 4
t ← [1, 2, 6]
trouve ← recherche(t, 6)
affiche à l'écran trouve
```

## Objet fonction

Une fonction peut être associée à un nom comme tout autre objet. Par exemple, en supposant que la fonction `recherche`{.language-} soit définie :

```pseudocode
f ← recherche
t ← [1, 2, 6]
trouve ← f(t, 6)

affiche à l'écran trouve
```

{% attention %}
Ne confondez pas `nom`{.language-} qui est l'algorithme et `nom(a, b)`{.language-} qui est le résultat de son exécution avec les paramètres `a`{.language-} et `b`{.language-}.
{% endattention %}

## Récursivité

Le fait que les variables et les noms définies dans les fonctions restent dans le cadre de la fonction actuellement exécuté nous donnent accès à la récursivité : Il suffit que notre pseudo-code s'appelle lui-même comme une fonction.

{% attention %}
Attention aux conditions d'arrêts pour garantir qu'une fonction ne s'appelle pas indéfiniment.
{% endattention %}
