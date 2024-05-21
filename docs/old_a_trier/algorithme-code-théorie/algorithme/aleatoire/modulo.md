---
layout: layout/post.njk

title: Générer des nombres

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Pour générer une suite de nombres entre 0 et $m-1$, on a coutume d'utiliser la formule :

<div>
$$
x_{i+1} = a \cdot x_i + c \mod{m}
$$
</div>

La graine est le nombre $x_0$.

{% note "**proposition**" %}
Montrer que la suite $(x_i)_{i \geq 0}$ telle que $x_{i+1} = a \cdot x_i + c \mod{m}$ est périodique quelque soient $a$, $c$, $m$ et $x_0$ et que sa période est au plus $m$
{% endnote %}
{% details "preuve", "open" %}

{% enddetails %}

 > avec le modulo

- théoriques :
  - choix de a,c , m pour une longue séquence
  - pr(xi > xi+1)

Ne pas faire n'importe quoi. A écrit dans the art of computer programming (vol 2.) :

> Random numbers should not be generated with a method chosen at random.

> $x_{i+1} = ax_i + c mod m$

- propriétés théoriques :
  - une longue séquence
  - pr(xi > xi+1)
- pratiques :
  - chi 2 : proba et indépendance séquences.

> TBD uniforme pas suffisant : 0000000111111111 est bien uniforme
> TBD xi > x(i+1) : théorique

> 1. faire avec des modulo [LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator). Voir aussi <https://www.staff.uni-mainz.de/pommeren/Cryptology/Bitstream/1_Classic/>
> Utiliser des merserne prime pour les [Lehmer LCG](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
