---
layout: layout/post.njk
title: "Problème CE"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons montrer que le problème Couverture Exacte est NP-complet

<span id="problème-EC"></span><span id="problème-CE"></span>

{% note "**Problème**" %}

- **Nom** : Couverture Exacte (_exact cover_)
- **Entrée** :
  - un ensemble fini $U$ d'éléments
  - un ensemble $\mathcal{S}$ de sous-ensembles de $U$
- **Sortie** : Un ensemble $\mathcal{P} \subseteq \mathcal{S}$ formant une partition de $U$ (ou `∅`{.language-} si cela n'est pas possible).
  {% endnote %}
  {% info %}
  Une partition $\mathcal{P}$ d'un ensemble $U$ est un ensemble de sous-ensembles de $U$ tel que :
- l'union des éléments de $\mathcal{P}$ vaut $U$,
- l'intersection de deux éléments différents de $\mathcal{P}$ est vide.
  {% endinfo %}

Illustrons ce problème en reprenant [un exemple tiré de Wikipédia](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_couverture_exacte#Exemple_2) :

- $U = \\{1, 2, 3, 4, 5, 6, 7\\}$
- $\mathcal{S} = \\{ \\{1, 4, 7\\}, \\{1, 4\\}, \\{4, 5, 7\\},\\{3, 5, 6\\},\\{2, 3, 6, 7\\},\\{2, 7\\}  \\}$

Résoudre ce problème revient à faire plein de choix. Parfois ces choix sont simple : si on place $\\{1, 4, 7\\}$ on ne peut plus mettre que la classe $\\{3, 5, 6\\}$ qui ne forme pas une partition ; parfois les choix sont plus cornéliens : doit-on placer la classe $\\{3, 5, 6\\}$, ce qui empêche d'utiliser la classe $\\{4, 5, 7\\}$ (par exemple) ? Ou ne pas la mettre ? A priori on ne sais pas.

{% exercice %}
Montrez que l'exemple possède une solution.
{% endexercice %}
{% details "solution" %}

On prend les 3 classes :

- $\\{1, 4\\}$,
- $\\{3, 5, 6\\}$,
- $\\{2, 7\\}$

{% enddetails %}

Prouver que le problème de Couverture Exact (CE) est NP-Complet va être plus facile que celle du théorème de Cook/Levin. En effet, maintenant que l'ensemble des problème NP-complet est non vide (il y a au moins SAT dedans), pour montrer qu'un problème $A$ est NP-complet il nous suffit maintenant de :

1. choisir un problème $B$ NP-complet
2. montrer qu'il existe une réduction polynomiale $B \leq A$

En effet, si $C$ est un problème quelconque de NP, on a $C\leq B$ (par définition de l'ensemble NP-complet) ce qui amène par transitivité de la réduction polynomiale à $C \leq A$.

Pour l'instant nous ne connaissons qu'un problème NP-Complet : SAT. Montrons donc que $SAT \leq CE$.

Les réductions pour montrer qu'un problème est NP-complet peuvent être étrange au premier regard. Elles nécessitent souvent des constructions baroques pour associer un problème à l'autre. On appelle ces constructions des **_gadget_**. Ceci est normal car on essaie de mettre en regard deux problèmes qui n'ont souvent rien à voir. On va le faire ici en mettant en parallèle un problème de logique SAT et un problème de recherche de sous-ensemble CE.

## Gadget

On considère une instance de SAT que l'on va transformer polynomialement en une instance de CE. Posons ses paramètres :

- $x_1, \dots, x_n$ : les $n$ variables booléennes
- $c_1 \land \dots \land c_m$ : les $m$ conjonctions de clauses
- $c_i = l^1_i \lor \dots \lor l^{k_i}_i$ : les littéraux formant les clauses.

On suppose de plus sans perte de généralité que :

1. il n'existe pas de clause ayant à la fois $x_i$ et $\overline{x_i}$ comme littéral (sinon cette clause est trivialement toujours vérifiée)
2. pour toute variable booléenne $x_i$ il existe une clause ayant $x_i$ comme littéral et une autre clause ayant $\overline{x_i}$ (sinon il suffit de mettre la modalité de $x_i$ à celle apparaissant dans les clauses pour les rendre trivialement vraies)

Notez que l'on peut transformer toute instance de $SAT$ en une instance satisfaisant les deux conditions ci-dessus en supprimant les clauses satisfaisant la première condition et en supprimant la variable booléenne satisfaisant la seconde condition. Cette transformation se fait en temps polynomial par rapport à l'entrée de $SAT$.

On peut maintenant transformer cette instance de $SAT$ en une instance de $CE$ ayant comme entrée :

<div>
$$
\begin{array}{lll}
U = &\{ x_i \vert 1 \leq i \leq n \} \cup&\text{variables booléenne}\\
&\{ c_i \vert 1 \leq i \leq m \} \cup&\text{clauses}\\
&\{ l_{i}^{j} \vert 1 \leq i \leq m, 1\leq j \leq k_i \}&\text{littéraux}\\
\mathcal{S} = &(\cup_{1\leq i \leq n}[\{ x_i \} \cup \{ l_{j}^{k} \vert l_{j}^{k} = x_i, 1 \leq j \leq m, 1\leq k \leq k_i\})] \cup &\text{littéraux vrais pour }x_i\\
&(\cup_{1\leq i \leq n}[\{ x_i\} \cup \{ l_{j}^{k} \vert l_{j}^{k} = \overline{x_i}, 1 \leq j \leq m, 1\leq k \leq k_i\})] \cup &\text{littéraux faux pour }x_i\\
&(\cup_{1\leq i \leq m}(\cup_{1\leq k \leq k_i}\{ c_i, l_{i}^{k} \})) &\text{liens entre clauses et littéraux}\\
&(\cup_{1\leq i \leq m}(\cup_{1\leq k \leq k_i}\{ l_{i}^{k} \})) &\text{les littéraux}\\
\end{array}
$$
</div>

L'ensemble de $CE$ couvre tous les éléments de $SAT$ : les variables booléennes, les clauses et les littéraux. Les classes forment les liens entre les différents éléments : pour chaque $x_i$ les littéraux valant $x_i$, pour chaque $x_i$ les littéraux valant $\overline{x_i}$ et pour chaque clause l'ensemble de ses littéraux. Cette construction est bien polynomiale par rapport à la taille de l'entrée du problème $SAT$.

Notre gadget transforme [L'instance exemple SAT](#exemple-SAT){.interne} en une instance de $CE$.

Formule SAT originelle :

<div>
$$
\underbracket{(x_1 \lor {x_2})}_{c_1 = l_1^1 \lor l_1^2} \land \underbracket{(\overline{x_1} \lor \overline{x_2} \lor \overline{x_3})}_{c_2 = l_2^1 \lor l_2^2 \lor l_2^3} \land \underbracket{(\overline{x_1} \lor x_3 \lor x_4 \lor \overline{x_5})}_{c_3 = l_3^1 \lor l_3^2 \lor l_3^3 \lor l_3^4} \land \underbracket{({x_1} \lor \overline{x_3} \lor \overline{x_4} \lor {x_5})}_{c_4 = l_4^1 \lor l_4^2 \lor l_4^3 \lor l_4^3}
$$
</div>

Entrée de CE associée :

<div>
$$
\begin{array}{ll}
U = &\{ x_1, x_2, x_3, x_4, x_5, c_1, c_2, c_3, c_4, l_1^1, l_1^2, l_2^1, l_2^2, l_2^3, l_3^1, l_3^2, l_3^3, l_3^4, l_4^1, l_4^2, l_4^3, l_4^4\}\\
\mathcal{S} = &\{\{x_1, l_1^1, l_4^1\}, \{x_2, l_1^2\}, \{x_3, l_3^2\}, \{x_4, l_3^3\}, \{x_5, l_4^4\},\\
& \{x_1, l_2^1, l_3^1\}, \{x_2, l_2^2\}, \{x_3, l_2^3, l_4^2\}, \{x_4, l_4^3\}, \{x_5, l_3^4\},\\
& \{c_1, l_1^1\}, \{c_1, l_1^2\}, \{c_2, l_2^1\}, \{c_2, l_2^2\}, \{c_2, l_2^3\}, \{c_3, l_3^1\}, \{c_3, l_3^2\}, \{c_3, l_3^3\}, \{c_3, l_3^4\}, \{c_4, l_4^1\}, \{c_4, l_4^2\}, \{c_4, l_4^3\}, \{c_4, l_4^4\}\\
& \{l_1^1\}, \{l_1^2\}, \{l_2^1\}, \{l_2^2\}, \{l_2^3\}, \{l_3^1\}, \{l_3^2\}, \{l_3^3\}, \{l_3^4\}, \{l_4^1\}, \{l_4^2\}, \{l_4^3\}, \{ l_4^4\}\}
\end{array}
$$
</div>

Nous allons montrer sur l'exemple que ce gadget fonctionne. Je cas général en découlera de lui-même. Il faut faire deux choses :

1. montrer que si le problème de CE admet une solution alors le problème SAT originel aussi
2. montrer que si le problème de CE n'admet pas de solution alors le problème SAT originel non plus

On montre très souvent la 2. condition par la réciproque (montrer que montrer que si le problème SAT originel admet une solution alors le problème CE aussi), ce qui permet d'être symétrique :

- Si CE à une solution alors SAT aussi
- Si SAT à une solution alors CE aussi

## Solution de CE vers une solution de SAT

Pour comprendre comment une solution de CE permet de trouver une solution de SAT, reprenons notre exemple et cherchons une partition solution. Il en existe plusieurs, par exemple :

<div>
$$
\begin{array}{ll}
\mathcal{P} = &\{ \{x_2, l_1^2\},  \{x_4, l_3^3\},\\
& \{x_1, l_2^1, l_3^1\}, \{x_3, l_2^3, l_4^2\}, \{x_5, l_3^4\},\\
& \{c_1, l_1^1\}, \{c_2, l_2^2\}, \{c_3, l_3^2\}, \{c_4, l_4^1\},\\
&   \{l_3^2\}, \{l_3^4\}, \{ l_4^3\}, \{ l_4^4\} \}
\end{array}
$$
</div>

Pour repasser de cette solution de CE à une solution de SAT, regardons comment elle est construite :

- il faut que la partition contienne les $c_i$ : de part la construction de $\mathcal{S}$ ceci signifie que la classe contenant $c_i$ va également contenir 1 $l_i^j$.
- il faut que la partition contienne les $x_i$ : de part la construction de $\mathcal{S}$ ceci signifie que la classe contenant $x_i$ va également contenir des $l_j^k$. Attention ces $l_j^k$ ne doivent pas être celui choisi dans la classe contenant $c_j$
- tous les autres littéraux pouvant être attribués comme on le souhaite on peut les _"oublier"_.

Pour notre exemple ceci donne :

<div>
$$
\begin{array}{l}
\{c_1, l_1^1\}, \{c_2, l_2^2\}, \{c_3, l_3^2\}, \{c_4, l_4^1\}\\
\{x_1, l_2^1, l_3^1\}, \{x_2, l_1^2\}, \{x_3, l_2^3, l_4^2\}, \{x_4, l_3^3\}, \{x_5, l_3^4\}\\
\end{array}
$$
</div>

Remarquez que le choix de la classe contenant la clause contraint la classe contenant la variable. En choisissant $\\{c_1, l_1^1\\}$ je force le choix de $\\{x_1, l_2^1, l_3^1\\}$ puisque $l_1^1 = x_1$. Vous venez de découvrir le gadget : la classe contenant $c_i$ force le choix pour $x_j$ en prenant le littéral opposé.

Comme une solution de SAT doit avoir au moins 1 littéral de vrai par clause, regardons ce qu'il se passe si on suppose que c'est celui choisi dans la clause est vrai. Dans l'exemple :

- $l_1^1$ est vrai donc $x_1$ est vrai
- $l_2^2$ est vrai donc $\overline{x_2}$ est vrai
- $l_3^2$ est vrai donc ${x_3}$ est vrai
- $l_4^1$ est vrai donc ${x_1}$ est vrai

On ne peut pas arriver àla conclusion qu'une variable booléenne est vrai **et** fausse, car sinon il est impossible de choisir une classe contenant cette variable : c'est le principe du gadget qui implique que ces choix sont cohérents avec les classes contenant les $x_i$ (qui correspondent aux littéraux faux).

On sait déjà que $x_1$, $\overline{x_2}$ et ${x_3}$ sont vrais. Pour connaître la valeur des autres variables, on regarde les classes choisies :

- $\{x_1, l_2^1, l_3^1\}$ donc $l_2^1 = \overline{x_1}$ et $l_3^1 = \overline{x_1}$ sont faux donc $x_1$ est vrai (ouf, c'est cohérent)
- $\{x_2, l_1^2\}$ donc $l_1^2 = {x_2}$ est faux (c'est cohérent)
- $\{x_3, l_2^3, l_4^2\}$ donc $l_2^3 = l_4^2 = \overline{x_3}$ est faux : $x_3$ est vrai (c'est cohérent)
- $\{x_4, l_3^3\}$ donc $l_3^3 = {x_4}$ est faux. On ne le savait pas encore
- $\{x_5, l_3^4\}$ donc $l_2^3 = l_3^4 = \overline{x_5}$ est faux : ${x_5}$ est vrai.

Au final, avoir une partition nous garantit que le problème SAT originel a une solution et la donne !

On reconstruit cette solution en temps (clairement) polynomial.

## Solution de SAT vers une solution de CE

Il faut maintenant montrer que si notre instance de $SAT$ à une solution alors notre instance de $CE$ en a également une.

Il suffit de faire la même chose que pour l'analyse précédente. Si l'instance de SAT a une solution, chaque clause $c_i$ possède au moins un littéral $l_i^{v(i)}$ qui est vrai. On peut alors considérer l'ensemble des classes formé de l'union de :

- $\\{c_i, l_i^{v(i)}\\}$ pour tout $ 1\leq i \leq m$,
- Considérons ensuite chaque littéral $l_i^j$ avec $ j \neq v(i)$ pour la solution de SAT. On a deux cas :
  - soit $l_i^j$ est vrai et on ajoute $\\{ l_i^j\\}$ à la solution de $CE$
  - soit $l_i^j$ est faux et on ajoute l'unique classe de $\mathcal{F}$ contenant $\\{x_i, l_i^j\\}$ à la solution de $CE$

De part nos hypothèses sur l'entrée de $SAT$ il est clair que cet ensemble de classes forme une solution à notre problème de $CE$. De plus, la construction de cette solution est bien polynomiale.

{% exercice %}
Donnez une solution de CE pour l'exemple différente de celle de l'exercice précédent et servez vous en pour reconstruire une solution du problème SAT initial.
{% endexercice %}
{% details "solution" %}

On peut par exemple prendre :

<div>
$$
\begin{array}{ll}
\mathcal{P} = &\{\{x_1, l_1^1, l_4^1\}, \{x_3, l_3^2\}, \{x_4, l_3^3\}, \\
& \{x_2, l_2^2\}, \{x_5, l_3^4\},\\
& \{c_1, l_1^2\}, \{c_2, l_2^3\}, \{c_3, l_3^1\}, \{c_4, l_4^2\},\\
& \{l_2^1\}, \{l_3^3\}, \{ l_4^3\}, \{ l_4^4\}\}
\end{array}
$$
</div>

Ce qui donne comme solution de $SAT$ : $\overline{x_1} = {x_2} = \overline{x_3} = \overline{x_4} = x_5 = 1$
{% enddetails %}

## Conclusion

On vient de prouver $SAT\leq CE$ car :

1. $CE$ est dans NP
2. il existe une réduction polynomiale de SAT vers CE
