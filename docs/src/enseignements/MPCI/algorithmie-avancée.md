---
layout: layout/post.njk 
title: "S5 : Algorithmie avancée"

eleventyNavigation:
  order: 3

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---

## TBD

> MIT algo. <https://www.youtube.com/playlist?list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp>

proba : <https://www.youtube.com/watch?v=pxzbbP7FmPA&list=PLYhJxc3T5xALIscExdC0YqPKdBgSp6EfP>

## Hasard

### mélanger

- permutation : <https://en.wikipedia.org/wiki/Permutation>

### pseudo-aléatoire

### Randomized algorithms

- Hasard ? Intros :
  - court : <https://www.youtube.com/watch?v=nBq4sFg3at0>
  - TB : <https://www.youtube.com/watch?v=_tN2ev3hO14>
  - le hasard est dans l'oeil de celui qui regarde. SI on ne peut pas prédire le suivant, pseudo-random = random. C'est comme le démon de Laplace.
- regarder dans le Kleinberg/Tardos
- cours Dieter Kratch
- <https://www.youtube.com/watch?v=0r2D32esF3Y> et <https://www.youtube.com/watch?v=GS2MxmorEzc>
- <https://www.youtube.com/watch?v=01ohO542NMI&list=PLkvhuSoxwjI_JL7GYcJHK7-EK55t0KYGO>
- ? <https://www.youtube.com/watch?v=bsZXgXdSomc&list=PLOMwD5hwqoJ_slbq9iSE6tURVqX5eLKq8>
- bpp : <https://cs.uwaterloo.ca/~eblais/cs365/PandBPP.html>
- <https://www.columbia.edu/~cs2035/courses/csor4231.S19/rand.pdf>
- <https://theory.stanford.edu/people/pragh/amstalk.pdf>
- monte carlo : <https://www.youtube.com/watch?v=CmpWM2HMhxw>
- las vegas : <https://en.wikipedia.org/wiki/Las_Vegas_algorithm>
- randomized cut : <https://www.youtube.com/watch?v=KqMGeNZuwfI>
- Krager's algorithm <https://web.stanford.edu/class/archive/cs/cs161/cs161.1166/lectures/lecture15.pdf> <https://www.youtube.com/watch?v=KqMGeNZuwfI> <https://cadmo.ethz.ch/education/lectures/FS18/SAADS/papers/SODA93_Global_Mincuts.pdf>. Utiliser union-find ? <https://fr.wikipedia.org/wiki/Union-find>

- prime number en polylog. Random et dérandomisation : <https://www.math.toronto.edu/swastik/courses/rutgers/ANT-F14/lec14.pdf>
- chebychef <https://math.univ-angers.fr/documents/08-ep2.pdf>

- <https://www.youtube.com/watch?v=QPk8MUtq5yA&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=9>
## Cryptographie

- reprendre cours 23-24
- zero knowledge proof : <https://www.youtube.com/watch?v=5ovdoxnfFVc>
- factorization :
  - statut inconnu : <https://en.wikipedia.org/wiki/Integer_factorization>
  - mais surement pas NP-complet <https://cstheory.stackexchange.com/a/160> car dans np/co-np
  - <https://www.youtube.com/watch?v=vfjN7MmSB6g&list=PLkvhuSoxwjI_UudECvFYArvG0cLbFlzSr>

## C et structures de données

- modèle von Neumann pour un ordinateur
- gestion de la mémoire :
  - noyau programme et mémoire
  - données : dépend du type des données.

- C : compilation et pointeurs
- binary search <https://www.youtube.com/watch?v=GU7DpgHINWQ&list=PLl0KD3g-oDOHpWRyyGBUJ9jmul0lUOD80&index=3>
- python et C
- structures de données en C :
  - <https://www.youtube.com/watch?v=VOpjAHCee7c&list=PL9IEJIKnBJjFiudyP6wSXmykrn67Ykqib>
  - pile/file : pointeur et à la Knuth
  - graphes et arbres : exemple de la FAT
  - B-tree : <https://www.youtube.com/watch?v=K1a2Bk8NrYQ>
  - LSM-tree : <https://www.youtube.com/watch?v=I6jB0nM9SKU> et <https://www.youtube.com/watch?v=ciGAVER_erw>

## Graphes

- bi-parti
- planaire
- coloration
- arbres : propriété, code Prüfer
- k-connectivité
- flots
- postier chinois
- couplage
- Hamilton
- graphes infinis
- random graphs
- union-find
- coloriable :
  - <http://o.togni.u-bourgogne.fr/CMGraphesCh3.pdf>
  - 3 coloriable :
    - NP complet <https://perso.eleves.ens-rennes.fr/people/pierre.le-barbenchon/devinfo/3colo.pdf>
    - planaire aussi : <https://perso.ens-lyon.fr/laureline.pinault/Algo1/TD11-correction.pdf>

## Complexité

- languages
- P et NP
- réductions
- Cook et Turing
- autres classes : <https://fr.wikipedia.org/wiki/BPP_(complexit%C3%A9)> : <https://www.youtube.com/watch?v=mZck0N_T9Cs>
