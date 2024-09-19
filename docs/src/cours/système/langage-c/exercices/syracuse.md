---
layout: layout/post.njk

title: Syracuse

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Variation sur le thème de la [suite de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse#Suite_de_Syracuse).

## <span id="syracuse-v1"></span> Un élément

{% faire %}
Créez une fonction qui rend le nombre d'étapes nécessaire pour arriver à 1 pour la [suite de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse#Suite_de_Syracuse) d'en entier passé en paramètre. Sa signature doit être :

```c
int syracuse_nb(int nombre);
```

Si le nombre passé en paramètre est plus petit ou égal à 1, la fonction doit rendre 0.
{% endfaire %}
{% faire %}

Demandez à l'utilisateur de rentrer un entier relatif (vous utiliserez la fonction [`scanf`{.language-}](../../langage/pointeurs/#scanf){.interne})dont vous donnerez le nombre de syracuse.

{% endfaire %}

## <span id="syracuse-v2"></span> Tous les éléments

{% faire %}
Créez une fonction (et testez la) qui rend tous les éléments de la suite de [suite de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse#Suite_de_Syracuse) d'un entier passé en paramètre. Sa signature doit être :

```c
int *syracuse_tab(int nombre);
```

Si le nombre passé en paramètre est est plus petit ou égal à 1, la fonction doit rendre le pointeur `NULL`{.language}.

{% endfaire %}

## <span id="syracuse-v3"></span> Paramètres d'exécutables

{% lien %}
[Utilisation de paramètres d'exécution](https://opensource.com/article/21/8/short-option-parsing-c)
{% endlien %}

{% faire %}
Créez un programme `syracuse`  qui prend un entier en paramètre et rend la liste des éléments de sa suite de syracuse. On faudra appeler le programme avec un paramètre, par exemple : `syracuse 20`.

Vous devrez certainement utiliser la fonction [`atoi`{.language-}](https://koor.fr/C/cstdlib/atoi.wp) qui transforme une chaîne de caractères en entier.

Faites également en sorte que si le programme n'a pas exactement un paramètre ou que son paramètre ne corresponde pas à un entier strictement positif le programme s'arrête.
{% endfaire %}

{% faire %}
Utilisez maintenant la fonction [`getopt`](https://www.gnu.org/software/libc/manual/html_node/Getopt.html) définie dans `<unistd.h>`{.fichier} pour ajouter une option facultative `-n` qui rend, en plus de la liste de syracuse, le nombre d'élément en premier. On pourra appeler syracuse de deux manières : `syracuse 20` ou `syracuse -n 20`.

{% endfaire %}
