---
layout: layout/post.njk

title: Colorabilité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[cours sur la coloration](https://www-sop.inria.fr/members/Frederic.Havet/Cours/coloration.pdf)

{% endlien %}

## Problème

{% aller %}
[Problème de la coloration d'un graphe](./problème/){.interne}
{% endaller %}

## Coloration des sommets

{% aller %}
[Coloration des sommets](coloration-sommets){.interne}
{% endaller %}

## Coloration des arêtes

{% aller %}
[Coloration des arêtes](coloration-arêtes){.interne}
{% endaller %}

## Coloration totale

{% aller %}
[Coloration totale](coloration-totale){.interne}
{% endaller %}
