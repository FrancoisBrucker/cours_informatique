---
layout: layout/post.njk

title: Graphes biparti

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les graphes biparti font parti de ces classes de graphes assez généraux pour être présent partout et assez spécifique pour que tous se passe bien (les principaux problèmes NP-complets dans le cas général deviennent polynomiaux voir triviaux).

{% note "**Définition**" %}
Un graphe $G=(V, E)$ est **_biparti_** s'il existe une bipartition $V_1$ et $V_2$ de $V$  en deux [stables](../structure/#definition-stable).
{% endnote  %}

Par exemple :

> TBD exemple
>

## Reconnaissance

Savoir si un graphe est biparti est _"facile"_ en utilisant un algorithme de marquage en associant des couleurs à chaque sommet.

Dans l'algorithme suivant, on considère que le graphe est connexe. S'il ne l'est pas on le relance sur chacune de ses parties connexes.

C'est le premier algorithme que vous voyez qui est basé sur le principe de marquage puis examen de sommets. Ce principe est général et permet de résoudre beaucoup de problèmes en théorie des graphes.

```python
Initialisation :

On possède deux couleurs.
Soit x un sommet du graphe que l'on marque avec une couleur

Boucle principale :

tant qu'il existe x, un sommet marqué non examiné:

    examiner x
    pour chaque voisin y de x :
        si y est marqué avec la couleur de x:
            FIN : le graphe n'est pas biparti
        sinon si y n'est pas marqué:
            marquer y avec la couleur différente de x
    
FIN : le graphe est biparti et la couleur des sommets determine les 2 stables

```

> TBD à écrire propre

1. on voit bien tous les sommets car connexe : on le fait par récurrence sur la longueur du chemin entre $x$ et $y$
2. chaque couleur est obligatoire
3. linéaire n+m si on stocke les éléments marqué non examiné dans une pile/file/ensemble.

> TBD si connexe, la bipartition est unique et sinon 2 puissance nb de parties connexes possibilité.

## Caractérisation

{% note "**Proposition**" %}

Un graphe est biparti si et seulement si il ne contient pas de cycle de longueur impaire.

{% endnote  %}

Vous allez en faire la démonstration grâce à deux exercices.

{% exercice %}

Un graphe biparti ne contient pas de cycle de longueur impaire.

{% endexercice  %}
{% details "corrigé" %}

Si le graphe possède un cycle, ses arêtes doivent passer d'un stable à l'autre un nombre pair de fois.

{% enddetails %}

Et dans l'autre sens :

{% exercice %}

Un graphe n'est pas biparti s'il contient un cycle de longueur impaire.

{% endexercice  %}
{% details "corrigé" %}
On utilise l'algorithme et si l'algorithme répond non c'est qu'on a un cycle de longueur impaire.
{% enddetails %}

## Généralisations

### Biparti complets

> TBD biparti complets $K_{p,q}$

### Triparti

> TBD 3-parti NP-complet. : <https://www.enseignement.polytechnique.fr/informatique/INF412/uploads/Main/chap13-goodINF412.pdf> p10 3-coloriable.
>
> un gadget : les preuve de NP-complétude le font.
> entre 2 et 3 le soucis. Comme 2 et 3 SAT

### $k$-parti

> TBD $k$-parti et $k$-parti complets

### split graph

> TBD split graph

## Biparti complets couvrants

> TBD <https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Graham-Pollak>

> exemple avec batailles : <https://www.youtube.com/watch?v=6ByCnuCbPsg>

## TBD

> TBD à placer les biparti là ou il faut dans la suite du cours : <https://en.wikipedia.org/wiki/Bipartite_graph>