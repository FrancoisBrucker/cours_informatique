---
layout: layout/post.njk

title:  "Sujet Test 5 : Structure de données"
authors:
    - François Brucker
---

## Barème

Une note sur 5 répartie comme suit :

1. sur 1 point
2. sur 1 point
3. sur 1 point
4. sur 1 point
5. sur 1 point

La note sur $20$ finale est obtenue en multipliant la note sur 5 par $4$

{% note "**Objectif du test**" %}

Voir si vous révisez le cours...

* **un élève *normal*** doit parvenir à faire parfaitement les 3 premières questions. Ce qui lui permet d'avoir 3/5, soit 12/20
* **un bon élève** doit parvenir à réussir les 4 questions.

{% endnote %}

* min : 3.6/20 (.9/5)
* max : 20/20 (5/5)
* moyenne : 12/20 (3/5)
* écart-type : 4.92/20 (1.23/5)
* 25% : 8/20 (2/5)
* médiane (50%) : 12.4/20 (3.1/5)
* 75% : 14.6/20 (3.65/5)

{% attention %}
Vous avez 15min pour faire le test.
{% endattention %}

## Réponses

Les deux premières questions sont des questions de cours.

### Question 1

Pour toute structure de donnée, il faut connaître :

* les complexité de création et de destruction de la structure
* les complexités des méthodes permettant d'ajouter et de supprimer des éléments à la structure

### Question 2

Les complexité sont presque les mêmes, mais l'un est en **complexité amortie** et l'autre en **complexité en moyenne**.

* liste :
  * création en $\mathcal{O}(1)$
  * suppression en $\mathcal{O}(1)$
  * ajout d'un élément en fin de structure $\mathcal{O}(1)$ (en complexité amortie)
  * suppression d'un élément en fin de structure $\mathcal{O}(1)$ (en complexité amortie)
  * ajout/suppression d'un élément à une position quelconque $\mathcal{O}(n)$ (avec $n$ la taille de la liste)
* dictionnaire :
  * création en $\mathcal{O}(1)$
  * suppression en $\mathcal{O}(m)$ (avec $m$ la taille de la liste contenue dans le dictionnaire)
  * ajout d'un élément : $\mathcal{O}(1)$ en moyenne et $\mathcal{O}(m)$ dans le cas le pire
  * suppression d'un élément : $\mathcal{O}(1)$ en moyenne et $\mathcal{O}(m)$ dans le cas le pire

### Question 3

On la construit exactement comme un dictionnaire. Si l'on possède une fonction de hachage $f$ donnant des valeurs de 0 à $m-1$, la structure ensemble sera une liste $L$ de $m$ liste initialement vides.

Lorsque l'on ajoute un élément $e$ à la structure, on :

1. vérifie si $e$ est dans la liste $L[f(e)]$
2. s'il n'y est pas on l'ajoute en fin de liste $L[f(e)]$ (ce qui garantie l'unicité de chaque élément dans l'ensemble)

Lorsque l'on supprime un élément $e$, on le supprime de $L[f(e)]$ s'il y est.

### Question 4

On veut rendre l’intersection $C$ entre 2 ensembles $A$ et$B$

1. on crée un ensemble $C$ initialement vide
2. pour chaque élément $e$ de $A$
   1. on parcourt tous les éléments de $B$ à la recherche de $e$
   2. si on le trouve dans $B$ on l'ajoute à $C$
3. on rend $C$
