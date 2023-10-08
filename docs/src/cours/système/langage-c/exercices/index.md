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

## Nombres aléatoires

Le but de cet exercice est de comprendre la compilation séparée, tout en jouant avec les nombres.

### Étude préliminaire

- Toutes les fonctions sont à écrire dans le programme principal, en dehors de la fonctions main.
- Le programme main doit permettre de tester chaque fonction demandée

{% faire %}
Créez une fonction de signature :

```c
int aléatoire_int(int min, int max);
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
int *aléatoire_int(int max, size_t nombre);
```

Qui tire : `nombre` nombre aléatoires entre 0 et max (inclus) et rend un tableau de max+1 cases (alloué dynamiquement) contenant pour chaque indice le nombre de fois où l'indice a été tiré.
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

.c et .h des fonctions aléatoires

### Matrice

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

### Lecture et buffer

<http://sekrit.de/webdocs/c/beginners-guide-away-from-scanf.html>

- scanf : attention buffer overflow
- avec strcmp pour stopper (si vide)
- scanf avec espaces
- scanf limité en taille
- while et getchar avec char32 pour être sur d'avoir un caractère utf8
- tableau de str (char**)

### Syracuse

- function
- lecture par ligne de commande
- ajout option avec getopt

### Qui est en Base

> compilation séparée.

#### Base16

{% faire %}
<https://en.wikipedia.org/wiki/Base64>
{% endfaire %}

décalage à droite et gauche de 4 bit pour faire la chaîne.

base16. Avec un décalage de 4bit puis reconstruction

#### Base64

1. décalage de bit
2. conversion de 3 byte.
3. association pour reconstruire la fin
4. déconversion pour reconstruire le stream.
  
{% faire %}
- <https://en.wikipedia.org/wiki/Base64>
- <https://stackoverflow.com/questions/342409/how-do-i-base64-encode-decode-in-c>
{% endfaire %}

### Tableaux de Pointeurs de fonctions

Tableaux de pointeurs de fonctions dans une boucle for

### Makefile et lib

- plusieurs fichier et makefile
- lib pas par défaut ? Sha-1 ?
