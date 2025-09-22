---
layout: layout/post.njk

title: Graphes planaires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD 2.2 sur le nombre de croisements <https://fr.wikipedia.org/wiki/In%C3%A9galit%C3%A9_arithm%C3%A9tico-g%C3%A9om%C3%A9trique>
> TBD : Il sont aussi extrêmement utilisés pour les mesh 3D. C'est une surface sans trous.

{% lien %}
[Graphes planaires avec Maria Chudnovski](https://www.youtube.com/watch?v=xBkTIp6ajAg)
{% endlien %}

> TBD playlist : <https://www.youtube.com/watch?v=wnYtITkWAYA&list=PLGxuz-nmYlQPgIHbqWtgD-F7NnJuqs4fH>

- <http://o.togni.u-bourgogne.fr/CMGraphesCh3.pdf>
- <https://perso.ens-lyon.fr/eric.thierry/Graphes2010/planar-slides.pdf>

- <http://o.togni.u-bourgogne.fr/CMGraphesCh3.pdf>

## Définition et premières propriétés

> TBD
>
> 1. définition
> 2. formule Euler sur les faces
> 3. majoration nombre d'arêtes : il n'y en a pas beaucoup
> 4. existe un sommet de degré ≤ 5

> TBD Triangulation d'un graphe planaire. S'il est triangulé pour une représentation, il l'est pour toute ?

## Théorème de Kuratowski

> TBD [mineurs](https://fr.wikipedia.org/wiki/Mineur_(th%C3%A9orie_des_graphes))

- définitions et propriétés + Kuratowsky : <https://perso.ens-lyon.fr/eric.thierry/Graphes2009/theophile-trunck.pdf>. On a besoin de :
  - coloriabilité via le problème de la galerie d'art :
    - <https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_galerie_d%27art>
    - exercices : <https://static.idm314.org/resources/activities/idm-art-gallery-fr.pdf>
    - TIPE : <https://cpge-paradise.com/TIPE/Baudoin_Solal/PPT_Baudoin_Solal.pdf>
    - théorème de Jordan : <https://minerve.ens-rennes.fr/images/Le_Th%C3%A9or%C3%A8me_de_Jordan_S.Quayle_V.Le_Gruiec..pdf>
  - k-connectivité
- preuve Kuratowski juste avec 2-connexité: <https://www.math.cmu.edu/~mradclif/teaching/228F16/Kuratowski.pdf>
- planaire et embedding : <https://www.youtube.com/watch?v=MNgKx4A1pXM&list=PLriUvS7IljvkGesFRuYjqRz4lKgodJgh2&index=13>

  - topologie et courbe fermée Jordan  : <https://pagesperso.g-scop.grenoble-inp.fr/~lazarusf/Enseignement/graphesPlans.pdf>
  - exercices : <http://www.gymomath.ch/javmath/polycopie/th_graphe5.pdf>
  - preuve simple ? <https://www.sciencedirect.com/science/article/pii/0012365X80901454>

## Algorithmes

### Reconnaissance

> Par blocks (2-connexe maximals).
> puis reconnaissance de blocs

### Dessin

> TBD dessin sans courbure dans un triangle.

- placement sur la grille :
  - <https://ics.uci.edu/~eppstein/gina/schnyder/>
  - papier : <https://acm.math.spbu.ru/~sk1/courses/1617f_au3/papers/schnyder-grid-embedding.pdf>
  - <https://ics.uci.edu/~eppstein/163/lecture10c.pdf>

## Coloration de graphes planaires

> TBD pareil que colorier les faces.
 
> TBD 3 colorable planaire np-complet : <https://www.cs.cmu.edu/afs/cs/academic/class/15451-s04/www/Lectures/chapter23.pdf>

- coloriable :

---

Nom de l'algorithme

> algo
> > autre algo $x_1 \leftarrow 3$
> fin

---

### Théorème des 4 couleurs

> TBD 6 par notre algo de coloration
> TBD 5 couleur : démonstration de Kempe.

> Elle ne fonctionne pas pour 4 couleurs. Pourquoi ?
> TBD Une démo du théorème des 4 couleurs par Kempe : <https://www.youtube.com/watch?v=adZZv4eEPs8>
> TBD théorème des 4 couleurs :
>
> - <https://www.lix.polytechnique.fr/~werner/PI-4C/sujet4C.html>
> - 4 couleurs : <https://inria.hal.science/hal-04034866/document>

### Algorithmes de coloration

> - 6 coloration avec l'algo de coloration
> - 5 coloration linéaire <https://www.enseignement.polytechnique.fr/profs/informatique/Francois.Morain/INF431/X06/5col.pdf>
> - 4 coloration d'un graphe planaire 3 colorable (Kawarabayashi et Ozeki 2009) <https://tgt.ynu.ac.jp/ozeki/2009KO2.pdf>. Soit il sort une 4 coloration, soit il dit que le graphe n'est pas 3 colorable. Pourquoi n'est-ce pas en contradiction avec le fait que le problème est NP-complet ?

### Variantes

> TBD pays non connexes
> TBD colonies lunaires

## Colorabilité et partage de secrets

> TBD un sujet qui lie tout ce qu'on a fait jusqu'à maintenant.

> <https://fr.wikipedia.org/wiki/Preuve_%C3%A0_divulgation_nulle_de_connaissance>
>
{% lien %}

- [Avi Wigderson parle des zero knowledge proof](https://www.youtube.com/watch?v=5ovdoxnfFVc)
- [le papier](https://www.wisdom.weizmann.ac.il/~oded/X/gmw1j.pdf)

{% endlien %}

> [Curry howard correspondance](https://fr.wikipedia.org/wiki/Correspondance_de_Curry-Howard)
## Odds and ends

Nombreux problèmes NP-complets sont facile à les graphes planaires.

### Propriétés

- 3 coloriable et problème de la galerie d'art : <https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_galerie_d%27art>

- Lemme de Sperner <https://www.youtube.com/watch?v=cpIexccvYjI&list=PLdUzuimxVcC0QCFYP0Af3TNldswjL8_ep&index=18>, on peut le démontrer avec la planarité : <https://www.ams.jhu.edu/~abasu9/AMS_550-472-672/sperner.pdf>. Attention, ce n'est **pas** de la coloration de graphes (pas de contrainte sur les voisins).

### Facile pour les graphes planaires

> TBD Theorem (Tutte, 1956). A 4-connected planar graph has a Hamiltonian cycle.
> TBD isomorphisme de graphe planaire
