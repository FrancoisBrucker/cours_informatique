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

Chemins de longueur minimum entre deux sommets pour un graphe orienté.

<!-- fin résumé -->

Pour ce cours, nous n'allons considérer **que des graphes orientés** car les notions et théorèmes présentés s'y prêtent mieux. Cela n'entraîne pas une grande perte de généralité : un graphe non orienté (valué) pouvant être considéré comme  un graphe orienté avec 2 arcs opposés (de même valuation).

Commençons par définir le problème :

{% note "**Définition**" %}
Soit $G = (V, E)$ un graphe orienté et $a, b$ deux sommets. Un **chemin de longueur minimum entre $a$ et $b$** est un chemin $v_0 \dots v_{k-1}$ tel que :

* $a = v_0$ et $b=v_{k-1}$
* il n'existe pas de chemin entre $a$ et $b$ de longueur strictement plus petite que $k$.
{% endnote %}

Que l'on généralise souvent aux **graphes valués** :

{% note "**Définition**" %}
Un **graphe orienté valué** est un couple $(G, f)$ où :

* $G=(V, E)$ est un graphe orienté
* $f: E \rightarrow \mathbb{R}$

Le **poids** d'une liste d'arc/arêtes $L$, noté $f(L)$ est la somme des valuations de ses arcs/arêtes et le poids d'un pseudo chemin $=cv_0\dots v_{k-1}$, noté $f(c)$, est la somme $\sum_{0\leq i < k-1}f(v_iv_{i+1})$ (le poids de la liste des arc/arêtes constituant le pseudo-chemin).
{% endnote %}
{% note "**Définition**" %}
Soit $(G, f)$ un graphe valué et $a, b$ deux sommets de $G$. Un **chemin de longueur minimum entre $a$ et $b$** est un chemin $c=v_0 \dots v_{k-1}$ tel que :

* $a = v_0$ et $b=v_{k-1}$
* il n'existe pas de chemin $w_0\dots w_{k'-1}$ de poids plus petit que celui de $c$.
{% endnote %}

Il est clair qu'un chemin de longueur minimum d'un graphe est un chemin de poids minimum où toutes les valuations sont égales à 1.

Attention cependant :

{% note "**Proposition :**" %}
Il peut exister **plusieurs chemins** de poids minimum entre $a$ et $b$ dans un graphe orienté valué $(G,f)$.
{% endnote %}
{% details "preuve" %}
Le graphe orienté $G = (\\{a, b, c, d\\}, \\{ab, bc, ad, dc\\})$ admet deux chemins de longueur minimum entre $a$ et $c$.
{% enddetails %}

Le problème du chemin de poids minimum fait partie de ces problèmes où l'on cherche à minimiser une fonction mais où ce qui nous intéresse c'est l'élément qui réalise le minimum. Ce genre de problème admet souvent un minimum (unique) réalisable par plusieurs éléments.

## Graphe à valuation positive

Commençons par restreindre le problème au cas intuitif où **la valuation $f$ des arcs correspond à un coût**. Pensez par exemple à google maps où les arcs sont des tronçons de route. Les valuations peuvent alors être la distance du tronçon, les péages ou encore le temps min (en respectant les limitations de vitesse) pour le parcourir.

Dans ce cas là, trouver un chemin de poids minimum ou un chemin élémentaire de poids minimum sont deux problème équivalents :
{% note "**Proposition :**" %}
S'il existe un chemin entre $a$ et $b$ dans un graphe orienté $G$, alors :

* **il existe** un pseudo-chemin de longueur minimum
* un pseudo-chemin de longueur minimum est nécessairement **élémentaire**

Plus généralement Si le graphe $G$ est valué par une fonction $f$ positive ($f: E \rightarrow \mathbb{R}^+$) alors :

* **il existe** un chemin de poids minimum
* parmi tous les chemins de poids minimum, ceux de longueur minimum sont **élémentaire**

{% endnote %}
{% details "preuve" %}
Le problème de longueur minimum est un cas particulier de valuation positive (la valeur est toujours égale à 1), on considère donc :

* un graphe orienté valué positivement $(G, f)$
* deux sommets $a$ et $b$ de $G$
* un chemin $c$ entre $a$ et $b$

Un chemin $c'$ réalisant le minimum est donc tel que $0 \leq f(c') \leq f(c)$. Comme l'intervalle $[0, f(c)]$ est un compact, la fonction $f$ va atteindre son minimum pour un élément de l'ensemble des chemins $c'$ entre $a$ et $b$ telles que $0 \leq f(c') \leq f(c)$. On en conclut qu'il existe $c^\star$, un chemin entre $a$ et $b$ dans $G$ de poids minimum.

Si $c^\star$ est un chemin non élémentaire, il existe une boucle. Cette boucle est de longueur strictement positive, la supprimer ne change pas l'origine et la fin du chemin tout en diminuant strictement sa longueur : $c^\star$ ne peut pas être un chemin de poids minimum de longueur minimum.

{% enddetails %}

De là :

{% note %}
On peut se restreindre à rechercher des **chemins élémentaires** de poids minimum sans perte de généralité.
{% endnote %}

Enfin, un propriété fondamentale des chemin de poids minimum pour des graphes valués positivement — et le moteur des algorithmes qui permettent de trouver des chemins de poids minimum — est qu'un chemin de poids minimum est lui-même composé de chemin de poids minimum :

{% note "**Proposition**" %}
Soit $c = v_0 \dots v_{k-1}$ un chemin de longueur minimum entre $v_0$ et $v_k$ pour un graphe orienté valué positivement $G(G, f)$. Alors pour tout $0 \leq i < j < k$ :$c'= v_{i} \dots v_j$ est un chemin de longueur minimum entre $v_i$ et $v_j$

{% endnote %}
{% details "preuve" %}
S'il existait un chemin $c'' = w_0 \dots w_{k'-1}$ entre $v_i$ et $v_j$ de poids strictement plus petit que $c'$, alors le [pseudo-chemin](../chemins-cycles-connexite#pseudo-) (les sommets et arêtes peuvent se répéter) : $c^\star = v_0\dots v_{i-1} w_0 \dots w_{k'-1} v_{j+1} \dots v_{k-1}$ serait de poids strictement plus petit que $c$. Comme de tout pseudo-chemin on peut extraire un chemin élémentaire (en supprimant itérativement les boucles) on peut *raffiner* $c^\star$ en un chemin élémentaire entre $v_0$ et $v_{k-1}$ de poids strictement plus petit que $c$, ce qui est impossible par hypothèse.

{% enddetails %}

### Dijkstra

L'[algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra) permet, à partir d'un graphe orienté valué positivement, de trouver un chemin de longueur minimum entre deux sommets $d$ (départ) et $a$ (arrivée).

Une implémentation en python en utilisant le codage par dictionnaire des graphes et une valuation également codée par un dictionnaire dont les clés sont les arcs et les valeurs la valuation est donnée ci-après :

```python#
def dijkstra(G, f, départ, arrivé):
    prédécesseur = dict()
    coût_entrée = {départ: 0}
    sommets_examinées = {départ}

    pivot = départ
    while pivot != arrivé:
        for x in G[pivot]:
            if x in sommets_examinées:
                continue

            if (x not in coût_entrée) or (
                coût_entrée[x] > coût_entrée[pivot] + f[(pivot, x)]
            ):
                coût_entrée[x] = coût_entrée[pivot] + f[(pivot, x)]
                prédécesseur[x] = pivot

        new = None
        for x in G:
            if (x in sommets_examinées) or (x not in coût_entrée):
                continue

            if (new is None) or (coût_entrée[new] > coût_entrée[x]):
                new = x

        pivot = new
        sommets_examinées.add(pivot)

    chemin = [arrivé]
    x = arrivé
    while x != départ:
        x = prédécesseur[x]
        chemin.append(x)
    chemin.reverse()

    return chemin
```

L'algorithme précédent peut être décomposé en plusieurs parties :

1. initialisation (lignes 2 à 4) : `prédécesseur`{.language-} et `coût_entrée`{.language-} sont des dictionnaires et `sommets_examinées`{.language-} un ensemble
2. boucle principale, qui correspond au `while`{.language-} (lignes 6 à 27). Cette boucle est composée de deux parties :
   1. mise à jour (lignes 8 à 16) : on considère tous les voisins de `pivot`{.language-} qui ne sont pas encore dans `sommets_examinées`{.language-} (test des lignes 9 et 10) et on les met à jour si nécessaire (lignes 12 à 16) : soit on les découvre pour la première fois (`x not in coût_entrée`{.language-}) soit on à mieux (`coût_entrée[x] > coût_entrée[pivot] + f[(pivot, x)]`{.language-})
   2. recherche d'un nouveau `pivot`{.language-} (lignes 18 à 27) : on choisit un sommet non encore examiné de coût d'entrée le plus faible
   3. la boucle principale s'arrête une fois que l'on choisi l'arrivé comme `pivot`{.language-}
3. construction du chemin (lignes 29 à 34) : on remonte de prédécesseur en prédécesseur en partant de `arrivé`{.language-} jusqu'à remonter en `départ`{.language-}.

#### Déroulement de l'algorithme

Avant de voir comment il fonctionne, testez le. Le graphe ci-après représente les différents vols et leurs durées entre différentes villes d'Europe :

![Paris à Rana](chemin_paris_rana.png)

Le codage en python est alors le suivant pour le graphe :

```python
G = {
    "Paris": {"Hambourg", "Amsterdam", "Londres"},
    "Hambourg": {"Stockholm", "Berlin"},
    "Amsterdam": {"Hambourg", "Oslo", "Londres"},
    "Londres": {"Édimbourg"},
    "Stockholm": {"Oslo", "Rana"},
    "Berlin": {"Stockholm", "Amsterdam", "Oslo"},
    "Oslo": {"Rana"},
    "Édimbourg": {"Amsterdam", "Oslo", "Rana"},
    "Rana": set(),
}
```

Et la fonction de valuation positive :

```python
f = {
    ("Paris", "Londres"): 4,
    ("Paris", "Amsterdam"): 3,
    ("Paris", "Hambourg"): 7,
    ("Hambourg", "Stockholm"): 1,
    ("Hambourg", "Berlin"): 1,
    ("Amsterdam", "Londres"): 1,
    ("Amsterdam", "Hambourg"): 2,
    ("Amsterdam", "Oslo"): 8,
    ("Londres", "Édimbourg"): 2,
    ("Stockholm", "Rana"): 5,
    ("Stockholm", "Oslo"): 2,
    ("Berlin", "Stockholm"): 2,
    ("Berlin", "Amsterdam"): 2,
    ("Berlin", "Oslo"): 3,
    ("Oslo", "Rana"): 2,
    ("Édimbourg", "Rana"): 6,
    ("Édimbourg", "Amsterdam"): 3,
    ("Édimbourg", "Oslo"): 7,
}
```

{% exercice %}
Faites un déroulé séquentiel de l'algorithme. Dans quel ordre les sommets sont-ils ajoutés dans `sommets_examinées`{.language-} ?
{% endexercice %}
{% details "solution" %}
Les différentes étapes de l'algorithme sont représentées dans les graphes ci-dessous.

* La figure se lit de gauche à droite et de haut en bas.
* les sommets de `sommets_examinées`{.language-} sont en vert
* en orange les valeurs de `prédécesseur`{.language-} et de `coût_entrée`{.language-}
* en magenta `pivot`{.language-} et les modifications de `prédécesseur`{.language-} et de `coût_entrée`{.language-} s'il y en a

![Dijkstra Paris à Rana](chemin_dijkstra_paris_rana.png)
{% enddetails %}

<div id="preuve-Dijkstra"></div>

#### Preuve

{% note "**Proposition**" %}
Pour un graphe orienté valué positivement $(G, f)$ et deux sommet $a$ et $b$ de $G$, l'algorithme de Dijkstra rend un chemin élémentaire de longueur minimum entre $a$ et $b$ (s'il existe).
{% endnote %}
{% details "solution" %}
On montre par récurrence qu'à chaque étape le chemin de `départ`{.language-} à `pivot`{.language-} constitué en remontant les prédécesseurs de `pivot`{.language-} jusqu'à arriver à `départ`{.language-} est de longueur minimale et de coût `coût_entrée[pivot]`{.language-}.

Au départ `pivot = départ`{.language-}, la propriété est donc vraie. On la suppose vrai jusqu'à la l'itération $i$ (qui correspond au fait que l'on ait $i$ sommets dans  `sommets_examinées`{.language-}). A l'étape $i+1$, on a choisi `pivot`{.language-} qui minimise le coût d'entrée parmi tous les sommets qui ne sont pas encore dans `sommets_examinées`{.language-}.

Comme tous les chemins alternatifs entre `départ`{.language-} et `pivot`{.language-} commencent en `départ`{.language-}, il existe un arc de ce chemin dont le départ  (disons $u$) est dans `sommets_examinées`{.language-} et l'arrivée (disons $v$) n'y est pas. Prenons la première arête $uv$ pour laquelle ça arrive.

Par hypothèse de récurrence, `coût_entree[u]`{.language-} est le coût minimum d'un chemin entre `départ`{.language-} et $u$ et `coût_entree[v]`{.language-} est donc plus grand que `coût_entree[u] + f[uv]`{.language-} (on a examiné ce cas lorsque l'on a fait rentrer $u$ dans `sommets_examinées`{.language-}) et de `coût_entree[pivot]`{.language-} (car c'est le min).

De là, le coût du chemin alternatif est plus grand également que `coût_entree[pivot]`{.language-} **car toutes les valuations sont positives** : notre hypothèse est vérifiée.

{% enddetails %}

#### Complexité

{% note "**Proposition**" %}
La complexité de l'algorithme de Dijkstra est en $\mathcal{O}(\vert E\vert + (\vert V \vert)^2)$
{% endnote %}
{% details "preuve" %}
On ajoute à chaque étape un élément, donc il y a au pire $\vert V \vert$ étapes. A chaque choix on compare les voisins de `pivot`{.language-}. Ces comparaisons sont donc de l'ordre de $\mathcal{O}(\delta(r))$ opérations. Comme `pivot`{.language-} est différent à chaque étapes, toutes ces comparaisons sont de l'ordre de $\mathcal{O}(\sum\delta(r)) = \mathcal{O}(\vert E \vert)$ opérations.

On prend ensuite le minimum parmi les éléments de `sommets_examinées`{.language-}, ce qui prend $\mathcal{O}(\vert V \vert)$ opérations.

La complexité totale est alors en $\mathcal{O}(\vert E\vert + (\vert V \vert)^2)$.

{% enddetails %}

La complexité dépend entièrement de la prise du minimum de `coût_entree`{.language-}. En optimisant cette opération, on peut drastiquement diminuer la complexité de l'algorithme. Par exemple Si l'on utilise un [tas](https://fr.wikipedia.org/wiki/Tas_(informatique)) pour prendre le min, on doit au pire mettre à jour le tas pour chaque arc. Comme il va y a voir au maximum $V$ éléments dans ce tas, la complexité de mise à jour est de $\mathcal{O}(\log_2(\vert V \vert))$, donc le coût total des mises à jour sera de $\mathcal{O}(\vert E \vert \log_2(\vert V \vert))$.

Enfin, comme on prend $\vert V \vert$ fois le minimum du tas, la complexité de trouver tous les `pivot`{.language-} est de $\mathcal{O}(\vert V \vert \log_2(\vert V \vert))$. La complexité de chercher le minimum $\vert V \vert$ fois plus la mise à jour du tas est donc de : $\mathcal{O}((\vert E \vert + \vert V \vert)\log_2(\vert V \vert))$.

La complexité de Dijkstra avec un tas est alors : $\mathcal{O}(\vert E \vert + (\vert E \vert + \vert V \vert)\log_2(\vert V \vert))$ ce qui est égal à $\mathcal{O}((\vert E \vert + \vert V \vert)\log_2(\vert V \vert))$.

Ceci est mieux de prendre le minimum si le graphe ne contient pas énormément d'arcs : $(\vert E \vert + \vert V \vert) \log_2(\vert V \vert) \leq \vert E\vert + (\vert V \vert)^2$, ce qui donne asymptotiquement $\vert E \vert \leq \frac{\vert V \vert^2}{\log_2(\vert V \vert)}$.

La [page wikipédia](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra#Complexit%C3%A9_de_l'algorithme) précise qu'en utilisant un tas amélioré, dit tas de Fibonacci, on arrive même à faire descendre la complexité à $\mathcal{O}(\vert E \vert + \vert V \vert\log_2(\vert V \vert))$, ce qui est du coup tout le temps mieux que la prise de minimum naïve.

#### Arborescence

On peut continuer l'algorithme de Dijkstra après que  ait été rentré dans `sommets_examinées`{.language-}, jusqu'à ce que l'on ait plus que des éléments de coût infini à faire rentrer dans `sommets_examinées`{.language-} ou que `sommets_examinées`{.language-} soit égal à $V$.

{% exercice %}
Montrez que pour tous les sommets $x$ qui ne peuvent pas entrer dans `sommets_examinées`{.language-}, il n'existe pas de chemin entre `départ`{.language-} et $x$ dans $G$
{% endexercice %}
{% details "solution" %}
A chaque fois que l'on ajoute un élément dans `sommets_examinées`{.language-} on vérifie tous ses voisins pour mettre à jour le coût d'entrée dans la structure. On procède comme le parcours en largeur et on a montré qu'il trouvait la composante connexe de sa racine.
{% enddetails %}

<div id="preuve-Dijkstra-arborescence"></div>

{% exercice %}
Montrez que si l'on peut continuer l'algorithme de Dijkstra jusqu'à ce que $V'$ soit égal à $V$ on obtient un graphe $G' = (V, E')$ tel que :

* $\vert E' \vert = \vert V \vert -1$
* il existe un unique chemin entre $d$ et tout autre sommet
* le chemin entre $d$ et $x$ dans $G'$ est de poids minimum dans $G$
{% endexercice %}
{% details "solution" %}
Cette preuve dérive directement de la preuve de l'algorithme de Dijkstra que l'on a fait précédemment.
{% enddetails %}

#### Fausses bonnes idées

**Attention !** si le graphe possède des valuations positives et négatives, l'algorithme de Dijkstra trouvera un chemin s'il existe, mais il ne garantit pas de trouver un chemin de longueur minimum.

L'exemple ci-après le montre :

![chemin poids négatif](chemin_poids_negatif.png)

Une autre fausse bonne idée serait de penser que renverser les inégalités dans l'algorithme (de rentrer dans la structure à chaque fois l'élément de plus grand coût), permet de trouver un chemin le plus long. Cette approche ne fonctionne évidemment pas, prenez par exemple le graphe suivant :

![Dijkstra pas hamilton](chemin_pas_hamilton.png)

Le chemin de longueur maximum $132$ ne sera jamais trouvé si les sommets sont rentrés dans l'ordre 1, 2, 3.

### $A^\star$

Un algorithme beaucoup utilisé lorsque le graphe peut changer ou s'il est très grand, voir inconnu (un terrain de jeu) est l'algorithme $A^*$.

Son principe est identique à celui de Dijkstra, mais plutôt que de prendre à chaque fois l'élément de coût minimum, on choisit un élément dont le `cout_entree` + une distance heuristique sur sa distance à l'arrivée est minimum.

Si l'heuristique est valide, l'algorithme va considérer moins de sommets que Dijkstra.

On l'utilise aussi souvent pour avancer directement à cet élément dans les algorithme de pathfinding par exemple.

{% exercice %}
Proposez une implémentation de l'algorithme $A^*$ pour le parcours dans une salle d'un petit robot (un étudiant lambda un jeudi matin par exemple).
{% endexercice %}
{% details "solution" %}

* On peut prendre comme graphe la grille 2D carré de pas 1m par exemple
* s'il y a des murs on ne mets pas d'arêtes
* l'heuristique sera la distance L1 entre la position et l'arrivée.

On peut même se déplacer à chaque itération et se rapprocher normalement du but petit à petit.
{% enddetails %}

On peut aussi montrer que si l'algorithme $A^*$ a une heuristique qui ne surestime pas la distance finale, il va bien trouver un chemin de poids minimum.

{% exercice %}
Donner un exemple qui montre que si l'algorithme $A^*$ a une heuristique qui surestime le coût du chemin réel il se peut qu'il ne rende pas le bon chemin.
{% endexercice %}
{% details "solution" %}
Pour montrer qu'il peut se tromper, on donne une estimation de coût 0 à un chemin qui n'est pas de longueur minimale et $+\infty$ à sous les autres.
{% enddetails %}

## Graphe à valuation quelconque

<https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford>

## pseudo-chemin de poids minimum

La définition que l'on s'est donné de chemin de poids minimum est intuitive : on cherche à aller d'un sommet $a$ à un sommet $b$ de la façon la plus rapide possible (pensez à un google maps par exemple). Mais cette notion est plus fine que l'on pourrait le croire lorsque l'on permet aux valuation d'être négative. 


{% info %}
Notez qu'un pseudo-chemin $c={(v\_{i})}\_{i \geq 0}$ de longueur infini pour un graphe fini est forcément de poids infini. Il n'y a en effet qu'un nombre fini d'arêtes donc un nombre fini de valuations : la suite $f(v_iv_{i+1})$ ne peut pas tendre vers 0 et donc la série $\sum_{i\geq 0}f(v_iv_{i+1})$ est grossièrement divergente.
{% endinfo %}

Les notions de pseudo-chemin de poids minimum et de chemin élémentaires de poids minimum sont très proches, voir équivalentes dans la majorité des cas. Nous allons expliciter tout cela en commençant par le cas simple où la valuation est positive

### Valuation positive

Les notions de pseudo-chemin de poids minimum et de chemin élémentaires de poids minimum sont très proches, comme le montre la proposition suivante :


### Valuation quelconque

Ici encore — mais seulement si le pseudo-chemin de longueur minimum existe — pseudo-chemin de poids minimum et de chemin élémentaires de poids minimum sont très proches :

{% note "**Proposition :**" %}
**S'il existe** un pseudo-chemin $c$ de poids minimum entre $a$ et $b$ pour un graphe orienté valué $(G, f)$, alors
 un pseudo-chemin de poids minimum de longueur minimum entre $a$ et $b$ est **élémentaire**.
{% endnote %}
{% details "preuve" %}
Soit $c =v_0\dots v_{k-1}$ un pseudo-chemin de poids minimum entre $a$ et $b$, s'il n'est pas élémentaire il existe $i < j$ tel que $v_i = v_j$ et dans ce cas là $f(v_i \dots v_j) = 0$. En effet :

* si $f(v_i \dots v_j) > 0$ il suffirait de le supprimer pour diminuer strictement le poids de $c$ ce qui est impossible
* si $f(v_i \dots v_j) < 0$ le chemin $c' = v_0 \dots v_j v_{i+1} \dots v_{k-1}$ serait de poids égal à $f(c) + f(v_i\dots v_j) < f(c)$ ce qui est également impossible.

On peut donc supprimer le chemin $v_i \dots v_{j-1}$ de $c$ sans changer son poids : on peut itérativement supprimer les circuit de $c$ sans changer son poids jusqu'à arriver à un chemin élémentaire de même poids.

{% enddetails %}

Attention cependant, on ne peut pas forcément extraire un chemin élémentaire de poids minimum à partir d'un pseudo-chemin de poids minimum



Mais surtout la notion même de chemin de poids minimum peut cesser d'exister.

{% note "**Définition :**" %}
Soit $(G, f)$ un graphe orienté valué. Un **circuit absorbant** est un circuit $c$ de poids strictement négatif.
{% endnote %}

Pour deux sommet d'un circuit absorbant, il n'existe pas de pseudo-chemin de poids minimum ! Il suffit en effet d'effectuer autant de fois que l'on veut le circuit pour diminuer d'autant qu'on veut le poids d'un chemin.

![circuit absorbant](circuit-absorbant.png)

Dans le graphe ci-dessus le poids du circuit $abca$ est de -3. De là :

* le pseudo-chemin de $a$ à $c$ : $abc$ vaut $-2$
* le pseudo-chemin de $a$ à $c$ : $abcabc$ vaut $-2 - 3 = -5$
* le pseudo-chemin de $a$ à $c$ : $abcabcabc$ vaut $-5 - 3 = -8$
* ...

Il n'existe pas de plus cours pseudo-chemin entre $a$ et $c$ car en joutant autant de fois que nécessaire le circuit absorbant on peut rendre le poids du pseudo-chemin aussi petit que l'on veut. On peut donc déjà donner la proposition suivante, qui donne une condition nécessaire pour pour qu'il existe un pseudo-chemin de poids minimum entre deux sommets :

{% note "**Proposition**"%}
Soit $(G, f)$ un graphe orienté valué ; $a$ et $b$ deux sommets de $G$.

S'**il existe** un pseudo-chemin $c=v_0\dots v_{k-1}$ entre $a$ et $b$ tel que :

* il existe $i < j$ tel que $v_i = v_j$
* qui est un **circuit absorbant** $f(v_i\dots v_j) < 0$

**Alors il n'existe pas** de pseudo-chemin de poids minimum entre $a$ et $b$.
{% endnote %}
{% details "preuve" %}
Le chemin :

<p>
\[
c_l = v_0 \dots v_j \underbracket{\underbracket{v_{i+1} \dots v_j} \dots \underbracket{v_{i+1} \dots v_j}}_{\mbox{répété $l$ fois}}v_{j+1} \dots v_{k-1}
\]
</p>
Est tel que :

<p>
\[
\lim_{l \rightarrow +\infty}f(c_l) = -\infty
\]
</p>

{% enddetails %}

La proposition précédente nous indique qu'il suffit d'atteindre un circuit absorbant depuis $a$ et pouvoir en repartir pour atteindre $b$ pour qu'il n'existe pas de pseudo-chemin de poids minimum. C'est même une équivalence :

{% note "**Proposition**"%}
Soit $(G, f)$ un graphe orienté valué **ne contenant pas** de circuit absorbant.

Quelques soient les sommets $a$ $b$ de $G$ tels qu'il existe un chemin entre $a$ et $b$ il existe un **chemin élémentaire** $c^\star$ entre $a$ et $b$ tel que pour tout pseudo-chemin $c$ entre $a$ et $b$ :

* la longueur de $c^\star$ est plus petite ou égale à la longueur de $c$
* le poids de $c^\star$ est plus petit ou égal au poids de $c$

{% endnote %}
{% details "preuve" %}
Soit $c = v_0\dots v_{k-1}$ un chemin entre $a$ et $b$. S'il existe $i < j$ tel que $v_i = v_j$ alors : $f(v_i \dots v_j) \geq 0$ puisqu'il n'existe pas de circuit absorbant par hypothèse et donc le chemin $c' = v_0 \dots v_i v_{j+1} \dots v_{k-1}$ est de poids inférieur. Un pseudo-chemin avec boucle est donc toujours de poids supérieur à un pseudo-chemin sans boucle (c'est à dire un chemin élémentaire).

Comme il existe un chemin, donc un chemin élémentaire entre $a$ et $b$, l'ensemble des chemins élémentaires $\mathcal{C}$ entre $a$ et $b$ est non vide. Comme il n'y en a qu'un nombre fini, on peut prendre $c^\star \in \mathcal{C}$ tel que $f(c^\star) = \min \\{ f(c) \mid c \in \mathcal{C}\\}$. D'près ce qui précède $c^\star$ est aussi de poids minimum parmi tous les pseudo-chemins.
{% enddetails %}

Le circuit absorbant n'a pas besoin d'être *à côté* ni de valuation très négative pour poser soucis :

![circuit absorbant](chemin_absorbant.png)

Pour un graphe orienté sans circuits absorbant, la notion de pseudo-chemin de poids minimum et de chemin élémentaire de poids minimum coïncident donc ! On peut donc donner le théorème d'existence suivant :

{% note "**Théorème**"%}
Soit $(G, f)$ un graphe orienté valué ; $a$ et $b$ deux sommets tel qu'il existe un chemin entre $a$ et $b$ dans $G$.

**Il existe** un pseudo-chemin de poids minimum entre $a$ et $b$ si et seulement si **il n'existe pas** de circuit absorbant $c=v_0\dots v_{k-1}$ tel que :

* il existe un chemin entre $a$ et un $v_i$
* il existe un chemin entre un $v_j$ et $b$

De plus, s'il existe un pseudo-chemin $c$ de poids minimum entre $a$ et $b$, on peut en extraire un chemin élémentaire $c^\star$ entre $a$ et $b$ tel qeu $f(c^\star) = f(c)$.

{% endnote %}
{% details "preuve" %}

{% enddetails %}


La notion de circuit absorbant est consubstantielle à la notion de chemin de poids minimum :

{% note "**Proposition :**"%}
Soit $(G, f)$ un graphe orienté valué ; $a$ et $b$ deux sommets de $G$ tel qu'il existe un chemin entre $a$ et $b$.
{% endnote %}

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


## Tous les chemins

Pour régler ce problème, on utilise l'algorithme de [Floyd-Warshall](https://fr.wikipedia.org/wiki/Algorithme_de_Floyd-Warshall) qui trouve, en $\mathcal{O}(\vert V \vert ^3)$ :

* les circuits absorbant s'il y en a
* tous les chemins de longueur minimum allant de $x$ à $y$ pour tous les sommets $x$ et $y$.

{% note %}
Si les poids sont positifs, il vaut mieux utiliser Dijkstra pour trouver 1 chemin entre $x$ et $y$ ou tous les chemins de $x$ à tous les autres sommets, mais si l'on cherche  tous les chemins, il vaut mieux utiliser Floyd-Warshall.
{% endnote %}
