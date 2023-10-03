---
layout: layout/post.njk

title: Les variables et leurs types

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


{% aller %}
<https://zestedesavoir.com/tutoriels/755/le-langage-c-1/notions-avancees/jeux-de-caracteres-et-encodages/>
{% endaller %}

Une chaîne de caractère est une suite contiguë de caractères se terminant par le caractère `\0`.

En `C` une chaîne de caractère est donc un tableau spécial de caractère (il possède un caractère `\0` qui termine la chaîne). On peut la définir de deux façons :

- sous la forme d'un tableau : `char s[] = "coucou"`
- sous la forme d'un pointeur : `char *s = "coucou"`

L'utilisation de la double quote `"` garantie que `C` ajoute bien le dernier caractère. Ceci permet d'utiliser la fonction `printf` :

```c
#include <stdio.h>
#include <string.h>

int main() {

char *s= "coucou";
char s2[] = "coucou";

printf("%s\n", s);
printf("%s\n", s2);

}

```

Le code précédent est identique à :

```c
#include <stdio.h>
#include <string.h>

int main() {

char s = {'c', 'o', 'u', 'c', 'o', 'u', '\0'};

printf("%s\n", s);

}

```

{% attention %}

- il faut toujours avoir assez de place dans le tableau à stocker pour le '\0' final.
- lire une chaîne qui ne finit pas par 0 done un comportement UB.

{% endattention %}

la `libc` de possède de nombreuses fonctions permettant de gérer les chaînes de caractères. Elles sont majoritairement définies dans [`string.h`]
(https://www.w3schools.com/c/c_strings_functions.php). Il est par exemple possible, avec la fonction [`strlen`](https://koor.fr/C/cstring/strlen.wp) de compter la taille d'une chaîne de caractères :

```c
strlen("coucou"); // rend 6, il ne compte pas le '\0' final.
```

Déclarer une chaîne sous la forme d'un tableau ou d'une chaîne sous la forme d'un tableau ou d'un pointeur est différent : D'un côté, la chaîne est traitée comme un pointeur, de l'autre comme un tableau. Ce [tutoriel](https://www.codingninjas.com/studio/library/whats-the-difference-between-char-s-and-char-s-in-c) explicite les différences.

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

### Écrire

printf envoie les caractères lues sur stdout. Si l'encodage des caractères est en UTF8 et que stdout l'est aussi, tout se passera bien.

### Lire

Lire des chaînes de caractère depuis stdin peut être assez pénible. Ce [tutoriel](https://www.scaler.com/topics/c/c-string-input-output-function/) explique certaines techniques pour le faire.
