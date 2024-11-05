---
layout: layout/post.njk

title: Graphes planaires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD

> TBD isomorphisme de graphe planaire
> 5 et 4 coloriable. 3 coloriable np-complet.

> secret sans informations.

> TBD kuratowski
> TBD dessin sans courbure dans un triangle.


{% lien %}
[Graphes planaires avec Maria Chudnovski](https://www.youtube.com/watch?v=xBkTIp6ajAg)
{% endlien %}

> TBD 3 color planaire est NP-complet : <https://graal.ens-lyon.fr/~yrobert/algoL3/color-np.pdf>, <https://www.youtube.com/watch?v=MJNpclV45rw>
> ce qui peut ensuite servir pour les [zero knowledge proof](https://www.youtube.com/watch?v=5ovdoxnfFVc)

> TBD 5 couleur ne passe pas à 4 couleurs : <https://www.youtube.com/watch?v=adZZv4eEPs8>

> TBD playlist : <https://www.youtube.com/watch?v=wnYtITkWAYA&list=PLGxuz-nmYlQPgIHbqWtgD-F7NnJuqs4fH>
>
> TBD Theorem (Tutte, 1956). A 4-connected planar graph has a Hamiltonian cycle.

- planaire :
  - <http://o.togni.u-bourgogne.fr/CMGraphesCh3.pdf>
  - <https://perso.ens-lyon.fr/eric.thierry/Graphes2010/planar-slides.pdf>
  - théorème des 4 couleurs : <https://www.lix.polytechnique.fr/~werner/PI-4C/sujet4C.html>
  - 4 colorier un graphe planaire 3 coloriable p27 : <https://perso.ens-lyon.fr/eric.thierry/ER02/esperet-col.pdf>
  - 5 coloration <https://www.enseignement.polytechnique.fr/profs/informatique/Francois.Morain/INF431/X06/5col.pdf>
  - coloriable :
  - 3 coloriable et problème de la galerie d'art : <<https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_galerie_d%27art>>
  - 3 coloriable et lemme de Sperner <https://www.youtube.com/watch?v=cpIexccvYjI&list=PLdUzuimxVcC0QCFYP0Af3TNldswjL8_ep&index=18>
  - <http://o.togni.u-bourgogne.fr/CMGraphesCh3.pdf>
  - 3 coloriable :
    - NP complet <https://perso.eleves.ens-rennes.fr/people/pierre.le-barbenchon/devinfo/3colo.pdf>
    - planaire aussi : <https://perso.ens-lyon.fr/laureline.pinault/Algo1/TD11-correction.pdf>

- 4 couleurs : <https://inria.hal.science/hal-04034866/document>
- planaire et embedding : <https://www.youtube.com/watch?v=MNgKx4A1pXM&list=PLriUvS7IljvkGesFRuYjqRz4lKgodJgh2&index=13>

- graphe planaire :
  - preuve Kuratowski juste avec 2-connexité: <https://www.math.cmu.edu/~mradclif/teaching/228F16/Kuratowski.pdf>
  - définitions et propriétés + Kuratowsky : <https://perso.ens-lyon.fr/eric.thierry/Graphes2009/theophile-trunck.pdf>. On a besoin de :
    - coloriabilité via le problème de la galerie d'art :
      - <https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_galerie_d%27art>
      - exercices : <https://static.idm314.org/resources/activities/idm-art-gallery-fr.pdf>
      - TIPE : <https://cpge-paradise.com/TIPE/Baudoin_Solal/PPT_Baudoin_Solal.pdf>
      - théorème de Jordan : <https://minerve.ens-rennes.fr/images/Le_Th%C3%A9or%C3%A8me_de_Jordan_S.Quayle_V.Le_Gruiec..pdf>
    - k-connectivité
  - placement sur la grille :
    - <https://ics.uci.edu/~eppstein/gina/schnyder/>
    - papier : <https://acm.math.spbu.ru/~sk1/courses/1617f_au3/papers/schnyder-grid-embedding.pdf>
    - <https://ics.uci.edu/~eppstein/163/lecture10c.pdf>
  - topologie et courbe fermée Jordan  : <https://pagesperso.g-scop.grenoble-inp.fr/~lazarusf/Enseignement/graphesPlans.pdf>
  - exercices : <http://www.gymomath.ch/javmath/polycopie/th_graphe5.pdf>
  - preuve simple ? <https://www.sciencedirect.com/science/article/pii/0012365X80901454>
  
> TBD Triangulation d'un graphe planaire. S'il est triangulé pour une représentation, il l'est pour toute ?
