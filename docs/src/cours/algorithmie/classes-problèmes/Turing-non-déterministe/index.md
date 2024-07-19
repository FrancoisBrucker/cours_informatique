---
layout: layout/post.njk 
title:  "Machine de Turing non déterministe"

eleventyNavigation:
    order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD trouver un endroit sympa où mettre ça.

Il existe enfin, [la machine de Turing non déterministe](https://fr.wikipedia.org/wiki/Machine_de_Turing_non_d%C3%A9terministe), qui se définit comme suit :

{% note "**définition**" %}
Une ***machine de Turing non déterministe*** diffère de la machine de Turing par sa fonction de transition définie sur $2^{Q \times \\{0, 1\\} \times \\{\leftarrow, \rightarrow\\}}$.
{% endnote %}

Cette machine se distingue de la machine de Turing normale parce que la fonction de transition rend un sous ensemble fini de $Q \times \\{0, 1\\} \times \\{\leftarrow, \rightarrow\\}$ et non juste un nouvel état, un nouveau caractère et une direction : elle donne plusieurs possibilités.

Ce qui nous intéresse ici ce n'est plus l'exécution effective d'une telle machine mais **s'il existe pour une entrée donnée, une suite de transitions emmenant à l'état final**. C'est à dire qu'il existe une suite de nombres $(t_1, \dots, t_k)$ telle que à chaque instruction $i$  on ait pu choisir le $t_i$ème choix pour que la $k$ instruction mène à un état final.

En représentant les choix sous la forme d'un arbre, on peut représenter $\delta$ comme ça :

![Turing non déterministe arbre](turing-nd-arbre.png)

Une exécution de la machine revient à suivre un chemin dans cet arbre, donc qu'à partir de l'état initial $e$ et du caractère $a$ sous le curseur, on a :

* $(e_{t_1}, a_{t_1}, f_{t_1}) \in \delta(e, a)$
* $(e_{t_1\dots t_i}, a_{t_1\dots t_i}, f_{t_1\dots t_i}) \in \delta(e_{t_1t_2\dots t_{i-1}}, a_{t_1t_2\dots t_1i-1})$

C'est un outil théorique très puissant car il permet de démontrer simplement beaucoup de théorèmes d'informatique théorique. Cependant, **elle ne permet pas de faire plus de chose qu'une machine normale** :

{% note %}
Pour toute machine de Turing non déterministe, on peut créer une machine de Turing *normale* qui s'arrêtera sur les même entrées.
{% endnote %}
{% details "idée de la preuve" %}
En utilisant la représentation arborée, on peut faire toutes les possibilités en parcourant l'arbre **couche par couche** (on appelle ça faire un [parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur)).

Pour chaque nœud parcouru, on s'arrête lorsque ce nœud est dans l'état `STOP`. On vérifie si le chemin allant du départ à celui si est possible. Si oui, on s'arrête, sinon on continue le parcourt.

Au final, cette machine de Turing s'arrêtera bien si et seulement si la machine de Turing non déterministe s'arrête.
{% enddetails %}
