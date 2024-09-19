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
[Utilisation de `getopt`](https://opensource.com/article/21/8/short-option-parsing-c)
{% endlien %}

{% faire %}
En utilisant la fonction `getopt` définie dans `<unistd.h>`{.fichier} et [`atoi`](https://koor.fr/C/cstdlib/atoi.wp) créez un programme `syracuse`  qui :

- prend un paramètre `x` qui est le premier élément de la liste
- sans option le programme rend la longueur de la suite de Syracuse (v1)
- avec l'option `-l` le programme rend la suite complète de syracuse (v2)

{% endfaire %}
