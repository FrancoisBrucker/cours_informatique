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

Pour réussir à supprimer/ajouter un élément en temps constant on va découper la liste en éléments indépendants, appelés _maillons_, collés les uns aux autres.

## Maillon

Commençons par définir un Maillon :

```pseudocode
structure Maillon<Type>:
    attributs:
        valeur: Type

        suivant: Maillon ← ∅
        précédent: Maillon ← ∅
```

Chaque maillon contient :

- sa valeur
- le maillon précédent de la chaîne
- le maillon suivant de la chaîne

Un maillon est une liste chaînée de 1 élément :

```pseudocode
M ← Maillon {valeur: 1}

L ← M
```

## Chaîne de maillons

Si on veut ajouter un maillon à la chaîne, on le peut le rajouter avant ou après l'élément comme le montre l'exemple suivant qui crée une chaîne de deux maillons :

```pseudocode
M ← Maillon {valeur: 1}

# ajout d'un maillon après M
M2 ← Maillon {valeur: 3}
M2.précédent  ← M
M.suivant  ← M2

```

On peut même insérer un élément :

```pseudocode
# insert d'un élément après M

M3 ← Maillon {valeur: 2}

M3.précédent ← M
M3.suivant ← M.suivant

M.suivant ← M3

```

À la fin de l'exemple on a une liste chaînée commençant au maillon `M`{.language-} et constitué de 3 maillons.

{% attention2 "**À retenir**" %}
Il n'y a pas de différence entre un maillon et la chaîne qui commence par lui.
{% endattention2 %}

De la remarque précédente on peut en déduire l'algorithme permettant de déterminer le nombre de maillons (_ie_ la longueur) après un maillon donné :

```pseudocode
algorithme taille(L: Maillon<T>) → entier:
    t ← 0
    tant que L ≠ ∅:
        t ← t + 1
        L ← L.suivant
    rendre t
```

## Structure

On a coutume de définir la liste chaînée via un type récursif :

{% note "**Définition**" %}
Une **_liste chaînée_** est soit :

- un Maillon isolé
- un Maillon suivi d'une liste chaînée

{% endnote %}

On peut écrire cette structure en ajoutant juste deux méthodes à notre maillon :

<span id="structure-liste-chaînée"></span>

```pseudocode
structure Maillon<Type>:
    attributs:
        valeur: Type

        suivant: Maillon ← ∅
        précédent: Maillon ← ∅
    méthodes:
        fonction append(L: Maillon<Type>) → ∅:  # ajoute L après self
            si L ≠ ∅: 
                L.précédent ← self
            self.suivant ← L

        fonction pop() → Maillon<Type>:  # supprime self de la liste 

            L ← self.suivant 

            self.suivant ← ∅ 
            si L ≠ ∅:
                L.précédent ← ∅

            rendre L

```

{% exercice %}
Écrivez un algorithme récursif permettant de concaténer deux listes chaînées avec une complexité égale à la taille de la première liste.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme concatène(L1: Maillon<T>, L2: Maillon<T>) → Maillon<T>:
    si L1 == ∅:
        rendre L2
    rendre L1.append(concatène(L1.suivant, L2))
```

{% enddetails %}

## Complexité

Le principal intérêt des liste chaînée est :

{% note %}
L'insertion et la suppression d'un maillon se fait en $\mathcal{O}(1)$ opérations
{% endnote %}

Ce qui en fait une structure très malléable. En revanche ceci à un coût :

{% note %}
Pour accéder au $i$ème élément d'une liste chaînée, il faut la parcourir à une complexité de $\mathcal{O}(i)$.
{% endnote %}

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
