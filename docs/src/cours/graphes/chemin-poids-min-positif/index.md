---
layout: layout/post.njk

title: Algorithme de Dijkstra
authors: 
    - François Brucker

eleventyNavigation:
  key: "Algorithme de Dijkstra"
  parent: "Graphes"
---

<!-- début résumé -->

Chemins de longueur minimum entre deux sommets pour un graphe orienté pour une valuation positive.

<!-- fin résumé -->

L'[algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra) permet, à partir d'un graphe orienté valué positivement, de trouver un chemin de longueur minimum entre deux sommets $d$ (départ) et $a$ (arrivée).

## Principe

L'algorithme de Dijkstra cherche à créer un arborescence à partir d'un graphe initial $G$. Précisons cela.

{% note "**Définition :**" %}

Soit $G =(V, E)$ un graphe orienté, $f$ une valuation positive des arcs de $G$ et $x$ un sommet du graphe. Une **arborescence** $T_{x} = (V', E')$ est un graphe tel que :

* $x \in V'$
* $V' \subseteq V$ et $E' \subseteq E$
* il existe un chemin $c^T_{xy}$ **unique** entre $x$ et $y$ dans $T_{x}$ por tout sommet $y \in V'$
* pour tout chemin $c^G_{xy}$ entre $x$ et $y$ dans $G$  on a $f(c^G_{xy}) \geq f(c^T_{xy})$

{% endnote %}

Par exemple :

![G et G'](./g_g_prim.png)

La définition d'une arborescence garantit le fait que tout ses chemins sont de poids minimum pour $G$. Remarquez de plus que pour tout graphe orienté $G$, il existe au moins une arborescence pour chacun de ses sommets en considérant $T_{x} = (\\{x\\}, \varnothing)$.

Enfin, la proposition suivant montre que l'on peut faire *grossir* les arborescences :

{% note "**Proposition :**" %}
Soit $G =(V, E)$ un graphe orienté valué par une fonction positive $f$. Et $T_x = (V', E')$ une de ses arborescence.

Si :

$$
W = \\{ uv \mid uv \in E, u \in V', v \in V \backslash V' \\}
$$

N'est pas vide alors il existe un arc $u^\star v^\star \in W$ tel que :

$$f(c^T_{xu}) + f(u^\star v^\star) = \min_{uv \in W}(f(c^T_{xu}) + f(uv))$$

Et
$$
T' = (V' \cup \\{v^\star\\}, E' \cup \\{ u^\star v^\star \\})
$$
est également une arborescence de $G$
{% endnote %}
{% details "preuve" %}

Comme on ne rajoute qu'un arc à $E'$ pour créer $E''$, il ne peut exister 2 chemins différents pour aller de $x$ à un autre sommet $y$ de $G'' =(V'', E'')$.

Supposons qu'il existe un chemin entre $x$ et $y$ dans $G$. Comme $x \in V$, on peut noter $v'$ le premier sommet de ce chemin qui n'est pas dans $V'$. Si $v' \neq y$ on se retrouve dans le cas de la figure ci-dessous :

![preuve Dijkstra](./preuve_dijkstra.png)

Le poids du chemin en pointillé de $x$ à $v'$ est par construction plus grand que le poids du chemin allant de $x$ à $v$ (en trait plein). Comme les poids sont positifs, le chemin en pointillé de $x$ à $v$ est donc de poids supérieur à celui en trait plein.

On conclut la preuve en notant que s'il n'y a qu'un seul chemin entre $x$ et tout élément de $V'$, la propriété est toujours vrai pour $V''$ puisque l'on a fat que rajouter un chemin (unique) entre $x$ et $v'$.

{% enddetails %}

Le principe de l'algorithme de Dijkstra qui cherche un plus court chemin entre deux sommets $x$ et $y$ d'un graphe orienté valué par une fonction positive $f$ est alors :

1. partir de l’arborescence $T_{x} = (\\{x\\}, \varnothing)$
2. tant que $W = \\{ uv \mid uv \in E, u \in V', v \in V \backslash V' \\}$ est non vide faire grossir l’arborescence
3. si le dernier sommet ajouté est $y$, l'algorithme s'arrête et rend le chemin entre $x$ et $y$ dans l'arborescence

L'implémentation naïve de cet algorithme serait cependant d'une complexité importante car on recalculerait trop souvent les mêmes choses.

## <span id="implementation-Dijkstra"></span> Implémentation

L'idée de l'algorithme de Dijkstra est d'implémenter le principe précédent de façon optimale.

### Pseudo-code

On cherche à trouver un plus court chemin entre deux sommets, nommées `départ` et `arrivé`, d'un graphe orienté $G$ valué par une fonction positive $f$.

```python#

Initialisation :
    prédécesseur[départ] = x  # pour retrouver les chemins
    
    coût[départ] = 0  # distances
    coût[u] = +∞ pour tous les autres sommets u
    
    sommets_examinées = {départ}  # les sommets de l'arborescence
    
    pivot = départ  # pivot est le dernier élément ajouté à l'arborescence

Corps de l'algorithme :
    tant que pivot ≠ arrivé :
        # mise à jour des coûts
        pour tous les voisins x de pivot dans G qui ne sont pas dans sommets_examinés :
            si coût[x] > coût[pivot] + f(pivot, x):   
                coût[x] = coût[pivot] + f(pivot, x)
                prédécesseur[x] = pivot
        
        # ajout d'un élément à la structure
        soit u un sommet de G qui n'est pas dans sommets_examinés et 
            qui minimise le coût pour ces éléments
        ajoute u à sommet_examinés

        pivot = u


    # restitution du chemin (pivot = arrivé au départ)
    chemin = []
    x = pivot
    tant que x ≠ départ:
        ajoute x au début de chemin
        x = prédécesseur[x]

Sortie de l'algorithme :
    rendre chemin

```

L'astuce est de voir que si l'on stocke les coûts, on a uniquement besoin de les mettre à jour lorsque l'on ajoute un nouveau sommet dans la structure

### Python

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

        nouveau_pivot = None
        for x in G:
            if (x in sommets_examinées) or (x not in coût_entrée):
                continue

            if (nouveau_pivot is None) or (coût_entrée[nouveau_pivot] > coût_entrée[x]):
                nouveau_pivot = x

        pivot = nouveau_pivot
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

### Déroulement de l'algorithme

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

### <span id="preuve-Dijkstra"></span> Preuve

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

### Complexité

{% note "**Proposition :**" %}
La complexité de l'algorithme de Dijkstra est en $\mathcal{O}(\vert E\vert + (\vert V \vert)^2)$
{% endnote %}
{% details "preuve" %}
On ajoute à chaque étape un élément, donc il y a au pire $\vert V \vert$ étapes. A chaque choix on compare les voisins de `pivot`{.language-}. Ces comparaisons sont donc de l'ordre de $\mathcal{O}(\delta(\mbox{pivot}))$ opérations. Comme `pivot`{.language-} est différent à chaque étape, toutes ces comparaisons sont de l'ordre de $\mathcal{O}(\sum\delta(\mbox{pivot})) = \mathcal{O}(\vert E \vert)$ opérations.

On prend ensuite le minimum parmi les éléments de `sommets_examinées`{.language-}, ce qui prend $\mathcal{O}(\vert V \vert)$ opérations.

La complexité totale est alors en :
<p>
\[
\mathcal{O}(\underbracket{\vert E\vert}_{\mbox{mises à jour du coût d'entrée}} + \underbracket{(\vert V \vert)^2}_{\vert V \vert \mbox{ choix de pivot}})
\]
<\p>

{% enddetails %}
{% note "**Corollaire :**" %}
En déduire que la complexité de l'algorithme de Dijkstra est en $\mathcal{O}((\vert V \vert)^2)$
{% endnote %}
{% details "preuve" %}
Clair puisque $\vert E \vert \leq \vert V \vert)^2$.
{% enddetails %}

On le voit dans la preuve de la proposition, le facteur limitant est la partie en $\mathcal{O}(\vert V \vert^2)$ qui n'est pas linéaire en la taille du graphe (en mémoire un graphe occupe de l'ordre de $\mathcal{O}(\vert E \vert + \vert V \vert)$ cases). Celle ci concerne le choix du nouveau pivot en cherchant un minimum de `coût_entree`{.language-}. En optimisant cette opération, on peut drastiquement diminuer la complexité de l'algorithme.

Une optimisation classique est d'utiliser un [tas](https://fr.wikipedia.org/wiki/Tas_(informatique)) pour trouver le min. On a alors que :

* une complexité de $\mathcal{O}(1)$  pour prendre un minimum
* une complexité de $\mathcal{O}(\log_2(M))$ où $M$ est le nombre d'éléments du tas pour mettre à jour la structure après chaque modification. Comme il va y a voir au maximum $V$ éléments dans ce tas, on peut borner cette complexité par $\mathcal{O}(\log_2(\vert V \vert))$

Enfin :

* il y a de l'ordre $\mathcal{O}(\vert V \vert)$ prise de minimum  : à chaque choix de `pivot`{.language-}
* il y a de l'ordre de $\mathcal{O}(\vert E \vert)$ modifications : à chaque modification de `coût_entree`{.language-}

On a donc une complexité de choix de `pivot`{.language-} qui passe alors de $\mathcal{O}(\vert V \vert^2)$ à $\mathcal{O}(\vert E \vert \log_2(\vert V \vert))$.

* S'il y a **peu d'arcs**, disons $\vert E \vert = \mathcal{O}(\vert V \vert)$, **c'est beaucoup mieux** puisque l'on a alors une complexité de : $\mathcal{O}((\vert V \vert)\log_2(\vert V \vert))$
* S'il y a **beaucoup d'arcs**, disons $\vert E \vert = \mathcal{O}(\vert V \vert^2)$, c'est **un peu moins bon**  puisque l'on a alors une complexité de : $\mathcal{O}((\vert V \vert)^2\log_2(\vert V \vert))$

La complexité de Dijkstra avec un tas est alors : $\mathcal{O}(\vert E \vert + (\vert E \vert + \vert V \vert)\log_2(\vert V \vert))$ ce qui est égal à $\mathcal{O}((\vert E \vert + \vert V \vert)\log_2(\vert V \vert))$ qui est beaucoup mieux que l'implémentation naïve si le graphe est peu dense et un peu moins bonne dans le cas où le graphe est dense

Comme souvent les graphes sont peu dense lorsque l'on cherche un chemin de poids min — pensez à google maps où il y a bien peu de routes par rapport aux nombre d'endroit où l'on peu aller — on utilise souvent cette implémentation.

{% note %}
La [page wikipédia](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra#Complexit%C3%A9_de_l'algorithme) précise qu'en utilisant un tas amélioré, dit tas de Fibonacci, on arrive même à faire descendre la complexité totale à $\mathcal{O}(\vert E \vert + \vert V \vert\log_2(\vert V \vert))$, ce qui est du coup tout le temps mieux que la prise de minimum naïve, mais nécessite une structure bien plus compliquée.
{% endnote %}

## <span id="arborescence"></span> Arborescence

On peut continuer l'algorithme de Dijkstra après que  ait été rentré dans `sommets_examinées`{.language-}, jusqu'à ce que l'on ait plus que des éléments de coût infini à faire rentrer dans `sommets_examinées`{.language-} ou que `sommets_examinées`{.language-} soit égal à $V$.

<span id="preuve-Dijkstra-arborescence"></span>
{% exercice %}
Montrez que pour tous les sommets $x$ qui ne peuvent pas entrer dans `sommets_examinées`{.language-}, il n'existe pas de chemin entre `départ`{.language-} et $x$ dans $G$
{% endexercice %}
{% details "solution" %}
A chaque fois que l'on ajoute un élément dans `sommets_examinées`{.language-} on vérifie tous ses voisins pour mettre à jour le coût d'entrée dans la structure. On procède comme le parcours en largeur et on a montré qu'il trouvait la composante connexe de sa racine.
{% enddetails %}

{% exercice %}
Montrez que si l'on peut continuer l'algorithme de Dijkstra jusqu'à ce que $V'$ soit égal à $V$ on obtient un graphe $G' = (V, E')$ tel que :

* $\vert E' \vert = \vert V \vert -1$
* il existe un unique chemin entre $d$ et tout autre sommet
* le chemin entre $d$ et $x$ dans $G'$ est de poids minimum dans $G$
{% endexercice %}
{% details "solution" %}
Cette preuve dérive directement de la preuve de l'algorithme de Dijkstra que l'on a fait précédemment.
{% enddetails %}

## $A^\star$

Un algorithme beaucoup utilisé lorsque le graphe peut changer ou s'il est très grand, voir inconnu (un terrain de jeu) est [l'algorithme $A^\star$](https://fr.wikipedia.org/wiki/Algorithme_A*), qui est une variante de l'algorithme de Dijkstra qui accélère la procédure de choix en sacrifiant l'optimalité : on obtient alors *rapidement* une solution *acceptable* plutôt qu'obtenir *lentement* une solution optimale.

Son principe est identique à celui de Dijkstra, mais plutôt que de prendre à chaque fois l'élément de coût minimum on choisit un élément dont le coût + une distance heuristique $h$ sur sa distance à l'arrivée est minimum. Son pseudo-code est donc identique à celui de Dijkstra à part l'ajout d'un élément à la structure (lignes 22 à 23) qui devient :

```python#20
        # ajout d'un élément à la structure
        soit u un sommet de G qui n'est pas dans sommets_examinés et 
            qui minimise la somme coût[x] + h[x] pour ces éléments
        ajoute u à sommet_examinés

```

Cette modification est faite pour considérer moins de sommets que Dijkstra (on ne va pas choisir de sommets inutiles) en estimant la coût qu'il reste à parcourir pour aller de $x$ à l'arrivée.

Remarquez que si $h[x] = 0$ pour tout $x$, 

Cette approche est utile dans une grande variété de cas d'application où il est pus important d'aller vite que d'être exacte : comme dans les jeux vidéo par exemple où on utilise cet algorithme dans le [*pathfinding*](https://fr.wikipedia.org/wiki/Recherche_de_chemin) par exemple.


{% exercice %}
Proposez une implémentation de l'algorithme $A^*$ pour le parcours dans une salle d'un petit robot.
{% endexercice %}
{% details "solution" %}

* On peut prendre comme graphe la grille 2D carré de pas 1m par exemple
* s'il y a des murs on ne mets pas d'arêtes
* l'heuristique sera la distance entre la position et l'arrivée.

{% enddetails %}

On peut aussi montrer que si l'algorithme $A^*$ a une heuristique qui ne surestime pas la distance finale, il va bien trouver un chemin de poids minimum.

{% exercice %}
Donner un exemple qui montre que si l'algorithme $A^*$ a une heuristique qui surestime le coût du chemin réel il se peut qu'il ne rende pas le bon chemin.
{% endexercice %}
{% details "solution" %}
Pour montrer qu'il peut se tromper, on donne une estimation de coût 0 à un chemin qui n'est pas de longueur minimale et $+\infty$ à sous les autres.
{% enddetails %}

## Chemine de poids minimum n'est pas équivalent à chemin de poids maximum

Penser que renverser les inégalités dans l'algorithme De Dijkstra (de rentrer dans la structure à chaque fois l'élément de plus grand coût), permet de trouver un chemin le plus long est une faute.

Donnons un exemple. Le graphe suivant avec une valuation de 1 sur tous les arc :

![Dijkstra pas Hamilton](chemin_pas_hamilton.png)

Le chemin de longueur maximum entre $1$ et $3$ est $132$. L'algorithme où l'on renverse toutes les inégalités trouvera ce chemin si les sommets sont examinés dans l'ordre $1$, $3$ puis $2$, **mais** il ne le trouvera pas si les sommets sont rentrés dans `sommets_examinées`{.language-} dans l'ordre 1, 2, 3 (ce qui est possible).

Même s'il existe des cas où l'algorithme de Dijkstra trouvera le chemin le plus long, il en existe d'autres où il ne le trouvera pas...
