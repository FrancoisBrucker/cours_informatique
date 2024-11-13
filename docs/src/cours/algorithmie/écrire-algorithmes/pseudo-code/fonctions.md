---
layout: layout/post.njk
title: Fonctions

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Dans un programme, de nombreuses phases sont répétées à divers endroits du code (sommer ou multiplier des vecteurs 3D dans un moteur physique par exemple). Pour éviter de devoir replacer toutes ces instructions à chaque fois on définis des _sous-programmes_ réutilisables à volonté, appelés _**fonctions_**.

{% note "**Définition**" %}
Une fonction est un algorithme. Elle a :

- un nom
- des paramètres d'entrée
- une sortie
- des instructions, appelées _**corps de la fonction_**

Une fois définie, on peut l'appeler comme une instruction (sa sortie est affectée à la variable `sortie`{.language-} dans l'exemple ci-après) :

```text
sortie = nom(entrée 1, ..., entrée n)
```

{% endnote %}

## Fonctions et algorithmes

### Appels de fonctions

On peut définir des fonctions puis les utiliser ensuite comme dans tout langage de programmation. Considérons l'algorithme suivant :

```text
Nom : recherche
Entrées :
    t : un tableau d'entiers
    x : un entier
Programme :
    pour chaque élément e de t:
        si e == x:
            Retour vrai
    Retour faux
```

On peut utiliser le pseudo code de nom _recherche_ dans d'autres pseudo-code comme une fonction. Par exemple :

```python
t = [1, 2, 6]
trouve = recherche(t, 6)
affiche à l'écran trouve
```

Est un pseudo-code valide puisque `recherche`{.language-} est bien défini et utilisé correctement (le type de ses paramètres est correct).

### Pseudo-code avec fonctions

On peut aussi directement coder des fonctions dans un pseudo-code. Par exemple :

```text
Nom : exorcisme
Entrées :
    t : un tableau d'entiers
Programme :
    Fonction :
        Nom : recherche
        Entrées :
            t : un tableau d'entiers
            x : un entier
        Programme :
            pour chaque élément e de t:
                si e == x:
                    Retour vrai
            Retour faux

    Si recherche(t, 666):
        affiche à l'écran "Aspergez votre ordinateur d'eau bénite. Vite !"
    Sinon:
        affiche à l'écran "Tout va bien, le tableau n'est pas possédé. Ouf"
```

Ce genre d'écriture devenant vite pénible, on lui préférera une écriture plus compacte, comme par exemple en python :

```python
def recherche(t, x):
    for e in t:
        if e == x:
            return True
    return False

def exorcisme(t):
    if recherche(t, 666):
        print("Aspergez votre ordinateur d'eau bénite. Vite !")
    else:
        print("Tout va bien, le tableau n'est pas possédé. Ouf")

```

### Signature d'une fonction

Lorsque l'on défini un algorithme ou un pseudo-code on explicite souvent le type des objets en entrées et en sortie. Par exemple l'algorithme recherche nécessite un tableau d'entier et un entier en paramètre et sa sortie est un booléen. Lorsque l'on écrit une fonction, en particulier en python on a pas toujours l'habitude (ni le besoin) de le faire, mais on peut le spécifier en utilisant **_les signatures de fonctions_**

{% note "**Définition**" %}
Une signature de fonction associe :

- son type à chaque paramètre (précédé d'un `:`)
- le type de sortie (précédé d'un `->`)
  {% endnote %}
  {% info %}
  Par exemple, la signature de [la fonction recherche](./#fonction-recherche) est :

```python
recherche(t: [int], x: int) -> bool
```

{% endinfo %}

On ne peut bien sur utiliser de signature que lorsque les entrées et les sorties sont de types parfaitement définis, ce qui n'est pas toujours le cas.

### Variables locales

Il est important de voir que lorsque l'on exécute une fonction, les variables qu'elle crée existeront dans un espace à elle, pas dans celui du pseudo-code appelant. Le code suivant affichera 4 et pas 6 qui est dernière valeur prise par la variable `e`{.language-} de la fonction `recherche`{.language-} :

```python
e = 4
t = [1, 2, 6]
trouve = recherche(t, 6)
affiche à l'écran e
```

## Objet fonction

Une fonction peut être associée à un nom comme tout autre objet. Par exemple, en supposant que la fonction `recherche`{.language-} soit définie :

```python
e = recherche
t = [1, 2, 6]
trouve = e(t, 6)

print(trouve)
```

{% attention %}
Ne confondez pas `nom`{.language-} qui est l'algorithme et `nom(a, b)`{.language-} qui est le résultat de son exécution avec les paramètres `a`{.language-} et `b`{.language-}.
{% endattention %}

## Récursivité

Le fait que les variables et les noms définies dans les fonctions restent dans le cadre de la fonction actuellement exécuté nous donnent accès à la récursivité : Il suffit que notre pseudo-code s'appelle lui-même comme une fonction.

{% attention %}
Attention aux conditions d'arrêts pour garantir qu'une fonction ne s'appelle pas indéfiniment.
{% endattention %}
