---
layout: layout/post.njk 
title:  "Problème SAT"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD tout algo est un sat.
> TBD on a vue que les opérations peuvent être mise sous forme logique. C'est aussi vrai pour les structures de contrôle.
> TBD on vu que toute fonction est un sat et que tout circuit logique est un sat. Le problème SAT va être fondamental.
> TBD dire que toute fonction booléenne vectorielle s'écrit comme une conjonction de clause. et que comme on passe d'un problème à l'autre, on peut le faire puisque nos entrées sont données.

> TBD dire taille des variables dépendant de la taille des entrées. Au pire = complexité. Ne change pas si dans P.

> TBD : Dire, mais laisser la démo pour plus tard, que SAT est supérieur à tout et donner exemple de réduction ≤ SAT et aussi ≥ SAT mais pas le sac à dos.

Nous allons intensivement utiliser la réduction pour classer les problèmes algorithmiques, et en particulier les réduction depuis [le problème SAT](https://fr.wikipedia.org/wiki/Probl%C3%A8me_SAT).

Nous avons entraperçu le problème lorsque nous avons parlé de [pseudo-assembleur](../exécuter-code/pseudo-assembleur#clauses) et que tout les fonctions de $\\{0, 1\\}^n$ dans $\\{0, 1\\}$ peuvent s'écrire comme conjonction de clauses :

Pour cela, commençons par définir un concept fondamental en logique la _**conjonction de clauses**_ :

<div id="clauses"></div>
{% note "**Définition**" %}
Soient $x_1, \dots, x_n$, $n$ variables binaires. On définit :

- un **_littéral_** $l$ comme étant soit une variable $l = x_i$, soit sa négation $l = \overline{x_i}$
- une **_clause_** comme étant une disjonction de littéraux $c = l_1 \lor \dots \lor l_k$ (avec $l_1, \dots l_k$ littéraux)
- une **_conjonction de clauses_** comme étant $c = c_1 \land \dots \land c_m$ (avec $c_1, \dots c_m$ des clauses)
{% endnote %}

{% note "**Définition**" %}

```text
nom: SAT
entrée : f une conjonction de clauses sur les variables x[1] à x[n]
Question: existe-t-il une assignation de x[1] à x[n] tel que f soit égale à 1 ?
```

{% endnote %}

Le problème `SAT` cherche à savoir s'il existe des valeurs pour lesquelles $f$ est vraie. Si telle est le cas, la conjonction de clause est dite **_satisfiable_**.

> TBD dire que si on a une solution potentielle alors facile de savoir si vrai solution (donner algo) mais que trouver l'algo on ne sait pas trop à part essayer toutes les solution (donner nb de solutions).
> TBD Résolution basique énumération en $2^n$ vrai/faux pour chaque variable.

> TBD toute formule logique peut s'écrire comme une conjonction de clause. CNF-SAT mais on peut passer de toute formule à SAT en temps linéaire :

## Modélisation

Tout problème se résout via un SAT. Pas toujours facile de s'y ramener, mais parfois c'est bien

### Fonctions booléennes

> TBD clauses et conjonction de clauses. Montrer que toute fonction booléennes sont des conjonctions de clauses.

on passe de dnf à cnf en passant au non. Voir <https://www.csd.uwo.ca/~mmorenom/cs2209_moreno/slide/lec8-9-NF.pdf>

### Formules logiques

{% lien %}
[Transformation de Tseitin](https://www.youtube.com/watch?v=v2uW258qIsM)
{% endlien %}

Évite l'exponentialité si on utilise [que la distributivité](https://fr.wikipedia.org/wiki/Forme_normale_conjonctive#Conversion_lin%C3%A9aire_%C3%A9quisatisfiable
) pour convertir les formules.

### Exemple du sudoku

> p47 <https://members.femto-st.fr/pierre-cyrille-heam/sites/femto-st.fr.pierre-cyrille-heam/files/content/Enseignement/cours-satsolveurs.pdf>

## <span id="3-sat"></span>3-SAT

Un cas particulier important du problème `SAT` est le problème `3-SAT` ou toutes les clauses ont exactement 3 littéraux.

### <span id="3-sat-exemple"></span> Exemple

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

### équivalent à SAT

> TBD <https://cse.iitkgp.ac.in/~palash/2018AlgoDesignAnalysis/SAT-3SAT.pdf>

Permet certaines réductions de façon bien plus facile.

## 2-SAT

> Réduction ne fonctionne pas. Autre problème
> 
> Algo poly par limited backtracking : <https://en.wikipedia.org/wiki/2-satisfiability#Limited_backtracking>
> limited backatracking car chaque cas est indépendant donc si on doit rbacktracker impossible.

> 2-sat poly : <https://cp-algorithms.com/graph/2SAT.html>

> TBD faire dans la partie graphe : strongly connected component : Tarjan <https://github.com/tpn/pdfs/blob/master/Depth-First%20Search%20and%20Linear%20Graph%20Algorithms%20-%20Tarjan%20(1972).pdf>

## Inversibilité du problème SAT

> TBD fct booléenne de l'addition ou du produit. Comme c'est une fonction booléenne cela permet d'avoir une réponse mais aussi d'avoir les entrées.
>
> TBD on y reviendra mais en crypto c'est crucial de ne pas pouvoir  faire... Par exemple pour les produit de 2 nombres premiers. On revient au fait que factor doit être de complexité importante.
> 
> polylog circuit et sat : <https://www.youtube.com/watch?v=6OPsH8PK7xM>
>
>

> exemple réduction :
>
> résolution 3-sat par backtracking
>
> TBD <https://courses.engr.illinois.edu/cs473/fa2011/lec/21_notes.pdf>
>
## Résolution de SAT

> TBD : <https://people.csail.mit.edu/virgi/6.s078/lecture3and4.pdf>
