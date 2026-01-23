---
layout: layout/post.njk

title: Mesures de complexités

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le calcul de la complexité d'un algorithme est une part importante de l'algorithmie. Elle met en oeuvre des outils puissant et peut nécessiter des des analyses et des raisonnements fins.

## Complexité algorithmique

{% aller %}
[Définitions](./définitions){.interne}
{% endaller %}

{% aller %}
[Importance](./importance){.interne}
{% endaller %}

## Problème du comptage exhaustif de la complexité

Nous avons calculé explicitement des complexité dans la partie précédente. Vous avez du vous en rendre compte, c'est assez pénible car plusieurs problèmes surviennent.

### Ligne au compte incertain

Certaines ligne n'ont pas le même nombre d'instruction selon comment on compte. Reprenons par exemple un compte que l'on a fait précédemment :

```pseudocode
F[i] ← F[i - 1] + F[i - 2]
```

On a considéré que cette instruction nécessitait 3 lectures de la variable `i`{.language-}. Mais dire que l'on ne lit `i`{.language-} qu'une seule fois aurait-été tout aussi légitime.

Ou encore le code suivant :

```pseudocode
pour chaque (i := entier) de [2 .. 9]:
  affiche i
```

Où l'on a considéré que l'on ne calculait pas tout l'intervalle à chaque itération et que l'on savait quel était l'élément suivant en 1 instruction, ce qui donne une complexité de $2+ 8\cdot 3 = 29$ :

- la première ligne est constituée de :
  - 2 création de bornes
  - 8 affectations
- l'affichage nécessite 1 opération et qu'il faut retrouver la valeur de $i$

Il aurait été tout aussi légitime de compter différemment, en créant tout le tableau, en stockant la valeur courante, etc. Selon ce que l'on considère le compte serait très différent.

### Algorithmes équivalents aux comptes très différents

Reprenons l'exemple précédent :

```pseudocode
pour chaque (i := entier) de [2 .. 9]:
  affiche i
```

En remplaçant la boucle for par une boucle tant que pour expliciter le calcul, on obtient :

```pseudocode
i := 2
tant que i ≤ 9:
  affiche i
  i ← i + 1
```

Qui est de complexité : $2+1+10(1+1+1) + 9(2+4) = 33 + 9 \cdot 6 = 87$ ce qui semble énorme !

En revanche, si l'on remplace $9$ par $n$ le rapport des deux complexité tend vers une constante : la différence n'est plus si importante que cela lorsque $n$ devient grand.

### Dépend du code/pseudo-code

En écrivant le pseudo-code en code, par exemple en python, il n'est pas garantie du tout que les instructions basiques de mon pseudo-code seront aussi les instructions basiques de l'interpréteur.

L'instruction python `x = 1`{.language-} en python prendra certainement plus que les 2 instructions élémentaires du pseudo-code `x ← 1`{.language-}. l'interpréteur python (il lui faut d'abord créer un objet de type entier, la variable puis les lier) et cela prendra encore plus d'instructions basiques au processeur pour réaliser tout ça. Ah oui, et ça dépend du processeur : un processeur ARM (comme sur les mac) prendra plus d'instructions qu'un processeur INTEL (sur les PC). Sans parler du fait que chaque instruction basique pour un processeur peut prendre plusieurs cycles processeur et que ce n'est pas constant, même pour une instruction donnée (à cause des prédictions).

### Beaucoup de calcul pour par grand chose

Enfin, ce calcul exact semble un peu vain puisqu'au final seule l'allure générale et asymptotique de la complexité nous intéresse. En effet, si les entrées sont de petites tailles c'est de toute façon rapide et lorsque les entrées deviennent grandes :

{% attention "**À retenir**" %}
Les coefficients multiplicatifs et additifs constants sont négligeable par rapport à l'allure logarithmique, linéaire, polynomiale ou exponentielle de la complexité.
{% endattention %}

## Comparaisons asymptotiques

Comme il est impossible de connaître le nombre exact d’instructions et qu'au final on s'en fiche puisque seule la forme générale et asymptotique est importante, on utilise des [comparaisons asymptotiques](https://fr.wikipedia.org/wiki/Comparaison_asymptotique). Avant de les utiliser en algorithmie, commençons par les définir formellement.

{% aller %}
[_fonctions_ de comparaisons asymptotiques](./comparaisons-asymptotiques){.interne}
{% endaller %}

{% aller %}
[Les $\mathcal{O}$ pour l'algorithmie](./O-pour-l-algorithmie){.interne}
{% endaller %}

## Comment calculer la complexité d'algorithmes

{% aller %}
[Calcul de complexités avec des $\mathcal{O}$](./complexité-algorithmes){.interne}
{% endaller %}

## Complexité d'un code

En code, on utilise souvent des fonctions non basiques (comme l'affichage à l'écran qu'on a déjà vu) ou des structures plus élaborées que des tableaux (des listes ou des dictionnaires en python par exemple). Il faut connaître la complexité de chacune de ces fonctions et de la manipulation de ces structures pour pouvoir calculer la complexité du code produit, utiliser une méthode plutôt qu'une autre pouvant mener à une augmentation dramatique de la complexité.

{% attention "**À retenir**" %}
Lorsque l'on calcule la complexité d'un code, toutes les méthodes et fonctions doivent être examinées.
{% endattention %}
