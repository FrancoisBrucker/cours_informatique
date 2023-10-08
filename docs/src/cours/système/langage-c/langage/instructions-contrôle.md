---
layout: layout/post.njk

title: Instructions de contrôle

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


En `C` le type booléen n'existe pas (il existe cependant un `typedef`{.language-} pour cela). Les tests qui résultent d'une condition booléenne comparent des entiers :

- la condition est vraie s'il est strictement positif
- elle est fausse s'il vaut 0

Outre l'utilisation d'entiers, on peut créer un booléen (0 ou 1) grâce aux opérateurs relationnels :

- `==`{.language-} : égalité
- `!=`{.language-} : différence
- `<`{.language-} ou `>`{.language-} : comparaison stricte
- `<=`{.language-} ou `>=`{.language-} : comparaison large

{% attention "**danger !**" %}
Les comparaisons ne fonctionnent pas avec des tableaux ou les chaînes de caractères.

Pour ces deux types, il peut utiliser des fonctions comme [`strcmp`{.language-}](https://fr.wikipedia.org/wiki/Strcmp) pour les chaines de caractères et [`memcmp`{.language-}](https://www.tutorialspoint.com/c_standard_library/c_function_memcmp.htm) pour comparer des plages de mémoire.
{% endattention %}

Combiner des conditions logiques se fait grâce aux opérateurs logiques :

- `&&`{.language-} : et
- `||`{.language-} : ou
- `!`{.language-} : non

Pour les conditions utiliser les [opérateurs logiques](https://www.tutorialspoint.com/cprogramming/c_logical_operators.htm).

{% attention "**danger !**" %}
Ne confondez pas `&&` qui est la condition logique et `&` qui est la comparaison bit à bit (idem pour `||` et `|`).

Comme on compare des entiers, c'est souvent identique mais il existe des cas où le résultat va être différent, donc préférez les opérateurs logique lorsque vous faite de la logique.
{% endattention %}

## If/else

```c
if (condition) {
  // bloc if
} else {
  // bloc else
}
```

Le else est facultatif.

{% attention "**danger !**" %}
Un bloc en `C` est :

- soit une instruction
- soit des instructions entouré d'accolades

Il est donc techniquement possible d'écrire :

```c

int i = -1;

if (i > 0) 
  printf("positif");
```

Ne le **faites cependant pas**, car souvent plus tard, on veut rajouter une ligne à cette condition et on écrira :

```c

int i = -1;

if (i > 0) 
  printf("strictement");
  printf("positif");
```

Qui est faut (la seconde instruction ne fait pas partie du `if`) à la place de :

```c

int i = -1;

if (i > 0) {
  printf("strictement");
  printf("positif");
}
```

Ce type de bug est très difficile à voir car l'œil est porté par les indentations et non les accolades...

EN conclusion : **utilisez toujours des `{}` dans vos conditions**.
{% endattention %}

La structure `elif` n'existe pas en `C`. On chaîne les tests :

```c
if (condition) {
  // bloc if
} 
else if (condition2) {
  // bloc else if
} else {
  // bloc else
}
```

> TBD exemple

## Opérateur ternaire

```c
condition ? expr2 : expr2;
```

Qui est équivalent à :

```c
if (condition) {
  expr1
} else (
  expr2
)
```

Vous verrez souvent ce genre de construction incluse dans une autre instruction. Vois par exemple [ce tutoriel](https://www.freecodecamp.org/news/c-ternary-operator/).

> TBD exercice

## While

Deux *flavors* de while :

```c
while (condition) {
  // bloc while
}
```

et :

```c
do {
  // bloc do while
} while (condition)
```

> TBD exemple

## Boucle for

```c
for (expr1 ; condition ; expr2) {
  // bloc for
}
```

Qui est équivalent à la structure while :

```c
expr1;
while (condition) {
  
  // bloc for

  expr2;
}
```

```c
for (size_t i = 0 ; i < 10 ; i++) {
  printf("%zu ", i);
}
printf("\n");
```

{% attention "**danger !**" %}
On se trompe rapidement dans l'ordre et les paramètres d la boucle for. En core une fois le mieux qui peut vous arriver est une erreur :

- l'échange de condition de fin et de test fonctionne de temps en temps
- remplacer les `;` par des `,` *peut* fonctionner (voir [`,` est un opérateur en C](https://en.wikipedia.org/wiki/Comma_operator))
- oublier un paramètre fonctionne. Par exemple, ceci : `for(;;) {}`{.language} est parfaitement légitime...
- etc

Bref, vérifier toujours deux fois vos boucles for.
{% endattention %}

## Switch

L'instruction `switch`{.language-} permet d'effectuer des actions différentes selon les modalités (discrètes) d'une variable

```c
switch (expression)
​{
    case constante1:
      // cas 1
      break;

    case constante2:
      // cas 2
      break;
    default:
      // par défaut
}
```

Si vous omettez le break, les instructions vont continuer. Exécutez par exemple le code ci-dessous puis supprimez les lignes 9 et 12.

```c#
#include <stdio.h>

int main() {
  int i = 0;
  switch (i)
  ​{
      case 0:
        printf("vaut 0\n");
        break;
      case 1:
        printf("vaut 1\n");
        break;
      default:
        printf("différent de 0 et 1\n");
  }
}
```

## Break/continue

Comme en python :

- [break](http://ressources.unit.eu/cours/Cfacile/co/Chap5_p14.html)
- [continue](http://ressources.unit.eu/cours/Cfacile/co/Chap5_p13.html)
