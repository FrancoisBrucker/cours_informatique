---
layout: layout/post.njk 
title: "Nombres pseudo-aléatoires"

eleventyNavigation:
  key: "Nombres pseudo-aléatoires"
  parent: Théorie

prerequis:
    - "../../algorithme/définition/"
---

<!-- début résumé -->

Comment générer du hasard avec des algorithmes déterministes.

<!-- end résumé -->

Un algorithme est par définition déterministe. Il **doit toujours** donner le même résultat s'il est appelé avec les mêmes paramètres. Il existe cependant de nombreuses applications où l'on a besoin d'obtenir un nombre aléatoire (pour crypter un mot de passe, pour mélanger un jeu de carte en ligne, utiliser des [algorithmes probabilistes](https://fr.wikipedia.org/wiki/Algorithme_probabiliste), ...). Nous allons montrer ici quelques techniques pour réaliser le prodige de simuler l'aléatoire à partir d'algorithmes qui ne le sont pas.

> TBD : seed = sauvegarde et répétabilité du process.

>TBD question : Garder que 1 bit ou des nombres ? est-ce pareil ?

## Aléatoire et pseudo-aléatoire

> TBD intro : <http://math.univ-lyon1.fr/~jberard/genunif-www.pdf>

aléatoire et pseudo-aléatoire
probabilité

> quand est-ce que c'est ok ? Règles

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

## Cryptographie

### Attaques

retrouver les états internes à partir des sorties pour prédire le nombre suivant.

### générateur cryptographique

perd la propriété de pouvoir tout rejouer à partir de la seed (pour tester des simulations/générer des maps sur des jeux/fare des sauvegardes plus petites)

<https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator>
<https://crypto.stackexchange.com/questions/39186/what-does-it-mean-for-a-random-number-generator-to-be-cryptographically-secure>

<https://www.schutzwerk.com/en/blog/attacking-a-rng/>
<https://crypto.stackexchange.com/questions/100503/is-mersenne-twister-hard-to-break-if-it-has-a-reduced-output>
<https://book-of-gehn.github.io/articles/2018/12/23/Mersenne-Twister-PRNG.html>

<https://en.wikipedia.org/wiki/Fortuna_(PRNG)> et update : <https://fr.wikipedia.org/wiki/Fortuna_(cryptographie)>

## Non uniforme
