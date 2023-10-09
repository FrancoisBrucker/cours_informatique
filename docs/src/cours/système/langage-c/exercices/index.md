---
layout: layout/post.njk

title: Exercices

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Il existe de nombreux sites compilant des exercices (plus ou moins corrigés) en `C`, par exemple :

- <https://www.lamsade.dauphine.fr/~manouvri/C/PolyExoC_MM.pdf>
- <https://perso.univ-perp.fr/langlois/images/pdf/ens/touslestd.pdf>

Nous en ajoutons quelques-un ci-après à faire à la suite.

Vos fonctions ne doivent produire ni erreurs ni warnings en utilisant les options de compilation :

```
-Wall -Wextra -pedantic -std=c23
```

## Nombre de chiffres d'un entier

{% faire %}
Créez une fonction qui rend le nombre de chiffre d'un entier (positif ou négatif). Sa signature doit être :

```c
int nb_chiffres(int nombre);
```

{% endfaire %}

## Syracuse

Variation sur le thème de la [suite de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse#Suite_de_Syracuse).

### <span id="syracuse-v2"></span> v1

{% faire %}
Créez une fonction (et testez la) qui rend le nombre d'étapes nécessaire pour arriver à 1 pour la [suite de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse#Suite_de_Syracuse) d'en entier passé en paramètre. Sa signature doit être :

```c
int syracuse(int nombre);
```

Si le nombre passé en paramètre est négatif ou nul, la fonction doit rendre -1.
{% endfaire %}

### <span id="syracuse-v2"></span> v2

{% faire %}
Créez une fonction (et testez la) qui rend tous les éléments de la suite de [suite de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse#Suite_de_Syracuse) d'en entier passé en paramètre. Sa signature doit être :

```c
int *syracuse_tab(int nombre);
```

Si le nombre passé en paramètre est négatif ou nul, la fonction doit rendre le pointeur `NULL`{.language}.

{% endfaire %}

### <span id="syracuse-v3"></span> v3

{% lien %}
[Utilisation de `getopt`](https://stacklima.com/getopt-fonction-en-c-pour-analyser-les-arguments-de-la-ligne-de-commande/)
{% endlien %}

En utilisant la fonction `getopt` définie dans `<unistd.h>`{.fichier} créez un programme `siracuse` qui :

- prend un paramètre `x` qui est le premier élément de la liste
- sans option le programme rend la longueur de la suite de Syracuse (v1)
- avec l'option `-l` le programme rend la suite complète de syracuse (v2)

## Structure de liste

Une [structure de liste](/cours/algorithme-code-théorie/algorithme/structure-de-données/liste/) en python est une version améliorée d'un tableau. On vous demande d'implémenter cette structure en `C` dans deux fichiers `liste.c`{.fichier} et `liste.h`{.fichier} dont vous testerez les fonctions dans un fichier `main.c`{.fichier}.

{% faire %}
Proposez une structure permettant de stocker une structure de liste contenant des entiers.

Créez le type `liste` associé à cette structure.
{% endfaire %}
{% faire %}
Créez les fonctions :

- de création d'une liste vide
- d'ajout d'un élément à la fin de la liste
- d'évaluation d'un élément de la liste
- de remplacement d'un élément
- de suppression de l'élément en fin de liste

Vous vérifierez sur des exemple que le tableau est bien correctement dimensionné
{% endfaire %}
{% info %}
Vous pourrez utiliser la fonction [`realloc`{.language-}](https://www.scaler.com/topics/c-realloc/) pour le dimensionnement des tableaux.
{% endinfo %}
{% faire %}
Reprenez l'exercice [Syracuse v2](./#syracuse-v2) et rendez une liste à la place d'un tableau.  
{% endfaire %}

Pour ne pas avoir d'overhead lors de la création de la liste :
{% faire %}
Créez une fonction de signature :

```c
liste *creation_liste(int *t, size_t n);
```

Qui crée une liste contenant une copie des `n>0` premiers éléments de`t`{.language-}.
{% endfaire %}

Pour l'instant notre liste est constituée uniquement d'entier.

{% faire %}
Comment procéderiez vous pour créer une liste pouvant contenir tout ce qu'on veut ?
{% endfaire %}
{% details "solution" %}
On utilise une double indirection et on crée des tableaux de type `void** t`;

Il faudra faire un cast pour chaque élément pour qu'il soit du bon type.
{% enddetails %}

## Nombres aléatoires

Le but de cet exercice est de comprendre la compilation séparée, tout en jouant avec les nombres.

### Étude préliminaire

- Toutes les fonctions sont à écrire dans le programme principal, en dehors de la fonctions main.
- Le programme main doit permettre de tester chaque fonction demandée

{% faire %}
Créez une fonction de signature :

```c
int aleatoire_int(int min, int max);
```

permettant de rendre un entier aléatoire entre min et max inclus (les deux paramètres de la fonction).

Pour cela, vous pourrez utiliser les fonctions (de la `libc`) suivantes définis dans `<stdlib.h>`{.language-} :

- [`srand`{.language-}](https://koor.fr/C/cstdlib/srand.wp) dont le but est d'initialiser l'algorithme de nombres aléatoire avec ue seed. Attention cette fonction n'est à n'utiliser qu'une fois par programme, au tout début.
- [`rand`{.language-}](https://koor.fr/C/cstdlib/rand.wp) qui rend un entier aléatoire entre 0 et et RAND_MAX
- le  modulo  (`%`{.language-}) qui permet de conserver l'équiprobabilité.
{% endfaire %}
{% faire %}
Testez la fonction précédente en faisant la moyenne de 100000 tirage de nombres entre -50 et +50 et en vérifiant pour chaque tirage que l'on est bien dans les bornes fixées.
{% endfaire %}
{% faire %}
Créez une fonction de signature :

```c
int *aleatoire_tab(int max, size_t nombre);
```

Qui tire : `nombre` nombre aléatoires entre 0 et max (exclu) et rend un tableau de max+1 cases (alloué dynamiquement) contenant pour chaque indice le nombre de fois où l'indice a été tiré.
{% endfaire %}
{% faire %}
Créez une fonction de signature :

```c
double aléatoire_01();
```

permettant de rendre un réel aléatoire entre 0 et 1.
{% endfaire %}
{% faire %}
Utilisez la fonction précédente pour créer une fonction de signature :

```c
int *aléatoire_01(double proba, size_t nombre);
```

Qui rend une liste de taille `nombre`{.language-} contenant des 0 ou des 1 tirés selon une probabilité `proba`{.language-}.
{% endfaire %}

{% faire %}
Testez la fonction précédente en tirant une liste de taille 100 avec une probabilité de .1, .5. et .75. Vérifier que les proportions sont bien vérifiées.
{% endfaire %}

### Compilation séparée

{% faire %}
Décomposez le code en deux unités fonctionnelles :

- le programme principal (fichier `main.c`{.fichier})
- le module aléatoire (deux fichiers `aleatoire.c`{.fichier} et `aleatoire.h`{.fichier})

Créez un fichier `Makefile`{.fichier} pour gérer la compilation de ce projet.
{% endfaire %}

## Structure de matrice

On souhaite créer un module permettant de gérer des matrices d'entiers.

On vous demande de faire une unité fonctionnelle contenant les fichiers `matrice.h`{.fichier} et `matrice.c`{.fichier} ainsi que de tester vos programmes dans un fichier `main.c`{fichier}

### Implémentation v1

{% faire %}
Si l'on considère une matrice comme un tableau de lignes, implémentez une fonction de signature :

```c
int **matrice_create(size_t nombre_lignes, size_t nombre_colonnes);
```

Qui crée dynamiquement une matrice où chaque élément vaut 0.
{% endfaire %}

Utilisez les matrices dans le programme principal.

{% faire %}
Créez dans le programme principal une fonction qui crée une matrice à 4 lignes et 6 colonnes et affecte $i+j$ à l'élément de ligne $i$ et de colonne $j$.
{% endfaire %}
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

Vous pourrez utiliser le [formatage des entiers](https://www.lix.polytechnique.fr/~liberti/public/computing/prog/c/C/FUNCTIONS/format.html) de printf pour justifier les entiers à droite (en supposant par exemple qu'ils ont tous au plus 3 chiffres).
{% endfaire %}

{% faire %}
Créez une fonction de signature :

```c
void matrice_destroy(int **matrice, size_t nombre_lignes, size_t nombre_colonnes);
```

Qui supprime une matrice précédemment crée avec la fonction `matrice_create`{.language-}.
{% endfaire %}
{% faire %}
Peut-on simplifier la fonction précédente en :

- supprimant le paramètre `nombre_colonnes`{.language-} ?
- supprimant le paramètre `nombre_lignes`{.language-} ?

Si oui, le faire.
{% endfaire %}

### Implémentation v2

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

### Implémentation v3

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
[technique du pointeur opaque](https://interrupt.memfault.com/blog/opaque-pointers)
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
  // definition de la structure
}

// fonctions
```

{% faire %}

- Pourquoi appelle-t-on ce pattern de création de structure "pointeur opaque" ?
- en qui cela peut-il faire penser à de la programmation objet ?

{% endfaire %}
{% faire %}

Implémentez cette nouvelle (et dernière) façon d'utiliser des matrices.

{% endfaire %}

Les types opaques sont une façon très utilisée d'implémenter des structures en C.
