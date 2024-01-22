---
layout: layout/post.njk

title: Outils de mesure

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Problème du comptage exhaustif de la complexité

Nous avons calculé explicitement des complexité dans la partie précédente. Vous avez du vous en rendre compte, c'est assez pénible car plusieurs problèmes surviennent.

### Ligne au compte incertain

Certaines ligne n'on pas le même nombre d'instruction selon comment on compte :

- est-ce que `x = a + 1`{.language-} c'est 1, 2 ou 3 instructions ? Ou plus ?
- quel est le nombre d'instructions de la ligne `pour chaque élément x du tableau T`{.language-} ? Une ou deux ?

### Algorithme équivalents aux comptes très différents

De plus, selon l'implémentation, un même algorithme peut avoir plusieurs complexités :

```text
pour i allant de 2 à 9:
  affiche à l'écran i
```

Peut être considéré de complexité $9\cdot 3 = 27$ si l'on considère que :

- la première ligne est uniquement une affectation
- l'affichage nécessite une opération et qu'il faut retrouver la valeur d $i$

En remplaçant la boucle for par une boucle tant que, on obtient :

```text
i = 2
tant que i ≤ 9:
  affiche à l'écran i
  i = i + 1
```

Qui est de complexité : $1 + 9\cdot (2+2+3) = 64$ ce qui semble énorme !

En revanche, si l'on remplace $9$ par $n$ le rapport des deux complexité tend vers une constante : la différence n'est plus si importante que cela lorsque $n$ devient grand.

### Dépend du code/pseudo-code

En écrivant le pseudo-code en code, par exemple en python, il n'est pas garantie du tout que les instructions basiques de mon pseudo-code seront aussi les instructions basiques de l'interpréteur.

L'instruction python `x = 1`{.language} prendra certainement plus d'une instruction élémentaire pur l'interpréteur python (il lui faut d'abort créer l'entier, la variable puis les lier) et cela prendra encore plus d'instructions basique au processeur pour réaliser tout ça.

Ah oui, et ça dépend du processeur : un processeur ARM (comme sur les mac) prendra plus d'instructions qu'un processeur INTEL (sur les PC).

Sans parler du fait que chaque instruction basique pour un processeur peut prendre plusieurs cycles processeur et que ce n'est pas constant, même pour une instruction donnée (à cause des prédictions).

### Beaucoup de calcul pour par grand chose

Enfin, ce calcul exact semble un peu vain puisqu'au final seule la forme générale et asymptotique de la complexité nous intéresse. Em effet, si les entrées sont de petites tailles c'est de toute façon rapide et plus important, [on a vu](../définitions/#forme-asymptotique) que :

{% note %}
Les coefficients multiplicatifs constants sont négligeable par rapport à la forme logarithmique, linéaire, polynomiale ou exponentielle de la complexité.
{% endnote %}

## Notation $\mathcal{O}$

Comme il est impossible de connaître le nombre exact d’instructions et qu'au final on s'en fiche puisque seule la forme générale et asymptotique est importante, on utilise l'outil de la [comparaison asymptotique](https://fr.wikipedia.org/wiki/Comparaison_asymptotique) : $\mathcal{O}$ pour tous les calculs de complexité.

> TBD : O et borne la plus fine possible

## Si on veut être plus précis

Omega et theta car un algo linéaire est en O exponentiel. Cela ne donne qu'une borne max.

> TBD outil pour la mesurer : $\mathcal{O}$ (parler de $\Omega$) et ajouter $\Theta$. Limite lorsque entree grossi. Si petit on s'en fiche ca va vite.
