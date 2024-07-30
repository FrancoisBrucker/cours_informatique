---
layout: layout/post.njk
title: "Machine de Turing non déterministe"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD dire que c'est équivalent à une machine de Turing et que certificat = choix.

La classe de problème $NP$ est construite via l'existence d'un vérifieur polynomial qui vérifie si la solution est correcte ou pas. Dans le case des problèmes de décision, la réponse (OUI on NON) est adjointe, dans le cas où la réponse est exacte, à un certificat qui donne la raison pour laquelle la solution est exacte.
L'ajout d'un certificat semble artificiel puisqu'on en a pas besoin pour les problèmes de classe $P$.

Nous allons montrer ici comment unifier proprement les classes $P$ et $NP$ sous la bannière des problèmes de décision en utilisant une machine de Turing spéciale (mais équivalente à la machine de Turing classique) : [la machine de Turing non déterministe](https://fr.wikipedia.org/wiki/Machine_de_Turing_non_d%C3%A9terministe).

## Définition

{% note "**Définition**" %}
Une **_machine de Turing non déterministe_** est une machine de Turing dont la fonction de transition est définie sur $2^{Q \times \\{0, 1\\} \times \\{\leftarrow, \rightarrow\\}}$.
{% endnote %}

Cette machine se distingue de la machine de Turing normale parce que la fonction de transition rend un sous ensemble fini de $Q \times \\{0, 1\\} \times \\{\leftarrow, \rightarrow\\}$ et non juste un nouvel état, un nouveau caractère et une direction : elle donne plusieurs possibilités. Une machine de Turing normale est un cas particulier de machine de Turing non déterministe.

{% info %}
On fait exactement la même chose que l'on avait fait avec les [automates déterministes et non-déterministes](../../structure-chaine-de-caractères/automates/){.interne} !
{% endinfo %}

Ce qui nous intéresse ici ce n'est plus l'exécution effective d'une telle machine mais **s'il existe pour une entrée donnée, une suite de transitions emmenant à l'état final**. C'est à dire qu'il existe une suite de nombres $(t_1, \dots, t_k)$ telle que à chaque instruction $i$ on ait pu choisir le $t_i$ème choix pour que la $k$ instruction mène à un état final.

En représentant les choix sous la forme d'un arbre, on peut représenter $\delta$ comme ça :

![Turing non déterministe arbre](turing-nd-arbre.png)

Une exécution de la machine revient à suivre un chemin dans cet arbre, donc qu'à partir de l'état initial $e$ et du caractère $a$ sous le curseur, on a :

- $(e_{t_1}, a_{t_1}, f_{t_1}) \in \delta(e, a)$
- $(e_{t_1\dots t_i}, a_{t_1\dots t_i}, f_{t_1\dots t_i}) \in \delta(e_{t_1t_2\dots t_{i-1}}, a_{t_1t_2\dots t_1i-1})$

C'est un outil théorique très puissant car il permet de démontrer simplement beaucoup de théorèmes d'informatique théorique. Cependant, **elle ne permet pas de faire plus de chose qu'une machine normale**.

## Équivalence avec une machine de Turing

{% note "**Proposition**" %}
Pour toute machine de Turing non déterministe, on peut créer une machine de Turing _normale_ qui s'arrêtera sur les même entrées.
{% endnote %}
{% details "preuve", "open" %}
Soit $M$ une machine de Turing non déterministe à $Q$ états. On va construire une machine de Turing déterministe sous la forme d'un pseudo-code, qui simule $M$.

```
k = 1

Tant que Vrai:
  on construit un tableau T contenant tous les mots de $Q$ de longueur $k$ (il y en a $2^k$)
  pour chaque élément e de T:
    exécuter M en suivant, si possible les éléments de e dans l'ordre lorsqu'il y a un choix.
    Si l'exécution de M est possible et se termine rendre la sortie de M
  k = k+1
```

> TBD renvoyer à l'exercice du lancer de $k$ dés pour le pseudo-code de l'algorithme qui trouve tous les mots de longueur $k$.

Si la machine $M$ s'arrête, c'est qu'il existe une suite de choix qui lui permette de s'arrêter. Cette suite étant de longueur finie, notre algorithme finira forcément par la considérer et il s'arrêtera.
{% enddetails %}

La machine de Turing non déterministe est, tout comme les automates non déterministes, qu'une façon plus simple de décrire les mêmes choses. Dans notre cas, cela va unifier la définition des classes $P$ et $NP$.

## P et NP revisités

Un problème de décision est équivalent à son langage. On peut donc définir $P$ et $NP$ uniquement comme ça.

{% note "**Définition**" %}
**_Un langage est de la classe_** $P$ s'il existe une machine de Turing de complexité polynomiale qui l'accepte.
{% endnote %}

{% note "**Définition**" %}
**_Un langage est de la classe_** $NP$ s'il existe une machine de Turing non déterministe de complexité polynomiale qui l'accepte.
{% endnote %}

Avec cette définition, le certificat est la suite de choix effectués par la machine de Turing non déterministe. Voyez ces choix comme un oracle (ou un prof) qui vous guide tout au long du déroulement de la machine. On peut s'en passer mais cela prendrait beaucoup de temps (faire tout les choix amène à une complexité exponentielle). Si on sait déjà ou aller en revanche, on peut trouver rapidement une solution (en temps polynomiale).

{% attention %}
Tout ceci fonctionne car le nombre d'état est une **constante**, il ne dépend pas de l'entrée qui peut être aussi grande que l'on veut.
{% endattention %}
