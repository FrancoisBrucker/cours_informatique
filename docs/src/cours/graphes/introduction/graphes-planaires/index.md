---
layout: layout/post.njk

title: Graphes planaires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Graphes planaires avec Maria Chudnovski](https://www.youtube.com/watch?v=xBkTIp6ajAg)
{% endlien %}


> thm des 4 couleurs qui est le 1er théorème assisté par ordinateur (pas une IA, c'est la preuve qui est un algorithme)
> tbd 3 colorable un graphe planaire NP-complet !

## Problème

{% aller %}
[Problème de la planarité d'un graphe](./problème/){.interne}
{% endaller %}
  
## Caractérisation des graphes planaires

{% aller %}
[Caractérisation](./caractérisation/){.interne}
{% endaller %}

## Propriétés

{% aller %}
[Propriétés](./propriétés/){.interne}
{% endaller %}

> TBD représentation graphique
> TBD idée 
> TBD forcé : 2-connexe. Est-ce grave ?
> TBD si on ne fait que refaire une représentation partielle ok. Pourquoi est-ce toujours le cas ?

## Algorithmes

### Dessin

> TBD dessin avec 2-connexe <https://perso.ens-lyon.fr/eric.thierry/Graphes2010/lucie-martinet.pdf>

> TBD dessin sans courbure dans un triangle:
>   - exemple <https://ics.uci.edu/~eppstein/gina/schnyder/> ou <https://ics.uci.edu/~eppstein/163/lecture10c.pdf>
>   - papier <https://acm.math.spbu.ru/~sk1/courses/1617f_au3/papers/schnyder-grid-embedding.pdf>

### Reconnaissance

>  Fraysseix–Rosenstiehl et DFS <https://en.wikipedia.org/wiki/Left-right_planarity_test> ; papier <https://arxiv.org/pdf/math/0610935>


## Coloration de graphes planaires

{% aller %}
[Coloration de graphes planaires](./coloration/){.interne}
{% endaller %}

<!-- 

## Odds and ends


- Lemme de Sperner <https://www.youtube.com/watch?v=cpIexccvYjI&list=PLdUzuimxVcC0QCFYP0Af3TNldswjL8_ep&index=18>, on peut le démontrer avec la planarité : <https://www.ams.jhu.edu/~abasu9/AMS_550-472-672/sperner.pdf>. Attention, ce n'est **pas** de la coloration de graphes (pas de contrainte sur les voisins). 
- isomorphisme de graphe planaire
> TBD Theorem (Tutte, 1956). A 4-connected planar graph has a Hamiltonian cycle. 

-->

## Références

{% lien %}
- <https://www.youtube.com/watch?v=wnYtITkWAYA&list=PLGxuz-nmYlQPgIHbqWtgD-F7NnJuqs4fH>
{% endlien %}

<!-- 
- <http://monge.univ-mlv.fr/~goaoc/lec1.pdf>
- <https://personalpages.manchester.ac.uk/staff/mark.muldoon/Teaching/DiscreteMaths/LectureNotes/PlanarGraphs.pdf> --> 

-->
