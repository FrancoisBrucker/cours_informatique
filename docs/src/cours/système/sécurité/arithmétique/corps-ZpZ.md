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


- corps -> intègre
- corps -> commutatif ([théorème de Wedderburn](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Wedderburn))
- 
Nous allons lister ici ces différentes notions et nous y ferons un rappel dans le cours si besoin. Nous nous restreignons bien sur au structures finies. De là tout cours sera commutatif .


## exponentiation modulaire

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
