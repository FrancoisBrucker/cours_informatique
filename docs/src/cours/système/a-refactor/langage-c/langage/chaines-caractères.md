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

> TBD : char *tab[] = {"coucou", "les", "gars"} idem que char **

## entrées et sorties

### stdout

printf envoie les caractères lues sur stdout. Si l'encodage des caractères est en UTF8 et que stdout l'est aussi, tout se passera bien.

### stdin

Lire des chaînes de caractère depuis stdin peut être assez pénible. Ce [tutoriel](https://www.scaler.com/topics/c/c-string-input-output-function/) explique certaines techniques pour le faire.

{% aller %}
<https://zestedesavoir.com/tutoriels/755/le-langage-c-1/notions-avancees/jeux-de-caracteres-et-encodages/>
{% endaller %}

## Unicode

{% lien %}
<https://beej.us/guide/bgc/html/split/unicode-wide-characters-and-all-that.html>
{% endlien %}

On rappelle qu'un `char` en `C` est le plus petit adressage possible. Sur (quasi) toutes les architectures, ce type est composé de 1 byte.

L'encodage par défaut de toute chaîne de caractère est actuellement utf-8.

{% lien %}

[utf8](https://fr.wikipedia.org/wiki/UTF-8)

{% endlien %}

Cet encodage est une façon de représenter des [*codepoint* Unicode](https://fr.wikipedia.org/wiki/Unicode) par un ou plusieurs byte. Il est donc tout à fait raisonnable d'utiliser des suite de char pour représenter une chaîne de caractères encodée en utf8.

Il faut cependant faire attention si l'on cherche à représenter ou afficher un caractère Unicode encodé en utf8, car les seuls caractères Unicode représentés par un unique byte (1 `char`{.language-}) sont ceux de [la table ASCII](https://en.wikipedia.org/wiki/ASCII), de code allant de 1 à 127 (le code 0 étant égal à la fin de la chaîne).

Le code suivant fonctionne donc uniquement avec des caractères de la table ASCII :

```c
char c = 'A'

printf("Caractère : %c\n", c);
printf("Code Unicode associé : %i\n", c);
```

### Caractères multi-bytes

Les codes supérieurs ou égal à 128 sont encodés sur plusieurs bytes, donc plusieurs `char`{.language-}. Par exemple le caractère Unicode "é" de code 233 (0xe9 en hexadécimal) est représenté par 2 bytes valant respectivement 195 (0xc3 en hexadécimal) et 169  (0xa9 en hexadécimal). Ces deux caractères sont des char `char`{.language-} mais ne peuvent être représentés graphiquement isolément.

Le `C` ne présuppose par si le type char doit être considéré comme un entier signé ou non. Le code suivant peut donc ou pas donner le bon résultat :

```c
char *s = "é"; // 2 char pour encoder é

printf("Caractère : %s ; Code utf8s associé : %i et %i\n", s, s[0], s[1]);
```

Il se trouve que :

- sur Linux, il donne le bon résultat `Caractère : é ; Codes utf8 associé : 195 et 169`
- sur mon mac, il donne le résultat `Caractère : é ; Codes utf8 associé : -61 et -87`

Sous Linux le type char est non signé alors qu'il l'est sur mon mac...

{% attention "**Danger !**" %}
N'utilisez jamais le type char tel quel pour représenter des entiers, vous ne savez pas s'ils seront signé ou non.
{% endattention %}

Pour éviter toute confusion, dans sa version c23, le `C` définit le type `char8_t`{.language-} dans `<uchar.h>`{.fichier} pour garantir que ce char est non signé et qu'il peut être utilisé pour représenter les entier associés aux caractères multi-byte de l'utf8. Il correspond à :

```c
typedef unsigned char char8_t;
```

Le code suivant fonctionnera donc toujours :

```c
printf("Caractère : %s ; Code utf8 associé : %i, %i\n", s, (char8_t)s[0], (char8_t)s[1]);
```

Si on a :

- soit définit le type `typedef unsigned char char8_t;`
- soit inclut `<uchar.h>`{.fichier} comme fichier d'entête sous le standard c23 (attention, ce header n'existe pas sous mac)

### wide characters

Si l'on ne veut pas d'encodage multi-byte, on peut utiliser le type `wchar_t`{.language-} défini dans `<wchar.h>`{.fichier}. Sur 99.9% des systèmes ce type correspond à un entier sur 32b qui contient directement le point de code Unicode, sans conversion.

Un point de code Unicode tenant sur 21bits, un type sur 4B est la taille minimum pour le contenir (il n'existe pas de structure entière sur 3 bytes. On ne garde que des puissances de 2 : 1, 2, 4 et 8).

On peut écrire directement une chaîne de caractère en `wchar_t`{.language-} en préfixant le *string literal* par un L :

```c
#include <stdio.h>
#include <wchar.h>


typedef unsigned char char8_t;

int main() {
wchar_t wc = L'é'; // 1 wchar_t pour encoder é

printf("Taille d'un wide char : %zu \n", sizeof(wchar_t));
printf("Pointcode : %i \n", wc);

}

```

{% attention "**Danger !**" %}
Ce à quoi correspond un `wchar_t`{.language-} n'est pas défini et dépend du locale. Il est dans 99.9% du temps égal à un pint de code Unicode sur 4 bytes, mais ce n'est pas garanti.

Oui, c'est nul.
{% endattention %}

{% attention "**Danger !**" %}
Il existe aussi l'encodage utf16, sur 2 bytes mais je ne vois aucune raison raisonnable d'utiliser un tel codage.
{% endattention %}

### Conversion

{% lien %}
[Conversion `char`{.language-} vers `wchar_t`{.language-}](https://zestedesavoir.com/tutoriels/755/le-langage-c-1/notions-avancees/les-caracteres-larges/)
{% endlien %}

{% attention "**Danger !**" %}
Pour faire fonctionner les conversion, il faut charger une locale spécifique (par défaut cette locale est "C" qui ne connaît que l'ASCII).

{% endattention %}

> TBD example de conversion et vérification de la taille finale.

### c23

Le standard c23 essaie de mettre un peu d'ordre dans ces conversions. On définit dans `<uchar.h>`{.fichier} :

- le type `char8_t`{.language-} (qui est un `unsigned char`{.language-} sur quasi tout système)
- le type `char32_t`{.language-} (qui est un `unsigned int`{.language-} sur quasi tout système)

On peut également directement écrire :

- `u8"une chaîne en utf8"`{.language-} ce qui dans 99.9% du temps est equivalent à `"une chaîne en utf8"`{.language-}
- `U"une chaîne en utf32"`{.language-} ce qui dans 99.9% du temps est equivalent à `L"une chaîne en utf32"`{.language-}

{% info %}
Il existe aussi `u"une chaîne en utf16"`{.language-} pour un encodage en utf16, mais il ne faut pas l'utiliser puisque le format utf16 est une aberration de la nature et ne devrait pas exister.
{% endinfo %}

> TBD : conversion c23 lorsque ça sera inclut dans le llvm mac.

Ce nest cependant pas encore parfait, mais tout devrait cependant bien se passer si vous compilez vos programmes pour un système récent.
