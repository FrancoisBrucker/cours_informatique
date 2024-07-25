---
layout: layout/post.njk 
title:  "Réduction de problèmes"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Une méthode classique de résoudre un problème algorithmique ($P_1$) est de le transformer en un autre problème ($P_1$) que l'on sait résoudre ($S_2$)puis de transformer sa solution en une solution du problème initial ($S_1$) :

<div>
$$
\begin{array}{ccc}
P_1 & \rightarrow & P_2\\
\uparrow &  & \downarrow\\
S_1 & \leftarrow & S_2
\end{array}
$$
</div>

La formalisation de cette opération s'appelle [une réduction](https://fr.wikipedia.org/wiki/R%C3%A9duction_(complexit%C3%A9)) et peut prendre plusieurs formes, que nous expliciterons. Outre ses applications pratiques évidentes pour le design d'algorithme et la résolution de problèmes, la réduction est est un outil fondamental permettant de comparer et de classer les problèmes algorithmique.

{% info %}
Nous ne parlerons pas ici de la [Réduction de Turing](https://en.wikipedia.org/wiki/Turing_reduction), trop générale et demandant des connaissances, comme [les machines à oracles](https://fr.wikipedia.org/wiki/Oracle_(machine_de_Turing)), dont nous ne parlerons pas dans ce cours d'algorithmie.
{% endinfo %}

## Définitions

{% note "**Définition**" %}
Soient $P_1$ et $P_2$ deux problèmes algorithmiques. Une **_réduction_** de $P_1$ en $P_2$ est un couple d'algorithmes $A_1$ et $A_2$ tels que :

- Si $E_1$ est une entrée du problème $P_1$ alors $A_1(E_1)$ est une entrée de du problème $P_2$
- Si $S_2$ est une solution au problème $P_2$ avec $A_1(E_1)$ comme entrée alors $A_2(S_2)$ est ue solution au problème $P_1$ d'entrée $E_1$.

Les réductions forment un ordre sur les problèmes algorithmiques : s'il existe une réduction de $P_1$ en $P_2$ on notera $P_1 \leq P_2$ et on dira
que $P_1$ est plus facile que $P_2$.
{% endnote %}

Cette définition, très générale, permet de montrer qu'un problème est plus général qu'un autre : $A \leq B$ signifie que $A$ est un cas particulier de $B$, mais il ne dit rien sur la complexité de passer du problème $A$ au problème $B$, il dit juste que c'est possible. C'est pourquoi on utilise souvent la réduction générale comme outils pour savoir si un problème est calculable on non. On a déjà utilisé ce genre de réduction sans le dire lorsque l'on a démontré [le théorème de Rice](../bases-théoriques/arrêt-rice/#théorème-rice){.interne} par exemple

{% lien %}
[réduction et calculabilité en 5 mins](https://www.youtube.com/watch?v=U4yGQp5aCTM&list=PLhqug0UEsC-IDomfNsn8e3neoy34o8oye&index=9)
{% endlien %}

Si l'on veut une utilisation plus pratique de la réduction, on va chercher le couple d'algorithmes avec la complexité la plus faible, si possible linéaire et au mieux polynomiale :

{% note "**Définition**" %}
Soient $P_1$ et $P_2$ deux problèmes algorithmiques. Une **_réduction polynomiale_** de $P_1$ en $P_2$ est une réduction ou le couple d'algorithmes $A_1$ et $A_2$ est de complexité polynomiale.
{% endnote %}

On a utilisé ce type de réduction lorsque l'on a étudié la complexité de [la recherche de l'enveloppe convexe](../enveloppes-convexes/#complexité-problème)

- réduction calculable : pour la calculabilité (trouver exemple)
- réduction polynomiale : pour la complexité du problème. Ex enveloppe convexe.


> TBD utilisation d'un autre algo = réduction de Turing mais on n'en parlera pas là.

## Exemples

> exemple décidable
> puis exemple pas utile pour arriver à réduction polynomiale
> TBD exemple pas utile. 

### Réduction et calculabilité

### Réduction polynomiale

> TBD définition puis exemple
>
## Le cas de SAT

## TBD

> en faire des exos.

> TBD "gadget" pour la transformation
> exemples.

selon ce que l'on cherche à faire.
passer d'un problème à un autre pour le résoudre.

> TBD
> https://en.wikipedia.org/wiki/Reduction_(complexity) 
> https://fr.wikipedia.org/wiki/R%C3%A9duction_polynomiale 
> exemple :
> - <https://web.stanford.edu/class/archive/cs/cs161/cs161.1138/handouts/070%20Guide%20to%20Reductions.pdf>
> parler du halting problem et de décidabilité
> mais aussi vrai de autre problème on a vu l'enveloppe convexe.
> 
> TBD utiliser les technique de résolution d'un problème dans un autre.
> ne pas parler de problème de décision.
> TBD langage d'une machine de Turing et reco aussi dure qu'on veut (prendre le bout de classe de pb)
> 
>  Doit tenir 2h pour montrer pourquoi NP = problème algo et réduction simple (max ≤ tri ; en trouver un autre.
> on a égalité si ≤ et ≥. Faire exemple simple puis faire SAT = 3-sat (le faire)).
> Faire 2-sat \leq 3-sat eq sat.
> 
>
> TBD : Dire, mais laisser la démo pour plus tard, que SAT est supérieur à tout et donner exemple de réduction ≤ SAT et aussi ≥ SAT mais pas le sac à dos.

> parler de 2-sat ≤ 3-sat = k-sat = sat
> exemple réduction : 
> - <https://opendsa-server.cs.vt.edu/OpenDSA/Books/CS4104/html/Reduction.html>
> - <https://www.cs.princeton.edu/courses/archive/spr03/cs226/lectures/reductions.pdf>