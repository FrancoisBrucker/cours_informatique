---
layout: layout/post.njk

title: Problème du comptage exhaustif de la compelxité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Nous avons calculé explicitement des complexités d'algorithmes dans la partie précédente. Vous avez du vous en rendre compte, c'est assez pénible et pose quelques problèmes.

## Ligne au compte exact incertain

### Plusieurs fois la même variable sur ue instruction

Certaines lignes n'ont pas le même nombre d'instruction selon comment on compte. Reprenons par exemple un compte que l'on a fait précédemment :

```pseudocode
F[i] ← F[i - 1] + F[i - 2]
```

On a considéré que cette instruction nécessitait 3 lectures de la variable `i`{.language-}. Mais dire que l'on ne lit `i`{.language-} qu'une seule fois aurait-été tout aussi légitime.

### itérateurs

Considérons le code suivant :

```pseudocode
pour chaque i de [2 .. 9]:
    affiche i
```

On peut très bien considérer que l'on ne calcule pas tout l'intervalle à chaque itération et que l'on sait quel est l'élément suivant en 1 instruction, ce qui donne une complexité de $2+ 8\cdot (1 + 2) = 26$ :

- la première ligne est constituée de :
  - 2 création de bornes
  - 8 affectations de la variable `i`{.language-}
- 8 affichages sur la seconde ligne d'une variable qu'il faut aller chercher

Il aurait été tout aussi légitime de compter différemment, en créant et en affectant tout le tableau, en stockant la valeur courante, etc. On aurait eu un compte de :

- création de la variable `i`{.language-}
- création d'une variable pour accéder au tableau : 1 instruction
- création du tableau : 8 instructions
- affectations des valeurs au tableau : 2 * 8 instructions (création de l'entier et affectation)
- à chaque itération :
  - affectation la variable `i`{.language-}
  - lecture puis affichage de `i`{.language-}

Pour un total de $2 + 8 \cdot 3 + 8 \cdot 3 = 50$ instructions ! 

Du simple au double. Et encore, que ce serait il passé si on avait écrit la boucle avec un `tant que`{.language-} ?

## Algorithmes équivalents aux comptes très différents

Remplaçons le code précédent par celui-ci qui lui est équivalent :

```pseudocode
ref i ← 2
tant que i ≤ 9:
  affiche i
  i ← i + 1
```

Qui est de complexité : $2+1+10(1+1+1) + 9(2+4) = 33 + 9 \cdot 6 = 87$ ce qui semble énorme !


## Dépend du code/pseudo-code

En écrivant le pseudo-code en code, par exemple en python, il n'est pas garantie du tout que les instructions basiques de mon pseudo-code seront aussi les instructions basiques de l'interpréteur.

L'instruction python `x = 1`{.language-} en python prendra certainement plus que les 2 instructions élémentaires du pseudo-code `x ← 1`{.language-}. l'interpréteur python (il lui faut d'abord créer un objet de type entier, la variable puis les lier) et cela prendra encore plus d'instructions basiques au processeur pour réaliser tout ça. Ah oui, et ça dépend du processeur : un processeur ARM (comme sur les mac) prendra plus d'instructions qu'un processeur INTEL (sur les PC). Sans parler du fait que chaque instruction basique pour un processeur peut prendre plusieurs cycles processeur et que ce n'est pas constant, même pour une instruction donnée (à cause des prédictions).


## Beaucoup de calcul pour par grand chose

Pour notre exemple remplaçons la borne max par n :

```pseudocode
pour chaque i de [2 .. n]:
    affiche i
```

```pseudocode
ref i ← 2
tant que i ≤ n:
  affiche i
  i ← i + 1
```

Et reprenons les calculs :

- 1er code, méthode de calcul 1. La complexité devient : $2+ 3\cdot n$
- 1er code, méthode de calcul 2. La complexité devient : $2 + 6 \cdot n$
- 2er code. La complexité devient : $6 + 9n$

Ces trois codes sont de complexité linéaire en la taille du tableau ce qui suffit largement en algorithmie où c'est l'évolution de la complexité par rapport à la taille des données qui nous intéresse.

On ne peut de toute façon par faire beaucoup mieux sans connaître exactement sur quelle machine sera exécuté le code. POur nos exemple, quelques soient les choix effectués ils sont tous de complexité linéaire ce qui nous suffit.

{% retenir %}
En algorithmie, seule l'allure générale et asymptotique de la complexité importe. 
{% endretenir %}

Si l'optimisation du nombre exacte d'instruction peut-être utile cela ne va servir que pour un code particulier exécuté sur une machine particulière en ayant au départ choisi l'algorithme ayant la meilleure courbe asymptotique possible !

On l'a vu changer la courbe fait gagner énormément, jouer sur la constante multiplicative ou additive ne fait ganger qu'un peu.

 
