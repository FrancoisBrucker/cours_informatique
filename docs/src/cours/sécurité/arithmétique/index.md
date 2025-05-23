---
layout: layout/post.njk

title: Arithmétique

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les algorithmes de cryptographie nécessitent certaines connaissances en arithmétique et leurs algorithmes associés, en particulier sur les anneaux et corps finis.

On considérera ici que l'on a des vecteurs de $n$ bits, allant du bit de poids faible au bit de poids fort :

```
index  :     876543210
valeur : x = 010100110
```

$n$ est grand. Même si $\mathcal{O}(1)$ pour des mot sur 64b, comme n>64, c'est plus.

C'est pourquoi les complexités (voir Knuth) sont souvent données en fonction de $n$, le nombre de bit des paramètres et de $B$, la base de calcul (64b pour nous actuellement). Nous ne nous embêterons pas ici avec ça et donnerons les complexités uniquement en fonction de $n$.

## Probabilités discrètes

{% aller %}
[Probabilités](probabilités){.interne}
{% endaller %}

## Entiers

{% aller %}
[Arithmétique entière](nombres){.interne}
{% endaller %}

## Corps Z/pZ

{% aller %}
[Corps $\mathbb{Z}/p\mathbb{Z}$](corps-ZpZ){.interne}
{% endaller %}

## Courbes elliptiques

{% aller %}
[Courbes elliptiques](courbes-elliptiques){.interne}
{% endaller %}

## Groupe $(\\{0, 1\\}^L, \oplus)$

Le groupe commutatif $(\\{0, 1\\}^L, \oplus)$ est l'extension cartésienne du groupe $(\\{0, 1\\}, \oplus)$. On notera $\mathbb{0} = (0, \dots, 0)$ (l'élément neutre) et $\mathbb{1} = (1, \dots, 1)$.

On a les propriétés remarquables suivantes, qui seront utiles à de multiples reprises :

- $x \oplus x = \mathbb{0}$
- $\mathbb{0} \oplus x = x$
- $\mathbb{1} \oplus x = \bar{x}$

### tbd

- division euclidienne donne Bezout et donne inversion avec les éléments indivisibles

>TBD : XOR le plus du groupe $(\mathbb{Z}/2\mathbb{Z})^L$

## TBD

- crypto dépend beaucoup :
  - division euclidienne et le modulo pour contrôler les sorties
  - la primalité pour garantir la bijectivité
  - [corps finis](https://en.wikipedia.org/wiki/Finite_field_arithmetic) est l'objet qui fait marcher le tout. Surtout pour les binaires ou addition = soustraction = XOR

- [arithmétique dans corps](https://stackoverflow.com/questions/70261458/how-to-perform-addition-and-multiplication-in-f-28)

- faire une partie anneau/corps z/pz
- importance d'Euclide et Euclide étendu
- complexité des algos

- génération de nombres premiers


## complexité

### Nombres premiers

{% exercice %}
Montrez que le problème de savoir si un nombre entier est premier (problème PRIME) est équivalent au problème de savoir si un nombre entier est composé (problème COMPOSÉ).

{% endexercice %}
{% details "corrigé" %}

un problème est la négation de l'autre.

{% enddetails %}

Il existe de plus un algorithme polynomial permettant de savoir un nombre est premier, mais sa preuve dépasse le cadre de ce cours.

{% lien %}
[Article montrant que le problème PRIME est polynomial](https://annals.math.princeton.edu/wp-content/uploads/annals-v160-n2-p12.pdf).
{% endlien %}

Cet algorithme ne permet cependant pas de déterminer les facteurs dont il est composé (problème FACTORS). On a cependant clairement COMPOSITE ≤ FACTOR.

{% exercice %}
Montrez que [l'algorithme du crible d'Ératosthène](https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne) n'est pas polynomial.
{% endexercice %}
{% details "corrigé" %}

Il faut regarder tous les nombres jusqu'à $\sqrt{n}$ alors qu'il ne faut que $\log_2{n}$ bits pour stocker $n$. L'algorithme est donc de complexité exponentiel par rapport à la taille des entrées.

{% enddetails %}

On espère, mais on a aucune preuve, qu'il n'existe pas de réduction polynomiale FACTOR ≤ COMPOSITE car le problème FACTORS est à la base des algorithmes actuels de cryptographie.
