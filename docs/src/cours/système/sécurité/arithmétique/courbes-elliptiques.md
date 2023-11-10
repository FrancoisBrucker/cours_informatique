---
layout: layout/post.njk

title: COurbes elliptiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD
>
> - Utilisées pour les problèmes de logarithmes discret
> - Ils permettent d'avoir des clés bien plus petite.

L'équation générale d'une courbe elliptique :

<div>
$$
y^2 + a_1 x \cdot y + a_3 \cdot y= x^3 + a_2\cdot x^2 + a_4\cdot x + a_6
$$
</div>

Avec les $a_i$ pris dans un corps.

Si on utilise le corps des réels, on peut utiliser l'[équation de Weierstrass](https://fr.wikipedia.org/wiki/%C3%89quation_de_Weierstrass) pur simplifier
Forme de Weierstrass :

<div>
$$
y^2 = x^3 + a\cdot x^2 + b\cdot x
$$
</div>

> TBD forme de Weierstrass
>

La courbe utilisée généralement en cryptographie est la [Curve25519](https://fr.wikipedia.org/wiki/Curve25519) :

<div>
$$
y^2 = x^3 + 486662\cdot x^2 + x
$$
</div>

Où les nombres sont pris dans le corps fini $\mathbb{Z}/p\mathbb{Z}, avec $p=2^{255} - 19$, le plus grand entier signé premier sur 256b (le dernier bit est un bit de signe).

Les éléments considérés sont les couples $(x, y)$ de la courbe où $x$ et $y$ sont dans le corps sous-jacent.

> TBD : définition de l'addition
> on se place dans le groupe avec l'addition.
> [compter les points d'une courbe elliptique](https://perso.univ-rennes1.fr/christophe.ritzenthaler/cours/point-counting-ec.pdf)
