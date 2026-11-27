---
layout: layout/post.njk

title: Registres à décalage

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## LGC

> retrouver le suivant à partir d'un nombre ? Retrouver les paramètres à partir d'une suite de nombres
attention aux paramètres.

## Registre à décalages

amélioration des LGC.
Bonnes performances

<https://peps.python.org/pep-0506/>

* <https://en.wikipedia.org/wiki/Linear_congruential_generator>
* <http://math.univ-lyon1.fr/~jberard/genunif-www.pdf>
* <https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rateur_de_nombres_pseudo-al%C3%A9atoires>
* <https://perso.u-cergy.fr/~atorcini/MATDID/PYTHON/lect2.pdf>
* <https://towardsdatascience.com/where-does-python-get-its-random-numbers-from-81dece23b712>
* <https://stackoverflow.com/questions/57208403/random-number-generation-algorithm-used-in-numpy>
* <https://theses.hal.science/tel-01236602v2/document>
* <http://cedric.cnam.fr/~saporta/algos29_10_2010_ajoutsPP.pdf>

* <https://people.eecs.berkeley.edu/~daw/papers/ddj-netscape.html>
* <https://en.wikipedia.org/wiki/Random_number_generator_attack>
* <https://www.vdouine.net/maths/mej/generation-de-nombres-pseudo-aleatoires-introduction/>
* <https://doc.lagout.org/science/0_Computer%20Science/2_Algorithms/The%20Art%20of%20Computer%20Programming%20%28vol.%202_%20Seminumerical%20Algorithms%29%20%283rd%20ed.%29%20%5BKnuth%201997-11-14%5D.pdf>

<https://docs.python.org/fr/3.10/library/random.html>
<https://medium.com/problem-solving-blog/rng-the-secret-of-cryptography-46d10a405924>

## Mersenne twister


## Non uniforme

> TBD LFSR

polynome groupes. <https://www.math.univ-paris13.fr/~boyer/enseignement/crypto/Chap3.pdf>
modulo pas crypto car on déduit a et b de deux variables.

<https://www.usna.edu/Users/math/dphillip/sa421.s16/chapter02.pdf>

> 2. faire avec des LSFR
> 
> LSFR <https://www.youtube.com/watch?v=-uVC2ISqHww>
> LSFR toutes les preuves sont là : <https://www.paris.inria.fr/secret/Anne.Canteaut/MPRI/chapters-10-13.pdf>
>
> <https://www.staff.uni-mainz.de/pommeren/Cryptology/Bitstream/3_FSR/FSR.pdf>
> 
> <https://www.youtube.com/watch?v=Ks1pw1X22y4>