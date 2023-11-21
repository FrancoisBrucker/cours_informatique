---
layout: layout/post.njk

title: Nombres Aléatoires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



D. Knuth cite dans le volume 2 de [Art of computer programming](https://www.amazon.fr/Art-Computer-Programming-Seminumerical-Combinatorial/dp/0137935102/) près d'une dizaine d'application où l'on a besoin de nombres aléatoires (simulation, échantillonnages, jeu, ...). Cependant, à part l'usage de [générateurs aléatoires physiques](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rateur_de_nombres_al%C3%A9atoires_mat%C3%A9riel) ou encore l'utilisation de [tables](https://fr.wikipedia.org/wiki/Table_de_nombres_al%C3%A9atoires), l'aléatoire semble cependant hors de portée d'un ordinateur, par essence déterministe.

{% lien %}
<https://www.random.org/>
{% endlien %}

Si un algorithme ne ne peut "créer" de nombres aléatoires, le relancer avec les mêmes paramètres redonnera exactement les mêmes résultats, on peut cependant des nombres ayant *l'air* d'être aléatoire. Ces nombres sont alors appelés ***nombres pseudo-aléatoires***.

Il nous faut cependant avant tout définir précisément ce qu'aléatoire veut dire avant de montrer deux méthodes permettant d'en générer.

{% attention %}
En tant qu'informaticien, nous ne nous intéresserons qu'à la génération d'entiers (première partie) voir juste de bits (seconde partie).
{% endattention %}

## Aléatoire ?

{% note "**Définition**" %}
Une séquence $(x_i)_{i\geq 0}$ d'entiers positifs inférieur strictement à $m$ est ***aléatoire*** si elle est constituée de nombres ***indépendants*** suivant une distribution ***uniforme***.

- ***indépendance*** : $Pr[x_i = a, x_j = b] = Pr[x_i = a] \cdot Pr[x_j = b]$
- ***distribution uniforme*** : $Pr[x_i = k] = \frac{1}{m}$ pour tout $0\leq k < m$.
{% endnote %}

Savoir si une suite finie donnée est aléatoire est problématique, puisque chaque suite à une probabilité, même faible, d'exister. Une suite binaire de 1 million de 0 a autant de chance d'arriver qu'une suite alternant les 0 et les 1.

{% info %}
C'est pourquoi les être humains ne sont pas bon pour générer des suites aléatoires. En demandant à des humains de générer des suites aléatoires, la suite constante sera sous-représentée.
{% endinfo %}

Déterminer si une suite est aléatoire ne peut se faire que via des tests statistiques qui vont assurer de telle ou telle propriété :

- alternance de 0 et de 1,
- probabilité uniforme,
- ...

### Test statistique

Un [test statistique](https://fr.wikipedia.org/wiki/Test_statistique) permet de déterminer avec une probabilité donnée si une hypothèse est vérifiée ou non.

Nous allons ici nous restreindre aux tests sur les suites finies d'entiers $(x_i)_{i\geq 0}$, on peut bien sur mathématiquement les définir de façon plus générale.

{% note "**Définition**" %}
Un ***test statistique*** $T$ dépend d'une ***hypothèse $H_0$*** sur
{% endnote %}

> TBD : H0 vs H1


### Pseudo-aléatoire

Un suite finie ne peut être considérée aléatoire qu'à l'aune d'un ensemble déterminé de tests qu'elle satisfait.

{% note "**Définition**" %}
Une séquence finie $(x_i)_{0 \leq i < n}$ de $n$ entiers positifs inférieur strictement à $m$ d'entiers est ***[pseudo-aléatoire](https://fr.wikipedia.org/wiki/Pseudo-al%C3%A9atoire)*** si elle est générée :

- par un algorithme polynomial
{% endnote %}

https://fr.wikipedia.org/wiki/Pseudo-al%C3%A9atoire

Comment savoir si une suite est aléatoire ?

- on ne sait pas. 1 million de fois 0 existe. Mais avec une proba faible. Tout comme une alternance de 0 et 1 ou toute autre suite.
- regarder par bout

définition Pseudo-aléatoire : satisfait à des tests :

- théoriques :
  - une longue séquence
  - pr(xi > xi+1)
- pratiques :
  - chi 2
  - dessins 2d, 3d
  - kolmogorv-smirnof
  - auto-corrélation

{% note "**Définition**" %}
Une séquence $(x_i)_{i\geq 0}$ d'entiers positifs inférieur strictement à $m$ d'entiers est ***pseudo-aléatoire*** si

> TBD finir

{% endnote %}

{% info %}
> TBD en crypto on veut qu'elle soit non prédictible plutôt que statistiquement correcte. Donc : n'utiosez pas de truc non crypto en crypto et faite attentions aux propriété que vous voulez pour vos simulations. 
{% endinfo %}

Il n'existe pas de définition formelle de ce qu'est une suite $(x_i)_{i\geq 0}$ de nombres aléatoire. On ne peut l'approcher que par des tests. Par exemple :

> TBD mix des deux : seed random avec entropy, puis pseudo-aléatoire [Linux `/dev/random`{.fichier}](https://en.wikipedia.org/wiki//dev/random)
Utiliser un être humain n'est pas adapté pour reconnaître des nombre aléatoire.

> TBD même seed pour débeuger.

## Un nombre

- théoriques :
  - choix de a,c , m pour une longue séqunce
  - pr(xi > xi+1)

Ne pas faire n'importe quoi. A écrit dans the art of computer programming (vol 2.) :

> Random numbers should not be generated with a method chosen at random.

> $x_{i+1} = ax_i + c mod m$

## Un bits

La façon le plus simple
polynome groupes. <https://www.math.univ-paris13.fr/~boyer/enseignement/crypto/Chap3.pdf>
modulo pas crypto car on déduit a et b de deux variables.

<https://www.usna.edu/Users/math/dphillip/sa421.s16/chapter02.pdf>

[Intro, exemples et tests pour la validité de PRNG](https://www.mi.fu-berlin.de/inf/groups/ag-tech/teaching/2012_SS/L_19540_Modeling_and_Performance_Analysis_with_Simulation/06.pdf)

> 1. faire avec des modulo [LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator). Voir aussi <https://www.staff.uni-mainz.de/pommeren/Cryptology/Bitstream/1_Classic/>
> Utiliser des merserne prime pour les [Lehmer LCG](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
> 2. faire avec des LSFR
> 
> LSFR <https://www.youtube.com/watch?v=-uVC2ISqHww>
> LSFR toutes les preuves sont là : <https://www.paris.inria.fr/secret/Anne.Canteaut/MPRI/chapters-10-13.pdf>
> 
> TBD trouver un nombre aléatoire ？

- génération de nombres premiers ?
- celui de python
- différence entre
  - aléatoire physique
  - aléatoire cryptographique
- entropie ?

[Registre à décalage](https://fr.wikipedia.org/wiki/Registre_%C3%A0_d%C3%A9calage_%C3%A0_r%C3%A9troaction_lin%C3%A9aire)

## pseudo-aléatoire Cryptographie

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
