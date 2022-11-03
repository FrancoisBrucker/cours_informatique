---
layout: layout/post.njk

title: Chemin de poids minimum
authors: 
    - François Brucker

eleventyNavigation:
  key: "Chemin de poids minimum"
  parent: "Graphes"
---

<!-- début résumé -->

Chemins de longueur minimum entre deux sommets.

<!-- fin résumé -->

{% note "**Définition :**" %}
Soit $G = (V, E)$ un graphe (orienté ou non) et $a, b$ deux sommets. Un **chemin de longueur minimum entre $a$ et $b$** est un chemin $v_0 \dots v_{k-1}$ tel que :

* $a = v_0$ et $b=v_{k-1}$
* il n'existe pas de chemin entre $a$ et $b$ de longueur strictement plus petite que $k$.
{% endnote %}

Souvent, on généralise cette définition aux graphes **valués**

{% note "**Définition :**" %}
Un **graphe valué** est un couple $(G, f)$ où :

* $G=(V, E)$ est un graphe (orienté ou non)
* $f: E \rightarrow \mathbb{R}$

Le **poids** d'un ensemble d'arête est la somme de ses valuations et le poids d'un pseudo chemin $v_0\dots v_{k-1}$ est la somme $\sum_{0\leq i < k-1}f(v_iv_{i+1})
{% endnote %}
{% note "**Définition :**" %}
Soit $(G, f)$ un graphe valué et $a, b$ deux sommets de $G$. Un **pseudo-chemin de longueur minimum entre $a$ et $b$** est un chemin $c=v_0 \dots v_{k-1}$ tel que :

* $a = v_0$ et $b=v_{k-1}$
* il n'existe pas de pseudo-chemin $w_0\dots w_{k'-1}$ de poids plus petit que celui de $c$.
{% endnote %}

Il est clair qu'un chemin de longueur minimum d'un graphe est un chemin de poids minimum où toutes les valuations sont égales à 1.

Pour la suite de ce cours, nous n'allons considérer **que des graphes orientés** car les notions et théorèmes présentés s'y prêtent mieux. Cela n'entraîne pas une grande perte de généralité : un graphe non orienté (valué) pouvant être considéré comme  un graphe orienté avec 2 arcs opposés (de même valuation).

## Existence

Notez que s'il existe un chemin entre $a$ et $b$ dans $G$, alors :

* il existe un chemin de longueur minimum
* un chemin de longueur minimum est nécessairement élémentaire

Cependant :

{% exercice %}
Montrer qu'il peut exister plusieurs chemin de longueur minimum entre $a$ et $b$
{% endexercice %}
{% details "solution" %}
Le cycle : $G = ({a, b, c, d}, {ab, bc, cd, da})$ admet deux chemin de longueurs minimum entre $a$ et $c$.
{% enddetails %}
Notez que si la valuation du graphe est positive ($f: E \rightarrow \mathbb{R}^+$) et qu'il existe un pseudo-chemin entre $a et $b$ alors :

* il existe un chemin de poids minimum entre $a$ b$b.
* un chemin de longueur minimum est nécessairement élémentaire

Mais cependant :
{% exercice %}
Montrer qu'il peut ne pas exister de pseudo-chemin de longueur minimum entre $a$ et $b$ même s'il existe un chemin entre $a$ et $b$.
{% endexercice %}
{% details "solution" %}
Le cycle orienté : $G = ({a, b, c, d}, {ab, bc, cd, da})$ avec comme valuation :

* $f(ab) = f(bc) = f(cd) = 1$
* $f(da) = -4$

N'admet aucun chemin de poids minimum. Il suffit en effet de parcourir le cycle $abcda$ de poids $-1$ autant de fois que nécessaire pour obtenir un poids aussi petit que l'on veut.

{% enddetails %}

> TBD : chemin min composé de sous-chemin eux-même min (prog dynamique)
> TBD : existe <=> circuit absorbant

## Dijkstra

L'[algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra) permet, à partir d'un graphe orienté valué, de trouver un chemin de longueur minimum entre deux sommets $d$ (départ) et $a$ (arrivée).

Il ressemble beaucoup à l'[algorithme de Prim]({{ "cours/graphes/arbres" | url }}#algo-prim) que l'on a vu précédemment, la seule différence est l'évaluation du coût d'entrée :

* dans l'algorithme de Prim il est égal à la valuation de l'arête rx
* dans l'algorithme de Diskstra il vaut l'addition de cout_entree(r) plus la valuation de l'arête rx.

Cette différence s'explique parce que le poids d'un arbre est la somme des valuations des arêtes qui le constitue alors que pour un chemin, avant d'aller en x, il faut déjà aller en r (dont le coût est cout_entree(x) ) puis de r à x (dont le coût est f(rx)).

{% attention %}
La valuation d'une arête est **forcément** positive ou nulle.
{% endattention %}

### pseudo-code

```text
Entrée :
    * un graphe orienté G = (V, E)
    * une valuation f qui associe un réel positif à toute arête de G
    * deux sommets d et a de V
Initialisation :
    * cout_entree(x) = +∞ pour tout sommet x
    * predecesseur(x) = x pour tout sommet x
    * V' = {}, E' = {}
Algorithme :
    * cout_entree(d) = 0
    * ajoute d à V' 
    * r = d   
    * tant que a n'est pas dans V':
        * pour tous les voisins sortant x de r qui ne sont pas dans V':
            * si cout_entree(x) >= cout_entree(r) + f(rx):
                cout_entree(x) = cout_entree(r) + f(rx)
                predecesseur(x) = r
        * soit x le sommet de V qui n'est pas dans V' minimisant cout_entree(x)
        * r = x
        * ajoute r à V' et (predecesseur(r), r) à E'
    * chemin = [a]
    * x = a
    * tant que x est différent de d:
        * x = predecesseur(x)
        * ajoute x au début de chemin        
Retour :
    chemin
```

### test

![Paris à Rana](chemin_paris_rana.png)

{% exercice %}
Allez de Paris à Rana en moins de temps possible en utilisant l'algorithme de Dijkstra sur le graphe ci-après, qui représente les différents vols et leurs durées entre différentes villes d'Europe.
{% endexercice %}
{% details "solution" %}

Les différentes étapes de l'algorithme sont représentées dans les graphes ci-dessous.

* La figure se lit de gauche à droite et de haut en bas.
* $V'$ est en vert
* en magenta $r$ et les modification des prédécesseur et du cout d'entrée s'il y en a
* en orange le prédécesseur et le cout d'entrée.

![Dijkstra Paris à Rana](chemin_dijkstra_paris_rana.png)

{% enddetails %}


### preuve { #preuve-dijkstra }

{% exercice %}
En utilisant la preuve de l'algorithme de Prim, montrez que l'algorithme de Dijkstra rend un chemin de longueur minimum entre $d$ et $a$
{% endexercice %}
{% details "solution" %}
On montre par récurrence que le chemin de x à r en remontant les prédécesseurs de r jusqu'à arriver à d est de longueur minimale et de coût cout_entree(r).

Au départ `r = d`, la propriété est donc vraie. On la suppose vrai jusqu'à l'étape $i$. A l'étape $i+1$, on a choisi `r` qui minimise le coût d'entrée parmi tous les éléments de `V` qui ne sont pas encore dans `V'`. Comme tous les chemins alternatifs entre `d` et `r` commencent en `d`, il existe une arête de ce chemin dont le départ  (disons $u$) est dans `V'` et l'arrivée (disons $v$) n'y est pas. Prenons la première arête $uv$ pour laquelle ça arrive.

Par hypothèse de récurrence, `cout_entree(u)` est le cout minimum d'un chemin entre `d` et $u$ et `cout_entree(v)` est donc plus grand que `cout_entree(u) + f(uv)` (on a examiné ce cas lorsque l'on a fait rentrer $u$ dans `V'`) et de `cout_entree(r)` (car c'est le min).

De là, le coût du chemin alternatif est plus grand également que `cout_entree(r)` **car toutes les valuations sont positives** : notre hypothèse est vérifiée.

{% enddetails %}

### complexité

{% exercice %}
Quelle est la complexité de l'algorithme de Disjkstra ?
{% endexercice %}
{% details "solution" %}
On ajoute à chaque étape un élément, donc il y a au pire $\vert V \vert$ étapes. A chaque choix on compare les voisins de `r`. Ces comparaisons sont donc de l'ordre de $\mathcal{O}(\delta(r))$ opérations. Comme `r` est différent à chaque étapes, toutes ces comparaisons sont de l'ordre de $\mathcal{O}(\sum\delta(r)) = \mathcal{O}(\vert E \vert)$ opérations.

On prend ensuite le minimum parmi les éléments de `V'`, ce qui prend $\mathcal{O}(\vert V \vert)$ opérations.

La complexité totale est alors en $\mathcal{O}(\vert E\vert + (\vert V \vert)^2)$.

On voit qu'elle dépend entièrement de la prise du minimum de `cout_entree`. En optimisant cette opération, on peut drastiquement diminuer la complexité de l'algorithme

Si l'on utilise un tas pour prendre le min, on doit au pire mettre à jour le tas pour chaque arête. Comme il va y a voir au maximum `V` éléments dans ce tas, la complexité de mise à jour est de $\mathcal{O}(\log_2(\vert V \vert))$, donc le coût total des mises à jour sera de $\mathcal{O}(\vert E \vert \log_2(\vert V \vert))$.

Enfin, comme on prend $\vert V \vert$ fois le minimum du tas, la complexité de trouver tous les `r` est de $\mathcal{O}(\vert V \vert \log_2(\vert V \vert))$. La complexité de chercher le minimum $\vert V \vert$ fois plus la mise à jour du tas est donc de : $\mathcal{O}((\vert E \vert + \vert V \vert)\log_2(\vert V \vert))$.

La complexité de Dijkstra avec un tas est alors : $\mathcal{O}(\vert E \vert + (\vert E \vert + \vert V \vert)\log_2(\vert V \vert))$ ce qui est égal à $\mathcal{O}((\vert E \vert + \vert V \vert)\log_2(\vert V \vert))$.

Ceci est mieux de prendre le minimum si le graphe ne contient pas énormément d'arêtes : $(\vert E \vert + \vert V \vert) \log_2(\vert V \vert) \leq \vert E\vert + (\vert V \vert)^2$, ce qui donne asymptotiquement $\vert E \vert \leq \frac{\vert V \vert^2}{\log_2(\vert V \vert)}$.

La [page wikipédia](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra#Complexit%C3%A9_de_l'algorithme) précise qu'en utilisant un tas amélioré, dit tas de fibonnaci, on arrive même à faire descendre la complexité à $\mathcal{O}(\vert E \vert + \vert V \vert\log_2(\vert V \vert))$, ce qui est du coup tout le temps mieux que la prise de minimum naïve.

{% enddetails %}


## arborescence

On peut continuer l'algorithme de Diskstra après que $a$ ait été rentré dans $V'$, jusqu'à ce que l'on ait plus que des éléments de coût infini à faire rentrer dans $V'$ ou que $V'$ soit égal à $V$.

{% exercice %}
Montrez que pour tous les sommets $x$ qui ne peuvent pas entrer dans $V'$, il n'existe pas de chemin entre $d$ et $x$ dans $G$
{% endexercice %}
{% details "solution" %}
A chaque fois que l'on ajoute un élément dans `V'` on vérifie tous ses voisins pour mettre à jour le coût d'entrée dans la structure. On procède comme le parcours en largeur et on a montré qu'il trouvait la composante connexe de sa racine.
{% enddetails %}

### preuve { #preuve-dijkstra-arborescence }

{% exercice %}
Montrez que si l'on peut continuer l'algorithme de Dijkstra jusqu'à ce que $V'$ soit égal à $V$ on obtient un graphe $G' = (V, E')$ tel que :

* $\vert E' \vert = \vert V \vert -1$
* il existe un unique chemin entre $d$ et tout autre sommet
* le chemin entre $d$ et $x$ dans $G'$ est de poids minimum dans $G$
{% endexercice %}
{% details "solution" %}
Cette preuve dérive directement de la preuve de l'algorithme de Dijkstra que l'on a fait précédemment.
{% enddetails %}
