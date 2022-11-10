---
layout: layout/post.njk
title: Chemins, cycles et connexité
authors: 
    - François Brucker

eleventyNavigation:
  key: "Chemins, cycles et connexité"
  parent: "Graphes"
---

<!-- début résumé -->

Chemins, cycle et connexité dans les graphes : définitions et premières propriétés.

<!-- fin résumé -->

Un graphe $G=(V, E)$ rend compte d'une *relation* (les arêtes) entre des objets (les sommets). Une grande part des applications des graphes viennent du fait que l'on cherche à décrire ou parcourir objets en suivant localement les relations. Cette curte partie vise à poser les diverses définitions relatives à ces notions et à exhiber quelques propriétés soit utiles, soit belles à démontrer, soit les deux.

## Chemin, cycles et circuits

{% note "**Définition :**" %}
Soit $G = (V, E)$ un (multi-)graphe (non) orienté. Un **chemin allant de $v_0$ à $v_{k-1}$** est une suite finie :

$$C = v_0v_1\dots v_i \dots v_{k-1}$$

de sommets du graphe telle que :

1. $v_iv_{i+1}$ soit une arête (*resp.* arc) du graphe quelque soit $0 \leq i < k-1$
2. les arcs (*resp.* arêtes) sont deux à deux distinctes.
  
Le chemin $C$ à une **longueur** de $k$ (c'est le nombre d'arêtes). Un chemin de longueur $0$ est le chemin conteant un unique sommet, sans arc (*resp.* arête).

{% endnote %}

On peut affaiblir la notion de chemin pour les graphes orienté :

{% note "**Définition :**" %}
Soit $G = (V, E)$ un (multi-)graphe orienté. Une **chaîne** est une suite :

$$C = v_0v_1\dots v_i \dots v_{k-1}$$

de sommets du graphe telle que :

1. soit $v_iv_{i+1}$ soit $v_{i+1}v_i$ est un arc du graphe pour tout $0 \leq i < k-1$
2. les arcs sont deux à deux distincts.
  
La chaîne $C$ à une **longueur** de $k$ (c'est le nombre d'arcs).

{% endnote %}

Un chemin nous permet de définir un cycle pour les graphes non-orientés :

{% note "**Définition :**" %}
Soit $G = (V, E)$ un (multi-)graphe non orienté. Un **cycle** est un chemin

$$C = v_0v_1\dots v_i \dots v_k$$

tel que $v_0 = v_k$

La cycle $C$ à une **longueur** de $k$ (c'est le nombre d'arêtes).
{% endnote %}

Pour les graphes orientés, ça se complique un peu car on a coutume de différentier cycle (le sens de l'arc est indifférent) de circuit (on peut parcourir le cycle dans l'ordre) :

{% note "**Définition :**" %}
Soit $G = (V, E)$ un (multi-)graphe orienté. Un **cycle**  est une suite finie :

$$C = v_0v_1\dots v_i \dots v_k$$

de sommets du graphe telle que :

1. soit $v_iv_{i+1}$ soit $v_{i+1}v_i$ est un arc du graphe quelque soit $0 \leq i < k$
2. les arcs sont deux à deux distinctes.
3. $v_0 = v_k$

{% endnote %}

{% note "**Définition :**" %}
Soit $G = (V, E)$ un (multi-)graphe orienté. Un **circuit** est un cycle :

$$C = v_0v_1\dots v_i \dots v_k$$

de sommets du graphe telle que $v_iv_{i+1}$ est un arc du graphe quelque soit $0 \leq i < k$

{% endnote %}

### Chemins et cycles élémentaires

Les définitions de chemins et cycles supposent que les arêtes ou arcs n'apparaissent pas deux fois. Si cette précaution permet d'éviter les chemin de taille infini, certains problèmes nécessitent de pouvoir passer plusieurs fois par les mêmes arêtes ou au contraire de ne passer qu'une seule fois par chaque sommet :

<div id="pseudo-"></div>

{% note "**Définition**" %}
Soit $G = (V, E)$ un graphe orienté. Un **pseudo-chemin** est une suite finie $C = v_0v_1\dots v_i \dots v_{k-1}$ une suite de sommets du graphe telle que $v_iv_{i+1}$ est un arc du graphe quelque soit $0 \leq i < k-1$.
{% endnote  %}
{% note "**Définition**" %}
Soit $G = (V, E)$ un graphe orienté. Un **chemin élémentaire** (*resp.* cycle ou circuit élémentaire) est un chemin (*resp.* cycle ou circuit) $C = v_0v_1\dots v_i \dots v_{k-1}$ tel que $v_i \neq v_j$ quelque soit $i \neq j.
{% endnote  %}

{% info %}
Notez qu'un pseudo-chemin/pseudo-cycle/pseudo-circuit où chaque sommet n'apparaît qu'une seule fois est forcément un chemin/cycle/circuit élémentaire !
{% endinfo %}

Ces notions sont bien sûr liées comme le montre les deux propositions ci-dessous :

{% note "**Proposition**" %}

* De tout pseudo-chemin, pseudo-chaîne, pseudo-cycle ou pseudo-circuit allant de $x$ à $y$ on peut extraire un chemin, chaîne, cycle ou circuit allant de $x$ à $y$.
* De tout chemin, chaîne, cycle ou circuit  allant de $x$ à $y$, on peut extraire un chemin, chaîne, cycle ou circuit élémentaire  allant de $x$ à $y$.
{% endnote %}
{% details "Preuve" %}
Nous n'allons faire la preuve que pour les chemins. Les autres preuves sont équivalentes.

Soit $G=(V, E)$ un graphe et $c=v_0 \dots v_p$ un de ses pseudo-chemins qui n'est pas un chemin. Il existe donc $i < j$ tel que $v_iv_{i+1} = v_jv_{j+1}$ et $c'= v_0\dots v_iv_{j+1}\dots v_k$ est un autre pseudo-chemin allant de $v_0$ à $v_k$ ayant strictement moins de répétition d'arêtes que $c$ : on peut itérativement supprimer les répétitions d'arêtes d'un pseudo-chemin pour obtenir un chemin.

De là même manière, si $c=v_0 \dots v_p$ est un chemins non élémentaire, il existe $i < j$ tel que $v_i = v_j$ : le chemin $c' = v_0 \dots v_iv_{j+1}\dots v_k$ est un autre chemin allant de $v_0$ à $v_k$ ayant strictement moins de répétition de sommets que $c$ : on peut itérativement supprimer les répétitions de sommets d'un chemin pour obtenir un chemin élémentaire.
{% enddetails %}

{% attention %}
La réduction d'un pseudo-cycles (ou pseudo-circuit) peut engendrer un cycle (ou circuit) de longueur nulle ! e n'est pas le cas pour tous les autres cas.
{% endattention %}

## Connexité

{% note "**Définition :**" %}
Un graphe est dit **connexe** si pour toute paire de sommets $x$ et $y$ il existe un chemin allant de $x$ à $y$ dans $G$.

Si le graphe est orienté :

* il est **connexe** si pour toute paire de sommets $x$ et $y$ il existe un chemin allant de $x$ à $y$ ou un chemin allant de $y$ à $x$ dans $G$.
* il est dit **fortement connexe** s'il existe pour toute paire $x$ et $y$ de sommet un chemin allant de $x$ à $y$ et un chemin allant de $y$ à $x$.
{% endnote %}

La connexité est une notion très importante en théorie des graphes. Elle permet de relier deux sommets entre eux par des relations. D'un point de vue pratique on aime bien les graphes connexes, pensez à *google maps* où l'on aime bien pouvoir faire des aller-retours.

{% note "**Définition :**" %}
Soit $G=(V, E)$ un graphe orienté ou non.

* Un **ensemble connexe** $Y \subseteq V$ de $G$ est tel que quelque soit $x \neq y \in Y$ il existe un chemin entre $x$ et $y$ ou entre $y$ et $x$.
* Un **ensemble fortement connexe** $Y \subseteq V$ de $G$ est tel que quelque soit $x \neq y \in Y$ il existe un chemin entre $x$ et $y$ et entre $y$ et $x$.
* Une **composante (fortement) connexe** $Y \subseteq V$ de $G$ est un ensemble (fortement) connexe maximal pour l'inclusion.

{% endnote %}

Les composantes connexes d'un graphe $G$ forment ainsi un Souvent (toujours) si un graphe n'est pas connexe on le partitionnera en ses **composantes connexes** qui peuvent être vues en vertu de la proposition suivante comme des graphes distincts que l'on peut analyser séparément.

{% note "**Proposition :**" %}

* Si $G=(V, E)$ est un graphe, l'ensemble $\mathcal{C} = \{ V_1, \dots, V_p \}$ de ses composantes connexe est une partition :

* $V_i \cap V_j = \varnothing$ si $i \neq j$
* quelque soit $x \in V_i$ et $y\in V_j$ avec $i \neq j$, $xy \notin E$
* $ \sum_i V_i = V$

Si le le graphe est orienté, on a le même résultat en considérant l'ensemble de des composantes fortement connexes.

{% endnote %}
{% details "Preuve :" %}
L'union de deux ensemble fortement connexes non disjointes est encore un ensemble fortement connexe : deux composantes fortement connexes sont forcément disjointes.
{% enddetails %}
{% attention %}
Les composantes connexes d'un graphe orienté ne sont pas forcément disjointes, comme le montre l'exemple ci-après :

![g carré g solution](./connexe_pas_fortement.png)

{% endattention %}
Enfin, Du point de vue de la connexité, certains sommet ou arêtes sont plus important que d'autres :

{% note "**Définition :**" %}
Soit $G$ un graphe connexe.

* Un **isthme** est une arête qui déconnecte le graphe si on la supprime
* Un **nœud d'articulation** est une arête qui déconnecte le graphe si on le supprime

{% endnote %}

Par exemple, dans des réseau routiers, les isthme et les nœuds n'articulations vont créer des bouchons s'ils sont saturés (le tunnel sous Fourvière par exemple).

## Propriétés fondamentales d'existence

On le verra plus précisément lorsque l'on parlera d'arbres, mais les notions de connexités, de chemins et de cycles (notions globales) sont très liés aux degrés des différents sommets (conditions locales). Les propositions fondamentales d'existence ci après le montrent. Bien qu'elles soient très simples, elles se révèlent souvent utile, soit par les propriétés elles-mêmes soit par leurs schémas de preuves qui s'appliquent très souvent.

Commençons par donner des condition d'existence de chemins et cycles de longueur donnée :

{% note "**Proposition :**" %}
<div id="prop-cycles-graphe"></div>
Soit $G = (V, E)$ un graphe. S'il existe un entier $k > 1$ tel que $\delta(x) \geq k$ pour tout $x \in V$, alors :

* pour tout $x \in V$ il existe un chemin élémentaire de longueur $k$ partant de $x$ ,
* il existe un cycle élémentaire de longueur au moins $k+1$,

{% endnote %}
{% details "preuve" %}

Soit $c = v_0\dots v_i$ un chemin de longueur $i < k$ partant de $x = v_0$ (pour $i = 0< k$, ce chemin est réduit au seul point $x$).

Comme $\delta(v_i) = k > i$ il existe un voisin $y$ de $v_i$ qui n'est pas un élément du chemin. On peut donc nommer $v_{i+1} = y$ et étendre $c$ d'un élément à $c= v_0\dots v_iv_{i+1}$. Ceci montre que l'on peut étendre $c$ à un chemin de longueur $k$.

Une fois que $c = v_0\dots v_i$ a atteint la longueur $k$, on peut continuer cette procédure en cherchant à agrandir $c$ par un sommet $v_{i+1}$ tel que :

* $v_iv_{i+1}$ est une arête du graphe
* n'ayant aucun sommet $v_j$ avec $i+1 - k < j < i+1$ comme voisin (il y en a $k-1$)

De deux choses l'une :

1. soit $v_{i+1}$ n'a aucun voisin dans $c$, on peut agrandir $c$ et recommencer
2. soit $v_{i+1}$ a un voisin dans $c$ et on a trouvé un cycle de longueur au moins $k+1$

Par finitude du graphe il arrivera forcément un moment où l'on atteindra le cas 2 ce qui conclut la preuve.

{% enddetails %}

De même pour garantir la connexité d'un graphe :

{% note "**Proposition :**" %}

Un graphe $G=(V, E)$ tel que (avec $\vert V \vert = n$ et $\vert E \vert = m$) :

$$
m > \frac{(n-1)(n-2)}{2}
$$

est connexe.
{% endnote %}
{% details "preuve" %}
On montre la preuve par récurrence. Si $n=2$, il faut évidemment avoir $m > 0$ pour que le graphe soit connexe. On suppose la propriété vraie pour $\vert V \vert = n-1$ et on se place à $\vert V \vert = n \geq 2$.

Si le graphe est complet on a $m = \frac{n(n-1)}{2} > \frac{(n-1)(n-2)}{2}$ et le graphe est trivialement connexe. Il existe donc un sommet $x$ de degré $\delta(x) < n-1$. De plus, s'il existait un sommet sans voisin, le nombre d'arêtes serait strictement plus petit $\frac{(n-1)(n-2)}{2}$ ce qui est impossible. On a donc également $\delta(x) \geq 1$.

Le nombre d'arêtes $m'$ du sous-graphe $G'$ induit par la suppression de $x$ dans $G$ vaut :

<div>
$$
\begin{array}{ccl}
m' & = & m - \delta(x) \\
&\geq &m - (n-2) \\
&> &\frac{(n-1)(n-2)}{2} - (n-2)\\
&> &\frac{(n-2)(n-3)}{2}\\
\end{array}
$$
</div>

Le graphe $G'$ est donc connexe par hypothèse de récurrence, donc $G$ l'est aussi puisque $\delta(x) > 0$ (la composante connexe contenant $x$ intersecte $V \backslash \{ x\}$ qui est un ensemble connexe de $G$).

{% enddetails %}

Notez bien que ces propositions ne sont que des implications. Si l'on prend le graphe $G=(\\{v_1, \dots, v_n\\}, E)$ avec $E = \\{ v_iv_{i+1} \mid 1 \leq i \leq n \\} \cup \\{ v_1v_n \\}$ il :

* est connexe alors qu'il a $n < \frac{(n-1)(n-2)}{2}$ arêtes si $n \geq 5$,
* admet un cycle de longueur $n$ alors que le degré de chaque élément est $2$.

## Algorithmes

On utilisera le graphe suivant pour nos algorithmes :

```python
G = {
    "a": {"b", "c"},
    "b": {"a", "c"},
    "c": {"a", "b"},
    "d": {}
}
```

{% note %}
L'encodage par défaut des graphes sera toujours celui [par dictionnaires](../encodage#dict).
{% endnote %}

### Algorithme de recherche de composante connexe

```python#
def composante_connexe(G, origine):
    composante = {origine}
    suivant = [origine]

    while suivant:
        x = suivant.pop()

        for y in G[x]:
            if y not in composante:
                composante.add(y)
                suivant.append(y)

    return composante
```

On utilise :

* méthodes des [liste](https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists) :
  * la méthode `pop`{.language-} qui permet de supprimer le dernier élément de la liste et le rendre
  * la méthode `append`{.language-} qui permet d'ajouter un élément à la fin de la liste
* méthodes des [ensembles](https://docs.python.org/fr/3/tutorial/datastructures.html#sets) :
  * création avec les accolades
  * méthode `add`{.language-} qui ajoute un élément à l'ensemble

#### Complexité <div id="comp-conn-complexité"></div>

L'algorithme précédent utilise un ensemble pour stocker la composante connexe car :

* ajouter un élément à un ensemble prend $\mathcal{O}(1)$ opérations en moyenne
* savoir si un élément est dans un ensemble prend $\mathcal{O}(1)$ opérations en moyenne

Pour une liste :

* l'ajout d'un élément à la liste avec la méthode `append`{.language-} prend $\mathcal{O}(1)$ opérations
* la suppression d'un élément à la liste avec la méthode `pop`{.language-} prend $\mathcal{O}(1)$ opérations

La complexité de l'algorithme va ainsi dépendre :

* du nombre de fois où la boucle while de la ligne 5 va être exécutée
* de la nature des éléments $x$ de la boucle

Pour notre encodage, Toutes les opérations élémentaires de l'algorithme sont donc en $\mathcal{O}(1)$ opérations au maximum sauf le test de la ligne 9 et l'ajout à la composante de la ligne 10 qui est en $\mathcal{O}(1)$ opérations en moyenne.

Enfin, comme chaque sommet ne peut-être ajouté à suivant que s'il n'est pas encore dans la composante, chaque sommet ne peut y être ajouté qu'une fois : il y a au pire $\vert V \vert$ itérations de la boucle `while`{.language-} de la ligne 5 et chaque sommet ne peut être choisi qu'au pire 1 fois comme élément `x`{.language-} de la ligne 6. Et pour chaque élément la complexité de la boucle while sera de l'ordre de $\mathcal{O}(\delta(x))$ opérations en moyenne (le nombre de fois où l'on rentre dans la la boucle for)

On en conclut :

{% note %}
La complexité de l'algorithme `composante_connexe`{.language-} est pour un graphe encodé par dictionnaire de $\mathcal{O}(\vert E\vert)$ opérations en moyenne.

Il est donc linéaire en moyenne par rapport à la taille du graphe en entrée.
{% endnote %}

{% exercice %}
Dans le cas où l'encodage du graphe est une liste d'adjacence, on peut changer la structure de `composante`{.language-} pour que sa complexité (maximale) soit en $\mathcal{O}(\vert E \vert)$ opérations.

Quelle est cette structure ?
{% endexercice %}
{% details "solution" %}
Dans le codage par liste d'adjacence, les sommets sont des entiers entre $0$ et $n-1$. On peut alors utiliser une liste de $n$ booléens pour composante. On place `composante[i]`{.language-} à `True`{.language-} lorsque l'on place le sommet $i$ dans la composante.

Toutes les opérations sur `composante`{.language-} effectuée par l'algorithme sont en $\mathcal{O}(1)$ opérations au maximum.

{% enddetails %}

#### Preuve <div id="comp-conn-preuve"></div>

L'algorithme va progresser de voisinage en voisinage et ajouter petit à petit les éléments qu'il n'a pas encore vu. S'il existe un chemin entre $x$ et $y$, $y$ chaque élément de ce chemin va être petit à petit intégré à la composante.

### Trouver un chemin

L'algorithme suivant, nommé `chemin`{.language-}, prend un graphe et deux sommets $a$ et $b$ en paramètres. Il rend soit un chemin entre $a$ et $b$ s'il existe soit le chemin vide si $a$ et $b$ sont dans deux composantes connexes différentes.

```python#
def chemin(G, a, b):
    examinés = {a}
    chemin = [a]

    x = a
    while x != b:
        suivants = G[x] - examinés
        if suivants:
            y = suivants.pop()
            examinés.add(y)
            chemin.append(y)
        else:
            chemin.pop()

        if chemin:
            x = chemin[-1]
        else:
            break

    return chemin
```

On utilise :

* méthodes des [liste](https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists) :
  * la méthode `pop`{.language-} qui permet de supprimer le dernier élément de la liste et le rendre
  * la méthode `append`{.language-} qui permet d'ajouter un élément à la fin de la liste
  * le fait quel'on puisse accéder au dernier élément d'une liste avec un indice de `-1`{.language-}
* méthodes des [ensembles](https://docs.python.org/fr/3/tutorial/datastructures.html#sets) :
  * création avec les accolades
  * méthode `add`{.language-} qui ajoute un élément à l'ensemble
  * la soustraction de deux ensembles qui rend un nouvel ensemble contenant les éléments du premier ensemble non présent dans le second.
* la commande `break`{.langage-} qui sort de la boucle la plus imbriquée, ici la boucle `while`{.language-} de la ligne 6.
* les tests des lignes 8 et 15 qui rendent faut si l'ensemble ou la liste sont respectivement vides.

#### Complexité <div id="chemin-complexité"></div>

La complexité de chaque itération `while`{.language-} de la ligne 6 et de l'ordre de $\mathcal{O}(\delta(x))$ opérations car il faut trouver un voisin non encore examiné. Comme à chaque fois qu'un voisin est utilisé, il est examiné, un même sommet pourra être le `x`{.language-} de la boucle while au maximum $\delta(x)$ fois. De là, la complexité globale de l'algorithme est de l'ordre de :

$$
C = \mathcal{O}(\sum_x (\delta(x))^2) \leq \mathcal{O}((\sum_x \delta(x))^2) = \mathcal{O}((2 \vert E \vert)^2) = \mathcal{O}(\vert E \vert^2)
$$

{% note %}
Notez que cet algorithme recalcule plein de fois la même chose : tous les voisins de $x$. Une version optimisée de cet algorithme, appelé parcours en profondeur et que nous verrons plus tard, permet de faire la même chose avec une complexité linéaire (c'est à dire la taille du graphe): $\mathcal{O}(\vert E \vert)$.
{% endnote %}

#### Preuve <div id="chemin-preuve"></div>

Le preuve de l'algorithme repose sur la proposition suivante :

{% note "**Proposition :**" %}
Soit $G = (V, E)$ un graphe connexe et $a, b\in V$.

S'il existe  un chemin allant de $a$ à $x$ :

* ne passant pas par $b$
* tel que tous les voisins de $x$ soient dans le chemin

Alors il existe un chemin allant de $a$ à $b$ ne passant pas par $x$.
{% endnote %}
{% details "preuve" %}

Soit $c= a\dots x = v_0\dots v_p$ le chemin allant de $a$ à $x$ et $c' = a \dots b = w_0\dots w_q$ un chemin allant de $a$ à $b$ passant par $x$.

On note $1 \leq i < q$ le plus grand indice tel qu'il existe $1\leq j < p$ avec $w_i = v_j$. Comme $x$ est sur $c'$ :

* cet élément existe
* il est placé après $x$ dans $c'$

Le chemin $v_0 \dots v_i w_{j+1} \dots w_q$ est un chemin allant de $a$ à $b$ ne passant pas pas $x$.

{% enddetails %}

> TBD : preuve détaillée de l'algorithme.

### Trouver un circuit ou un cycle

Pour trouver un cycle, l'algorithme `chemin`{.language-} précédent ne fonctionne pas directement en prenant $a=b$. En effet, c'est le cycle de longueur nulle qui est rendu. Il faut ajouter une *sentinelle* pour que la sortie ne se fasse que si la longueur du chemin est strictement positive.

Ceci n'est cependant pas suffisant car comme $a$ est dans l'ensemble `examiné`{.language-} dès le départ, il ne pourra jamais être retrouvé par l'algorithme. Il faut donc commencer par un ensemble de sommets examinés vide.

Ceci est suffisant pour trouver des circuits dans des graphes orienté. On obtient l'algorithme suivant :

<div id="algo-cycle-oriente"></div>

```python#
def circuit(G, a):
    examinés = set()
    chemin = [a]

    x = a
    while (x != a) or (len(chemin) == 1):
        suivants = G[x] - examinés
        if suivants:
            y = suivants.pop()
            examinés.add(y)
            chemin.append(y)
        else:
            chemin.pop()

        if chemin:
            x = chemin[-1]
        else:
            break

    return chemin
```

Si les graphes sont non orientés, on risque de trouver de *faux* cycle de type $[a, b, a]$ où on réutilise la même arête deux fois (prise une fois dans $G[a]$ et l'autre fois dans $G[b]$). Il ne faut donc permettre à l'algorithme de choisir $a$ que si la longueur du chemin est strictement plus grande que 1. On obtient finalement l'algorithme suivant pour les graphes non-orienté :

<div id="algo-cycle-non-oriente"></div>

```python#
def cycle_non_orienté(G, a):
    examinés = set()
    chemin = [a]

    x = a
    while (x != a) or (len(chemin) == 1):
        suivants = G[x] - examinés
        if suivants:
            y = suivants.pop()
            if y == a and (len(chemin) < 3):
                if suivants:
                    y = suivants.pop()
                    examinés.add(y)
                    chemin.append(y)
                else:
                    chemin.pop()
            else:
                examinés.add(y)
                chemin.append(y)
        else:
            chemin.pop()

        if chemin:
            x = chemin[-1]
        else:
            break

    return chemin
```