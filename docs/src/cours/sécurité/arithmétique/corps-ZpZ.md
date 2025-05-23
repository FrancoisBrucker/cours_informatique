---
layout: layout/post.njk

title: Corps Z/pZ

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On définit $(\mathbb{Z}/n\mathbb{Z}, +, \cdot)$ comme l'[anneau](https://fr.wikipedia.org/wiki/Anneau_unitaire#D%C3%A9finition) commutatif tel que :

- les éléments de l'anneau sont des entiers allant de 0 à $n-1$
- l'addition est l'addition usuelle modulo $n$
  - l'élément neutre est 0
  - l'opposé de $x$ est $n-x$
- la multiplication est la multiplication usuelle modulo $n$
  - l'élément neutre est 1
- $x \mathbin{\small\\%} n$ vaut le reste de la division entière de $x$ par $n$

Si $n$ est premier, $\mathbb{Z}/n\mathbb{Z}$ est même un corps :

- tout élément $x$ a un inverse noté $x^{-1}$
- il est intègre : $x\cdot y = 0$ implique que soit $x$ soit $y$ vaut $0$.

{% note "**Proposition**" %}
Si $p$ est premier, $(\mathbb{Z}/p\mathbb{Z}, +, \cdot)$ est un corps commutatif.
{% endnote %}
{% details "preuve" %}
> TBD
{% enddetails %}

{% info %}
[théorème de Wedderburn](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Wedderburn) montre que tout corps fini est commutatif.
{% endinfo %}

## <span id="groupe-cyclique"></span>Groupe cyclique

Si $n$ est premier $(\mathbb{Z}/p\mathbb{Z}^\star, \cdot)$ est un [groupe cyclique](https://fr.wikipedia.org/wiki/Groupe_cyclique).

> TBD

## <span id="exponentiation-modulaire">Exponentiation modulaire

{% lien %}
[square and multiply](https://www.youtube.com/watch?v=cbGB__V8MNk)
{% endlien %}

L'exponentiation dans l'anneau $\mathbb{Z}/n\mathbb{Z}$ se fait mathématiquement très bien en utilisant l'exponentiation indienne, cependant le nombre de bits des nombres calculés deviennent vite non tractable en pratique surtout qu'à la fin on refait un modulo de tout ça.

L'idée est de faire le modulo à chaque étape de l'exponentiation indienne :

```
expo(x, y):

  r = 1
  tant que y n'est pas nul :
    si y est impair:
      y = y - 1
      r = r * y  mod n
    sinon:
      x = x / 2
      y = y * y  mod n
  
  rendre r
```

On peut même stocker les valeurs des exposants trouvés dans un dictionnaire pour ne pas avoir à recalculer deux fois la même chose.

Lorsque les nombres sont stockés sur $k$ bits, [la complexité totale de cet algo est donc $\mathcal{O}(k^3)$](../nombres#exponentiation){.interne}.

{% note "**Proposition**" %}
Si $p$ est premier : $a^{p-1} = 1 \mathbin{\small\\%} p$.
{% endnote %}
{% details "preuve" %}

> TBD

{% enddetails %}
{% lien %}
Cette propriété est connue sous le nom de [petit théorème de Fermat](https://fr.wikipedia.org/wiki/Petit_th%C3%A9or%C3%A8me_de_Fermat)
{% endlien %}

## <span id="logarithme-discret"></span>Logarithme discret

{% lien %}
[Logarithme discret](https://fr.wikipedia.org/wiki/Logarithme_discret)
{% endlien %}

On ne connaît pas d'algorithme efficace pour trouver $x$ tel que $g^x =y \mathbin{\small\\%} n$.

Le seul algorithme connut est le brute-force et de tester tous les éléments de 0 à $n-1$.

Notez que cette équation n'a pas forcément de solution.

> TBD exemple

Pour garantir l'existence de solutions à l'équation $g^x =y \mathbin{\small\\%} p$, il suffit que :

- $p$ est premier
- $g$ soit un générateur du groupe cyclique $(\mathbb{Z}/n\mathbb{Z}^\star, \cdot)$

Explicitons les termes :

1. dans $(\mathbb{Z}/p\mathbb{Z}^\star, \cdot)$ est un groupe (abélien) si et seulement si $p$ est premier
2. Le groupe $(\mathbb{Z}/p\mathbb{Z}^\star, \cdot)$ est cyclique, c'est à dire qu'il existe $g$ tel que $g^n = 1$ et g^{n-1} \neq 1$.

{% note "**Proposition**" %}
Si $p$ est premier, $(\mathbb{Z}/p\mathbb{Z}^\star, \cdot)$ est cyclique.
{% endnote %}
{% details "preuve" %}

> TBD

{% enddetails %}

### Corps $(\\{0, 1\\}, \oplus, \land)$

Le couple $(\\{0, 1\\}, \oplus, \land)$ est un [corps](https://fr.wikipedia.org/wiki/Corps_(math%C3%A9matiques)) où chaque élément est son opposé.


>TBD : anneau commutatif intègre $(\mathbb{Z}/n\mathbb{Z}, +, *)$
>TBD : cas particulier l'anneau $(\mathbb{Z}/2\mathbb{Z}, +, *)$ est un corps.


<https://maths-olympiques.fr/wp-content/uploads/2017/09/arith_zn.pdf>