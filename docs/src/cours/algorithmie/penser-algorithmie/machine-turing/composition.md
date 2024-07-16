---
layout: layout/post.njk 
title:  "Compositions de machines"

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD ajouter M1+M2

Nous allons montrer comment combiner plusieurs machines entres-elles afin de réaliser des machines de plus en plus complexe. Ce processus d'agrégation montre que le modèle très simple de la machine de Turing permet en fait de fait tout ce que l'on veut, si l'on sépare bien le problème à résoudre en élément facile à écrire.

Nous allons expliciter les deux principes fondamentaux en algorithmie :

* l'exécution séquentielle de plusieurs machines/instruction
* l'exécution conditionnelle d'une machine/instruction ou d'une autre

## Succession de Machines

Nous formalisons ici l'[addition](./#addition-turing) vue dans la partie entrée.

<span id="exécution-séquentielle"></span>
{% note "**définition**" %}
Soient $M_i$, $1\leq i \leq n$, $n$ machines de Turing de fonctions de transition respectives $\delta^i(q, r) = (\delta^i_e(q, r), \delta^i_c(q, r), \delta^i_d(q, r))$.

L'***exécution séquentielle*** des $M_i$ machines est alors la machine définie par la fonction de transition $\delta$ telle que :

* Initialisation :
  * $\delta(\text{START}, r) = (\text{START}', r, \rightarrow)$
  * $\delta(\text{START}', r) = ((1, \text{START}), r, \leftarrow)$
* Re-labellisation des états des machines :
  * Pour tout état $q$ de la machine $M_i$ :  $\delta((i, q), r) = ((i+1, \delta^i_e(q, r)), \delta^i_c(q, r),\delta^i_d(q, r))$
* Exécution successive des $n$ machines :
  * $\delta((i, \text{STOP}), r) = ((i, \text{STOP}'), r,\rightarrow)$
  * $\delta((i+1, \text{STOP}'), r) = ((i+1, \text{START}), r,\leftarrow)$

{% endnote %}
{% info %}
On a ajouté une machine qui fait un aller-retour d'une case entre chaque exécution d'une machine pour garantir que la case du début de la machine $i+1$ est bien la même que la case qui a déclenchée la transition de fin de la machine $i$. Cela est cohérent avec la définition de $M+M'$ et rend indépendant les instructions $i$ et $i+1$.
{% endinfo %}

On pourra écrire l'exécution séquentielle des machines $M_i$ comme l'*algorithme* :

* $1$: $M_1$
* ...
* $i$: $M_i$
* ...
* $n$: $M_n$

Chaque ligne correspond à une *instruction* indépendante,  l'interaction entre les machines se faisant grâce au ruban.

## Exécution conditionnelle de machines

Pour l'instant nos compositions sont des successions indépendantes de machines. Nous allons utiliser les fonctions de transition pour pouvoir exécuter conditionnellement une machine ou une autre.

Dans la partie précédente, nous avons exécuté des machines de façons successives en utilisant des "*labels*" entiers : la machine de label $i$ s'exécutant juste avant la machine de Label $i+1$. Explicitons cela :

{% note "**définition**" %}
Un ***programme*** est une machine de Turing définie par une succession de lignes : **LABEL: MACHINE**, où chaque label est unique.

Un programme est toujours composé d'un label nommé **MAIN**.

Si on note $\delta^M(q, r) = (\delta^M_e(q, r), \delta^M_c(q, r),\delta^M_d(q, r))$ la fonction de transition d'une machine de uring $M$, la fonction de transition $\delta$ associée à un programme est définie pour chaque ligne **LABEL: M** telle que :

$$
\delta((LABEL, q)) = ((LABEL, \delta^M_e(q, r)), \delta^M_c(q, r),\delta^M_d(q, r))
$$

Le label spécial **MAIN** constitue le départ du programme. Pour démarrer l'exécution du programme, on ajoute à la fonction de transition :

* $\delta(START, r) = (\text{START}'), r,\rightarrow)$
* $\delta(\text{START}', r) = ((MAIN, \text{START}), r,\leftarrow)$

{% endnote %}

Un programme démarre toujours en exécutant la machine de label **START**. Pour passer d'un label à un autre, on peut utiliser la machine spéciale nommée **ALLER label**.

{% note "**définition**" %}
Dans un programme, La machine ***ALLER LABEL*** est définie par la fonction de transition :

* $\delta(START, r) = (\text{START}'), r,\rightarrow)$
* $\delta(\text{START}', r) = ((\text{LABEL}, \text{START}), r,\leftarrow)$

{% endnote %}

Nous n'avons pour l'instant que redéfini de façon plus générale l'[exécution séquentielle](./#exécution-séquentielle) de machines.

{% exercice %}
Utilisez les labels et la machine **ALLER label**, pour redéfinir l'[exécution séquentielle](./#exécution-séquentielle) de machines.
{% endexercice %}
{% details "solution" %}
> TBD
{% enddetails %}

Pour aller plus loin, il nous faut formaliser une machine permettant l'exécution conditionnelle de machines.

{% note "**définition**" %}
Dans un programme, La machine ***SI $x$ LABEL1 SINON LABEL2*** avec $x \in \\{0, 1\\}$ est définie par la fonction de transition :

* $\delta(START, 0) = ((\text{START}', 0), 0,\rightarrow)$
* $\delta(START, 1) = ((\text{START}', 1), 1,\rightarrow)$
* $\delta((\text{START}', 0), r) = ((\text{LABEL1}, \text{START}), r,\leftarrow)$
* $\delta((\text{START}', 1), r) = (((\text{LABEL2}, \text{START}), r,\leftarrow)$

{% endnote %}

## Procédure

Souvent lorsque l'on crée un programme avec une machine de Turing on se trouve confronté à des machines qui doivent être exécutées dans des contextes différents. Un peu comme un appel de fonction dans du pseudo-code classique.

Pour permettre d'écrire cela de façon condensée on peut définir des labels spéciaux dans nos programmes :

{% note "**définition**" %}

Dans un programme, on permet de définir un label générique **LABEL($p_1, \dots, p_k$): M** où les $p_i$ peuvent prendre toutes les valeurs d'un ensemble $P_i$ **fini**. On peut utiliser les noms $p_i$ ($1\leq i \leq k$) dans la définition de la machine M.

On génère pour cette ligne les transitions :

$$
\delta((\text{LABEL}(p_1, \dots, p_k), q)) = ((\text{LABEL}(p_1, \dots, p_k), \delta^M_e(q, r)), \delta^M_c(q, r),\delta^M_d(q, r))
$$

Pour tous les $(p_1, \dots, p_k) \in P_1 \times \dots \times P_k$
{% endnote %}
{% attention %}
Attention, ce ne sont pas vraiment des fonctions car on ne fait que créer une fonction de transition pour tous les cas possible. Il est donc nécessaire que le nombre de possibilité soit fini.
{% endattention %}

## Exemples de composition

### Doublement de bâtons

Utilisons cette formalisation pour réaliser une machine un peu plus complexe que ce que nous avons fait jusqu'à présent :

> Nous allons créer une machine de Turing qui prend en entrée un suite finie de $k$ `1` ($k$ *bâtons*) et rend comme sortie une suite de $2k$ `1` ($2k$ *bâtons*).

Cette machine fait l'opération *fois 2* si l'on encode les entiers positifs par un [système unaire](https://fr.wikipedia.org/wiki/Syst%C3%A8me_unaire).

Pour cela, nous allons utiliser le fait que l'exécution successive de deux machines est également une machine pour décomposer le problème en plusieurs machines élémentaires.

L'idée est de fabriquer la sortie à droite de l'entrée en supprimant itérativement un bâton à l'entrée et d'en ajouter 2 à la sortie. Lorsque l'on aura supprimé tous les bâtons de l'entrée, il ne restera que la sortie et la machine s'arrêtera :

![doublement de bâtons](./turing_double_batons.gif)

Créons cette procédure en combinant des étapes élémentaires (ie pouvant être facilement crées avec une machine de Turing) :

1. Si l'entrée est vide arrêter le programme, sinon écrire un 0 et aller au début de la sortie
2. aller à la fin de la sortie et écrire `11` sur le ruban
3. revenir à la fin de l'entrée
4. revenir au début de l'entrée et retour en 1.

Ce qui donne avec une entrée l'algorithme suivant :

```
entrée      : 011100000000
               ^
fin étape 1 : 001100000000
                   ^ 
fin étape 2 : 001101100000
                     ^ 
fin étape 3 : 001101100000
                 ^ 
fin étape 4 : 001101100000
                ^ 
fin étape 1 : 000101100000
                   ^ 
fin étape 2 : 000101111000
                       ^ 
fin étape 3 : 000101111000
                 ^ 
fin étape 4 : 000101111000
                 ^ 
fin étape 1 : 000001111000
                   ^ 
fin étape 2 : 000001111110
                         ^ 
fin étape 3 : 000001111110
                 ^ 
fin étape 4 : 000001111110
                  ^ 
fin étape 1 : 000001111110
                   ^ 
```

Pour conclure, il nous reste à montrer que notre algorithme peut s'écrire sous la forme d'une machine de Turing.

{% exercice %}
Montrez que chacune des quatre étapes peut être simulées par une machine de Turing
{% endexercice %}
{% details "solution" %}
> TBD
{% enddetails %}
{% exercice %}
En conclure qu'il existe une machine de Turing permettant de faire le doublement de bâton et donnez en la fonction de transition.
{% endexercice %}
{% details "solution" %}
La machine $M = M1 + M2 + M3 + M4$ est presque la solution. Il faut juste s'assurer que l'on stoppe la machine si on lit `0` dans l'état start : \delta^M(\text{START}, 0) = (\text{STOP}, 0, \rightarrow)$, ce qui n'est plus le cas après addition.

{% enddetails %}
{% exercice %}
Combinez les quatres machine en une seule et visualisez le résultat.
{% endexercice %}
{% details "solution" %}

```
blank: 0
start state: START
input: '111'
table:
  START:
    0: {
      write: 0,
      R: STOP
    }
    1: {
      write: 0,
      R: RETOUR
    }
  RETOUR:
    1: {
      write: 1,
      R: RETOUR
    }
    0: {
      write: 0,
      R: START'
    }
  START':
    0: {
      write: 1,
      R: ÉCRIT
    }
    1: {
      write: 1,
      R: START'
    }      
  ÉCRIT:
    0: {
      write: 1,
      L: START''
    }
  START'':
    1: {
      write: 1,
      L: START''
    }
    0: {
      write: 0,
      L: START'''
    }
  START''':
    1: {
      write: 1,
      L: START'''
    }
    0: {
      write: 0,
      R: START
    }
  STOP:
```

{% enddetails %}

### Écrire toutes les k cases

> TBD : à partir d'une machine $M$,  saut de 1 puis de 2 puis 3 et on recommence
