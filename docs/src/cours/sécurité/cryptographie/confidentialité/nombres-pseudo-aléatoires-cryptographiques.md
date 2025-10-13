---
layout: layout/post.njk

title: Nombres pseudo-aléatoires cryptographique

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD definition

Avec $G(k)$ une fonction permettant de générer $t$ bits à partir de $s$ bit (avec $s < n$, voir $s << n$).

```
  ---------
  | k bit |
  ---------
  :        \
  :         \
  :          \
  :           \
  --------------
  |G(k) à t bits|
  --------------
```

S'il est clair que $F(k, \cdot)$ est une permutation quelque soit $k$ (l'inverse étant la fonction elle même), nous allons allons montrer qu'elle est sémantiquement sécurisée si le générateur $G$ l'est.

> TBD c'est un algorithme

## PRNG non cryptographique

> TBD cherche à être uniforme
> ex mod
> xorshift
> mersenne twister de python

## CPRNG

> TBD cryptographique
> TBD cherche non predictabilité
> montre que ce n'est pas le cas avec le mod

def de semantiquement securisé.

> TBD exemple des registres à décalage. En faire un TP.

## Générateur de nombre

Générer des nombres purement aléatoire est impossible pour un algorithme. Il faut donc trouver une façon de simuler ce hasard, ou tout du moins de garantir qu'un algorithme efficace ne puisse voir la supercherie.

<div id="PRG"></div>

{% note "**Définition**" %}
Un **générateur de nombres pseudo-aléatoire sécurisé** (_secure PRG, secure pseudo random generator_) doit avoir les propriétés suivantes :

- $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^n$, avec $s <<n$
- $G$ doit être implémentable par algorithme efficace
- tout algorithme efficace ne peut avoir qu'un avantage négligeable au jeu de la reconnaissance  [jeu de la reconnaissance](../définitions/#jeu-reconnaissance) entre :

- un élément $G(k) \in \\{0, 1\\}^t$ pour $k$ uniformément choisi,
- un élément de \\{0, 1\\}^t$ uniformément choisi.

{% endnote %}
{% info %}
Le paramètre de $G$ est appelé _seed_
{% endinfo %}

La définition explicite fait qu'il est impossible de distinguer efficacement $G(k)$ d'un mot aléatoire et ce, quelque soit la _seed_ choisie.

{% note %}
En règle générale, en cryptographie, utilisez des générateurs fait pour cela. Ils sont plus lent mais sont non prédictible : simuler (le monde physique) est différent de se protéger.
{% endnote %}


### Cryptographie en python

> TBD module [secrets](https://docs.python.org/fr/3/library/secrets.html#module-secrets)

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
