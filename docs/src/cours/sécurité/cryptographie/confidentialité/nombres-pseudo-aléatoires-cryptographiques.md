---
layout: layout/post.njk

title: Nombres pseudo-aléatoires cryptographique

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Pour qu'Alice et Bob puissent générer la clé $K$ à $t$ bits à partir de la clé partagée à $s <t$ bits aléatoire, il est nécessaire d'avoir un algorithme déterministe permettant de générer (au moins) $t$ bits à partir des $s$ bits de $k$.

```
  ---------     
  | s bit |            #  k
  ---------     
  :        \     
  :         \     
  :          \     
  :           \     
  --------------     
  |   t bits    |     # G(k)
  --------------     
```

## Définition

Pour que l'algorithme de Vernam fonctionne il faut que $K$ le plus uniforme possible, ce qui impose la définition suivante :

<div id="CPPRG"></div>

{% note "**Définition**" %}
Un **générateur de nombres pseudo-aléatoire sécurisé** (_secure PRG, secure pseudo random generator_) doit avoir les propriétés suivantes :

- $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^t$, avec $s <<t$
- $G$ doit être implémentable par algorithme efficace
- tout algorithme efficace ne peut avoir qu'un avantage négligeable au jeu de la reconnaissance  [jeu de la reconnaissance](../définition-sécurité/#jeu-reconnaissance) entre :

- un élément $G(k) \in \\{0, 1\\}^t$ pour $k$ uniformément choisi,
- un élément de \\{0, 1\\}^t$ uniformément choisi.

{% endnote %}
{% info %}
Le paramètre de $G$ est appelé _seed_
{% endinfo %}

Notez que cette condition est différente de celle des [PRNG](/cours/misc/aléatoires){.interne} qui ne supposent que l'uniformité d'une réalisation.

Avec $G(k)$ une fonction permettant de générer $t$ bits à partir de $s$ bit (avec $s < n$, voir $s << n$).

La définition explicite fait qu'il est impossible de distinguer efficacement $G(k)$ d'un mot aléatoire et ce, quelque soit la _seed_ choisie.

{% attention "**À retenir**" %}
En cryptographie utilisez des générateurs fait pour cela. Ils sont plus lent mais sont non prédictible : simuler (le monde physique) est différent de se protéger.
{% endattention %}

## Non prédictabilité

> TBD 


## Chiffrement sémantiquement sécurisé

> TBD 
> predictible (si on voie l'etat 1 pas pouvoir prédir le futiur) et non retracable (si on vol l'ordi on ne doitpas pouvoir revenir en arriere)
> <https://blog.cr.yp.to/20170723-random.html>

> TBD ? <https://crypto.stackexchange.com/questions/53295/using-chacha20-as-a-prng-with-a-variable-length-seed>
> 
## Construction

> TBD produire des elements par calcul (mod, lfsr)  plutot pour prng par permutation plutot cprng.
> 
Construire un CPRNG n'est pas une chose facile. Nous allons en montrer une qui va nous être utile lorsque nous présenterons un chiffre moderne.

> TBD chacha20. juste melange, puis compteur. On ne parle pas de nonce (ce sera pour ensuite)
> 
## Implémentations
 


### Cryptographie en python

> TBD module [secrets](https://docs.python.org/fr/3/library/secrets.html#module-secrets)

## Attaques

retrouver les états internes à partir des sorties pour prédire le nombre suivant.

### générateur cryptographique

> TBD

perd la propriété de pouvoir tout rejouer à partir de la seed (pour tester des simulations/générer des maps sur des jeux/fare des sauvegardes plus petites)

<https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator>
<https://crypto.stackexchange.com/questions/39186/what-does-it-mean-for-a-random-number-generator-to-be-cryptographically-secure>

<https://www.schutzwerk.com/en/blog/attacking-a-rng/>
<https://crypto.stackexchange.com/questions/100503/is-mersenne-twister-hard-to-break-if-it-has-a-reduced-output>
<https://book-of-gehn.github.io/articles/2018/12/23/Mersenne-Twister-PRNG.html>

<https://en.wikipedia.org/wiki/Fortuna_(PRNG)> et update : <https://fr.wikipedia.org/wiki/Fortuna_(cryptographie)>
