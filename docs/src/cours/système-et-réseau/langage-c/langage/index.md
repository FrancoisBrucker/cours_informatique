---
layout: layout/post.njk

title: Langage C

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


{% attention "**danger !**" %}
Le `C` est un langage de bas niveau et fait pour être exécuté rapidement. Les conséquences sont :

- il vous permet de tout faire
- il ne vérifie pas vos actions

Il y a donc quelques règles à respecter pour se simplifier la tâche de développement :

- être explicite
  - pas de magic number
  - typage explicite
- on ne fait pas le malin :
  - avec le préprocesseur
  - avec les subtilités syntaxiques du langage

{% endattention %}

Le `C` est organisé autour d'une fonction principale appelée main.

Cette fonction va contenir le corps du programme. Elle peut être définie de plusieurs manière, nous utiliserons en majorité celle ci :

```c
int main (){

  return 0;
}
```

- cette fonction ne prend pas de paramètres
- son retour sera le retour du process qui exécutera le code compilé. Si c'est 0 tout est ok.

Toutes les fonctions que l'on ne définira pas seront ajoutée dans la partie édition de lien. Pour que le compilateur soit content il faudra que leur signature soit définie, ceci se fait via les instructions préprocesseur `#include <nomlib.h>` qui incluent les headers de la bibliothèque utilisée.

L'exemple minimal est celui donné précédemment :

```c#
#include <stdio.h>

int main() { 
    printf("Hello World!\n");

    return 0; 
}
```

Qui utilise la fonction de la libc `printf`{.language-} dont la signature est définie dans le fichier de header `stdio.h`{.fichier}.

## Commentaires

Deux types de commentaires.

Sur plusieurs lignes :

```c
/* un commentaire sur 

plusieurs

lignes

*/
```

Tout ce qui est entre `/*` et `*/` est ignoré

{% attention "**danger !**" %}

Les commentaires ne peuvent être imbriqués :

```c

/* /* */ */

```

N'est pas un commentaire valide en `C`.

{% endattention %}

Sur une ligne :

```
// commentaire sur une ligne
```

Tout ce qui est après `//` sur la même ligne est ignoré.

## Bases

### Types de données

{% aller %}
[Types de données](types-base){.interne}
{% endaller %}

### Fonctions

{% aller %}
[Fonctions](fonctions){.interne}
{% endaller %}

### Structures de contrôle

{% aller %}
[Instructions de contrôle](instructions-contrôle){.interne}
{% endaller %}

## Pointeurs

{% aller %}
[Pointeurs](pointeurs){.interne}
{% endaller %}

## Types dérivés

Les types dérivés sont des collections de types de base (entier, réel, caractère ou pointeur).

### Tableaux

{% aller %}
[Tableaux](tableaux){.interne}
{% endaller %}

### Chaînes de caractères

{% aller %}
[Chaînes de caractères](chaines-caractères){.interne}
{% endaller %}

### Structures

{% aller %}
[Structures](structures){.interne}
{% endaller %}

### enum

Le `C` permet aussi d'utiliser des [enum](https://www.w3schools.com/c/c_enums.php) pour gérer des modalités discrètes.

## Types complexes

{% lien %}

- [règle de la spirale](https://c-faq.com/decl/spiral.anderson.html)
- [comprendre les types alambiqués de C](https://www.codeproject.com/Articles/7042/How-to-interpret-complex-C-C-declarations)

{% endlien %}

## Gestion de la mémoire

{% aller %}
[Gestion du tas](gestion-tas){.interne}
{% endaller %}

## Ligne de commande

Pour utiliser les paramètres du programme, on peut écrire la fonction main ainsi :

```c
int main(int argc, char *argv[argc+1]) {

for (size_t i = 0; i < argc; i++) {
     printf("l'argument numéro %d vaut %s", i, argv[i]);
 }

}
```

- `argc` est le nombre de paramètres passés au programme
- `argv` est un tableau de chaines de caractères correspondant au tableau `$@` des scripts. Il contient :
  - le nom du programme en premier élément
  - les options passées dans l'ordre comme éléments suivant
  - un pointeur nul (`NULL`{.language-}) en fin de tableau

Vous verrez aussi les signatures suivantes, équivalentes :

- int main(int argc, char *argv[])
- int main(int argc, char **argv)

Obtenir les valeurs d'une variable d'environnement peut se faire avec la fonction [getenv](https://koor.fr/C/cstdlib/getenv.wp) de la libc (définie dans `<stdlib.h>`{.fichier}) :

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

for (size_t i = 0; i < argc; i++) {
     printf("l'argument numéro %d vaut %s", i, argv[i]);
 }

const char* s = getenv("PATH");
printf("PATH :%s\n", (s != NULL) ? s : "pas de PATH défini");

}
```

{% lien %}
<https://www.thegeekstuff.com/2013/01/c-argc-argv/>
{% endlien %}

## Règles

Attention aux [Undefined Behavior (UB)](https://en.wikipedia.org/wiki/Undefined_behavior) résultant d'erreur de code qui font que :

- ces erreurs ne sont pas détectées à la compilation
- elles produisent des résultats différents selon les fois, les gens ou les compilateurs.

Voir par exemple [ce court tuto](https://www.youtube.com/watch?v=VONnWLo7abU) ou [celui-ci](https://www.youtube.com/watch?v=va_UZwTVR5g) (un peu plus long)

Cela rend le déboguage très difficile. Il faut donc toujours essayer d'être le plus explicite possible et surtout rester simple.
