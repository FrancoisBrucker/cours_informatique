---
layout: layout/post.njk
title: Exercices gloutons

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Exercices de créations d'algorithmes gloutons pour résoudre divers problèmes d'optimisation. On a séparé les exercices en deux grandes parties : la première où la stratégie gloutonne est optimale (et où il faut le démontrer), la seconde où elle ne l'est pas mais dont on peut garantir les performances.

> TBD Attention souvent pas de garanties du tout. Beaucoup d'algorithmes gloutons sont juste des heuristiques qui peuvent être aussi mauvaises que possible. Les utiliser dépend alors de la nature des données. Et au final, les étudiants ont rarement besoin des prof pour écrire des algorithmes non optimaux et sans garanties...

## Gloutons optimal

Comme toujours lorsque l'on crée un algorithme glouton, la principale difficulté est de trouver l'ordre dans lequel considérer les objets. Une fois cet ordre trouvé les preuves sont toujours les mêmes (mais il faut tout de même la faire).

### Recouvrement

{% exercice %}
Donnez un algorithme glouton exhibant un nombre minimal $K$ d'intervalles unités $I_k = [u_i, u_{i+1}]$ ($1\leq i \leq K$) permettant de recouvrir $n$ réels donnés $x_1, \dots, x_n$.

{% endexercice %}

### Réservation SNCF

On suppose que $n$ personnes veulent voyager en train un jour donné. La personne $i$ veut prendre le train $t_i$.

Les données du problème sont :

- $k$ trains qui partent dans la journée, 
- le train $j$ part avant le train $j+1$,
- chaque train ne peut contenir plus de $K$ passagers.

{% exercice "**Solution possible ?**" %}
Proposez un algorithme qui vérifie que pour un nombre de trains donné et une liste de trains choisis, il est possible de faire voyager tout le monde.
{% endexercice %}

On suppose maintenant que la personne $i$, si elle ne peut pas prendre le train $t_i$ parce qu’il est complet, accepte de prendre un des trains suivants (s’il y en a un).

{% exercice "**Solution approchée**" %}
Proposez un algorithme minimisant l'attente globale pour faire voyager tous les voyageurs.

{% endexercice %}

### Ordonnancement, la variante

On reprend [le problème d'ordonnancement du cours](../principes/#exemple-ordonnancement){.interne}, mais avec des pénalités et pas des gains : ne pas réaliser une tâche $i$ coûte une pénalité $p_i$.


{% exercice %}
Proposez un algorithme glouton permettant de trouver un ordre d'exécution des tâches permettant de minimiser la somme totale des pénalités.
{% endexercice %}

### Ordonnancement, le retour

On suppose que l'on a $n$ tâches à réaliser par **un unique** ouvrier et chaque tâche $1\leq i \leq n$ met $p_i$ unités de temps à être effectuée. Une fois que l'ouvrier commence une tâche, il l'a termine : s'il effectue la tâche $i$, il ne fait rien d'autre pendant $p_i$ unités de temps.

On veut minimiser la date de fin de réalisation des tâches.

#### Formalisation du problème

En supposant que l'on a effectué les tâches dans l'ordre croissant :

- donnez la valeur de la moyenne de réalisation des fins de tâches
- donner la valeur optimale si l'on a trois tâches de temps de réalisation 3, 1 et 5.

#### Algorithme

Donnez (et prouvez) un algorithme glouton permettant de trouver l'ordre optimal d'exécution des tâches pour minimiser la valeur moyenne de fin de réalisation.

#### Dates de disponibilité

On suppose maintenant que toutes les tâches ne sont pas immédiatement disponibles. Chaque tâche $i$ a maintenant une date $d_i$ à partir de la quelle elle peut être réalisée.

Donnez (et prouvez) un algorithme glouton permettant de trouver l'ordre optimal d'exécution des tâches.

#### Interruption de tâches

On suppose maintenant que l'ouvrier peut mettre en pause la réalisation du tâche puis la reprendre ultérieurement. Par exemple il peut commencer la tâche $i$ de temps de réalisation $p_i = 5$, la réaliser pendant 2 unités de temps, puis la mettre en pause pour réaliser la tâche $j$ puis, une fois la tâche $j$ terminée, reprendre la tâche $i$ et la finir en y passant les 3 unités de temps restantes.

Donnez (et prouvez) un algorithme glouton permettant de trouver l'ordre optimal d'exécution des tâches.


### Ordonnancement 

> et 20/21

### Une quête d'essence

Une route comporte $n$ stations services numérotées dans l’ordre du parcours, de $0$ à $n-1$. La distance du départ de la station $i$ est de $d_i$ kilomètres et on considère que $d[0] = 0$.

Le but est d'atteindre la dernière station de la route avec un réservoir de $L$ litres d'essence, en considérant qu'un litre d'essence permet de faire 1 kilomètre.

#### Admissibilité

Donnez une condition nécessaire et suffisante pour que l'automobiliste puisse parcourir toute la route jusqu'à la dernière station service.

#### Algorithme

Écrivez un algorithme glouton qui donne le nombre minimum de stations auxquelles il faut mettre de l'essence dans le réservoir pour arriver à destination, en supposant que le réservoir est initialement vide. 

#### Prix fluctuant 

On suppose que le prix de l'essence à la station $i$ vaut $p_i$. 

Donnez un algorithme glouton optimal permettant de réaliser le parcours au prix minimum.

## Glouton pas optimal mais pas mal

> A performance garanties. 

### Équilibrage de charge

> exam 21/22

### Plan de tables

> ET 22/23

### Empaquetage

Bon glouton pas forcément bon tout le temps.
> 
> <https://ics.uci.edu/~goodrich/teach/cs165/notes/BinPacking.pdf>
> <https://en.wikipedia.org/wiki/Bin_packing_problem>
> <https://www.dil.univ-mrs.fr/~gcolas/algo-licence/slides/gloutons.pdf>
