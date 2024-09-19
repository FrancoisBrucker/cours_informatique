---
layout: layout/post.njk

title: Exercices

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Vos fonctions ne doivent produire ni erreurs ni warnings en utilisant les options de compilation :

```
-Wall -Wextra -pedantic -std=c23
```

Déclarez bien vos variables dans une fonction (au pire dans la fonction main), sans quoi elle seront stockées dans la partie data de votre programme et pas la pile.

## Bases

Création de fonctions simples et compilation avec des bibliothèques annexes.

{% aller %}
[Nombre de chiffres d'un entier](./nb-chiffres){.interne}
{% endaller %}

## Retour de Pointeurs

On utilise des pointeurs comme retour de fonctions et on termine en créant un makefile.

{% aller %}
[Nombres aléatoires](./nb-aléatoires){.interne}
{% endaller %}

## Syracuse

Quelques petits exercices puis on personnalise notre exécutable avec des paramètres.

{% aller %}
[Syracuse](./syracuse){.interne}
{% endaller %}

## <span id="liste"></span> Structure de liste

Une [structure de liste](/cours/algorithmie/structure-conteneurs/liste/){.interne} en python est une version améliorée d'un tableau. On vous demande d'implémenter cette structure en `C` dans deux fichiers `liste.c`{.fichier} et `liste.h`{.fichier} dont vous testerez les fonctions dans un fichier `main.c`{.fichier}.

En `C` on utilisera [les structures](../langage/structures/) pour gérer des type composés comme les listes qui nécessitent à la fois un tableau, sa taille et le nombre actuel d'éléments présents.

### Implémentation

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

Pour ne pas avoir d'overhead lors de la création d'une liste utilisée comme un tableau :
{% faire %}
Créez une fonction de signature :

```c
liste *liste_create(int *t, size_t n);
```

Qui :

- crée une liste contenant une copie des `n>0` premiers éléments de`t`{.language-} si `t`{.language-} est non `NULL`{.language-}
- crée une liste vide de taille `n`{.language-} si `t`{.language-} est `NULL`{.language-}
{% endfaire %}

### Pile

Notre structure de liste peut très facilement se décliner en [pile](https://fr.wikipedia.org/wiki/Pile_(informatique)).

{% faire %}
Quelles sont les opérations (et leurs complexités) pour une structure de pile ?
{% endfaire %}
{% faire %}
Créez les fonctions permettant de mettre en œuvre les opérations liées à une pile pour la structure de liste.
{% endfaire %}

### Liste générique

Pour l'instant notre liste est constituée uniquement d'entier.

{% faire %}
Comment procéderiez vous pour créer une liste pouvant contenir tout ce qu'on veut ?
{% endfaire %}
{% details "solution" %}
On utilise une double indirection et on crée des tableaux de type `void** t`;

Il faudra faire un cast pour chaque élément pour qu'il soit du bon type.
{% enddetails %}

## <span id="matrice"></span>Structure de matrice

On souhaite créer un module permettant de gérer des matrices d'entiers.

On vous demande de faire une unité fonctionnelle contenant les fichiers `matrice.h`{.fichier} et `matrice.c`{.fichier} ainsi que de tester vos programmes dans un fichier `main.c`{fichier}

### Implémentation v1 : double indirection

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

Contrainte : utilisez l'arithmétique des pointeurs pour trouver vos éléments.
{% endfaire %}
{% info %}
Vous pourrez utiliser le [formatage des entiers](https://www.lix.polytechnique.fr/~liberti/public/computing/prog/c/C/FUNCTIONS/format.html) de printf pour justifier les entiers à droite (en supposant par exemple qu'ils ont tous au plus 3 chiffres).
{% endinfo %}
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

### Implémentation v2 : simple indirection

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

### Implémentation v3 : pointeur opaque

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
  int *matrice;
  size_t lignes;
  size_t colonnes;
}

// corps fonctions
```

{% faire %}

- Pourquoi appelle-t-on ce pattern de création de structure "pointeur opaque" ?
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
void matrice_shuffle(matrice_t m);
```

Qui mélange les ligne et les colonnes de la matrice passée en paramètre.
{% endfaire %}
{% info %}
Vous pourrez :

1. créer avec le [mélange de Knuth](./#mélange){.interne} une permutation $t_l$ des indices de lignes et une permutation $t_c$ des indices de colonnes
2. créer une nouvelle matrice `m2`{.language-} avec le même nombre de lignes et de colonnes que `m`{.language-}
3. effectuer `matrice_set(m2, matrice_get(m, i, j), t_l[i], t_c[j])`{.language-} pour tout i et j.
4. terminer en affectant `m2->matrice`{.language-} à `m->matrice`{.language-}
5. libérer la mémoire allouée par `m2`{.language-}.

{% endinfo %}

## Listes doublement chaînées

{% lien %}
[liste chaînée](https://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e)
{% endlien %}

Une liste doublement chaînées est la structure :

```c
typedef _element* element;
struct _element {
  void* data;
  element next;
  element pred;
}
```

Initialisée telle que :

```c
element element_create(void *data) {
  element = malloc(sizeof(struct _element));
  element->data = data;
  element->next = NULL;
  element->pred = NULL;
}
```

Et détruite telle que :

```c
void* element_destroy(element e) {
  void *data = e->data;
  free(e);

  return data;
}
```

Il est important de rendre la donnée sinon on risque la fuite de mémoire.

La liste doublement chaînée est une généralisation de la liste chaînée. Son intérêt en général est de garantir un ordre arbitraire dans une suite où l'ajout et la suppression d'élément est courante.

C'est un trade-off. On optimise l'ajout et la suppression d'éléments au détriment de a localisation d'un élément particulier :

- la liste à une complexité en $\mathcal{O}(1)$ pour accéder au $i$ème élément alors que la liste chaînée est en $\mathcal{O}(n)$
- la liste à une complexité en $\mathcal{O}(n)$ pour supprimer un élément donné quelconque alors que la liste chaînée est en $\mathcal{O}(1)$

{% faire %}
Montrer que dans les cas suivants, une liste chaînée n'est ps avantageuse :

1. si l'on ne modifie que peu la structure ou si l'ajoute/supprime que les derniers élément
2. si l'ordre n'est pas important.
{% endfaire %}

### Unité fonctionnelle

Pour garantir l'utilisation d'une liste doublement chaînée il faut implémenter les élément suivants :

```c
element element_create(void *data);
void* element_destroy(element e);
void element_ajoute_suivant(element e, element suivant);
void element_ajoute_precedent(element e, element precedent);
```

{% faire %}
Implémentez les 4 fonctions précédentes dans l'unité fonctionnelle.
{% endfaire %}

### Utilisation

{% lien %}
<https://medium.com/future-vision/data-structures-algorithms-linked-lists-fc0b8a82d609>
{% endlien %}

On a coutume d'appeler `liste`{.language-} un pointeur sur un élément telle que :

- le champ `data`{.language-} contient `NULL`{.language-}
- le champ `next`{.language-} contient le premier élément de la liste
- le champ `pred`{.language-} contient `NULL`{.language-}

Ce premier élément n'est pas un élément de la liste, mais un élément abstrait. Ceci permet de maintenir unique le début de la liste, même si son premier élément change. Le dernier élément de la liste étant facile à trouver c'est celui tel que son champ `next`{.language-} contient `NULL`{.language-}.

Vous allez implémenter un algorithme qui maintient une liste d'éléments dans l'ordre inverse de leur utilisation.

Vous utiliserez pour cela 10 données de structure :

```c
struct _personne {
  size_t id;
  char *nom;
}

```

Où `id` va de 0 à 9, et choisissez le nom comme vous voulez.

{% faire %}
Créez la liste doublement chaînée contient les 10 données dans l'ordre de leurs id.
{% endfaire %}

Pour afficher le nom de chaque élément de la liste on vous demande de :

{% faire %}
Implémentez la fonction de signature :

```c
void element_parcours(element liste, void (*f)(void *));
```

Qui va appliquer à tous les éléments `e`{.language-} de la liste la fonction : `f(e->data)`{.language-}

{% endfaire %}
{% faire %}
Utilisez `element_parcours`{.language-} avec une fonction `f`{.language-} qui affiche à l'écran l'identifiant suivi du nom de la donnée.

{% endfaire %}

Vous allez maintenant simuler l'utilisation de la liste :

{% faire %}
Faire 13 fois :

1. tirer un nombre aléatoire entre 0 et 9
2. placer la donnée d'identifiant le nombre tiré en tête de liste
3. afficher les données de la liste dans l'ordre

{% endfaire %}
