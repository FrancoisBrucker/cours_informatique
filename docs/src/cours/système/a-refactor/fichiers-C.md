---
layout: layout/post.njk

title: Fichiers en C

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Un système de fichier est composé de...fichiers. La `libc` propose une grande variété de fonction permettant de les manipuler.

Dans le monde unix, un fichier peut être beaucoup de choses. Nous y reviendrons. Pour l'instant nous nous contenterons de manipuler les éléments les plus représentatifs d'un système de fichiers :

- les fichiers "*réguliers*" (ie composés d'une suite d'octets) stockant des données texte (comme des codes sources), binaire (comme des images) ou des fichiers exécutables
- les dossiers qui organisent hiérarchiquement le système de fichier.

## Contrôle du système de fichier

Les fichiers `<unistd.h>`{.fichier} et `<sys/stat.h>`{.fichier} définissent des fonctions permettant de contrôler le système de fichier.

Certaines fonctions permettent de controller le dossier courant du programme **C** :

- le connaître avec [`getcwd`{.language-}](https://koor.fr/C/unistd.h/getcwd.wp)
- le changer avec [`chdir`{.language-}](https://koor.fr/C/unistd.h/chdir.wp)

> TBD getcwd : comment est stocké le résultat et le type de retour.

D'autres de créer ou de supprimer des dossiers :

    - `mkdir`{.language-}
    - `rmdir`{.language-}

Et enfin les dernières les permissions des fichiers et si besoin les modifier :

- `chmod`{.language-}
- `stat`{.language-}

> TBD stat et mkdir pour check et créer un dossier.

## Structure FILE

Un fichier "*régulier*"

{% lien %}

[Utiliser FILE pour gérer ses fichiers](https://www.youtube.com/watch?v=bOF-SpEAYgk&list=PLhQjrBD2T381k8ul4WQ8SQ165XqY149WW&index=20)

{% endlien %}

Bufferisé pour la rapidité : attention au flush.

## Entrées et sorties formatées

- fprintf
- fscanf

## stdin/out

> test avec un PID dun autre process et envoie du texte dans le stdin d'au autre process
> faire avec 1 fichier C et une commande, puis avec 2 fichiers C.

[stdin/out](https://stackoverflow.com/questions/15883568/reading-from-stdin)

## TBD

aussi [`getwchar`{.language-}](https://www.ibm.com/docs/en/i/7.3?topic=functions-getwchar-get-wide-character-from-stdin) ?

```c

#include <stdio.h>

// ...

while ((c = getchar()) != EOF) {
    putchar(c);
}
  
```

```c
#include <stdio.h>
FILE *fp = stdin; // ou tout autre fichier
char c;

// ...

while ((c = getc(fp)) != EOF) {
    putc(c, stdout);
}
      
```
