---
layout: layout/post.njk

title: Graphes parfaits

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Graphes parfait avec Maria Chudnovsky](https://www.youtube.com/watch?v=C4Zr4cOVm9g)
{% endlien %}

- [$\omega(G)$](../structure/#definition-notation-clique-stable-maximum){.interne}
- [$\chi(G)$](../colorabilité/#definition-notation-coloration-minimum){.interne}

> TBD def
>
> TBD différence non bornée : <https://perso.ens-lyon.fr/edouard.bonnet/publi/tree-zykov.pdf> et <https://math.uchicago.edu/~may/VIGRE/VIGRE2008/REUPapers/Zhang.pdf>
> TBD dessins de quelques graphes parfait
>
> NP complet en general mais poly en perfect graphs : <https://www.graphclasses.org/classes/gc_56.html> et <https://en.wikipedia.org/wiki/Perfect_graph#Algorithms>

On en connaît déjà :

- graphes biparti (donc les arbres)
- line graphs

Et il y en a plein d'autres :

- [graphes cordées](https://fr.wikipedia.org/wiki/Graphe_cordal) (https://math.stackexchange.com/questions/4045122/why-are-chordal-graphs-always-perfect-graphs), donc aussi [les graphes d'intervalles](https://fr.wikipedia.org/wiki/Graphe_d%27intervalles)
- [graphes de comparabilités](https://fr.wikipedia.org/wiki/Graphe_de_comparabilit%C3%A9)
- ...

> TBD exo : Threshold graphs are perfect : <https://en.wikipedia.org/wiki/Threshold_graph>

[Strong Perfect Graph Theorem (179 pages sans un seul dessin)](https://annals.math.princeton.edu/wp-content/uploads/annals-v164-n1-p02.pdf)

Le théorème fort des graphes parfait permet de faire des algorithmes de reconnaissance polynomiaux : <https://algorithms.leeds.ac.uk/wp-content/uploads/sites/117/2017/09/FOCS03final.pdf>

On va montrer ici un théorème plus simple :

> [Weak Perfect Graph Theorem](https://www.youtube.com/watch?v=Koc63QhxPgk)

> tbd le line graph d'un graphe biparti est parfait.
