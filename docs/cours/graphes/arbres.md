---
layout: page
title:  "Théorie des graphes : arbres"
category: cours
tags: informatique graphes
author: "François Brucker"
---

> [graphes]({% link cours/graphes/index.md %}) / [arbres]({% link cours/graphes/arbres.md %})
{: .chemin}

## But

Explorer les propriétés et l'intérêt de l'arbre.

> Tous les graphes de cette partie seront considérés comme étant *simple*
{: .attention}

[éléments de corrigé]({% link cours/graphes/arbres-corrige.md %})

## définitions

Un **arbre** est un *graphe simple* $T = (V, E)$ qui est :

* connexe
* sans cycle

### graphe simple

> Redonnez la définition d'un graphe simple. Combien d'arêtes au maximum peut contenir un graphe simple ?
{: .a-faire}

### arbre ou pas arbre ?

> Déduire de la définition lequel des 2 graphes ci-dessous est un arbre.
{: .a-faire}

|![graphe A]({{ "/assets/cours/graphes/pas_arbre.png" | relative_url }})|![graphe B]({{ "/assets/cours/graphes/arbre.png" | relative_url }})|
|A|B|

### algorithme de reconnaissance

#### graphe connexe

>1. Donnez un algorithme permettant de savoir si un graphe $G = (V, E)$ donné est connexe.
>2. Quelle structure de graphe utiliseriez vous pour que cet algorithme ait la plus petite complexité possible ?
{: .a-faire}

**Indice** : On pourra partir d'un sommet $x$ et trouver itérativement tous les sommets que l'on peut atteindre avec lui.

#### graphe sans cycle ?

Là comme ça, ça n'a pas l'air simple de répondre à cette question. On va plutôt ruser et prouver deux propriétés des graphes connexes à la place.

>* Tout graphe sans cycle contient au maximum $\vert V \vert - 1$ arêtes.
>* Tout graphe connexe contient au minimum $\vert V \vert - 1$ arêtes.
{: .a-faire}

#### conditions

En déduire que :

>Un graphe $G=(V, E)$ est un arbre si et seulement si :
>
>* il est connexe
>* $\vert E \vert = \vert V \vert - 1$
{: .a-faire}

Sur votre lancée prouvez aussi que :

>un graphe $G=(V, E)$ est un arbre si et seulement si :
>
>* il est sans cycle
>* $\vert E \vert = \vert V \vert - 1$
{: .a-faire}

Pour enfoncer le clou et montrer que les arbres sont une structure de connexité minimale vous pouvez aussi :

> prouver que :
>
>* Si on ajoute une arête à un arbre (n'importe laquelle) on ajoute un cycle
>* Si on supprime une arête à un arbre (n'importe laquelle) on le déconnecte
{: .a-faire}

#### conclusion

Les conditions précédentes nous permettent de ne pas avoir à chercher si un graphe à un cycle, ce qui rend l'algorithme de reconnaissance plus aisé :

> Donnez l'algorithme final pour savoir si un graphe est un arbre.
{: .a-faire}

## arbre enracinées

En informatique on utilise souvent la structure d'arbre en l'**enracinant**, c'est à dire qu'on choisi un sommet qui sera la racine et tous les autres sommets vont être dépendant de lui. Ceci est possible de part une importante propriété des arbres : **l'unicité des chemins**

### chemin et arbres

Soit $T = (V, E)$ un arbre.

>Montrez que quelques soient deux sommets $x$ et $y$, il n'existe qu'un seul chemin entre $x$ et $y$.
{: .a-faire}

### ordonnancement des sommets {#ordo-sommets}

L'unicité des chemins permet d'ordonner les sommets par rapport à leur chemin par rapport à la racine. On a coutume de les faire *"tomber"* depuis la racine. On peut en effet les ranger par rapport à **leur chemin** par rapport à celle ci :

![arbre_plante]({{ "/assets/cours/graphes/arbre_plante.png" | relative_url }}){:style="margin: auto;display: block;"}

Vocabulaire :

* $y$ est un **ancêtre** de $x$ : si $y$ est sur le chemin entre la racine et $x$
* $x$ est un **descendant** de $y$ : si $y$ est sur le chemin entre la racine et $x$
* $x$ est une **feuille** s'il n'a pas de descendant
* $x$ est un **nœud intérieur** s'il n'est pas une feuille
* $x$ est un **successeur** de $y$ : si $y$ est le sommet juste avant $x$ dans le chemin de la racine à $x$
* $y$ est un **prédécesseur** de $x$ : si $y$ est le sommet juste avant $x$ dans le chemin de la racine à $x$
* la **hauteur** de $x$ est la longueur du chemin entre la racine et $x$.
* la **hauteur** de l'arbre est la longueur du plus long chemin entre la racine et un autre sommet.

> Donnez un exemple de chacun des termes pour le graphe ci-avant.
{: .a-faire}

Cet ordonnancement est [très utilisé en biologie](https://fr.wikipedia.org/wiki/Arbre_phylog%C3%A9n%C3%A9tique) par exemple car il permet de rendre compte de l'évolution des espèces. En analyse des données on utilise ce paradigme pour classer les données (qui sont les feuilles) selon ce qu'elles ont en commun (les leurs ancêtres).

## arbre binaire planté

En informatique, c'est souvent les arbres binaires planté que l'on utilise :

Un arbre planté est binaire si tout noeud intérieur a **au plus 2 successeurs**. On aura parfois aussi besoin qu'il soit **complet**, c'est à dire que les noeuds intérieurs qui n'ont pas 2 successeurs sont en bas de l'arbre (à la hauter de l'arbre -1).

### propriété fondamentale des arbres binaires

>Montrer que pour un arbre binaire, si noeud intérieur a exactement 2 successeurs, alors en notant $f$ le nombre de feuilles de l'arbre, on a :
>
>* la hauteur de l'arbre est égale à $\log_2(f)$
>* $f$ est égal au nombre de nœuds intérieurs plus 1.
{: .a-faire}

Ces propriétés ci-dessus montrent que si l'on veut organiser $n$ données, on a besoin que d'un arbre de hauteur $\log_2(n)$. Comme le chemin depuis la racine nous permet de retrouver les données, si on associe une question à chaque nœud intérieur, on peut retrouver $n$ éléments en ne posant que $\log_2(n)$ questions. C'est le principe des **arbres de décisions**, si utiles en apprentissage automatique.

> La différence en $log_2(n)$ et $n$ est très importante ! On par exemple besoin d'uniquement 100 questions pour trier 1267650600228229401496703205376 éléments.
> Un informaticien est prêt à beaucoup, beaucoup de choses pour avoir une structure en $\log_2(n)$.

### exemple du tas

Nous allons montrer ici une utilité de l'arbre binaire complet pour résoudre le problème d'une file de priorité.

#### le problème

Une salle d'attente des urgences d'un hôpital contient des patients dont la gravité d'état est donnée par un entier. Des patients peuvent arriver et partir de la salle d'attente et leur état peut s'améliorer (la gravité d'état baisse) ou se détériorer (leur gravité d'état augmente). A chaque fois qu'un médecin est libre, on prend en charge le patient avec l'état de gravité le plus important.  

#### une solution possible (naïve)

On regarde chaque patient et on prend le patient ayant la gravité d'état le plus important.

> Quel est le coût algorithmique d'utiliser une telle solution ?
{: .a-faire}

Si l'on suppose que l'état de gravité d'un patient est connu, on peut faire bien mieux.

#### un tas

Un tas est un arbre binaire planté complet dont les sommets sont des entiers. On considère en plus qu'un tas est **plein**, c'est à dire que les feuilles de hauteur maximum forment un intervalle à gauche de l'arbre.

![arbre_plante_tas_?]({{ "/assets/cours/graphes/arbre_plante_tas_abc.png" | relative_url }}){:style="margin: auto;display: block;"}

> Des trois arbres ci-dessus lequel (il n'y en a qu'un) est binaire, complet et plein ?
{: .a-faire}

De plus, pour un tas, chaque nœud est de valeur plus grande que chacun de ses descendants direct.

> * Créez un tas avec les nombres : 42, 12, 1, 3, 6, 5.
> * Y a-t-il plusieurs possibilités ?
> * que peut-on dire du nœud ayant le plus grand nombre ?
{: .a-faire}

#### manipulation d'un tas

> Donner les algorithmes pour effectuer les opérations suivantes :
>
>1. ajout d'un élément
>2. modification d'une valeur
>3. suppression de la racine
{: .a-faire}

On peut s'en sortir avec des algorithme dont le nombre d'opération est proportionnelle à la hauteur du tas.

> En conclure que l'utilisation du tas est bien meilleure que la solution naïve.
{: .a-faire}

#### pour la bonne bouche

> * En déduire une façon de trier un tableau de nombre.
> * trouver un de représenter un tas par une liste (on pourra parcourir le tas de haut en bas et de droite à gauche).
{: .a-faire}

## parcours

Pour modifier la structure du tas on a du évoluer dans la structure d'arbre planté. Un autre intérêt (encore un !) des abres planté est que tout sommet peut-être considéré comme la racine de sous-arbre. On a donc uniquement besoin de créer l'algorithme qui fonctionnera pour la racine et le re-exécuter ensuite sur les descendants.

On utilise ce principe pour parcourir tous les sommets d'un arbre planté efficacement, c'est à dire en ne regardant chaque sommet qu'un nombre constant de fois.

### trois parcours classiques

> Pour chaque parcours ci-après, donnez le résultat pour l'arbre de la partie [ordonnancement des sommets](#ordo-sommets) en supposant que `Examen de la Racine`signifie : affiche le numéro de la racine à l'écran.
>
> Une fois ceci fait, trouvez un ordre qui lira les sommets dans l'ordre alphabétique.
{: .a-faire}

#### pré-ordre

```text
pré-ordre(racine)
Si la racine a des descendants:
    Examen de la Racine 
    pré-ordre(Fils Gauche) 
    pré-ordre(Fils Droit)
```

#### post-ordre

```text
post-ordre(racine)
Si la racine a des descendants:
    post-ordre(Fils Gauche) 
    post-ordre(Fils Droit)
    Examen de la Racine 
```

#### en-ordre

```text
en-ordre(racine)
Si la racine a des descendants:
    en-ordre(Fils Gauche) 
    Examen de la Racine 
    en-ordre(Fils Droit)
```

## arbre dans des graphes connexe

> Montrer que pour tout graphe connexe $G = (V, E)$, il existe au moins un arbre $T=(V, E')$ tel que $E' \subseteq E$.
{: .a-faire}

On appelle ces arbres les **arbres couvrants** d'un graphe.

Les arbres couvrant d'un graphe sont beaucoup utilisés en optimisation. Nous allons montrer un exemple ci-après.

### graphe valué

On peut associer à tout graphe $G = (V, E)$ une **valuation** $f: E \rightarrow \mathbb{R}$.

#### une mise en situation

On suppose que vous êtes chef d'un état. Vous voulez que votre territoire soit connexe (que les gens puissent aller partout sur votre territoire), mais vous ne voulez pas payer trop cher (vous voulez être ré-élu et ça fait mauvais genre d'augmenter les impôts).

Vous demandez donc à vos conseillez de créer un graphe dont les sommets correspondant à vos villes et dont les arêtes sont valuées par le coût de construction d'une route entre ces 2 villes. Ce graphe n'a pas forcément toutes les arêtes si le coût de construction est prohibitif par exemple.

La solution la plus efficace consiste à trouver de ce graphe un graphe couvrant dont la somme des valuation est minimale parmi tous les graphes couvrant.

> Pourquoi ?
{: .a-faire}

#### un exemple

On considère le graphe ci-dessous :

![graphe exemple]({{ "/assets/cours/graphes/prim_graphe_exemple.png" | relative_url }}){:style="margin: auto;display: block;"}

Avec un peu d'imagination considérez que c'est le graphe de construction d'une petite île du pacifique dont vous êtes le nouveau chef d'état.

> * Quel est l'arête qui sera forcément dans tous les arbres couvrant de poids minimum ?
> * Quel est l'arête qui ne sera forcément jamais dans un arbre couvrant de poids minimum ?
> * y a-t-il plusieurs arbres couvrant de poids minimum pour ce graphe ?
{: .a-faire}

#### propriété

> * montrez que s'il existe deux arbres couvrant de poids minimum ne différent que d'une arête, alors elles on même valuation
> * montrez que si toutes les valuations sont différentes, il n'existe qu'un seul arbre couvrant de poids minimal.
> * montrez que la réciproque n'est pas vraie
{: .a-faire}

#### un algorithme

Ce problème à l'air dur, mais il possède un algorithme (assez) simple pour le résoudre. L'algorithme suivant est l'algorithme de Prim (1957) :

```text
Entrée :
    * un graphe G = (V, E)
    * une valuation f qui associe un réel à toute arête de G
Initialisation :
    * cout_entree(x) = +∞ pour tout sommet x
    * predecesseur(x) = x
    * V' = {}, E' = {}
Algorithme :
    * on choisit un sommet r quelconque
    * cout_entree(r) = 0
    * ajoute r à V'    
    * tant que V' n'est pas V:
        * pour tous les voisins x de r qui ne sont pas dans V':
            * si cout_entree(x) >= cout_entree(r) + f(rx):
                cout_entree(x) = cout_entree(r) + f(rx)
                predecesseur(x) = r
        * soit x le sommet de V qui n'est pas dans V' minimisant cout_entree(x)
        * r = x
        * cout_entree(r) = 0
        * ajoute r à V' et {r, predecesseur(r)} à E'
Retour :
    T = (V', E')
```

Commencer par :

> Prouver que si G est connexe, alors T est connexe et est un arbre
{: .a-faire}

Une fois ceci fait :

> Prouver que $T$ est **un arbre couvrant de poids minimal** pour $G$
{: .a-faire}

Maintenant qu'on est sur que ça marche :

> Réalisez l'algorithme en entier sur le graphe précédent.
{: .a-faire}
