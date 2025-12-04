---
layout: layout/post.njk

title: "Syracuse"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% info %}
En utilisant le fait que le modulo s'écrit `%`{.language-} en python.
{% endinfo %}

## Écrivez une fonction `syracuse`{.language-} telle que

- **entrée** : un entier $x$
- **sortie** :
  - $x/2$ si $x$ est pair
  - $3x + 1$ si $x$ est impair

## 2. Une fonction qui rend tous les éléments de la suite de Syracuse associée à un nombre

- **entrée** : un entier $x$
- **sortie** : les élément de la suite de Syracuse associée à $x$

La suite de Syracuse est définie telle que :

- $u_0 =x$
- $u_{n+1} = \mbox{syracuse}(u_n)$
- on s'arrête lorsque $u_n =1$

## 3. Le programme principale demande à l'utilisateur de taper un nombre et rend la suite de Syracuse de ce nombre

- vous supposerez que l'utilisateur ne se trompe pas (pas besoin de gérer ses erreurs potentielles)
- vous utiliserez [la fonction `input()`{.language-}](https://docs.python.org/fr/3.13/library/functions.html#input) qui rend une chaîne de caractères tapée par l'utilisateur
- `int(x)`{.language-} est l'entier représenté par la chaîne de caractère `x`{.language-}.
