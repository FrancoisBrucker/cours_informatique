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

## Petites fonctions

Vos fonctions ne doivent produire ni erreurs ni warnings en utilisant les options de compilation :

```
-Wall -Wextra -pedantic -std=c23
```

### Nombre de chiffres d'un entier

{% faire %}
Créez une fonction qui rend le nombre de chiffre d'un entier (positif ou négatif). Sa signature doit être :

```c
int nb_chiffres(int nombre);
```

{% endfaire %}

### Syracuse v1

{% faire %}
Créez une fonction (et testez la) qui rend le nombre d'étapes nécessaire pour arriver à 1 pour la [suite de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse#Suite_de_Syracuse) d'en entier passé en paramètre. Sa signature doit être :

```c
int syracuse(int nombre);
```

Si le nombre passé en paramètre est négatif ou nul, la fonction doit rendre -1.
{% endfaire %}

### <span id="syracuse-v2"></span>Syracuse v2

{% faire %}
Créez une fonction (et testez la) qui rend tous les éléments de la suite de [suite de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse#Suite_de_Syracuse) d'en entier passé en paramètre. Sa signature doit être :

```c
int *syracuse_tab(int nombre);
```

Si le nombre passé en paramètre est négatif ou nul, la fonction doit rendre le pointeur `NULL`{.language}.

{% endfaire %}

### Liste

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
Testez la fonction précédente en tirant 100000 nombres réels entre 0 et 1 et vérifiez que sa moyenne vaut environ `.5`.
{% endfaire %}

### Compilation séparée

{% faire %}
Décomposez le code en deux unités fonctionnelles :

- le programme principal (fichier `main.c`{.fichier})
- le module aléatoire (deux fichiers `aleatoire.c`{.fichier} et `aleatoire.h`{.fichier})

Créez un fichier `Makefile`{.fichier} pour gérer la compilation de ce projet.
{% endfaire %}

## Matrice

On souhaite créer un module permettant de gérer des matrices d'entiers.

### Implémentation v1

{% faire %}
Si l'on considère une matrice comme un tableau de lignes, implémentez une fonction de signature :

```c
int **matrice_nulle(size_t nombre_lignes, size_t nombre_colonnes);
```

Qui crée dynamiquement une matrice où chaque élément vaut 0.
{% endfaire %}
{% faire %}
Créez dans le programme principal une fonction qui crée une matrice à 4 lignes et 6 colonnes et affecte $i+j$ à l'élément de ligne $i$ et de colonne $j$.
{% endfaire %}
{% faire %}
Créez une fonction qui affiche à l'écran une matrice crée par la fonction `matrice_nulle`{.language-}. Elle devra afficher par exemple :

```
1  2   3
11 4 111
```

Vous pourrez utiliser la fonction `nb_chiffres` crée dans un exercice précédent et utiliser le [formatage des entiers](https://www.lix.polytechnique.fr/~liberti/public/computing/prog/c/C/FUNCTIONS/format.html) de printf pour justifier les entiers à droite.
{% endfaire %}

{% faire %}
Créez une fonction de signature :

```c
void free_matrice(int **matrice, size_t nombre_lignes, size_t nombre_colonnes);
```

Qui supprime une matrice précédemment crée avec la fonction `matrice_nulle`{.language-}.
{% endfaire %}
{% faire %}
Peut-on simplifier la fonction précédente en :

- supprimant le paramètre `nombre_colonnes`{.language-} ?
- supprimant le paramètre `nombre_lignes`{.language-} ?

Si oui, le faire.
{% endfaire %}

### Implémentation v2

{% faire %}
La fonction précédente peut créer des défauts de cache si l'on 
Si l'on considère une matrice comme un tableau de lignes, implémentez une fonction de signature :

```c
int **matrice_nulle(size_t nombre_lignes, size_t nombre_colonnes);
```

Qui crée une matrice où chaque élément vaut 0.
{% endfaire %}

> TBD rendre matrice
> puis rendre structure

### Type opaque

{% faire %}
En utilisant ce post sur les listes chaînées et leur utilisation sous la forme d'un [type opaque](https://x0r.fr/blog/30).
{% endfaire %}

> TBD rendre matrice

### Aléatoire

0 ou 1 avec proba.

- ou placer la matrice :
  - faire une VLA avec paramètre dans une fonction : dans la pile
  - rendre un pointeur int* et malloc
  - rendre un [pointeur opaque](https://interrupt.memfault.com/blog/opaque-pointers) sur une struct plus les fonction pour les gérer plus .h et .c

- remplir aléatoirement avec des 0 ou 1 et probas.
- <https://stackoverflow.com/questions/822323/how-to-generate-a-random-int-in-c>
- `random_value = (double)rand()/RAND_MAX*2.0-1.0;//float in range -1 to 1`
- nb lignes et colonnes en paramètre : retour (*int[][] ?)
- lire élément par élément avec un int*

### Mallocs de Structures

malloc et free d'un tableau de structure et utilisation

## Syracuse

- ajout option avec getopt



## Lecture et buffer

<http://sekrit.de/webdocs/c/beginners-guide-away-from-scanf.html>

- scanf : attention buffer overflow
- avec strcmp pour stopper (si vide)
- scanf avec espaces
- scanf limité en taille
- while et getchar avec char32 pour être sur d'avoir un caractère utf8
- tableau de str (char**)

## Qui est en Base

### Base16

{% faire %}
<https://en.wikipedia.org/wiki/Base64>
{% endfaire %}

décalage à droite et gauche de 4 bit pour faire la chaîne.

base16. Avec un décalage de 4bit puis reconstruction

### Base64

1. décalage de bit
2. conversion de 3 byte.
3. association pour reconstruire la fin
4. déconversion pour reconstruire le stream.
  
{% faire %}

- <https://en.wikipedia.org/wiki/Base64>
- <https://stackoverflow.com/questions/342409/how-do-i-base64-encode-decode-in-c>

{% endfaire %}
