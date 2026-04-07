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
(M1 := ListeChaînée<entier>) ← ListeChaînée<entier>{valeur: 4}
M1.queue ← ListeChaînée<entier>{valeur: 2}

```

{% attention2 "**À retenir**" %}
Une liste chaînée est un type récursif et n'a pas de notion de capacité ou de longueur : une liste chaînée est potentiellement infinie
{% endattention2  %}

## Complexité

> Ajout en tête de liste
> concaténation
> mais soucis de trouver un élément
> 
Outre le fait qu'une liste chaînée puisse grossir en ajoutant des éléments
Le principal intérêt des liste chaînée est :

{% note %}
L'insertion et la suppression d'un maillon se fait en $\mathcal{O}(1)$ opérations
{% endnote %}

Ce qui en fait une structure très malléable. En revanche ceci à un coût :

{% note %}
Pour accéder au $i$ème élément d'une liste chaînée, il faut la parcourir à une complexité de $\mathcal{O}(i)$.
{% endnote %}

## Utilisation

> parcours, ajout et suppression d'élément dont on connaît la position (le premier ou le dernier)

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

C'est cette dernière utilisation fait que cette structure est plébiscité par les approches récursives où l'on construit petit à petit nos listes. Voyons ça avec quelques exercices qui reprennent avec des listes chaînées [des exercices que l'on a déjà vu avec des tableaux](../projet-itératif-récursif/#algorithme-max-tableau-rec){.interne}, vous verrez que les algorithmes sont de complexité linéaire ce qui n'était pas le cas avec des tableaux.

{% exercice %}
Donnez un algorithme récursif et sa complexité de recherche de la valeur maximale dune liste chaînée d'entiers.
{% endexercice %}
{% details "corrigé" %}

L'algorithme suivant est clairement correct :

```pseudocode
algorithme maximum(L: Maillon<entier>) → entier:
    si L.suivant == ∅:
        rendre L.valeur
    rendre max(L.valeur, maximum(L.suivant))
```

L'équation de sa complexité est : $C(n) = \mathcal{O}(1) + C(n-1)$ où $n$ es la taille de la liste. Cette équation a pour solution $C(n) = \mathcal{O}(n)$
{% enddetails %}

{% exercice %}
Donnez un algorithme récursif et sa complexité permettant de supprimer une valeur d'ue liste.
{% endexercice %}
{% details "corrigé" %}

L'algorithme suivant est clairement correct :

```pseudocode
algorithme supprime(L: Maillon<T>, v: T) → Maillon<T>:
    si L == ∅:
        rendre ∅
    si L.valeur == v:
        rendre supprime(L.suivant, v)
    rendre L.append(supprime(L.suivant, v))
```

L'équation de sa complexité est : $C(n) = \mathcal{O}(1) + C(n-1)$ où $n$ es la taille de la liste. Cette équation a pour solution $C(n) = \mathcal{O}(n)$.

{% enddetails %}

{% exercice %}
Donnez un algorithme récursif et sa complexité permettant de retourner une liste chaînée
{% endexercice %}

{% details "corrigé" %}

Utilisons la concaténation :

```pseudocode
algorithme retourne(L: Maillon<T>) → Maillon<T>:
    si L == ∅:
        rendre ∅
    L2 ← L.pop()
    rendre concaténation(retourne(L2), L)
```

La complexité vaut :

$C(n) = \mathcal{O}(n) + C(n-1)$ où $n$ es la taille de la liste. ce qui donne une complexité de $\mathcal{O}(n^2)$ ce qui est un peut trop.

La complexité importante est due au fait que l'on fait trop de concaténations inutiles. Pour palier ça, utilisons les accumulateurs !

```pseudocode
algorithme retourne(L: Maillon<T>, acc: Maillon<T>) → Maillon<T>:
    si L == ∅:
        rendre acc
    L2 ← L.pop()
    L.append(acc)
    rendre retourne(L2, L)
```

Et on retourne la liste en commençant par un accumulateur vide. Par exemple si on cherche à retourne la liste `[1, 2, 3]`{.language-} :

```pseudocode
retourne([1, 2, 3], ∅)  = 
retourne([2, 3], [1])   =
retourne([3], [2, 1])   =
retourne([], [3, 2, 1]) = [3, 2, 1]
```

La complexité est maintenant à nouveau de $C(n) = \mathcal{O}(1) + C(n-1)$ donc bien linéaire en la taille de la liste chaînée.
{% enddetails %}

