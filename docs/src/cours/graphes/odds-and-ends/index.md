---
layout: layout/post.njk
title: Odds ena ends

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD à recaser là où on en parle.







## Graphes dérivés

A tout graphe on peut lui associer d'autres graphes, dérivés de celui-ci.

### Graphe complémentaire

{% lien %}
<https://fr.wikipedia.org/wiki/Graphe_compl%C3%A9mentaire>
{% endlien %}

complémentaire de complémentaire = graphe

> TBD tout graphe est complémentaire d'un autre. le carré est identité

### Graphe adjoint

{% lien %}
<https://fr.wikipedia.org/wiki/Line_graph>
{% endlien %}
Aussi appelé line graph

> TBD stable pour cycle, diminue pour chemin et augmente pour clique
> TBD tout graphe n'est pas adjoint d'un autre (exemple ?)
adjoint de adjoint = graphe


## Morphismes de graphes

Les notions définies dans cette partie le seront -- par commodité -- pour des graphes mais elles se généralisent directement à des graphes orienté ou à des multigraphes.

### Définitions

{% note2 "**Définition**" %}
Soient $G = (V, E)$ et $G' = (V', E')$ deux graphes. Une fonction $f: V\to V'$ est un **_morphisme_** entre $G$ et $G'$ si $xy \in E$ implique $f(x)f(y) \in E'$.

{% endnote2 %}

> TBD exemple
> G = ({1, 2, 3, 4}, {12, 23, 34}) et G'=({u, v}, {uv}) et f(x) = f(z) = u ; f(y) = f(t) = v

On le voit dans l'exemple $f$ n'est pas forcément une bijection de $V$ dans $V'$ et l'implication n'est que dans un sens : l'arête  $f(x)f(y)$ peut exister dans $G'$ alors que $xy \notin E$. Pour avoir une correspondance parfaite entre $G$ et $G'$ il faut qu'il existe un **_isomorphisme_** entre eux :

{% note2 "**Définition**" %}
Soient $G = (V, E)$ et $G' = (V', E')$ deux graphes.  Une fonction $f: V\to V'$ est un **_isomorphisme_** entre $G$ et $G'$ si :

- $f$ est une bijection
- $f$ est un morphisme entre $G$ et $G'$
- $f^{-1}$ est un morphisme entre $G'$ et $G$

{% endnote2 %}

> TBD exemple.

{% lien %}
<https://www.bourbaki.fr/TEXTES/1125.pdf>
{% endlien %}

### Reconnaissance

{% lien %}
<https://perso.ens-lyon.fr/eric.thierry/Graphes2009/jonas-lefevre.pdf>
{% endlien %}

Définissons le problème algorithmique associé :

{% note "**Problème de décision**" %}

- **nom** : isomorphisme de graphe
- **données** : deux graphes
- **question** : les deux graphes sont-ils isomorphes ?

{% endnote %}

Si on se donne une fonction $f$ allant de l'ensemble des sommets d'un graphe à un autre, il est facile de vérifier si c'est un isomorphisme entre les deux graphes ou non : le problème de l'isomorphisme de graphe est donc clairement dans NP.

En revanche, on ne connaît pas son status exact : on ne sait ni s'il est NPcomplet, ni s'il est polynomial. [Le meilleur algorithme connu](https://en.wikipedia.org/wiki/Graph_isomorphism_problem) est de complexité $2^{\mathcal{O}(\log^3(n))}$ ce qui est plus que polynomial mais moins qu'exponentiel. On verra que pour certaines classes de graphes, le problème est simple.

