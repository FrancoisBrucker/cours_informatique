---
layout: layout/post.njk

title: Électronique

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On montrera ici juste le strict nécessaire pour se convaincre que l'on peut construire pour de vrai un ordinateur.

On va voir comment associer un signal électrique à des bits et les combiner sous la forme de formules logiques.

{% lien %}
- [CODE, de Charles Petzhold](https://www.amazon.fr/Code-Language-Computer-Hardware-Software/dp/0137909101/)
- [Circuits and electronics (MIT 6.002)](https://www.youtube.com/watch?v=AfQxyVuLeCs&list=PL9F74AFA03AA06A11)
{% endlien %}

On a vu que toutes les formules logiques peuvent s'écrire sous la forme d'un DAG où les sommets sont :

- les variables et alors il n'a pas de sommets entrant
- la sortie et alors il n'a pas de sommets sortant
- l'opération NON : une entrée et au une sortie
- l'opération OU ou ET : deux entrée et une sortie
- un nœud de transit avec au moins une entrée et au moins une sortie.

On utilise ensuite l'intensité ou la tension pour les états :

- $\leq K_0$ pour l'état 0
- $\geq K_1$ pour l'état 1

C'est Shannon qui a le premier montré la faisabilité  de créer un réseau booléen en utilisant des relais.

{% lien %}
[A Symbolic Analysis of Relay and Switching Circuits (Shannon, 1938)](https://en.wikipedia.org/wiki/A_Symbolic_Analysis_of_Relay_and_Switching_Circuits)
{% endlien %}

## Bases physique

{% aller %}
[Bases physiques](./bases-physique/)
{% endaller %}

## Circuits

{% aller %}
[Circuits électroniques](./circuits/)
{% endaller %}
