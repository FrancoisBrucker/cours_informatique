---
layout: layout/post.njk
title: "Problème SAT"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

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

## Formule logique et SAT

{% note "**Définition**" %}
[Une formule logique](https://fr.wikipedia.org/wiki/Formule_logique) est soit :

- une variable booléenne
- si $\phi$ est une formule alors $\overline{\phi}$ en est une également
- si $\phi$ et $\psi$ sont deux formules alors :
  - $\phi \land \psi$ en est une également
  - $\phi \lor \psi$ en est une également
  - $\phi \Rightarrow \psi$ en est une également
  - $\phi \Leftrightarrow \psi$ en est une également

Deux formules sont **_égales_** si elles ont les même table de vérité.

{% endnote %}

On peut se ramener aux formules sans implications ou équivalences en utilisant le fait que :

- $\phi \Rightarrow \psi$ est égale à $\overline{\phi} \lor \psi$
- $\phi \Leftrightarrow \psi$ est égale à $(\phi \Rightarrow \psi)\land (\psi \Rightarrow \phi) = (\overline{\phi} \lor \psi) \land (\overline{\psi} \lor \phi)$

{% exercice %}
Montrer que $a \Leftrightarrow (b \lor c)$ peut s'écrire comme une conjonction de clauses.
{% endexercice %}
{% details "corrigé" %}

<div>
$$
\begin{array}{lcl}
a \Leftrightarrow (b \lor c) &=& (\overline{a} \lor (b\lor c)) \land (\overline{b \lor c} \lor a)\\
&=& (\overline{a} \lor b\lor c) \land ((\overline{b} \land \overline{c}) \lor a)\\
&=& (\overline{a} \lor b \lor c) \land (a \lor \overline{b}) \land (a \lor \overline{c})\\
\end{array}
$$
</div>

{% enddetails %}
{% exercice %}
Montrer que $a \Leftrightarrow (b \land c)$ peut s'écrire comme une conjonction de clauses.
{% endexercice %}
{% details "corrigé" %}

<div>
$$
\begin{array}{lcl}
a \Leftrightarrow (a \land c) &=& (\overline{a} \lor (b\land c)) \land (\overline{b \land c} \lor a)\\
&=& ((\overline{a} \lor b)\land (\overline{a} \lorc)) \land ((\overline{b} \lor \overline{c}) \lor a)\\
&=& (\overline{a} \lor b)\land (\overline{a} \lor c) \land (\overline{b} \lor \overline{c} \lor a)\\
\end{array}
$$
</div>

{% enddetails %}

De plus, les propriétés classique suivantes des fonctions logiques permettent d'assurer que l'on peut obtenir toutes les formules classiques avec notre définition.

{% note "**Proposition**" %}

On a les propriétés suivantes :

- idempotence : $\phi \land \phi = \phi$ et $\phi \lor \phi = \phi$
- double négation : $\overline{\overline{\phi}} = \phi$
- commutativité
- associativité

{% endnote %}

> TBD en particulier l'associativité permet de toujours séparer une formule en 2.
> TBD longueur d'une formule = nb de signes logiques.
> TBD pas sous la forme sat donc trouver des équivalents

Enfin, en associant une valeur de vérité à chaque variable, une formule sera vraie ou fausse. Une formule est ainsi une fonction booléenne. On peut alors parler d'égalité de formule si quelque soit la valeur des variables les formules sont égales :

> TBD on peut le faire en utilisant prop distributivité :

{% note "**Proposition**" %}

On a les propriétés suivantes :

- distributivité
- loi de morgan

{% endnote %}
{% details "preuve", "open" %}

> TBD on utilise des tables de vérité.
{% enddetails %}

> TBD  mais possiblement exponentiel.

> exemple

> TBD on peut faire mieux

{% lien %}
[Transformation de Tseitin](https://www.youtube.com/watch?v=v2uW258qIsM)
{% endlien %}

> TBD p26 <https://perso.ensta-paris.fr/~chapoutot/teaching/master-logic/slides/lecture1.pdf>
on peut associer une valeur de vérité à chaque formule et les combiner de façon linéaire

> TBD :
> 1. écrire la formule sous la forme d'un arbre 
> 2. associer une variable à chaque noeud
> 3. propager les équivalences de vérité entre le noeud et ses enfants (non, et, ou).
> 4. la formule finale est équivalente à la formule initiale


> TBD supposé complètement parenthésé, sinon on ajoute par associativité (à gauche)
> 
> 
Évite l'exponentialité si on utilise [que la distributivité](https://fr.wikipedia.org/wiki/Forme_normale_conjonctive#Conversion_lin%C3%A9aire_%C3%A9quisatisfiable
) pour convertir les formules

## Algorithme et SAT

> TBD polylog

tout algorithme s'écrit comme un SAT à résoudre sachant les entrées qui sont données (ex somme). Mais si on connaît la somme, on peut la fixer et l'algo va trouver des entrées !

Si SAT est facile alors trouver des entrées à partir de sorties devient facile et toute la crypto se casse la gueule.

## <span id="3-sat"></span>Le problème 3-SAT

Un cas particulier important du problème `SAT` est le problème `3-SAT` ou toutes les clauses ont exactement 3 littéraux.

### Définition

> résolution 3-sat par backtracking
>
> TBD <https://courses.engr.illinois.edu/cs473/fa2011/lec/21_notes.pdf>
>

### <span id="3-sat-exemple"></span>Exemple

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

### SAT ≤ 3-SAT

- un literal -> 3 littéraux en ajoutant (x) -> (x ou z ou non z)
- deux littéraux -> 3 littéraux (x ou y) -> (x ou y ou z) et (non z)
- n > 3 littéraux (x1 ou ... xn) -> (x1 ou ... xn-2 ou z) et (non z ou xn-1 ou xn)

La transformation est bien linéaire. et résoudre SAT implique 3-sat car les variables binaires ajoutées s'annulent (dans 2 clauses l'une vrai et l'autre fausse) et si 3-SAT alors on en déduit SAT car dans les méta clauses, il y a forcément un des litéraux initiaux qui est vrai.

## Et 2-SAT ?

> Réduction ne fonctionne pas. Autre problème
> 
> Algo poly par limited backtracking : <https://en.wikipedia.org/wiki/2-satisfiability#Limited_backtracking>
> limited backatracking car chaque cas est indépendant donc si on doit backtracker impossible.
> 2-sat poly : <https://cp-algorithms.com/graph/2SAT.html>

On vérifie les conséquences de chaque choix. Une fois tous les obligés fait si pas de contradiction on a un sous ensemble stable et on peut supprimer les clauses ayant ces affectations. Sous cas et on recommence. Si contradiction, on prend l'affectation contraire et on reteste. Si ça rate encore alors affectation impossible.

> TBD refaire dans la partie graphe : strongly connected component : Tarjan <https://github.com/tpn/pdfs/blob/master/Depth-First%20Search%20and%20Linear%20Graph%20Algorithms%20-%20Tarjan%20(1972).pdf>
