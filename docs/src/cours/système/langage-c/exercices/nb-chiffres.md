---
layout: layout/post.njk

title: Nombre de chiffres d'un entier

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Créez une fonction qui rend le nombre de caractères utilisés pour écrire un entier (positif ou négatif) écrit en base 10. Par exemple 42 est composé de 2 chiffres en base 10, 7 seulement d'un seul et -1 de deux.

Vous implémenterez cette fonction de 3 manières différentes. Vous ajouterez chaque fonction dans le même fichier `nombre-chiffres.c`{.fichier}.

## V1

{% faire %}
Utilisez une boucle qui divise par 10 le nombre tant qu'il est > 10 pour coder cette fonction.

Sa signature doit être :

```c
int nb_chiffre_v1(int i);
```

{% endfaire %}

{% faire %}

Testez la fonction codée avec 123456, 0 et -1.

{% endfaire %}

## Valeurs de test

{% faire %}

Rangez vos trois valeurs de test (123456, 0 et -1) dans un tableau d'entiers et affichez à l'écran leurs valeurs et leurs nombre de chiffres dans une boucle `for`{.language-}.

{% endfaire %}

## V2

{% faire %}
Utilisez la fonction `log10` définie dans [`<math.h>`{.fichier}](https://fr.wikipedia.org/wiki/Math.h) pour coder cette fonction.

```c
int nb_chiffre_v2(int i);
```

{% endfaire %}
{% info %}

- vous pourrez aussi être amené à utiliser la fonction [`ceil`{.language-}](https://en.cppreference.com/w/c/numeric/math/ceil) de [`<math.h>`{.fichier}](https://fr.wikipedia.org/wiki/Math.h)
- Il vous faudra sûrement inclure la bibliothèque math (`-lm`) lors de la compilation (pour la phase de l'édition de lien)

{% endinfo %}

## V3

{% faire %}
Utilisez la fonction [`sprintf`](https://www.tutorialspoint.com/c_standard_library/c_function_sprintf.htm) définie dans `<stdlib.h>`{.fichier} et la fonction [`strlen`](https://koor.fr/C/cstring/strlen.wp#google_vignette) définie dans `<string.h>`{.fichier}  pour coder cette fonction.

```c
int nb_chiffre_v3(int i);
```

{% endfaire %}
{% info %}

Attention à [`sprintf`](https://www.tutorialspoint.com/c_standard_library/c_function_sprintf.htm), elle ne renvoie rien. Elle modifie le contenu du pointeur de chaîne de caractères placée n premier paramètre.

Il faut s'assurer d'avoir la place de stocker votre résultat soit en le déclarant soit avec un tableau soit avec un `malloc`{.language-} en choisissant bien la taille (nombre de caractères avec un tableau, nombre de bytes avec un `malloc`{.language-}), par exemple 100.
{% endinfo %}

## Cerise sur le gâteau

{% faire %}

Demandez à l'utilisateur de rentrer un entier relatif (vous utiliserez la fonction [`scanf`{.language-}](../../langage/pointeurs/#scanf){.interne}) dont vous donnerez également le nombre de chiffres.

{% endfaire %}
