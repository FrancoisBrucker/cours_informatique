---
layout: layout/post.njk
title: "Liste doublement Chaînée"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD amélioration lorsque l'on veut modifier une liste sans rendre un nouveau début.
> TBD structurée en maillon.

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

### Chaîne de maillons

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

### Structure

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
