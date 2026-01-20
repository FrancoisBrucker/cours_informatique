---
layout: layout/post.njk
title: Abus de notation

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Il sera parfois plus simple d'écrire des raccourci dans un pseudo-code pour le rendre plus lisible. 

Nous allons montrer dans cette partie plusieurs raccourcis courants et utilisés dans ce cours ainsi que leurs traductions en instructions élémentaires.

## Définitions de variables

Le but d'un pseudo-code est d'être explicite, c'est pourquoi :

- les variables doivent être définies avant d'être utilisée
- une variable ne peut contenir que des objets d'un type donné

Mais cela ne doit pas rendre le code lourd. On se permettra donc, **lorsqu'il n'y a pas d’ambiguïté possible**, l'abus de notations qui crée et affecte une variable en une seule fois comme : 

```pseudocode
(a := entier) ← 3
```

Si le type d'affectation est déterminable via l'affectation, on pourra se permettre d'écrire directement `a := 3`{.language-} pour rendre la formulation plus légère.

Vous verrez aussi parfois cet opérateur remplacé par le mot "soit", en particulier lorsqu'il y a plusieurs variables à créer :

```pseudocode
soient a, b et c trois entiers
```

Ou peut-être plus clair :

```pseudocode
a, b, c := entier
```

{% attention %}

En pseudo-code on ne se permettra cependant jamais d'initialiser une variable avant de l'avoir définie (comme on le ferai en python).

{% endattention %}


## Affectations multiples

```pseudocode
a, b ← c, d
```

pour :

```pseudocode
a' := c
b' := d
a ← a'
b ← b'
```

{% info %}
On utilise des variables intermédiaires pour garantir que `a, b ← b, a`{.language-} échange bien les valeurs des deux variables.
{% endinfo %}

## Répétitions

### Déclaration des variables

On écrira :

```pseudocode

pour chaque (i := entier) de [a .. b]:
    # ...
```

À la place de : 

```pseudocode

i := entier
pour chaque i de [a .. b]:
    # ...
```

Cependant on n'écrira cet abus que lorsque la variable de la boucle n'est utilisé que dans la boucle. Pour que ce soit clair il ne faut pas qui'il existe d'autres variables valant i et utilisées hors de la boucle.

{% attention %}
Plus généralement on ne définira pas de variable à l'intérieur d'un bloc si :

- ce bloc est une répétition (cela redéfinirait plusieurs fois la variable)
- la variable est ensuite utilisée en-dehors du bloc

{% endattention %}

### Nombre constant de répétitions

Si on n'utilise pas la variable de boucle :

```pseudocode
répéter k fois:
    # ...
```

Pour :

```pseudocode
(i := entier) ← 0
tant que (i < k):
    i ← i + 1 
    # ...
```

### Répétitions par borne

Tout un tas de variations sont possibles, du moment que ce soit compréhensible. Par exemple :

```pseudocode
i := entier
pour i de a à b:
    # ...
```

Ou encore :

```pseudocode
i := entier

pour i=a à i=b:
    # ...
```

Pour :

```pseudocode
i := entier
pour chaque i de [a .. b]:
    # ...
```

### Répétitions à pas fixé

```pseudocode
i := entier
pour i de a à b par par pas de k:
    # ...
```

ou encore :

```pseudocode
i := entier
pour chaque i de [a .. b] par pas de k:
    # ...
```

pour :

```pseudocode
(i := entier) <- a
tant que i ≤ b:
  # ...

  i ← i + k
```

## Affectation d'une tranche de tableau

```pseudocode
T[a:b] ← k
```

pour :

```pseudocode
pour chaque i de [a .. b[:
    T[i] ← k
```

Fonctionne aussi pour :

```pseudocode
T[:] ← k
```

Qui correspond à :

```pseudocode
pour chaque i de [0 .. T.longueur[:
    T[i] ← k
```

Ou encore à :

```pseudocode
T[a:b] ← T'[a':]
```

Qui correspond à :

```pseudocode
pour chaque i de [0 .. b-a[:
    T[a + i] ← T'[a' + i]
```

{% attention %}
Les affectations de tranches ne sont **pas** une instruction simple, mais nécessitent plusieurs instructions : ceux de la boucle sous-jacente.

Ainsi, le code suivant nécessite $1 + j - i$ instructions (1 instruction de création du nouveau tableau puis j-i affectations) :

```pseudocode
T' ← un nouveau tableau contenant T[i:j]  # j - i + 1 instructions en 1 ligne
```

{% endattention %}

## Concaténation

Avec deux tableaux :

```pseudocode
T := T1 + T2
```

pour :

```pseudocode
T ← un nouveau tableau de taille T1.longueur + T2.longueur

pour chaque i de [0 .. T1.longueur[:
    T[i] ← T1[i]
pour chaque i de [0 .. T2.longueur[:
    T[T1.longueur + i] ← T2[i]

```
