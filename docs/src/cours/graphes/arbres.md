---
layout: layout/post.njk
title: Arbres

authors: 
    - François Brucker
---

{% chemin %}
[Graphes]({{ ".." }}) / [{{title}}]({{ "." }})
{% endchemin %}
{% pres-requis %}
* [Chemins, cycles et connexité](../chemins-cycles-connexite)
{% endpres-requis %}

<!-- début résumé -->

Explorer les propriétés et l'intérêt de l'arbre.

<!-- fin résumé -->

## définitions

Un **arbre** est un *graphe* $T = (V, E)$ qui est :

* connexe
* sans cycle

### graphe

{% exercice %}
Redonnez la définition d'un graphe. Combien d'arêtes au maximum peut il-contenir ?
{% endexercice %}
{% details "solution" %}
Voir la [définition du cours](../structure#definition-graphe). Le nombre maximum d'arête est obtenu pour le [graphe complet](../structure#definition-graphe-complet), c'est à dire $\frac{n(n-1){2}}$ arêtes pour $n$ sommets.
{% enddetails %}

### arbre ou pas arbre ?

{% exercice %}

Déduire de la définition lequel des 2 graphes ci-dessous est un arbre.

| :-: | :-: |
|![graphe A](../assets/img/pas_arbre.png)|![graphe B](../assets/img/arbre.png)|
|A|B|

{.no-border}

{% endexercice %}
{% details "solution" %}
C'est bien sûr le graphe B qui est connexe et ne contient pas de cycle. Le graphe A est connexe mais il contient des cycles.

{% enddetails %}

### algorithme de reconnaissance

#### graphe connexe

{% exercice %}

1. Donnez un algorithme permettant de savoir si un graphe $G = (V, E)$ donné est connexe.
2. Quelle structure de graphe utiliseriez-vous pour que cet algorithme ait la plus petite complexité possible ?

**Indice** : On pourra partir d'un sommet $x$ et trouver itérativement tous les sommets que l'on peut atteindre avec lui.

{% endexercice %}
{% details "solution" %}
On utilise le [parcours en largeur des graphes](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur). Comme il faut examiner tous les voisins d'un sommet, on a coutume d'utiliser les listes d'adjacence pour que le nombre d'opérations de l'algorithme soit proportionnel au nombre d'arêtes du graphe ($\mathcal{O}(\vert E \vert)$) : il est donc optimal.

{% enddetails %}


#### graphe sans cycle ?

Là comme ça, ça n'a pas l'air simple de répondre à cette question. On va plutôt ruser et prouver deux propriétés des graphes connexes à la place.

{% exercice %}

* Tout graphe sans cycle contient au maximum $\vert V \vert - 1$ arêtes.
* Tout graphe connexe contient au minimum $\vert V \vert - 1$ arêtes.

{% endexercice %}
{% details "solution" %}
Pour la 1ère preuve, on suppose alors qu'il existe un graphe $G= (V, E)$, tel que $\vert E \vert \geq \vert V \vert$ et qu'il n'y ait pas de cycles.

Commençons par remarquer que si $\vert E \vert \geq \vert V \vert$, alors forcément $\vert V \vert \geq 3$ et s'il n'a pas de cycle alors $\vert V \vert > 3$. De là, on peut choisir $G$ avec le plus petit nombre de sommets possible.

S'il existait dans ce graphe un sommet de degré plus petit ou égal à 1, on pourrait le supprimer du graphe et on aurait un graphe $G' = (V', E')$ avec strictement moins de sommets que $G$, tel que $\vert E' \vert \geq \vert V' \vert$ et qui ne contiendrait pas de cycle (on ne peut pas ajouter de cycle en supprimant une arête ou un sommet à un graphe). Ce qui est impossible par choix de $G$.

Donc tout sommet de $G$ a un degré d'au moins 2 et il existe un cycle ([c'est dans le cours](chemins-cycles-connexite#prop-cycles-graph)) : notre hypothèse était fausse.

Pour la seconde preuve, on la montre par récurrence. La propriété est clairement vraie pour un graphe à 1 ou 2 sommets. On la suppose alors vraie jusqu'à $n$ sommets et on considère un graphe connexe à $n+1$ sommets.

Pour ce graphe on choisi un sommet, $x$, que l'on supprime du graphe. Ce dernier n'est alors plus connexe et possède $p \leq \delta(x)$ composantes connexes qui respectent l'hypothèse de récurrence : $\vert E_i \vert \geq \vert V_i \vert -1$ pour chacune d'elles. En sommant le tout on a alors :

$$\sum \vert E_i \vert \geq \sum (\vert V_i \vert -1)$$

On conclut en remarquant que $\sum \vert E_i \vert = \vert E \vert - \delta(x) \leq \vert E \vert - p$ et $\sum \vert V_i \vert = V - 1$.
{% enddetails %}

#### conditions

En déduire que :

{% exercice %}

Un graphe $G=(V, E)$ est un arbre si et seulement si :

* il est connexe
* $\vert E \vert = \vert V \vert - 1$

{% endexercice %}
{% details "solution" %}
clair avec ce qui précède.
{% enddetails %}

Sur votre lancée prouvez aussi que :

{% exercice %}

Un graphe $G=(V, E)$ est un arbre si et seulement si :

* il est sans cycle
* $\vert E \vert = \vert V \vert - 1$

{% endexercice %}
{% details "solution" %}
Tout pareil, clair avec ce qui précède.
{% enddetails %}

Pour enfoncer le clou et montrer que les arbres sont une structure de connexité minimale vous pouvez aussi :

{% exercice %}

Prouver que :

* Si on ajoute une arête à un arbre (n'importe laquelle) on ajoute un cycle
* Si on supprime une arête à un arbre (n'importe laquelle) on le déconnecte

{% endexercice %}
{% details "solution" %}
Encore une fois, c'est clair (ils sont vraiment trop faciles ces exercices).
{% enddetails %}

#### conclusion

Les conditions précédentes nous permettent de ne pas avoir à chercher si un graphe a un cycle, ce qui rend l'algorithme de reconnaissance plus aisé :

{% exercice %}

Donnez l'algorithme final pour savoir si un graphe est un arbre.

{% endexercice %}
{% details "solution" %}
On utilise le parcours en largeur pour obtenir la composante connexe à partir d'un élément. Si elle contient tous les éléments, le graphe est connexe, et si ce graphe a $\vert V \vert -1$ arêtes, alors c'est un arbre.

{% enddetails %}

## arbre enraciné

En informatique on utilise souvent la structure d'arbre en l'**enracinant**, c'est-à-dire qu'on choisi un sommet qui sera la racine et tous les autres sommets vont être dépendants de lui. Ceci est possible de part une importante propriété des arbres : **l'unicité des chemins**

### chemins et arbres

Soit $T = (V, E)$ un arbre.

{% exercice %}

Montrez que quels que soient deux sommets $x$ et $y$, il n'existe qu'un seul chemin entre $x$ et $y$.

{% endexercice %}
{% details "solution" %}
S'il existait 2 chemins distincts pour aller de $x$ à $y$ on se placerait au premier élément distinct et au premier élément en commun après celui-ci et on aurait un cycle.
{% enddetails %}

### ordonnancement des sommets {#ordo-sommets}

L'unicité des chemins permet d'ordonner les sommets par rapport à leur chemin par rapport à la racine. On a coutume de les faire *"tomber"* depuis la racine. On peut en effet les ranger par rapport à **leur chemin** par rapport à celle ci :

![arbre_plante](../assets/img/arbre_plante.png)

Vocabulaire :

* $y$ est un **ancêtre** de $x$ : si $y$ est sur le chemin entre la racine et $x$
* $x$ est un **descendant** de $y$ : si $y$ est sur le chemin entre la racine et $x$
* $x$ est une **feuille** s'il n'a pas de descendant
* $x$ est un **nœud intérieur** s'il n'est pas une feuille
* $x$ est un **enfant** de $y$ : si $y$ est le sommet juste avant $x$ dans le chemin de la racine à $x$
* $y$ est un **parent** de $x$ : si $y$ est le sommet juste avant $x$ dans le chemin de la racine à $x$
* la **hauteur** de $x$ est la longueur du chemin entre la racine et $x$.
* la **hauteur** de l'arbre est la longueur du plus long chemin entre la racine et un autre sommet.

{% exercice %}

Donnez un exemple de chacun des termes pour le graphe ci-avant.

{% endexercice %}
{% details "solution" %}
* $a$ est un **ancêtre** de $n$
* $g$ est un **descendant** de $d$
* $k$ est une **feuille**
* $c$ est un **nœud intérieur**
* $b$ est un **enfant** de $a$
* $h$ est un **parent** de $m$
* la **hauteur** de $i$ est 2
* la **hauteur** de l'arbre est 4

{% enddetails %}

Cet ordonnancement est [très utilisé en biologie](https://fr.wikipedia.org/wiki/Arbre_phylog%C3%A9n%C3%A9tique) par exemple car il permet de rendre compte de l'évolution des espèces. En analyse des données on utilise ce paradigme pour classer les données (qui sont les feuilles) selon ce qu'elles ont en commun (les leurs ancêtres).

## arbre binaire planté {#arbre-binaire}

En informatique, c'est souvent les arbres binaires planté que l'on utilise :

Un arbre planté est binaire si tout noeud intérieur a **au plus 2 enfants**. On aura parfois aussi besoin qu'il soit **complet**, c'est-à-dire que les noeuds intérieurs qui n'ont pas 2 enfants sont en bas de l'arbre (à la hauteur de l'arbre -1).

### propriété fondamentale des arbres binaires

{% exercice %}

Montrer que pour un arbre binaire, si tout nœud intérieur a exactement 2 enfants, alors en notant $f$ le nombre de feuilles de l'arbre, on a :

* la hauteur de l'arbre est égale à $\log_2(f)$
* $f$ est égal au nombre de nœuds intérieurs plus 1.

{% endexercice %}
{% details "solution" %}
Si chaque nœud intérieur a 2 enfants $ \sum \delta(x) = 2 + f + (n-f - 1) \cdot 3$. Comme $\vert E \vert = \vert V \vert -1 = n -1$, on assemble ces deux équations pour obtenir $n + 1 = 2f$.
{% enddetails %}

Les propriétés ci-dessus montrent que si l'on veut organiser $n$ données, on n'a besoin que d'un arbre de hauteur $\log_2(n)$. Comme le chemin depuis la racine nous permet de retrouver les données, si on associe une question à chaque nœud intérieur, on peut retrouver $n$ éléments en ne posant que $\log_2(n)$ questions. C'est le principe des **arbres de décisions**, si utiles en apprentissage automatique.

> La différence en $\log_2(n)$ et $n$ est très importante ! On par exemple besoin d'uniquement 100 questions pour trier 1267650600228229401496703205376 éléments.
> Un informaticien est prêt à beaucoup, beaucoup de choses pour avoir une structure en $\log_2(n)$.
{.note}

### exemple du tas

Nous allons montrer ici une utilité de l'arbre binaire complet pour résoudre le problème d'une file de priorité.

#### le problème

Une salle d'attente des urgences d'un hôpital contient des patients dont la gravité d'état est donnée par un entier. Des patients peuvent arriver et partir de la salle d'attente et leur état peut s'améliorer (la gravité d'état baisse) ou se détériorer (leur gravité d'état augmente). A chaque fois qu'un médecin est libre, on prend en charge le patient avec l'état de gravité le plus important.  

#### une solution possible (naïve)

On regarde chaque patient et on prend le patient ayant la gravité d'état le plus important.

{% exercice %}

Quel est le coût algorithmique d'utiliser une telle solution ?
{% endexercice %}
{% details "solution" %}
On a simplement besoin de regarder chaque patient lorsqu'il faut en prendre en charge un nouveau. On n'a pas besoin de faire des choses lorsque les patients changent d'état de gravité ou partent et arrivent. Mais à chaque fois c'est $\mathcal{O}(n)$ opérations.
{% enddetails %}

Si l'on suppose que l'état de gravité d'un patient est connu, on peut faire bien mieux.

#### un tas

Un tas est un arbre binaire planté complet dont les sommets sont des entiers. On considère en plus qu'un tas est **plein**, c'est-à-dire que les feuilles de hauteur maximum forment un intervalle à gauche de l'arbre.

![arbre_plante_tas_?](../assets/img/arbre_plante_tas_abc.png)

{% exercice %}

Des trois arbres ci-dessus lequel (il n'y en a qu'un) est binaire, complet et plein ?

{% endexercice %}
{% details "solution" %}
* (a) est binaire mais pas complet
* (b) est binaire complet mais pas plein
* (c) est binaire, complet et plein.
{% enddetails %}

De plus, pour un tas, chaque nœud est de valeur plus grande que chacun de ses descendants direct.

{% exercice %}

* Créez un tas avec les nombres : 42, 12, 1, 3, 6, 5.
* Y a-t-il plusieurs possibilités ?
* que peut-on dire du nœud ayant le plus grand nombre ?

{% endexercice %}
{% details "solution" %}
![tas possibles](../assets/img/tas_2-possibilites.png)

Le plus grand nœud est **toujours** la racine du tas.
{% enddetails %}

#### manipulation d'un tas

{% exercice %}

Donner les algorithmes pour effectuer les opérations suivantes :

1. ajout d'un élément
2. modification d'une valeur
3. suppression de la racine

{% endexercice %}
{% details "solution" %}
1. on l'ajoute à la fin et on le remonte (récursivement) si nécessaire
2. on change la valeur puis on échange récursivement
   * avec son parent si la valeur est plus grande ou
   * avec son enfant de valeur maximum si la valeur est plus petite
3. on prend la dernière feuille, on la supprime et on modifie (avec l'opération 2) la racine avec la valeur de la feuille enlevée.
{% enddetails %}


On peut s'en sortir avec des algorithmes dont le nombre d'opérations est proportionnel à la hauteur du tas.

{% exercice %}

En conclure que l'utilisation du tas est bien meilleure que la solution naïve.

{% endexercice %}
{% details "solution" %}
Toutes les opérations nécessitent un nombre de calculs proportionnel à la hauteur $h$ du tas. Et il y a $n = 2^h$ éléments dans celui-ci. Nos opérations sont donc toutes en $\mathcal{O}(\log_2(n)) = \mathcal{O}(h)$ opérations.
{% enddetails %}

#### pour la bonne bouche

{% exercice %}

* En déduire une façon de trier un tableau de nombres.
* trouver un moyen de représenter un tas par une liste (on pourra parcourir le tas de haut en bas et de droite à gauche).

{% endexercice %}
{% details "solution" %}

On commence par un tas vide et on le remplit petit à petit (cela prend $n$ fois $\mathcal{O}(\log_2(n))$ opérations). Puis on supprime itérativement la racine $n$ fois. Ce qui prend encore $n$ fois $\mathcal{O}(\log_2(n))$ opérations.

On a donc un tri en $\mathcal{O}(n\log_2(n))$ opérations.

Pour la représentation en tableau, voir Voir [wikipedia](https://fr.wikipedia.org/wiki/Tas_(informatique)) (on les place dans l'ordre de haut en bas et de droite à gauche).
{% enddetails %}

## parcours

Pour modifier la structure du tas on a dû évoluer dans la structure d'arbre planté. Un autre intérêt (encore un !) des arbres plantés est que tout sommet peut être considéré comme la racine de sous-arbre. On a donc uniquement besoin de créer l'algorithme qui fonctionnera pour la racine et le re-exécuter ensuite sur les descendants.

On utilise ce principe pour parcourir tous les sommets d'un arbre planté efficacement, c'est à dire en ne regardant chaque sommet qu'un nombre constant de fois.

### trois parcours classiques

{% exercice %}

Pour chaque parcours ci-après, donnez le résultat pour l'arbre de la partie [ordonnancement des sommets](#ordo-sommets) en supposant que `Examen de la Racine` signifie : affiche le numéro de la racine à l'écran.

Une fois ceci fait, trouvez un ordre qui lira les sommets dans l'ordre alphabétique à partir de la lettre b (en oubliant la racine).

{% endexercice %}
{% details "solution" %}

* pré-ordre : a-b-h-l-m-n-i-j-k-c-d-e-g-f
* post-ordre : l-n-m-h-j-k-i-b-g-e-f-d-c-a
* en-ordre : l-h-n-m-b-j-i-k-a-c-g-e-d-f

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

## arbre dans des graphes connexes

{% exercice %}

Montrer que pour tout graphe connexe $G = (V, E)$, il existe au moins un arbre $T=(V, E')$ tel que $E' \subseteq E$.

{% endexercice %}
{% details "solution" %}
Si un graphe est connexe et n'est pas un arbre, alors il existe un cycle. En supprimant une arête de ce cycle le graphe reste connexe et a strictement moins d'arêtes. On peut alors itérativement supprimer des arêtes à un graphe connexe qui contient un cycle jusqu'à obtenir un graphe connexe à $\vert V \vert -1$ arêtes qui ne contient pas de cycles : ce sera un arbre.
{% enddetails %}

On appelle ces arbres les **arbres couvrants** d'un graphe.

Les arbres couvrant d'un graphe sont beaucoup utilisés en optimisation. Nous allons montrer un exemple ci-après.

### graphe valué

On peut associer à tout graphe $G = (V, E)$ une **valuation** $f: E \rightarrow \mathbb{R}$.

#### une mise en situation

On suppose que vous êtes chef d'un état. Vous voulez que votre territoire soit connexe (que les gens puissent aller partout sur votre territoire), mais vous ne voulez pas payer trop cher (vous voulez être ré-élu et ça fait mauvais genre d'augmenter les impôts).

Vous demandez donc à vos conseillers de créer un graphe dont les sommets correspondant à vos villes et dont les arêtes sont valuées par le coût de construction d'une route entre ces 2 villes. Ce graphe n'a pas forcément toutes les arêtes si le coût de construction est prohibitif par exemple.

La solution la plus efficace consiste à trouver de ce graphe un arbre couvrant dont la somme des valuations est minimale parmi tous les arbres couvrant.

{% exercice %}

Pourquoi ?

{% endexercice %}
{% details "solution" %}
Un arbre est la structure minimale en nombre d'arêtes qui garantie la connexité. Parmi tous les arbres couvrants du graphe, on peut prendre un de ceux qui ont une somme des valuations de ses arêtes minimale (il y en a un nombre fini, le min existe donc mais il peut y en avoir plusieurs). Si la valuation d'une arête représente le coût, un arbre couvrant de poids minimal représente une solution de coût minimal pour rendre connexe le territoire.
{% enddetails %}

#### un exemple

On considère le graphe ci-dessous :

![graphe exemple](../assets/img/prim_graphe_exemple.png)

Avec un peu d'imagination considérez que c'est le graphe de construction d'une petite île du pacifique dont vous êtes le nouveau chef d'état.

{% exercice %}

* Quel est l'arête qui sera forcément dans tous les arbres couvrants de poids minimum ?
* Quel est l'arête qui ne sera forcément jamais dans un arbre couvrant de poids minimum ?
* y a-t-il plusieurs arbres couvrants de poids minimum pour ce graphe ?

{% endexercice %}
{% details "solution" %}

Toutes les preuves de cette partie et de la partie suivante vont fonctionner la même manière :

1. on va ajouter une arête à un arbre
2. ce nouveau graphe n'est plus un arbre mais il est connexe : il existe un cycle
3. en supprimant n'importe quelle arête de ce cycle, le graphe redevient un arbre.
4. si on supprime judicieusement l'arête du cycle, on arrivera à une contradiction. car le nouvel arbre sera mieux que l'arbre initial.

* Il n'y a qu'une seule arête avec une valuation minimale. S'il existait un arbre couvrant qui ne la possédait pas, on pourrait l'ajouter à cet arbre. Ce ne serait alors plus un arbre, il existerait donc un cycle. En supprimant une arête de ce cycle (on peut choisir une arête de valuation non minimale) on aurait à nouveau un arbre (connexe et nombre minimum d'arête), mais qui serait de valuation totale strictement plus petite que notre premier arbre. Ce qui est impossible puisqu'il était déjà de valuation minimale.
* Il n'y a qu'une seule arête avec une valuation maximale. De plus, il existe des cycles la contenant dans le graphe initial. Si on suppose qu'un arbre couvrant possède cette arête de valuation maximale et qu'on la supprime de l'arbre, on va se retrouver avec 2 parties connexes. Comme il existe un cycle contenant l'arête de valuation maximale dans le graphe initial, il va exister une arête du graphe initial qui relie les 2 parties connexes nouvellement créées. L'ajouter à notre graphe va à nouveau le rendre connexe : ce sera à nouveau un arbre. Comme il serait de valuation strictement plus petite que notre arbre initial, ce n'est pas possible.
* Oui, il existe plusieurs arbres couvrant car le cycle k-g-j-l est de valuation constante et valant 2. Un raisonnement identique aux 2 précédent montre que l'on peut échanger une arête de valuation 2 par une autre dans un arbre de valuation minimale.
{% enddetails %}

#### propriété

{% exercice %}

* montrez que s'il existe deux arbres couvrants de poids minimum qui ne différent que d'une arête, alors elles ont même valuation
* montrez que si toutes les valuations sont différentes, il n'existe qu'un seul arbre couvrant de poids minimal.
* montrez que la réciproque n'est pas vraie

{% endexercice %}
{% details "solution" %}

* Les 2 arbres ont même valuation de la somme des valuations de leurs arêtes :les 2 arêtes différentes ont donc forcément même valuation.
* On range les valuations des 2 arbres par ordre croissant. Les deux arbres étant différents, on s'arrête à la 1ère position dans cet ordre qui contient 2 arêtes différentes. L'une des arêtes va avoir une valuation inférieure à l'autre. On peut alors procéder comme précédemment et ajouter l'arête de valuation la plus petite dans l'autre arbre. Il faudra alors à nouveau supprimer une arête qui forme un cycle, mais on pourra enlever une arête de valuation plus grande, ce qui est impossible car l'arbre initial était de valuation minimale.
* Si le graphe de départ est un arbre, il n'y a qu'un seul arbre couvant et les valuations peuvent être égales.
{% enddetails %}

#### un algorithme {#algo-prim}

Ce problème a l'air dur, mais il possède un algorithme (assez) simple pour le résoudre. L'algorithme suivant est l'algorithme de Prim (1957) :

```text
Entrée :
    * un graphe G = (V, E)
    * une valuation f qui associe un réel à toute arête de G
Initialisation :
    * cout_entree(x) = +∞ pour tout sommet x
    * predecesseur(x) = x pour tout sommet x
    * V' = {}, E' = {}
Algorithme :
    * on choisit un sommet r quelconque
    * cout_entree(r) = 0
    * ajoute r à V'    
    * tant que V' n'est pas V:
        * pour tous les voisins x de r qui ne sont pas dans V':
            * si cout_entree(x) >= f(rx):
                cout_entree(x) = f(rx)
                predecesseur(x) = r
        * soit x le sommet de V qui n'est pas dans V' minimisant cout_entree(x)
        * r = x
        * cout_entree(r) = 0
        * ajoute r à V' et {r, predecesseur(r)} à E'
Retour :
    T = (V', E')
```

{% exercice %}

1. Prouver que si G est connexe, alors T est connexe et est un arbre
2. Prouver que $T$ est **un arbre couvrant de poids minimal** pour $G$.
{% endexercice %}
{% details "solution" %}
Voir [wikipedia](https://fr.wikipedia.org/wiki/Algorithme_de_Prim). Tout y est très bien expliqué.
{% enddetails %}

Maintenant qu'on est sur que ça marche :

{% exercice %}
Réalisez l'algorithme en entier sur le graphe précédent.
{% endexercice %}
