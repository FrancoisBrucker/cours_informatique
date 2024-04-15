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

Attention, souvent les algorithmes gloutons n'ont pas de garanties du tout. Beaucoup d'algorithmes gloutons sont juste des heuristiques qui peuvent être aussi mauvaises que possible, les utiliser dépend alors de la nature des données. Nous n'en parlons cependant pas ici car, en général, les étudiants ont rarement besoin de profs pour écrire des algorithmes non optimaux et sans garanties...

## Gloutons optimal

Comme toujours lorsque l'on crée un algorithme glouton, la principale difficulté est de trouver l'ordre dans lequel considérer les objets. Une fois cet ordre trouvé les preuves sont toujours les mêmes (mais il faut tout de même la faire).

### Recouvrement

{% exercice %}
Donnez un algorithme glouton exhibant un nombre minimal $K$ d'intervalles unités $I_k = [u_i, u_{i+1}]$ ($1\leq i \leq K$) permettant de recouvrir $n$ réels donnés $x_1, \dots, x_n$.

{% endexercice %}

### Réservation SNCF

On suppose que $n$ personnes veulent voyager en train un jour donné. La personne $i$ veut prendre le train $t_i$.

Les données du problème sont :

- $K$ trains partent dans la journée, 
- le train $j$ part avant le train $j+1$,
- chaque train ne peut contenir plus de $P$ passagers.

{% exercice "**Solution possible ?**" %}
Proposez un algorithme qui vérifie que pour un nombre de trains donné et une liste de trains choisis, il est possible de faire voyager tout le monde.
{% endexercice %}

On suppose maintenant que la personne $i$, si elle ne peut pas prendre le train $t_i$ parce qu’il est complet, accepte de prendre un des trains suivants (s’il y en a un).

{% exercice "**Solution approchée**" %}
Proposez un algorithme minimisant l'attente globale pour faire voyager tous les voyageurs.

{% endexercice %}

### Une quête d'essence

Une route comporte $n$ stations services numérotées dans l’ordre du parcours, de $0$ à $n-1$. La distance du départ de la station $i$ est de $d_i$ kilomètres et on considère que $d[0] = 0$.

Le but est d'atteindre la dernière station de la route avec un réservoir de $L$ litres d'essence, en considérant qu'un litre d'essence permet de faire 1 kilomètre.

{% exercice  "**Admissibilité**" %}
Donnez une condition nécessaire et suffisante pour que l'automobiliste puisse parcourir toute la route jusqu'à la dernière station service.

{% endexercice  %}

#### Algorithme

Écrivez un algorithme glouton qui donne le nombre minimum de stations auxquelles il faut mettre de l'essence dans le réservoir pour arriver à destination, en supposant que le réservoir est initialement vide. 

#### Prix fluctuants 

On suppose que le prix de l'essence à la station $i$ vaut $p_i$. 

Donnez un algorithme glouton optimal permettant de réaliser le parcours au prix minimum.

## Problèmes d'ordonnancements

Les problèmes d'ordonnancements sont très important car nombre de problèmes courant peuvent s'écrire sous cette forme. Nous allons voir dans cette partie quelques exemplex où l'approche gloutonne est optimale.

### Ordonnancement avec pénalité

Comme dans le cours mais chaque tâche a un cout si on ne la réalise pas à temps. Le but est de minimiser la somme des pénalités.

### Ordonnancement avec départ différé

On suppose que l'on a $n$ tâches à réaliser par **un unique** ouvrier et chaque tâche $1\leq i \leq n$ met $p_i$ unités de temps à être effectuée. Une fois que l'ouvrier commence une tâche, il l'a termine : s'il effectue la tâche $i$, il ne fait rien d'autre pendant $p_i$ unités de temps.

On veut minimiser la somme des fin de réalisations des tâches.

{% exercice  "**Formalisation du problème**" %}
En supposant que l'on a effectué les tâches dans l'ordre $\sigma_1, \dots, \sigma_n$ :

1. donnez le temps minimum de départ et de fin des tâches $\sigma_1$, $\sigma_2$ et $\sigma_3$
2. en déduire que la valeur de la somme totale des temps de départ des tâches vaut $\sum_i(n-i)p_{\sigma_i}$
{% endexercice %}

{% exercice  "**Exemple**" %}
Quel est l'ordre d'exécution des tâches minimisant la somme des fins de tâches pour trois tâches de temps de réalisation 1, 3 et 5.
{% endexercice %}

L'exemple précédent a du vous donner une idée de l'ordre associé au glouton :


{% exercice  "**Ordre d'exécution des tâches**" %}
Donnez (et prouvez) un algorithme glouton permettant de trouver l'ordre optimal d'exécution des tâches pour minimiser la valeur moyenne des débuts de réalisations.

{% endexercice %}

On suppose maintenant que toutes les tâches ne sont pas immédiatement disponibles. Chaque tâche $i$ a maintenant une date $d_i$ à partir de la quelle elle peut être réalisée.

{% exercice  "**Départs différés**" %}
Donnez (et prouvez) un algorithme glouton permettant de trouver l'ordre optimal minimisant la valeur moyenne des débuts de réalisations.

{% endexercice %}

On suppose maintenant que l'ouvrier peut mettre en pause la réalisation du tâche puis la reprendre ultérieurement. Par exemple il peut commencer la tâche $i$ de temps de réalisation $p_i = 5$, la réaliser pendant 2 unités de temps, puis la mettre en pause pour réaliser la tâche $j$ puis, une fois la tâche $j$ terminée, reprendre la tâche $i$ et la finir en y passant les 3 unités de temps restantes.

{% exercice  "**Tâches fragmentables**" %}
Donnez (et prouvez) la méthode permettant de minimiser la moyenne des fins de chaque tâches.

{% endexercice %}


### Ordonnancement avec retard

On suppose que pour mener à bien un projet, on doit réaliser $n$ tâches où chaque tâche $t_i$ a :

- une durée de réalisation : $d_i$
- un temps de fin conseillé : $f_i$

Si on note $s_i$ le début de la réalisation de la tâche $t_i$ on définit son retard par : 

<div>
$$
    r_i = \max(0, s_i + d_i - f_i)
$$
</div>

Si $r_i > 0$ la tâche $t_i$ est en retard. Le but du problème est de trouver un algorithme glouton qui affecte à chaque tache son début et qui minimise le retard maximum : $$R = \max_{1\leq i \leq n} r_i$$ 

Comme on a qu'un seul ouvrier pour réaliser les tâches, on ne peut créer qu'une tâche à la fois.


{% exercice  "**Premières propriétés**" %}

1. Montrez que le retard d'une solution ne peut pas augmenter si l'on supprime les temps d'inactivité de celle-ci : l'ouvrier enchaîne les tâches sans s'arrêter jusqu'à ce que toutes les tâches aient été réalisées.
2. En déduire que la solution de notre problème est un ordonnancement des tâches selon un ordre particulier : c'est un algorithme glouton sans étape de choix (toutes les tâches sont dans la solution).

{% endexercice  %}

On suppose que les tâches $(t_i)_{1\leq i \leq n}$ sont rangées dans un certain ordre. Écrivez l'algorithme qui calcule le retard maximum pour cet ordre. Quel est sa complexité ?

{% exercice  "**Mauvais ordres**" %}
Montrez que les ordres suivants ne sont pas optimaux :
- item Les tâches triées par durée décroissante.
- Les tâches triées par durée croissante.

{% endexercice  %}

{% exercice  "**Ordre optimal**" %}

-Montrez que si une solution possède deux tâches successives $t_{i}$ et $t_{i+1}$ telles que $f_{i} > f_{i+1}$, les échanger n'augmente pas le retard.
- Montrez que si une solution ne possède aucunes tâches successives $t_{i}$ et $t_{i+1}$ telles que $f_{i} > f_{i+1}$, alors les tâches sont rangées par temps de fin conseillé croissante.
- En déduire que l'ordre optimal est réalisé pour l'ordre des temps de fin conseillé croissante.

{% endexercice  %}

## Glouton pas optimal mais pas mal

Les algorithmes gloutons suivants ne sont pas optimaux, mais on peut démontrer qu'ils permettent tout de même de n'être pas trop éloigné de celle-ci.

{% note "**Définition**" %}
Un algorithme est **_à performance garantie_** si sa solution est plus grande que $\alpha \cdot P(e)$ où $P(e)$ est la solution optimale pour une entrée $e$.
{% endnote %}

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
