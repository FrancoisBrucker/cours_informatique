---
layout: layout/post.njk

title: Arbres

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Explorer les propriétés et l'intérêt de l'arbre.

## Définitions et propriétés

{% aller %}

[Définitions et premières propriétés](définitions){.interne}

{% endaller %}

### Représentation graphique

{% aller %}

[Tracés d'arbre](tracés){.interne}

{% endaller %}

### Problème de l'arbre couvrant

{% aller %}

[Arbres couvrants](arbres-couvrants){.interne}

{% endaller %}

### Arbres de Cayley

 > TBD aussi nombre d'arbres (avec un joli algo) et première façon de tirer des arbres aléatoirement. Attention au tirages aléatoires de structures discrète, ce n'est pas aussi simple qu'on le croit.

{% aller %}

[Arbres de Cayley](cayley){.interne}

{% endaller %}

## Arbres plantés

{% lien %}
[Arbre pour l'algorithmique](https://chauvin.perso.math.cnrs.fr/book.pdf)
{% endlien %}

{% aller %}

[Arbres plantés](arbres-plantés){.interne}

{% endaller %}

### Arbres planaires

> TBD arbre planaires. Suite de voisins. Montrer approche avec suites de mots.
> un DFS. pour encoder les arbres planaires. c'est un mot de Dyck (E(nfant suivant)/P(arent)) <https://moodle1.u-bordeaux.fr/pluginfile.php/462061/mod_resource/content/0/Slides.pdf>. C'est une bijection. Encode en +1, -1 ou en chemins.
> TBDTrouver exam centrale PC 2011 <https://www.doc-solus.fr/prepa/sci/adc/bin/view.corrige.html?q=PC_MATHS_CENTRALE_1_2021https://www.doc-solus.fr/prepa/sci/adc/bin/view.corrige.html?q=PC_MATHS_CENTRALE_1_2021>
> TBD enumértion avec un dijkstra sur arbre orienté sur demi-grille.
### Arbres de Catalan

> Dit binaires
>
> On connaît l'ordre gauche ou droite des enfants.

{% aller %}

[Arbres de Catalan](arbres-catalan){.interne}

{% endaller %}

### Arbres de Galton-Watson

{% aller %}

[Arbres de Galton-Watson](arbre-galton-watson){.interne}

{% endaller %}

## Isomorphisme d'arbres

{% exercice %}
Montrez que tout automorphisme d'arbre laisse invariant au moins un sommet ou une arête.

{% endexercice %}
{% details "solution" %}

> TBD écrire propre

1. vrai à 1 ou 2 sommets
2. les feuilles sont envoyées sur les feuilles par automorphisme
3. on supprime les feuilles
4. la restriction de l'automorphisme est un automorphisme de l'arbre effeuillé et la récursion passe.

{% enddetails %}

> TBD polynomial pour les arbres

> TBD Aho, Hopcroft and Ullman <https://hal.science/hal-04232137/document>
> <https://perso.ens-lyon.fr/eric.thierry/Graphes2010/marthe-bonamy.pdf>
> TBD TP <https://info.faidherbe.org/MPII/11.pdf>

### Arbres de Pólya

> Arbres planté

### Arbres non plantés

> TBD exo sommet ou arête conservée pour tout automorphisme.

## Arbres et classes

> TBD X-arbre et représentation combinatoire des arbres par bi-partition.
> TBD c'est l'ET 2024-2025
