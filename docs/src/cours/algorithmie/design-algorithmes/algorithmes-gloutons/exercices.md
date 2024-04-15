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

[Comme dans le cours](../principe/#exemple-ordonnancement){.interne} mais chaque tâche a un cout si on ne la réalise pas à temps. 

{% exercice %}
Le but est de minimiser la somme des pénalités.
{% endexercice %}

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

Montrez que si une solution possède deux tâches successives $t_{i}$ et $t_{i+1}$ telles que $f_{i} > f_{i+1}$, les échanger n'augmente pas le retard.

En déduire l'ordre optimal.
{% endexercice  %}

## Glouton pas optimal mais pas mal

Les algorithmes gloutons suivants ne sont pas optimaux, mais on peut démontrer qu'ils permettent tout de même de n'être pas trop éloigné de celle-ci.

{% note "**Définition**" %}
Un algorithme est **_à performance garantie_** si sa solution est plus grande que $\alpha \cdot P(e)$ où $P(e)$ est la solution optimale pour une entrée $e$.
{% endnote %}

### Empaquetage

On veut faire une partition de $n$ entiers en $m$ ensembles tel que la somme des entiers dans chaque ensemble ne dépasse pas $K$. Le but est de minimiser $m$ sachant les $n$entiers et la borne $K$.

{% exercice "**Applications**" %}
Donnez quelques cas d'application concret de ce problème.
{% endexercice %}

Commencez par montrer la propriété suivante :
{% exercice "**Solution optimale**" %}
Le nombre minimum d'ensemble est plus grand que la somme de tous les entiers divisé par $K$.
{% endexercice %}

On va utiliser l'algorithme glouton suivant :

```text
Es = []
E = []
pour chaque entier ni:
    si somme(E) + ni ≤ K:
        ajoute ni à E
    sinon:
        ajoute E à Es
        E = [ni]
```

{% exercice "**Propriété**" %}
1. Montrez que la somme des entiers de deux éléments successifs de `Es`{.language-} est strictement plus grand que $K$
2. en déduire que la somme de tous les entiers est plus grande que $K \cdot \frac{m}{2}$
{% endexercice %}
Les deux propriétés précédentes doivent vous permettre de prouver :
{% exercice "**Performance garantie**" %}
Montrez que l'algorithme précédent trouve au maximum 2 fois la solution optimale.
{% endexercice %}

Cet algorithme permet d'être utilisé même si l'on ne connait pas tous les entiers. En revanche, il peut être très mauvais : 

{% exercice "**Cas le pire**" %}
Donnez un exemple où l'algorithme rend une solution valant$2M-2$ où $M$ est le nombre minimum d'ensembles. 
{% endexercice %}

### Équilibrage de charge

On appelle **_équilibrage de charge_** le problème suivant : 

- On possède $m$ machines et $n$ tâches à effectuer.
- Chaque tâche $j$ nécessite $t_j$ unités de temps pour être effectuée par une machine.
- Pour chaque machine $i$, on associe l'ensemble $M_i$ des tâches effectuées par celles-ci, et on note $T_i$ le temps passé à effectuer ses tâches : $T_i = \sum_{j \in M_i} t_j$.

On cherche à trouver les ensembles $M_i$ permettant de minimiser la quantité : $\max_{1\leq i \leq m} T_i$. On note $T^\star$ ce minimum.

{% exercice  "**Quelques propriétés**" %}
1. montrez que l'on a $T^\star \geq \max_{1 \leq j\leq n} t_j$.
2. Montrez que l'on a $T^\star \geq \frac{1}{m}\sum_{1 \leq j\leq n} t_j$ (**attention**, c'est bien $\frac{1}{m}$ et non $\frac{1}{n}$).

{% endexercice  %}

L'algorithme glouton que l'on utilisera pour résoudre le problème consistera à ajouter itérativement une tâche à la machine $i$ réalisant $T_i = \min_{1\leq j \leq m} T_j$.

{% exercice  "**Un algorithme glouton**" %}
- Dans quel ordre proposez vous de ranger les tâches ? Justifiez votre réponse.
- Montrez que s'il y a $m$ tâches ou moins à classer, l'algorithme glouton trouve la solution optimale.
{% endexercice %}


On considère une réalisation de l'algorithme. Soit $i^\star$ la machine réalisant $T_{i^\star} = \max_{1\leq i \leq m} T_i$ à la fin de l'algorithme, et $j$ l'indice de la dernière tâche qui lui a été assignée au cours de l'exécution de l'algorithme.

{% exercice  "**Propriétés**" %}

1. Montrez qu'à la fin de l'algorithme, on a $T_{i^\star} -t_j \leq T_k$ pour tout $k$.
2. En déduire que $T_{i ^\star} - t_j \leq \frac{1}{m}\sum_{1\leq k\leq m}T_k$.
3. Déduire de la déduction que $T_{i ^\star} - t_j \leq T^\star$.
4. Puis que $T_{i ^\star} \leq 2 \cdot T^\star$.

{% endexercice %}

Les propriétés précédentes nous permettent de déduire que l'algorithme glouton est à performance garantie :

{% exercice  "**Performances**" %}

- Montrez que la solution proposée par l'algorithme glouton est au pire 2 fois moins bonne que la solution optimale.
- Montrer que cette performance est atteinte quelque soit l'ordre des tâches utilisé.
{% endexercice %}


### Plan de tables

Une de vos cousines se marie et vous a demandé de faire le plan de table du repas de noces. Pour maximiser la convivialité du repas elle vous demande :

- de ne mettre à chaque table que des personnes qui s'entendent;
- d'avoir un petit nombre de tables.

{% attention %}
On ne demande pas que le nombre de tables soit minimum.
{% endattention %}

#### Modélisation

Un plan de table $P$ est une structure de données contenant :

- une liste $\verb|NOMS|$ contenant le nom de tous les invités;
- une liste $\verb|IC|$ d'incompatibilités où $\verb|IC[i]|$ contient un ensemble d'indices tel que si $\verb|j|$ est dans $\verb|IC[i]|$ alors $\verb|NOMS[i]|$ ne peut être à la même table que $\verb|NOMS[j]|$.

On suppose de plus que la relation d'incompatibilité est symétrique (si $\verb|j|$ est dans $\verb|IC[i]|$ alors $\verb|i|$ est dans $\verb|IC[j]|$). Par exemple si les invités sont : _"tata Guillemette"_, _"cousin Valentin"_, _"tonton Julien"_, _"papy François"_ et _"soeur Manon"_ et que les relations sont :

- _"tata Guillemette"_ aime bien tout le monde
- _"papy François"_ n'aime personne à part _"tata Guillemette"_
- _"cousin Valentin"_ ne supporte pas _"soeur Manon"_

On a la structure de données suivante (où $\verb|{...}|$ représente des ensembles) :

- $\verb|NOMS = ["tonton Julien", "papy François", "tata Guillemette", "cousin Valentin", "soeur Manon"]|$
- $\verb|IC = [{1}, {0, 3, 4}, {}, {1, 4}, {3, 1} ]|$

Résoudre le problème revient à trouver un plan de table (chaque invité est associé à une table unique) valide (deux invités à une même table ne doivent pas avoir d'incompatibilité), c'est-à-dire créer une liste $\verb|tables|$ telle que :

- chaque élément de $\verb|tables|$ est un ensemble d'indices tel que si $i \in \mbox{tables}[k]$ alors l'invité $\verb|NOMS[i]|$ est placé à la table numéro $k$
- pour tout indice $i\geq 0$ strictement plus petit que le nombre d'invités, il existe un unique $k$ tel que $i \in \mbox{tables}[k]$
- si $i, j \in \mbox{tables}[k]$ alors $j \notin \mbox{IC}[i]$

{% exercice %}
1. Montrez que quelles que soient les incompatibilités et le nombre d'invités, il existe un plan de table valide.
2. Justifiez que pour l'exemple, le nombre minium de tables est 3.
3. Combien de solutions à 3 tables différentes existe-t-il ?
4. Montrez que si l'on supprime l'incompatibilité entre _"papy François"_ et _"soeur Manon"_ dans l'exemple alors il existe une solution à 2 tables.
{% endexercice %}

Trouvons le nombre minimum de tables d'un plan de table valide pour un cas particulier de plan de table.
On se place dans le cas où la relation d'incompatibilité est **_anti-transitive_**, c'est-à-dire que si l'invité $A$ est incompatible avec l'invité $B$ et l'invité $B$ incompatible avec l'invité $C$, alors l'invité $A$ est **_compatible_** avec l'invité $C$.


{% exercice %}
Démontrez que s'il existe une solution à 2 tables alors la relation d'incompatibilité est anti-transitive.
{% endexercice %}

{% exercice %}
Démontrez que si la relation d'incompatibilité est anti-transitive alors il existe une solution à 2 tables.
{% endexercice %}

{% exercice %}
Déduire de la question précédente un algorithme permettant de rendre un plan de table valide à deux tables lorsque la relation d'incompatibilité est anti-transitive.

{% endexercice %}

On se propose d'écrire un algorithme glouton permettant de résoudre le problème dans le cas général (on ne suppose pas les relations anti-transitives). La structure de cet algorithme est la suivante :

1. créer une liste $\verb|ordre|$ contenant les indices de tous les convives;
2. créer une liste vide $\verb|tables|$
3. pour chaque élément $\verb|i|$ de $\verb|ordre|$, ajouter $\verb|i|$ à la première table de $\verb|tables|$ possible (la première table ne contenant aucune de ses incompatibilités) si elle existe ou en créer une nouvelle sinon.

{% exercice %}
1. Pourquoi l'algorithme précédent est-il glouton ?
2. Démontrez qu'il donne bien une réponse au problème quel que soit $\verb|ordre|$. Quel ordre utiliseriez-vous par défaut pour résoudre le problème ? Et pourquoi ?
3. Cet algorithme est efficace mais on va voir qu'il dépend fortement de la liste $\verb|ordre|$. Montrez que l'algorithme peut rendre un nombre de tables strictement plus grand que 2 pour une relation anti-transitive.
{% endexercice %}

En utilisant la structure de l'algorithme glouton :
{% exercice %}
- démontrez que le nombre minimum de tables ne peut excéder le nombre maximum d'incompatibilités pour une personne plus 1;
- donnez un cas où cette borne est atteinte;
- donnez un cas où on peut faire strictement mieux que cette borne.
{% endexercice %}

