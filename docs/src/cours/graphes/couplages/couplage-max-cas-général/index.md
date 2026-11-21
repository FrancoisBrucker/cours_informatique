---
layout: layout/post.njk
title: Couplages maximum cas général

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD pour le dual/primal : <https://www.kurims.kyoto-u.ac.jp/EMIS/journals/DMJDMV/vol-ismp/34_pulleyblank-william.pdf>


## Couplage parfait de poids maximum

L'algorithme également proposé par Edmonds est similaire à celui utilisé pour les graphes bi-partis.

> TBD : idée est de faire comme pour le graphe bi-parti en cherchant un chemin augmentant. Si on trouve une fleur on fusionne la corolle et on recommence. Au final, soit on trouve un chemin augmentant soit on est dans un graphe bi-parti et on augmente les arêtes du graphe.

 est le premier cas connu de résolution par [le framework primal/dual](https://math.mit.edu/~goemans/PAPERS/book-ch4.pdf). Sa démonstration dépasse le cadre de ce cours mais il est tres similaire à celui vu pour les graphes bi-partis.

Trouver un couplage de poids maximum peut toujours se ramener à un couplage parfait d'un graphe complet en doublant le graphe et en mettant des 0 sur les arêtes qui relient les 2 copies du graphe.

L'algorithme suivant permet de trouver un couplage parfait de poids maximum d'un graphe complet avec un nombre pair de sommets.

> TBD l'écrire et le prouver avec : <https://theory.stanford.edu/~jvondrak/MATH233B-2017/lec6.pdf>

1. graphe
2. cherche un chemin augmentant avec l'algorithme des fleurs
3. si pas de chemin augmentant, on ajoute des arêtes au graphe et on recommence

{% lien %}

- [programmation linéaire et couplage](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15850-f20/www/notes/lec7.pdf)
- [primal dual et problèmes combinatoires](https://www.youtube.com/watch?v=Z0eSQapcE6A&list=PLXsmhnDvpjORcTRFMVF3aUgyYlHsxfhNL&index=42)

{% endlien %}
