---
layout: layout/post.njk
title: "Machine de Turing non déterministe"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Une machine de Turing non déterministe est un modèle abstrait  de machine ou il y a plusieurs possibilité par transition. On montre cependant ce que modèles est équivalent à une machine de Turing.

## Définition

{% note "**Définition**" %}
Une **_machine de Turing non déterministe_** est une machine de Turing dont la fonction de transition est définie sur $2^{Q \times \\{0, 1\\} \times \\{\leftarrow, \rightarrow\\}}$.
{% endnote %}

Cette machine se distingue de la machine de Turing normale parce que la fonction de transition rend un sous ensemble fini de $Q \times \\{0, 1\\} \times \\{\leftarrow, \rightarrow\\}$ et non juste un nouvel état, un nouveau caractère et une direction : elle donne plusieurs possibilités. Une machine de Turing normale est un cas particulier de machine de Turing non déterministe.

## Usage

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

La machine de Turing non déterministe n'est qu'une façon plus simple de décrire les mêmes choses. Dans notre cas, cela va unifier la définition des classes $P$ et $NP$.
