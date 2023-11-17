---
layout: layout/post.njk

title: Nombres Aléatoires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

polynome groupes. <https://www.math.univ-paris13.fr/~boyer/enseignement/crypto/Chap3.pdf>

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

## PRG et *prédictabilité*

{% note %}
Une suite $g(k,1), \dots g(k, m + 1)$ est non prédictible si tout algorithme efficace ne peut peut prédire $g(k, m + 1)$ sachant $g(k, 1), \dots, g(k, m)$ qu'avec un avantage négligeable.
{% endnote %}

Le générateur de nombre pseudo-aléatoire tel que $x_i = a \cdot x_{i-1} + b \mod p$ ne l'est pas, malgré le fait qu'il possède de belle propriétés statistiques si $p$ est premier. Pour qu'un générateur de nombre puisse être utilisé de façon cryptographe, on s'intéresse moins à ses propriété d'uniformité qu'à sa non prédictibilité.

Non prédictible est équivalent à non distinguable.

{% note "**Proposition**" %}
Un PRG sécurisé est non prédictible.
{% endnote %}
{% details "preuve" %}

Supposons qu'un secure PRG soit prédictible. Il existe alors un algorithme efficace A qui possède un avantage non négligeable pour déterminer le $m+1$ ème bit à partir des $m$ premiers.

On peut utiliser cet algorithme pour déterminer si $G$ est un PRG sécurisé : on ne considère que les $m+1$ premiers bits et on rend la valeur donnée par l'algorithme $A$. L'avantage est le même et est non négligeable.

{% enddetails %}

{% note "**Théorème (Yao, 1982)**" %}
Un PRG non prédictible est sécurisé.
{% endnote %}
{% details "preuve" %}
Soit $G$ un générateur non prédictible, et R un générateur aléatoire.

Supposons qu'il existe $i$ tel que que le générateur $G(k) [:i]\\; ||\\; R[i:]$ soit non sécurisé. Prenons $i$ le plus petit et soit A l'algorithme efficace qui réalise cet avantage.

Cet algorithme nous permettra de discerner $G(k) [:i-1]\\; ||\\; R[i-1:]$ de $G(k) [:i]\\; ||\\; R[i:]$ avec le même avantage et donc de prédire $G(k) [i]$ à partir de $G(k) [:i-1]$ avec encore une fois le même avantage. Ceci n'est pas possible puisque $G$ est non prédictible.

le générateur $G(k) [:i]\\; ||\\; R[i:]$ est donc sécurisé pour tout $i$ donc également pour $i=n$.

{% enddetails %}
{% info %}

- on note `||` l'opérateur de concaténation
- `m[:n]` correspond aux n-1 premiers bits de $m$
- `m[n:]` correspond à $m$ privé de ses $n-1$ premiers bits

{% endinfo %}

{% lien %}
[Article originel de Yao, 1982](https://www.di.ens.fr/users/phan/
secuproofs/yao82.pdf)
{% endlien %}
