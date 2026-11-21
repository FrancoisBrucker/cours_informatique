---
layout: layout/post.njk 
title:  "Quelques exemples de problème NP complets"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD à étoffer

Il y a un grand nombre de problèmes NP complets. Ce sont donc fondamentalement plusieurs façons différentes de raconter la même chose : un problème dont les solutions peuvent se trouver partout. Un problème sans structure à laquelle s'accrocher pour trouver des algorithmes efficaces.

> TBD comment faire pour montrer NP-complet. Utilisation de [gadgets](<https://fr.wikipedia.org/wiki/Gadget_(informatique)>)
> montrer qu'un problème NPC connu est plus simple que le problème dont on cherche à montrer la NPcomplétude. Il faut faire une réduction efficace.

## SUBSETSUM

> subsetsum 3-SAT :<https://community.wvu.edu/~krsubramani/courses/fa16/Aaoa/lecnotes/NP-completness%20(Proofs)/subsum.pdf>

## Partition

> depuis subsetsum : <https://www.geeksforgeeks.org/set-partition-is-np-complete/>

## Sac à dos

> Passer du problème d'optimisation au problème de décision. Au départ pas de décision et donc pas dans NP.
> TBD depuis partition : <https://datamove.imag.fr/denis.trystram/SupportsDeCours/2023Knapsack.pdf>

## Autres exemples

> TBD exemple de choses NP complete : <https://www.enseignement.polytechnique.fr/informatique/INF423/uploads/Main/chap12-good.pdf>
