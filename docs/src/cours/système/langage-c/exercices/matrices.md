---
layout: layout/post.njk

title: Matrices

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On souhaite créer un module permettant de gérer des matrices d'entiers.

## Implémentation v1 : double indirection

{% faire %}
Si l'on considère une matrice comme un tableau de lignes, implémentez une fonction de signature :

```c
int **matrice_create(size_t nombre_lignes, size_t nombre_colonnes);
```

Qui crée dynamiquement une matrice où chaque élément vaut 0.
{% endfaire %}

On va ajouter une fonction pour afficher la matrice à l'écran :
{% faire %}
Créez une fonction qui affiche à l'écran une matrice crée par la fonction `matrice_create`{.language-}. Elle devra afficher par exemple :

```
1  2   3
11 4 111
```

Sa signature sera :

```c
void matrice_affiche(int **matrice, size_t nombre_lignes, size_t nombre_colonnes);
```

**Contrainte** : utilisez l'arithmétique des pointeurs pour trouver vos éléments.
{% endfaire %}
{% info %}
Vous pourrez utiliser le [formatage des entiers](https://www.lix.polytechnique.fr/~liberti/public/computing/prog/c/C/FUNCTIONS/format.html) de printf pour justifier les entiers à droite (en supposant par exemple qu'ils ont tous au plus 3 chiffres).
{% endinfo %}

Utilisons les matrices :

{% faire %}
Le programme principal crée une matrice à 4 lignes et 6 colonnes et affecte $i+j$ à l'élément de ligne $i$ et de colonne $j$. Puis affichez là.
{% endfaire %}

Il nous rest à créer la fonction qui supprime la matrice :
{% faire %}
Créez une fonction de signature :

```c
void matrice_destroy(int **matrice, size_t nombre_lignes, size_t nombre_colonnes);
```

Qui supprime une matrice précédemment crée avec la fonction `matrice_create`{.language-}.
{% endfaire %}
{% exercice %}
Peut-on simplifier la fonction précédente en :

- supprimant le paramètre `nombre_colonnes`{.language-} ?
- supprimant le paramètre `nombre_lignes`{.language-} ?

Si oui, le faire.
{% endexercice %}
{% details "corrigé" %}
Comme la matrice est crée comme un tableau de ligne, le nombre de colonnes est superflu : on libère juste chaque ligne une à une.
{% enddetails %}

## Implémentation v2 : simple indirection

{% faire %}
La fonction précédente peut créer des défauts de cache si l'on adresse les éléments par colonne. L'idée est de rassemble les lignes et les connes en un seul tableau.

Réimplémentez les fonctions d création et de suppression de la matrice avec cette nouvelle structure. Les signatures des fonctions doivent être  :

```c
int *matrice_create(size_t nombre_lignes, size_t nombre_colonnes);
void matrice_destroy(int *matrice);
void matrice_affiche(int *matrice, size_t nombre_lignes, size_t nombre_colonnes);
```

{% endfaire %}

Il est cependant maintenant plus dure d'accéder directement à un élément de la matrice :

{% faire %}
Faire des fonctions permettant d'accéder et de modifier un élément de la matrice. Ces fonctions doivent être de signature :

```c
int matrice_get(int *matrice, size_t ligne, size_t colonne, size_t nombre_lignes, size_t nombre_colonnes);
int matrice_set(int *matrice, int element, size_t ligne, size_t colonne, size_t nombre_lignes, size_t nombre_colonnes);
```

Et utilisez-les dans le fichier `main.c`{.fichier}.

{% endfaire %}

## Implémentation v3 : pointeur opaque

Manipuler une matrice devient très lourd puisqu'il faut connaître et stocker tous les paramètres de la matrice. Améliorons ça :

{% faire %}
Proposez une structure permettant de stocker la matrice et tous ses paramètres
{% endfaire %}

{% faire %}
Utilisez cette structure dans toutes les fonctions. Elles deviennent de signature :

```c
matrice *matrice_create(size_t nombre_lignes, size_t nombre_colonnes);
void matrice_destroy(matrice *m);
void matrice_affiche(matrice *m);
int matrice_get(matrice *m, size_t ligne, size_t colonne);
int matrice_set(matrice *m, int element, size_t ligne, size_t colonne);
```

{% endfaire %}

Pour que les utilisateurs ne puissent pas connaître le contenu de la structure on peut organiser les fichiers de telle sorte de cacher la structure proprement dite.

On appelle cette façon de faire :

{% lien %}
[Technique du pointeur opaque](https://interrupt.memfault.com/blog/opaque-pointers)
{% endlien %}

Ce qui donne pour notre matrice :

Fichier `matrice.h`{.fichier} :

```c
#ifndef FILE_MATRICE
#define FILE_MATRICE

typedef struct matrice* matrice_t;

matrice_p matrice_create(size_t nombre_lignes, size_t nombre_colonnes);
void matrice_destroy(matrice_t m);
void matrice_affiche(matrice_t m);
int matrice_get(matrice_t m, size_t ligne, size_t colonne);
int matrice_set(matrice_t m, int element, size_t ligne, size_t colonne);

#endif
```

Fichier `matrice.c`{.fichier} :

```c
#define "matrice.h"

struct matrice {
  int *matrice;
  size_t lignes;
  size_t colonnes;
}

// corps des fonctions
```

{% faire %}

- Pourquoi appelle-t-on ce pattern de création de structure _"pointeur opaque"_ ?
- en qui cela peut-il faire penser à de la programmation objet ?

{% endfaire %}
{% faire %}

Implémentez cette nouvelle (et dernière) façon d'utiliser des matrices.

{% endfaire %}

Les types opaques sont une façon très utilisée d'implémenter des structures en C.

Ce type de structure à un autre avantage, il permet de modifier la matrice sans modifier le pointeur opaque ! Pour s'en convaincre :

{% faire %}
Ajouter à l'unité fonctionnelle une fonction de signature :

```c
void matrice_transpose(matrice_t m);
```

Qui transpose la matrice.
{% endfaire %}
{% info %}
Vous pourrez :

1. créer une nouvelle matrice `m2`{.language-} avec le même nombre de lignes et de colonnes que `m`{.language-}
2. effectuer la transposition en plaçant les ligne de la matrice originelle dans la nouvelle matrice
3. terminer en affectant `m2->matrice`{.language-} à `m->matrice`{.language-}
4. libérer la mémoire allouée par `m2`{.language-} (sans libérer la matrice en elle même).

{% endinfo %}
