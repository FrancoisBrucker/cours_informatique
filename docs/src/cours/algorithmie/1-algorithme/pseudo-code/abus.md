---
layout: layout/post.njk
title: '"Abus" de notation'

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Il sera parfois plus simple d'écrire des raccourcis dans un pseudo-code pour le rendre plus lisible. Nous allons montrer dans cette partie plusieurs raccourcis courants et utilisés dans ce cours ainsi que leurs traductions en instructions élémentaires.

## Définitions de variables

Le but d'un pseudo-code est d'être explicite, c'est pourquoi :

- les variables doivent être définies avant d'être utilisées
- une variable ne peut contenir que des objets d'un type donné

Mais cela ne doit pas rendre le code lourd. On se permettra donc plusieurs abus de notation :

### Déclarer plusieurs variables

{% definition "**Abus de notation**" %}
On déclare plusieurs variables du même type :

```pseudocode
ref a, b, c <type>
```

{% enddefinition %}

Par exemple 

```pseudocode
ref i, j, k int
```

### Déclarer puis affecter une variable

{% definition "**Abus de notation**" %}
On déclare et on affecte directement :

```pseudocode
ref a <type> ← <objet>
```

{% enddefinition %}


Par exemple

```pseudocode
ref réponse int ← 42
```

Pour ce type de déclaration/affectation il n'y a pas d’ambiguïté sur le type de la variable, on peut ainsi se permettre d'écrire directement :

{% definition "**Abus de notation**" %}
Type implicite si déclaration et affectation d'un objet de type connu :

```pseudocode
ref a ← <objet de type connu>
```

{% enddefinition %}

Par exemple :

- `ref a ← 3`{.language-} 
- `ref T ← [3]int`{.language-} 

{% attention %}

En pseudo-code on ne se permettra cependant jamais d'affecter une variable avant de l'avoir définie (comme on le ferait en python).

{% endattention %}


### Affectations multiples

{% definition "**Abus de notation**" %}
Plusieurs affectations en même temps :

```pseudocode
a, b ← c, d
```

{% enddefinition %}


pour :

```pseudocode
ref a' ← c
ref b' ← d
a ← a'
b ← b'
```

{% info %}
On utilise des variables intermédiaires pour garantir que `a, b ← b, a`{.language-} échange bien les valeurs des deux variables.
{% endinfo %}

## Tableaux

On va souvent manipuler (affecter, copier, créer) des parties de tableaux. Plutôt que d'expliciter les différentes boucles nécessaires à ces opérations qui alourdissent le pseudo code on aime à les remplacer par des notations plus compactes.

{% attention %}
Ces différentes affectations ne sont **pas** des instructions simples, mais nécessitent des boucles. 

{% endattention %}

### Affectation d'une tranche de tableau

{% definition "**Abus de notation**" %}
Plusieurs affectations en même temps :

```pseudocode
T[a:b] ← k
```

{% enddefinition %}

Pour remplacer :

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
Les affectations de tranches ne sont **pas** des instructions simples, mais nécessitent plusieurs instructions : celles de la boucle sous-jacente.

Ainsi, le code suivant nécessite $1 + j - i$ instructions (1 instruction de création du nouveau tableau puis j-i affectations) :

```pseudocode
T' ← un nouveau tableau contenant T[i:j]  # j - i + 1 instructions en 1 ligne
```

{% endattention %}

### Création de tableaux

{% definition "**Abus de notation**" %}
Création directe d'objets tableaux :

```pseudocode
[1, 2, 3]
```

{% enddefinition %}

Pour remplacer :

```pseudocode
T ← [3]int
T[0] ← 1
T[1] ← 2
T[2] ← 3
```

On pourra alors aussi directement créer un nouveau tableau et l'affecter :

{% definition "**Abus de notation**" %}
Création directe d'objets tableaux :

```pseudocode
ref T []int ← [1, 2, 3]
ref T' []int ← [1 .. 10[
```

voire encore plus directement :

```pseudocode
ref T ← [1, 2, 3]
ref T' ← [1 .. 10[
```

{% enddefinition %}

Pour remplacer :

```pseudocode
ref T []int
T ← [3]int

T[0] ← 1
T[1] ← 2
T[2] ← 3

ref T' []int
T' ← [9]int

pour chaque i de [0 .. 9[:
    T[i] ← i + 1

```

### Concaténation

{% definition "**Abus de notation**" %}
Création de tableau par concaténation de deux tableaux de même type :

```pseudocode
ref T ← T1 + T2
```

{% enddefinition %}

Pour remplacer :

```pseudocode
ref T ← [T1.longueur + T2.longueur](type T1)

pour chaque i de [0 .. T1.longueur[:
    T[i] ← T1[i]
pour chaque i de [0 .. T2.longueur[:
    T[T1.longueur + i] ← T2[i]

```

### Liste en compréhension

{% lien %}
[Liste en compréhension](https://www.docstring.fr/glossaire/comprehension-de-liste/){.externe}
{% endlien %}

On pourra aussi utiliser les listes en compréhension (_list comprehension_) popularisées par python. De nombreux formats existent, du moment que c'est compréhensible :

{% definition "**Abus de notation**" %}
Écriture à la python :

```pseudocode
[<expression> pour chaque <variable> de <énumérable> si <condition logique>]
```

Ou plus ensembliste :

```pseudocode
[<expression> | <variable> ∈ <énumérable>, <condition logique>]
```
{% enddefinition %}

Par exemple :

```pseudocode
[2 * x pour chaque x de [1 .. 5]]   # [2, 4, 6, 8, 10]
[2 * x | x ∈ [1 .. 5]] 
```

Ou, avec la notation mathématique :

```pseudocode
[1 + 4 * k pour chaque k de [1 .. ] si 1 + 4 * k < 20]   # [5, 9, 13, 17]
[1 + 4 * k | k ∈ [1 .. ], 1 + 4 * k < 20]  
[1 + 4 * k |  1 ≤ k ≤ 4]  
```

Pour que la notation mathématique soit déterministe, on suppose que la variable sera énumérée selon l'ordre sous-jacent de l'ensemble.

## Variable muette

Si on n'utilise pas la variable de boucle on utilise une variable muette `_` :

```pseudocode
pour chaque _ de [1 .. k]:
    # ...
```


