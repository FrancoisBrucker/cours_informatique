---
layout: layout/post.njk
title: "Compositions de machines"

eleventyNavigation:
  order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons montrer comment combiner plusieurs machines entres-elles afin de réaliser des machines de plus en plus complexe et aura les mêmes structures de contrôle que le [pseudo-assembleur](../../../exécuter-code/pseudo-assembleur/){.interne} :

1. exécution séquentielle
2. saut
3. saut conditionnel
4. appel de procédures

## Exécution séquentielle de machines

Nous formalisons ici l'[addition](../définitions/#addition-turing){.interne} vue dans la partie entrée.

<span id="exécution-séquentielle"></span>
{% note "**définition**" %}
Soient $M_i$, $1\leq i \leq n$, $n$ machines de Turing de fonctions de transition respectives $\delta^i(q, r) = (\delta^i_e(q, r), \delta^i_c(q, r), \delta^i_d(q, r))$.

L'**_exécution séquentielle_** des $M_i$ machines est alors la machine définie par la fonction de transition $\delta$ telle que :

- Initialisation :
  - $\delta(\text{START}, r) = (\text{START}', r, \rightarrow)$
  - $\delta(\text{START}', r) = ((1, \text{START}), r, \leftarrow)$
- Re-labellisation des états des machines :
  - Pour tout état $q$ de la machine $M_i$ : $\delta((i, q), r) = ((i, \delta^i_e(q, r)), \delta^i_c(q, r),\delta^i_d(q, r))$
- Exécution successive des $n$ machines :
  - $\delta((i, \text{STOP}), r) = ((i, \text{STOP}'), r,\rightarrow)$
  - $\delta((i, \text{STOP}'), r) = ((i+1, \text{START}), r,\leftarrow)$

{% endnote %}
{% info %}
On a ajouté une machine qui fait un aller-retour d'une case entre chaque exécution d'une machine pour garantir que la case du début de la machine $i+1$ est bien la même que la case qui a déclenchée la transition de fin de la machine $i$. Cela est cohérent avec la définition de $M+M'$ et rend indépendant les instructions $i$ et $i+1$.
{% endinfo %}

On pourra écrire l'exécution séquentielle des machines $M_i$ comme l'_algorithme_ :

- $1$: $M_1$
- ...
- $i$: $M_i$
- ...
- $n$: $M_n$

Chaque ligne correspond à une _instruction_ indépendante, l'interaction entre les machines se faisant grâce au ruban.

## Saut

L'exécution séquentielle des machines permet de créer une machine permettant de _sauter_ à une autre ligne du programme. Pour cette machine, on ne relabelle que ses états `START` et `START'` pour coller à son numéro de ligne dans le programme, son état interne sautant déjà vers une ligne donnée du programme :

{% note "**définition**" %}
Dans un programme, La machine **_GOTO LIGNE_** est définie par la fonction de transition :

- $\delta(\text{START}, r) = (\text{START}', r,\rightarrow)$
- $\delta(\text{START}', r) = ((\text{LIGNE}, \text{START}), r,\leftarrow)$

{% endnote %}

## Saut conditionnel

Cette machine est une adaptation de la machine `GOTO`. Elle saute uniquement s'il y a un `1` sur le ruban au niveau du curseur.
Comme pour la machine de saut, on ne relabelle que ses états `START`, `START'` et `STOP` et pas l'état interne qui saute vers une ligne du programme.
La machine suivante saute à une ligne particulière
 :

{% note "**Définition**" %}
La machine **_IF 1 GOTO LIGNE_** est définie par la fonction de transition :

- $\delta(START, 0) = (\text{STOP}, 0,\rightarrow)$
- $\delta(START, 1) = (\text{START}', 1,\rightarrow)$
- $\delta(\text{START}', r) = ((\text{LIGNE}, \text{START}), r,\leftarrow)$

{% endnote %}

Créez le pendant de cette machine :

{% exercice %}
Définissez la machine qui saute à la ligne $\text{LIGNE}$ s'il y a un `0` sur le ruban au niveau du curseur.
{% endexercice %}
{% details "corrigé" %}

La machine **_IF 0 GOTO LIGNE_** est définie par la fonction de transition :

- $\delta(START, 1) = (\text{STOP}, 1,\rightarrow)$
- $\delta(START, 0) = (\text{START}', 0,\rightarrow)$
- $\delta(\text{START}', r) = ((\text{LIGNE}, \text{START}), r,\leftarrow)$

{% enddetails %}

## Appel de procédures

Souvent lorsque l'on crée un programme avec une machine de Turing on se trouve confronté à des machines qui doivent être exécutées dans des contextes différents. Un peu comme un appel de fonction dans du pseudo-code classique.

Pour permettre d'écrire cela de façon condensée on peut définir des labels spéciaux dans nos programmes :

{% note "**définition**" %}

Dans un programme, on permet de définir un label générique **LIGNE: ($p_1, \dots, p_k$): M** où les $p_i$ peuvent prendre toutes les valeurs d'un ensemble $P_i$ **fini**. On peut utiliser les noms $p_i$ ($1\leq i \leq k$) dans la définition de la machine M.

On génère pour cette ligne les transitions :

$$
\delta((\text{LIGNE}(p_1, \dots, p_k), q)) = ((\text{LIGNE}(p_1, \dots, p_k), \delta^M_e(q, r)), \delta^M_c(q, r),\delta^M_d(q, r))
$$

Pour tous les $(p_1, \dots, p_k) \in P_1 \times \dots \times P_k$
{% endnote %}

Cette astuce permet de créer rapidement toute une variété (fini) de cas d'exécutions possibles de la ligne $i$. Elles correspondent cependant à $\vert P \vert^k$ machines différents, ce ne sont pas à proprement parler des paramètres de fonction :

{% attention %}
Attention, ce ne sont pas vraiment des fonctions car on ne fait que créer une fonction de transition pour tous les cas possible. Il est donc nécessaire que le nombre de possibilité soit fini.
{% endattention %}

On a donc une propriété sympathique des machines de Turing :

{% note "**À retenir**" %}
Lorsque le nombre de choix est fini, on peut les simuler par autant d'états différents : on a pas besoin de stocker les possibilités sur le ruban.
{% endnote %}

## Exemple de composition

La composition de machines de Turing permet d'écrire du code comme en pseudo-assembleur, chaque ligne étant soit :

- une machine de Turing
- un saut à une ligne donné
- un saut conditionnel à une ligne donné

Utilisons cette formalisation pour refaire le [doublement de batons](../exemple-doublement-batons) que nous avons fait précédemment.

On va décomposer la machine en plusieurs opérations _"élémentaires"_ :

1. Si `0` aller ligne 9
2. Écrire `0` et aller à droite jusqu'à arriver sur un `0`. Aller à droite.
3. Si `0` aller ligne 5
4. Aller à droite jusqu'à arriver sur un `0`
5. écrire `1` et aller à droite. Écrire `1` et aller à gauche jusqu'à arriver sur un `0`. Aller à gauche.
6. Si `0` aller ligne 8
7. Aller à gauche jusqu'à arriver sur un `0`. Aller à droite
8. retour en 1
9. Aller à droite. Aller à droite

On peut ensuite écrire chacun de ses machines puis les composer.

{% exercice %}
Vérifiez que le programme précédant fonctionne avec `111` comme entrée
{% endexercice %}
{% details "solution" %}

```
entrée      : 011100000000
               ^
fin ligne 2 : 001100000000
                   ^
fin ligne 5 : 001101100000
                 ^
fin ligne 7 : 001101100000
                ^
fin ligne 2 : 000101100000
                   ^
fin ligne 4 : 000101100000
                     ^
fin ligne 5 : 000101111000
                 ^
fin ligne 7 : 000101111000
                 ^
fin ligne 2 : 000001111000
                   ^
fin ligne 4 : 000001111000
                       ^
fin ligne 5 : 000001111110
                 ^
fin étape 3 : 000001111110
                 ^
```

{% enddetails %}

> TBD à finir en écrivant les différentes machines élémentaires