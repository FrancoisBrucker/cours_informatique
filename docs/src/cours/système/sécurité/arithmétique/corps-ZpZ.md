---
layout: layout/post.njk

title: Corps Z/pZ

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


On définit $(\mathbb{Z}/n\mathbb{Z}, +, \cdot)$ comme l'[anneau](https://fr.wikipedia.org/wiki/Anneau_unitaire#D%C3%A9finition) commutatif tel que :

- les éléments de l'anneau sont des entiers allant de 0 à $n-1$
- l'addition est l'addition usuelle modulo $n$
  - l'élément neutre est 0
  - l'opposé de $x$ est $n-x$
- la multiplication est la multiplication usuelle modulo $n$
  - l'élément neutre est 1
- $x \mod n$ vaut le reste de la division entière de $x$ par $n$

Si $n$ est premier, on dit alors $\mathbb{Z}/n\mathbb{Z}$ c'est même un corps :

- tout élément $x$ a un inverse noté $x^{-1}$
- il est intègre : $x\cdot y = 0$ implique que soit $x$ soit $y$ vaut $0$.

{% info %}
[théorème de Wedderburn](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Wedderburn) montre que tout corps fini est commutatif.
{% endinfo %}

## exponentiation modulaire

L'exponentiation dans l'anneau $\mathbb{Z}/n\mathbb{Z}$ se fait mathématiquement très bien en utilisant l'exponentiation indienne, cependant le nombre de bits des nombres calculés deviennent vite non tractable en pratique.
algo :

{% lien %}
[square and multiply](https://www.youtube.com/watch?v=cbGB__V8MNk)
{% endlien %}

Va très vite !

facile

## logarithme modulaire

très dur.

### Corps $(\\{0, 1\\}, \oplus, \land)$

Le couple $(\\{0, 1\\}, \oplus, \land)$ est un [corps](https://fr.wikipedia.org/wiki/Corps_(math%C3%A9matiques)) où chaque élément est son opposé.


>TBD : anneau commutatif intègre $(\mathbb{Z}/n\mathbb{Z}, +, *)$
>TBD : cas particulier l'anneau $(\mathbb{Z}/2\mathbb{Z}, +, *)$ est un corps.
