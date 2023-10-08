---
layout: layout/post.njk

title: Les variables et leurs types

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Une chaîne de caractère est une suite contiguë de caractères se terminant par le caractère `\0` (son code est l'entier 0). 

Par exemple :

```c
#include <stdio.h>

int main() {

char s[] = {'p', 'o', 'u', 't', 'o', 'u', '\0'};

printf("%s\n", s);

}

```

{%exercice%}

En utilisant la chaîne de caractères définie dans le code précédent :

- quel est la taille de `s` ?
- en utilisant la fonction [`strlen`](https://koor.fr/C/cstring/strlen.wp) déterminez la taille de la chaîne de caractères contenue dans `s`
{% endexercice %}
{% details "solution" %}

> TBD

{% enddetails %}

Si l'on demande à `printf` d'afficher une chaîne de caractère, il va afficher la suite de caractères jusqu'à arriver au caractère `\0`. Ceci permet d'écrire plusieurs chaînes dans un tableau, comme le montre le code suivant :

```c
#include <stdio.h>

int main() {

char s[] = {'p', 'o', 'u', '\0', 't', 'o', 'u', '\0'};

printf("%s\n", s);

}

```

{%exercice%}
En utilisant la chaîne de caractères définie dans le code précédent :

- quel est la taille de `s` ?
- en utilisant la fonction [`strlen`](https://koor.fr/C/cstring/strlen.wp) déterminez la taille de la chaîne de caractères contenue dans `s`
- comment afficher la seconde chaîne de caractères ?
{% endexercice %}
{% details "solution" %}

> TBD :`&s[4]`

{% enddetails %}

Il faut cependant faire très attention, si on oublie d'ajouter `\0` à la fin du tableau, le comportement est UB (et résultera dans le meilleur des cas à un crash).

Pour éviter ceci, `C` fournit l'outil des [*strings literals*](https://learn.microsoft.com/fr-fr/cpp/c-language/c-string-literals?view=msvc-170) :

en écrivant `"une chaîne"`, le compilateur `C` crée dans la partie data du code (même une partie en lecture seule) un tableau contenant toute la chaîne suivie du caractère `\0`. Il est alors possible d'accéder à cette chaîne via un pointeur, comme le montre le code suivant :

```c
#include <stdio.h>

int main() {

char *s = "poutou";

printf("%s\n", s);

}

```

Le pointeur `s` vaut l'adresse du premier caractère du *strings literal*. Ce string literals étant dans la partie en lecture seule de la partie data du programme, il est impossible de la modifier. Tenter de modifier un caractère d'un strings literal est UB.

On peut cependant mixer les deux approchent en écrivant :

```c
#include <stdio.h>

int main() {

char s[] = "poutou";

s[0] = s[3] = 'c';

printf("%s\n", s);

}

```

Son fonctionnement est le suivant :

1. le compilateur `C` place toujours le strings literal dans la partie data du code (il faut bien que la chaîne soit connue à l'exécution)
2. lors de l'exécution, à la création du tableau, les caractères de la strings literal sont copiés dans le tableau (et donc la pile), ce qui permet de les modifier.

{% aller %}
Ce [tutoriel](https://www.codingninjas.com/studio/library/whats-the-difference-between-char-s-and-char-s-in-c) résume les différences dans ces deux modes de création.

{% endaller %}

En particulier :

- s++ impossible sous la forme de tableau
- s[i] = c impossible sous la forme d'un pointeur
- sous la forme d'un pointeur la chaîne est stockée dans la partie data du programme et est non modifiable
- sous la forme d'un tableau la chaîne est stockée dans la pile et est modifiable

{% attention "**danger !**" %}

Si vous stockez des chaînes de caractères dans des tableaux, assurez vous bien d'avoir toujours de la place pour stocker le `\0` final !

{% endattention %}

{% exercice %}

Exécutez le code suivant et expliquer la différence de taille entre les trois tableaux :

```c
#include <stdio.h>
#include <string.h>

int main() {

char *s= "coucou";
char s2[] = "coucou";
char s3[20] = "coucou";

printf("%lu\n", sizeof(s));
printf("%lu\n", sizeof(s2));
printf("%lu\n", sizeof(s3));

}

```

{% endexercice %}

La `libc` de possède de nombreuses fonctions permettant de gérer les chaînes de caractères. Elles sont majoritairement définies dans [`string.h`]
(https://www.w3schools.com/c/c_strings_functions.php). Vous connaissez déjà [`strlen`](https://koor.fr/C/cstring/strlen.wp) mais il y en a de nombreuses autres :

- comparer deux chaînes de caractères
- copier une chaîne dans une autre
- ...

{% exercice %}

Créez un programme qui concatène les trois chaînes "hello", "world" et "!" puis affiche le résultat.
{% endexercice %}
{% details "solution" %}

> TBD

{% enddetails %}

> TBD : > TBD : 
> - char *tab[] = {"coucou", "les", "gars"} idem que char **


## entrées et sorties

### stdout

printf envoie les caractères lues sur stdout. Si l'encodage des caractères est en UTF8 et que stdout l'est aussi, tout se passera bien.

### stdin

Lire des chaînes de caractère depuis stdin peut être assez pénible. Ce [tutoriel](https://www.scaler.com/topics/c/c-string-input-output-function/) explique certaines techniques pour le faire.

{% aller %}
<https://zestedesavoir.com/tutoriels/755/le-langage-c-1/notions-avancees/jeux-de-caracteres-et-encodages/>
{% endaller %}



