---
layout: layout/post.njk
title: "Problème SAT"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD rappeler la def de la partie NP

Le problème SAT cherche à vérifier si une formule logique peut-être satisfaite.

Pour cela, commençons par définir un concept fondamental en logique la **_conjonction de clauses_** :

<div id="définition-clauses"></div>

{% note "**Définition**" %}
Soient $x_1, \dots, x_n$, $n$ variables booléennes. On définit :

- un **_littéral_** $l$ comme étant soit une variable $l = x_i$, soit sa négation $l = \overline{x_i}$
- une **_clause_** comme étant une disjonction de littéraux $c = l_1 \lor \dots \lor l_k$ (avec $l_1, \dots l_k$ littéraux)
- une **_conjonction de clauses_** comme étant $c = c_1 \land \dots \land c_m$ (avec $c_1, \dots c_m$ des clauses)
{% endnote %}

Le problème `SAT` cherche à savoir s'il existe des valeurs pour lesquelles $f$ est vraie. Si telle est le cas, la conjonction de clause est dite **_satisfiable_** :

{% note "**Problème**" %}

- **Nom** : SAT
- **Entrée** : $f$ une conjonction de clauses sur les variables $x_1$ à $x_n$
- **Sortie** : Une assignation des variables $x_1$ à $x_n$ telle que $f$ soit vraie (ou `∅`{.language-} si cela n'est pas possible).

{% endnote %}
{% info %}
Une formule logique sous la forme d'une disjonction de clause est dite sous la [forme normale conjonctive](https://fr.wikipedia.org/wiki/Forme_normale_conjonctive). Toute formule logique peut être mise sous cette forme grâce à [la transformation de Tseitin](https://fr.wikipedia.org/wiki/Transformation_de_Tseitin) qui est linéaire en nombre d'opérations. Ceci exige de se retrouver avec un nombre exponentiel de clauses si on utilise juste [la distributivité des opérations logiques](https://fr.wikipedia.org/wiki/Forme_normale_conjonctive#Conversion_lin%C3%A9aire_%C3%A9quisatisfiable).

{% endinfo %}

## Formule logique et SAT

> TBD on peut passer par distributivité d'un problème à un autre mais possiblement exponentiel.
> TBD 
[ exemple

> TBD clauses et conjonction de clauses. Montrer que toute fonction booléennes sont des conjonctions de clauses. on passe de dnf à cnf en passant au non. Voir <https://www.csd.uwo.ca/~mmorenom/cs2209_moreno/slide/lec8-9-NF.pdf>

{% lien %}
[Transformation de Tseitin](https://www.youtube.com/watch?v=v2uW258qIsM)
{% endlien %}

Évite l'exponentialité si on utilise [que la distributivité](https://fr.wikipedia.org/wiki/Forme_normale_conjonctive#Conversion_lin%C3%A9aire_%C3%A9quisatisfiable
) pour convertir les formule

## <span id="3-sat"></span>3-SAT est NP-complet

Un cas particulier important du problème `SAT` est le problème `3-SAT` ou toutes les clauses ont exactement 3 littéraux.

> résolution 3-sat par backtracking
>
> TBD <https://courses.engr.illinois.edu/cs473/fa2011/lec/21_notes.pdf>
>


{% lien %}
[Exemple de Wikipédia](https://fr.wikipedia.org/wiki/Probl%C3%A8me_3-SAT#Description)
{% endlien %}

<div>
$$
(x_1 \lor x_2 \lor x_3) \land (\overline{x_1} \lor x_2 \lor x_4) \land (\overline{x_1} \lor x_2 \lor \overline{x_5})\land (\overline{x_3} \lor x_4 \lor x_5)
$$
</div>

Ce qui correspond formellement à :

- la conjonction de 4 clauses $\mathcal{C} = c_1 \land c_2 \land c_3 \land c_4$,
- les 4 clauses $c_i = l_i^1 \lor l_i^2 \lor l_i^3$ pour $1\leq i \leq 4$
- les littéraux $l_i^j$ avec $1\leq i \leq 4$ et $1\leq j \leq 3$ :
  - $l_1^1 = x_1$, $l_1^2 = x_2$, $l_1^3 = x_3$,
  - $l_2^1 = \overline{x_1}$, $l_1^2 = x_2$, $l_1^3 = x_4$,
  - $l_3^1 = \overline{x_1}$, $l_3^2 = x_2$, $l_3^3 = \overline{x_5}$,
  - $l_4^1 = \overline{x_3}$, $l_4^2 = x_4$, $l_4^3 = x_5$.

On a alors les différentes valuations pour les variables, clauses et la conjonctions :

<div>
$$
\begin{array}{ccccc||cccc||c}
x_1&x_2&x_3&x_4&x_5& x_1 \lor x_2 \lor x_3 & \overline{x_1} \lor x_2 \lor x_4 & \overline{x_1} \lor x_2 \lor \overline{x_5} & \overline{x_3} \lor x_4 \lor x_5 & \mathcal{C}\\
0&0&0&0&0& 0&1&1&1&0\\
0&0&0&0&1& 0&1&1&1&0\\
0&0&0&1&0& 0&1&1&1&0\\
0&0&0&1&1& 0&1&1&1&0\\
0&0&1&0&0& 1&1&1&0&0\\
0&0&1&0&1& 1&1&1&1&1\\
0&0&1&1&0& 1&1&1&1&1\\
0&0&1&1&1& 1&1&1&1&1\\
0&1&0&0&0& 1&1&1&0&0\\
0&1&0&0&1& 1&1&1&1&1\\
0&1&0&1&0& 1&1&1&1&1\\
0&1&0&1&1& 1&1&1&1&1\\
0&1&1&0&0& 1&1&1&0&0\\
0&1&1&0&1& 1&1&1&1&1\\
0&1&1&1&0& 1&1&1&1&1\\
0&1&1&1&1& 1&1&1&1&1\\
1&0&0&0&0& 1&0&1&0&0\\
1&0&0&0&1& 1&0&0&1&0\\
1&0&0&1&0& 1&1&1&1&1\\
1&0&0&1&1& 1&1&0&1&0\\
1&0&1&0&0& 1&0&1&0&0\\
1&0&1&0&1& 1&0&0&1&0\\
1&0&1&1&0& 1&1&1&1&1\\
1&0&1&1&1& 1&1&0&1&0\\
1&1&0&0&0& 1&1&1&0&0\\
1&1&0&0&1& 1&1&1&1&1\\
1&1&0&1&0& 1&1&1&1&1\\
1&1&0&1&1& 1&1&1&1&1\\
1&1&1&0&0& 1&1&1&0&0\\
1&1&1&0&1& 1&1&1&1&1\\
1&1&1&1&0& 1&1&1&1&1\\
1&1&1&1&1& 1&1&1&1&1
\end{array}
$$
</div>

Il existe donc plusieurs affectations qui vérifient l'ensemble des clauses. On donne dans le tableau suivant le nombre de littéraux vrais par clause :

<div>
$$
\begin{array}{ccccc||cccc}
x_1&x_2&x_3&x_4&x_5& x_1 \lor x_2 \lor x_3 & \overline{x_1} \lor x_2 \lor x_4 & \overline{x_1} \lor x_2 \lor \overline{x_5} & \overline{x_3} \lor x_4 \lor x_5\\
0&0&1&0&1& 1&1&1&1\\
0&0&1&1&0& 1&2&1&1\\
0&0&1&1&1& 1&2&1&2\\
0&1&0&0&1& 1&2&1&2\\
0&1&0&1&0& 1&3&1&2\\
0&1&0&1&1& 1&3&1&3\\
0&1&1&0&1& 2&2&1&1\\
0&1&1&1&0& 2&3&1&1\\
0&1&1&1&1& 2&3&1&2\\
1&0&0&1&0& 1&2&1&2\\
1&0&1&1&0& 2&1&1&2\\
1&1&0&0&1& 2&1&1&2\\
1&1&0&1&0& 2&2&1&2\\
1&1&0&1&1& 2&2&1&3\\
1&1&1&0&1& 3&1&1&1\\
1&1&1&1&0& 3&2&1&1\\
1&1&1&1&1& 3&2&1&2
\end{array}
$$
</div>

Pour que notre instance ne puisse plus avoir de solution, il faut lui rajouter des clauses. Par exemple les 6 clauses suivantes :

- $x_1 \lor x_2 \lor \overline{x_3}$
- $x_1 \lor \overline{x_2} \lor \overline{x_4}$
- $x_1 \lor \overline{x_2} \lor \overline{x_5}$
- $\overline{x_1} \lor x_2 \lor \overline{x_4}$
- $\overline{x_1} \lor \overline{x_2} \lor x_3$
- $\overline{x_1} \lor \overline{x_2} \lor \overline{x_3}$

Le fait qu'une conjonction de clauses fonctionne ou pas est très dur a voir sans faire tous les cas.


## Et 2-SAT ?

> Réduction ne fonctionne pas. Autre problème
> 
> Algo poly par limited backtracking : <https://en.wikipedia.org/wiki/2-satisfiability#Limited_backtracking>
> limited backatracking car chaque cas est indépendant donc si on doit backtracker impossible.

> 2-sat poly : <https://cp-algorithms.com/graph/2SAT.html>

> TBD faire dans la partie graphe : strongly connected component : Tarjan <https://github.com/tpn/pdfs/blob/master/Depth-First%20Search%20and%20Linear%20Graph%20Algorithms%20-%20Tarjan%20(1972).pdf>
