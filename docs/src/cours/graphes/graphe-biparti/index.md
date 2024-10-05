---
layout: layout/post.njk

title: Graphes biparti

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les graphes biparti font parti de ces classes de graphes assez généraux pour être présent partout et assez spécifique pour que tous se passe bien (les principaux problèmes NP-complets dans le cas général deviennent polynomiaux voir triviaux).

{% note "**Définition**" %}
Un graphe $G=(V, E)$ est **_biparti_** s'il existe une bipartition $V_1$ et $V_2$ de $V$  en deux [stables](../structure/#definition-stable).
{% endnote  %}

Par exemple le graphe suivant :

![exemple biparti](exemple-biparti.png)

On a déjà vu ce genre de graphe, sans le savoir lors de [l'étude du transport amoureux](../projet-flots-modélisation/#transport-amoureux) : le problème du mariage entre 2 populations distinctes se modélise comme un graphe bi-parti où chaque population est un stable.

{% exercice %}
Montrez que si un graphe bi-parti est connexe, sa bi-partition en deux stables est unique.
{% endexercice %}
{% details "solution" %}
Si le graphe est connexe, on peut parcourir celui-ci (en largeur ou en profondeur) à partir d'une racine pour créer un arbre planté.

Chaque élément sera forcément dans le stable différent de son parent : l'affectation de chaque élément dépend uniquement de l'affectation de la racine.

{% enddetails %}

La propriété précédente n'est bien sur plus vraie si le graphe n'est pas connexe :

{% exercice %}
Montrez que  le graphe discret (sans arêtes) à $n$ sommets possède $2^{n-1}-1$ bi-partitions possibles.

{% endexercice %}
{% details "solution" %}

Par récurrence. Un graphe discret à 2 sommets possède bien $2^{2-1}-1 = 1$ bipartition.

On suppose la propriété vrai pour les ensembles à $n$ éléments et soit le graphe discret $G=(V, \varnothing)$ à $n+1$ sommets et soit $x$ un de ces éléments. Pour toute les bipartitions $x$ est dans une des deux partitions et, à part celle où $x$ est tout seul dans une classes, si on supprime $x$ on a une bipartition d'un ensemble à $n$ éléments : une bipartition à $n+1$ élément est donc soit :

- $\\{\\{x\\}, V\backslash \\{x\\}\\}$
- $\\{U\cup \\{x\\}, V\\}$ ou $\\{U, V\cup \\{x\\}\\}$ avec $\\{U, V\\}$ une bipartition de $V\backslash \\{x\\}$

Il y a donc $2\cdot (2^{n-1}-1) + 1 = 2^n-1$ bipartitions à $n+1$ éléments (il y en a $2^{n-1}-1$ pour un ensemble à $n$ éléments par hypothèse de récurrence), ce qui conclut la preuve.

{% enddetails %}
{% info %}
Le nombre de partitions d'un ensemble à $n$ éléments en $k$ sous-ensembles est appelé [nombre de Stirling de second espèce](https://fr.wikipedia.org/wiki/Nombre_de_Stirling#Nombre_de_Stirling_de_seconde_esp%C3%A8ce)
{% endinfo %}

En conclure :

{% exercice %}
Montrez qu'un graphe biparti à $p$ composantes connexes possède $2^{p}-1$ bipartitions possibles.
{% endexercice %}
{% details "solution" %}

Soient $\\{X_i, Y_i\\}$, $1\leq i \leq p$, les $p$ bipartitions associées au stables des $p$ composantes connexes de $G$. Un des deux stables de $G$ sera alors :

- soit l'union de tous les $X_i$
- soit une partie des $X_i$, ce qui correspond à ue bipartition des $X_i$, $1\leq i \leq p$.

Il y a donc autant de de façon de faire que de bipartition à $p$ élément plus 1.

{% enddetails %}

## Reconnaissance

Savoir si un graphe est biparti est _"facile"_ en utilisant un algorithme de marquage qui associe une couleur à chaque sommet.

On considère que le graphe est connexe dans l'algorithme suivant, o. S'il ne l'est pas on le relance sur chacune des parties connexes.

On retrouve un algorithme de marquage puis examen de sommets, comme [l'algorithme de recherche de chaîne augmentante de Ford et Fulkerson](../flots). Ce principe général permet de résoudre efficacement beaucoup de problèmes en théorie des graphes.

```python
Initialisation :

    On possède deux couleurs.
    Soit x un sommet du graphe que l'on marque avec une couleur

Boucle principale :

    tant qu'il existe x, un sommet marqué non examiné:

        examiner x
        pour chaque voisin y de x :
            si y est marqué avec la couleur de x:
                FIN : le graphe n'est pas biparti
            sinon si y n'est pas marqué:
                marquer y avec la couleur différente de celle de x
    
    FIN : le graphe est biparti et la couleur des sommets determine les 2 stables

```

> TBD à écrire propre

1. on voit bien tous les sommets car connexe : on le fait par récurrence sur la longueur du chemin entre $x$ et $y$
2. chaque couleur est obligatoire
3. linéaire n+m si on utilise un parcours en largeur (les éléments marqués sont dans une file).

## Caractérisation

{% note "**Proposition**" %}

Un graphe est biparti si et seulement si il ne contient pas de cycle de longueur impaire.

{% endnote  %}

Vous allez en faire la démonstration grâce à deux exercices.

{% exercice %}

Un graphe biparti ne contient pas de cycle de longueur impaire.

{% endexercice  %}
{% details "corrigé" %}

Si le graphe possède un cycle, ses arêtes doivent passer d'un stable à l'autre un nombre pair de fois.

{% enddetails %}

Et dans l'autre sens :

{% exercice %}

Un graphe n'est pas biparti s'il contient un cycle de longueur impaire.

{% endexercice  %}
{% details "corrigé" %}
On utilise l'algorithme et si l'algorithme répond non c'est qu'on a un cycle de longueur impaire.
{% enddetails %}

## Généralisations

### Biparti complets

{% note "**Définition**" %}
Un **_graphe biparti complet_** est le graphe $K_{p,q} = (V_p \cup V_q, V_p \times V_q)$, avec $\vert V_p \vert = p$ et $\vert V_q \vert = q$

{% endnote %}

Le graphe $K_{2, 3}$ est par exemple :

![$K_{2, 3}$](k23.png)

{% info %}
Les graphes bipartis complets sont aussi parfois appelé [**_une biclique**_](https://fr.wikipedia.org/wiki/Graphe_biparti_complet)

{% endinfo %}

On retrouve les graphes bi-partis complets dans plein de champs de la théorie des graphes car ils ont plein de chouettes propriétés. Par exemple :

{% exercice %}
Montrez que si un graphe biparti est hamiltonien, alors la taille des 2 stables est identique. En déduire que seuls graphes bipartis complets hamiltoniens sont les graphes $K_{p, p}$ avec $p\geq 1$.

{% endexercice %}
{% details "solution" %}

Si le graphe biparti admet un cycle hamiltonien il est connexe et donc n'admet qu'un 2 stables. Soit $x_1x_2\dots x_nx_1$ un cycle hamiltonien. Comme un graphe biparti ne peut avoir de cycle de longueur impaire $n$ est forcément paire.

On conclue la preuve en remarquant que les $x_i$ paires et les $x_i$ impairs sont forcément dans des stables différents.

{% enddetails %}

### Triparti

> TBD 3-parti NP-complet. Reconnaissance est NP-complet !
>
>
> un gadget : les preuve de NP-complétude le font.
> entre 2 et 3 le soucis. Comme 2 et 3 SAT
> NPC 3 coloriable : <https://www.enseignement.polytechnique.fr/informatique/INF412/uploads/Main/chap13-goodINF412.pdf> p10 3-coloriable.

### $k$-partis

> TBD $k$-parti et $k$-parti complets

## Partition en graphes Biparti

Le problème de partition d'un graphe en graphes bipartis est un problème de communication réseau initialement posé (et résolu) par les deux chercheurs Graham et Pollak des laboratoires Bell dans les années 1970.

{% lien %}
[Problème de Graham-Pollak](https://www.youtube.com/watch?v=ZtXfGagSUlA)
{% endlien %}

Posons le problème en commençant par définir une partition d'un graphe.

{% note "**Définition**" %}
Une **_partition_** d'un graphe $G=(V, E)$ est une suite $G_i=(V_i, E_i)$, avec $1\leq i \leq m$ telle que :

- $V_i \subseteq = V$ pour tout $1\leq i \neq j \leq m$
- $\cup_{1\leq i \leq m} E_i = E$
- $E_i \cap E_j = \varnothing$ pour tout $1\leq i \neq j \leq m$

{% endnote %}

La définition explicite le fait que l'on partitionne l'ensemble des arêtes d'un graphe. On spécifie souvent la famille de graphe à laquelle la partition doit appartenir (pour nous des graphes bipartis) et comme tout graphe à $n$ sommet est inclut dans $K_n$ la clique à $n$ sommet, c'est lui que l'on va chercher à partitionner.

Notre problème de partition est :

{% note "**Définition**" %}
Combien faut-il au minimum de graphes bipartis complets pour partitionner $K_n$ ?

{% endnote %}

Remarquons tout de suite que ce problème admet une solution, il en faut moins de $n(n-1)/2$ puisque les graphes G_{i,j} = (\\{i, j\\}, \\{ij\\})$ sont tous bipartis.

On peut bien sur faire mieux, comme le montre l'exemple suivant qui partitionne $K_6$ en 6 graphes bi-partis complets :

![exemple biparti](k6-en-6.png)

Vous avez peut-être remarqué, mais la partition ci-dessus n'est pas minimale, on peut faire mieux :

{% exercice %}

Montrer que l'on peut toujours décomposer $K_n$ en $n-1$ étoiles.
{% endexercice  %}
{% note "**Définition**" %}
Une **_étoile_** est un graphe $G = (V, E)$ tel qu'il existe $x\in V$ avec $E = \\{xy | y \in V\backslash \\{x\\}\\}$
{% endnote  %}

{% details "corrigé" %}

Les étoiles en questions sont $G_i = (V_i, E_i)$ avec $1\leq i < n$ :

- $V_i = \\{j | j \geq i \\}$
- $E_i = \\{\\{i, j\\} | i < j \\}$

{% enddetails %}

Le partitionnement en étoile n'est pas unique, par exemple avec $K_6$ :

![exemple biparti min](k6-en-5.png)

En revanche, $n-1$ est bien le minimum :

{% note "**Proposition**" %}

On ne peut décomposer $K_n$ en moins de $n-1$ graphes bipartis complets.

{% endnote  %}
{% details "preuve", "open" %}

La preuve est atypique et ne parlera pas de graphes. De plus, on ne connaît pas de preuve combinatoire. J'ai repris la preuve de _Proofs from the book_ (chapitre 11, théorème 4 de la sixième édition) qui comme chacune des preuves du livre est extrêmement élégante.

Soit $K_n$ le graphe complet avec comme ensemble de sommets $V = \\{1, \dots, n\\}$. Soit $(B_k)_{1\leq k \leq m}$ une de ses décompositions en en $m$ graphes bipartis complets, et on note également $\\{U_k, V_k\\}$ les deux stables de $B_k$.

Soient $x_1, \dots, x_n$, $n$ variables réelles. On considère alors [Le système d'équations linéaires](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27%C3%A9quations_lin%C3%A9aires) formé des $m+1$ équations suivantes :

- $\sum_{1\leq i \leq n}x_i = 0$
- $\sum_{i \in U_k}x_i = 0$ pour tout $1\leq k \leq m$

Si $m + 1 < n$ [ce système va posséder une solution non nulle](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27%C3%A9quations_lin%C3%A9aires#Nombre_de_solutions_d%E2%80%99un_syst%C3%A8me_d'%C3%A9quations) $(c_1, \dots, c_n)$ (il existe $i$ tel que $c_i \neq 0$). Nous allons montrer que ceci est impossible.

En effet, comme pour tout $i \neq j$, il n'existe qu'un unique $k$ tel que $x_i \in U_k$ et $x_j \in V_k$, de là on a l'égalité :

<div>
$$
\begin{array}{lcl}
\sum\limits_{i < j}x_ix_j &=& \sum\limits_{1\leq k \leq m}(\sum\limits_{(i, j) \in U_k\times V_k} x_i \cdot x_j)\\
&=& \sum\limits_{1\leq k \leq m}[(\sum\limits_{i \in U_k} x_i)\cdot (\sum\limits_{i \in V_k} x_j)]
\end{array}
$$
</div>

Comme $\sum_{1\leq i\leq n}c_i = 0$ on a aussi :

<div>
$$
\begin{array}{lcl}
0 &=& (\sum\limits_{1\leq i\leq n}c_i)^2\\
&=&\sum\limits_{1\leq i\leq n}c_i^2 + \sum\limits_{i < j}c_ic_j\\
&=&\sum\limits_{1\leq i\leq n}c_i^2 + \sum\limits_{1\leq k \leq m}[(\sum\limits_{i \in U_k} c_i)\cdot (\sum\limits_{i \in V_k} c_j)]\\
\end{array}
$$
</div>

Or $\sum_{i \in U_k}x_i = 0$ pour tout $1\leq k \leq m$, donc $\sum_{i \in U_k}c_i = 0$ également, ce qui implique :

<div>
$$
\begin{array}{lcl}
0 &=& \sum\limits_{1\leq i\leq n}c_i^2\\
\end{array}
$$
</div>

Ce qui n'est possible que si $c_i = 0$ pour tout $1\leq i \leq n$ : contradiction. Notre hypothèse était donc fausse, on a $m + 1 = n$.

{% enddetails %}
