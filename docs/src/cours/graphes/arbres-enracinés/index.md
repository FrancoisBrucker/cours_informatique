---
layout: layout/post.njk

title: Arbres enracinés

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD à refaire mieux.

## arbre enraciné

> TBD mettre dans une section à part ?
> TBD calcul de hauteur récursif
> TBD arbres régulier.
> TBD tracé dendrogramme (et voir Knuth <https://llimllib.github.io/pymag-trees/>)

En informatique on utilise souvent la structure d'arbre en l'**enracinant**, c'est-à-dire qu'on choisi un sommet qui sera la racine et tous les autres sommets vont être dépendants de lui. Ceci est possible de part une importante propriété des arbres : **l'unicité des chemins**

### ordonnancement des sommets { #ordo-sommets }

L'unicité des chemins permet d'ordonner les sommets par rapport à leur chemin par rapport à la racine. On a coutume de les faire _"tomber"_ depuis la racine. On peut en effet les ranger par rapport à **leur chemin** par rapport à celle ci :

![arbre_plante](./arbre_plante.png)

Vocabulaire :

- $y$ est un **ancêtre** de $x$ : si $y$ est sur le chemin entre la racine et $x$
- $x$ est un **descendant** de $y$ : si $y$ est sur le chemin entre la racine et $x$
- $x$ est une **feuille** s'il n'a pas de descendant
- $x$ est un **nœud intérieur** s'il n'est pas une feuille
- $x$ est un **enfant** de $y$ : si $y$ est le sommet juste avant $x$ dans le chemin de la racine à $x$
- $y$ est un **parent** de $x$ : si $y$ est le sommet juste avant $x$ dans le chemin de la racine à $x$
- la **hauteur** de $x$ est la longueur du chemin entre la racine et $x$.
- la **hauteur** de l'arbre est la longueur du plus long chemin entre la racine et un autre sommet.

{% exercice %}

Donnez un exemple de chacun des termes pour le graphe ci-avant.

{% endexercice %}
{% details "solution" %}

- $a$ est un **ancêtre** de $n$
- $g$ est un **descendant** de $d$
- $k$ est une **feuille**
- $c$ est un **nœud intérieur**
- $b$ est un **enfant** de $a$
- $h$ est un **parent** de $m$
- la **hauteur** de $i$ est 2
- la **hauteur** de l'arbre est 4

{% enddetails %}

Cet ordonnancement est [très utilisé en biologie](https://fr.wikipedia.org/wiki/Arbre_phylog%C3%A9n%C3%A9tique) par exemple car il permet de rendre compte de l'évolution des espèces. En analyse des données on utilise ce paradigme pour classer les données (qui sont les feuilles) selon ce qu'elles ont en commun (les leurs ancêtres).

## arbre binaire planté { #arbre-binaire }

En informatique, c'est souvent les arbres binaires planté que l'on utilise :

Un arbre planté est binaire si tout noeud intérieur a **au plus 2 enfants**. On aura parfois aussi besoin qu'il soit **complet**, c'est-à-dire que les noeuds intérieurs qui n'ont pas 2 enfants sont en bas de l'arbre (à la hauteur de l'arbre -1).

### propriété fondamentale des arbres binaires

{% exercice %}

Montrer que pour un arbre binaire, si tout nœud intérieur a exactement 2 enfants, alors en notant $f$ le nombre de feuilles de l'arbre, on a : $f$ est égal au nombre de nœuds intérieurs plus 1.

{% endexercice %}
{% details "solution" %}
Si chaque nœud intérieur a 2 enfants $ \sum \delta(x) = 2 + f + (n-f - 1) \cdot 3$. Comme $\vert E \vert = \vert V \vert -1 = n -1$, on assemble ces deux équations pour obtenir $n + 1 = 2f$.
{% enddetails %}

> TBD \* la hauteur de l'arbre est égale à $\log_2(f)$ si les feuilles sont à h ou h-1

Les propriétés ci-dessus montrent que si l'on veut organiser $n$ données, on n'a besoin que d'un arbre de hauteur $\log_2(n)$. Comme le chemin depuis la racine nous permet de retrouver les données, si on associe une question à chaque nœud intérieur, on peut retrouver $n$ éléments en ne posant que $\log_2(n)$ questions. C'est le principe des **arbres de décisions**, si utiles en apprentissage automatique.

> La différence en $\log_2(n)$ et $n$ est très importante ! On par exemple besoin d'uniquement 100 questions pour trier 1267650600228229401496703205376 éléments.
> Un informaticien est prêt à beaucoup, beaucoup de choses pour avoir une structure en $\log_2(n)$.
> {.note}

## parcours

Pour modifier la structure du tas on a dû évoluer dans la structure d'arbre planté. Un autre intérêt (encore un !) des arbres plantés est que tout sommet peut être considéré comme la racine de sous-arbre. On a donc uniquement besoin de créer l'algorithme qui fonctionnera pour la racine et le re-exécuter ensuite sur les descendants.

On utilise ce principe pour parcourir tous les sommets d'un arbre planté efficacement, c'est à dire en ne regardant chaque sommet qu'un nombre constant de fois.

### trois parcours classiques

{% exercice %}

Pour chaque parcours ci-après, donnez le résultat pour l'arbre de la partie [ordonnancement des sommets](#ordo-sommets) en supposant que `Examen de la Racine` signifie : affiche le numéro de la racine à l'écran.

Une fois ceci fait, trouvez un ordre qui lira les sommets dans l'ordre alphabétique à partir de la lettre b (en oubliant la racine).

{% endexercice %}
{% details "solution" %}

- pré-ordre : a-b-h-l-m-n-i-j-k-c-d-e-g-f
- post-ordre : l-n-m-h-j-k-i-b-g-e-f-d-c-a
- en-ordre : l-h-n-m-b-j-i-k-a-c-g-e-d-f

```text
alphabétique(racine)
    examen enfant gauche
    examen enfant droit
    alphabétique(enfant droit)
    alphabétique(enfant gauche)

```

{% enddetails %}

#### pré-ordre

```text
pré-ordre(racine)
Si la racine existe:
    Examen de la racine
    pré-ordre(enfant gauche)
    pré-ordre(enfant droit)
```

#### post-ordre

```text
post-ordre(racine)
Si la racine existe:
    post-ordre(enfant gauche)
    post-ordre(enfant droit)
    Examen de la racine
```

#### en-ordre

```text
en-ordre(racine)
Si la racine existe:
    en-ordre(enfant gauche)
    Examen de la racine
    en-ordre(enfant droit)
```

{% info %}
Les [parcours d'arbres](https://fr.wikipedia.org/wiki/Arbre_syntaxique) sont utilisés en linguistique pour analyser syntaxiquement une phrase. Un exercice classique est de créer un [arbre à partir d'une expression arithmétique](https://diu-uf-bordeaux.github.io/bloc4/td/arbres/expression/) pour la résoudre de façon optimale en nombre d'opérations.
{% endinfo %}
