---
layout: layout/post.njk
title: "Liste Chaînée"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Liste chaînée](https://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e)
{% endlien %}

Les **_listes chaînées_** sont très utilisés en algorithmie lorsque l'on a uniquement besoin de parcourir une suite d'éléments et que l'on souhaite pouvoir supprimer ou ajouter un élément quelconque de cette liste en temps constant.

Commençons par définir le type `ListeChaînée`{.language-} :

```pseudocode
structure ListeChaînée<T>:
    tête: T
    queue: ListeChaînée<T> ← ∅
```

Chaque Liste chaînée contient :

- une tête qui contient une valeur
- une queue qui contient le reste de la liste chaînée

Par exemple une liste chaînée à 2 éléments :

```pseudocode
(L := ListeChaînée<entier>) ← ListeChaînée<entier>{tête: 4}
L.queue ← ListeChaînée<entier>{tête: 2}

```

{% attention2 "**À retenir**" %}
Une liste chaînée est un type récursif et n'a pas de notion de capacité ou de longueur : une liste chaînée est potentiellement infinie
{% endattention2  %}

## Complexité

On peut faire grossir une liste en ajoutant un élément en tête de liste en temps constant, à condition de rendre une nouvelle liste :

{% note "**Proposition**" %}
Ajouter ou supprimer un élément en tête de liste se fait en $\mathcal{O}(1)$ opération avec les méthodes suivantes :

```pseudocode
méthode (l: ListeChaînée<T>) ajoute(valeur: T) → ListeChaînée<T>:
    (V := ListeChaînée<T>) ← ListeChaînée<T>{tête: valeur}
    V.queue ← l

    rendre V

méthode (l: ListeChaînée<T>) supprime() → ListeChaînée<T>:
    rendre l.queue
```

{% endnote  %}

{% note "**Proposition**" %}
Concaténer une liste à une autre est de complexité $\mathcal{O}(n)$ où $n$ est le nombre d'éléments dans la liste :

```pseudocode
méthode (l: ListeChaînée<T>) concatène(l2: ListeChaînée<T>):

    (V := ListeChaînée<T>) ← l
    tant que V.queue ≠ ∅:
        V ← V.queue
    V.queue ← l2 

```

{% endnote  %}


Les deux propositions précédentes montre que cette structure est très malléable. En revanche ceci à un coût :

{% note "**Proposition**" %}
Accéder au $i$ème élément d'une liste chaînée est de une complexité de $\mathcal{O}(i)$.
{% endnote %}
{% details "preuve", "open" %}
Il faut parcourir tous les éléments de la liste un à un.
{% enddetails %}

## Utilisation

On utilise les listes chaînées lorsque l'on doit très souvent insérer ou supprimer des éléments à l'intérieur d'une liste ou lorsque l'on construit une liste par étapes.

### Stockage sur disque

Les listes chaînées sont utilisées pour stocker des fichiers sur un disque physique.

{% lien %}
[Systèmes d'Allocation de fichiers FAT](https://fr.wikipedia.org/wiki/FAT32)
{% endlien %}

<!-- TBD

> TBD décrire le principe en deux structures :
>
> - file allocation table qui est le début
> - bloques sur le disque
>
> dire qu'il y a des améliorations mais que ce principe subsiste jusqu'à maintenant (ext4, zfs, ntfs) 

-->

### Algorithmes récursifs

C'est cette dernière utilisation fait que cette structure est plébiscité par les approches récursives où l'on construit petit à petit nos listes. Voyons ça avec quelques exercices qui reprennent avec des listes chaînées [des exercices que l'on a déjà vu avec des tableaux](../../projet-itératif-récursif/#algorithme-max-tableau-rec){.interne}, vous verrez que les algorithmes sont de complexité linéaire ce qui n'était pas le cas avec des tableaux.

{% exercice %}
Donnez un algorithme récursif et sa complexité de recherche de la valeur maximale dune liste chaînée d'entiers.
{% endexercice %}
{% details "corrigé" %}

L'algorithme suivant est clairement correct :

```pseudocode
algorithme maximum(L: ListeChaînée<entier>) → entier:
    si L.suivant == ∅:
        rendre L.tête
    rendre max(L.tête, maximum(L.queue))
```

L'équation de sa complexité est : $C(n) = \mathcal{O}(1) + C(n-1)$ où $n$ es la taille de la liste. Cette équation a pour solution $C(n) = \mathcal{O}(n)$
{% enddetails %}

{% exercice %}
Donnez un algorithme récursif et sa complexité permettant de supprimer une valeur d'une liste.
{% endexercice %}
{% details "corrigé" %}

L'algorithme suivant est clairement correct :

```pseudocode
algorithme supprime(L: ListeChaînée<T>, v: T) → ListeChaînée<T>:
    si L == ∅:
        rendre ∅
    si L.tête == v:
        rendre supprime(L.queue, v)
    rendre L.queue ← supprime(L.queue, v)
```

L'équation de sa complexité est : $C(n) = \mathcal{O}(1) + C(n-1)$ où $n$ es la taille de la liste. Cette équation a pour solution $C(n) = \mathcal{O}(n)$.

{% enddetails %}

