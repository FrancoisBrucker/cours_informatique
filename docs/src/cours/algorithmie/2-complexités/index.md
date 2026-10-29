---
layout: layout/post.njk

title: Mesures de complexités

eleventyNavigation:
  prerequis: 
    - "/cours/coder-et-développer/apprendre-programmation/coder-projets/"


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Cette partie s'intéresse à la notion de complexités pour un algorithme qui permet de mesurer ses performances.

{% lien %}
[une intro très bien faite sur la complexité des problèmes algorithmiques](https://www.youtube.com/watch?v=n8Z7v09zrl0&list=PLF0b3ThojznQJ6u4FUcpyzi0it5EpR3dh&index=12){.externe}
{% endlien %}

## Complexité d'un algorithme

Cette partie s'intéresse à la notion de complexité d'un algorithme et donne les moyens de la calculer.

{% aller %}
[Définition et outil de mesure](./définitions-mesure-O)
{% endaller %}

Utilisation pour calculer théoriquement et en pratique la complexité d'algorithmes :

{% aller %}
1. [Calcul de complexités avec des $\mathcal{O}$](./complexité-algorithmes)
2. [Complexité en moyenne](./complexité-moyenne)
{% endaller %}

Enfin, comment mesurer la complexité en pratique (et en python) :

{% aller %}
[Mesurer la complexité d'un code](./complexité-code)
{% endaller %}

## On s'entraîne

### Projet 


### Complexités du cours

> 1. boucles /n = cte sum_{k \leq i \leq n}

> 4. faire varier k aléatoirement et montrer que du coup il faut prendre la moyenne.
>   - boucles imbriquées dépendantes = n^2

### Recherche dichotomique

> TBD théorique puis en pratique. Vérifier que log ok avec régression linéaire


## Mot de 01

> égalité mots de 01
> max/moyenne ?
> TBD faire les tests et séparer main et fct pour qu'ils puissent reprendre le code fait dans les prochains tds.


## Maximum d'un tableau

> 
> TBD nb de mise à jour du maximum. 
> 1. calcul max
> 2. nombre de mise a jour de l'algo simple : Max n et en moyenne ln(n) (Knuth) (avec les main le prochain > est à la moitié.)




> TBD pour aller plus loin
> TBD ajouter pyperf pour les perf d'un programme et cprofile pour le profilage des bootleneck <https://www.stephane-robert.info/docs/developper/programmation/python/profiling/>
> 3. modif pour mise a jour dans une fonction et vérifier que cprofile ou pyperf le voit

>

{% aller %}
[Création et preuve de l'algorithme maximum récursif](../../1-algorithme/projet/#algorithme-max-tableau-rec)
{% endaller %}

<span id="algorithme-max-tableau-complexité"></span>
{% exercice %}
 Donnez sa complexité de l'algorithme `maximum_rec`{.language-}.

{% endexercice %}
{% details "corrigé" %}

Toutes les lignes de l'algorithme sont en $\mathcal{O}(1)$ à part la récursion. Comme la récursion est faite sur la taille du tableau, on va noter $C(n)$ sa complexité où $n$ est la taille du tableau passé en paramètre. Elle satisfait alors l'équation :

<div>
$$
C(n) = \mathcal{O}(1) + C(n-1)
$$
</div>

On a vu en cours que cette équation se résout en : $C(n) = \mathcal{O}(n)$.

{% enddetails %}

> TBD pour aller plus loin timeit et pypertf.
> TBD code
> voir qu'il y a une légère variation à chaque appel même avec les même données. DOnc faire une moyenne.
> pyperf
 
### Calculs

> TBD exo recherche : min/max/moyenne. Un autre ou moyenne proche du min
Maintenant que l'on peut calculer les complexités, on peut reprendre les algorithmes itératifs et récursifs que [nous avons crées précédemment](../1-algorithme/projet) :

{% aller %}
[Projet : calculer des complexités d'algorithmes itératifs et récursifs](./projet)
{% endaller %}

> TBD k-moyenne de la partie non corrigée. Elle mérite d'être corrigée
> TBD ne garder que les exos qui font sens. Et de difficulté croissante.
> 
On vérifie qu'on sait faire :

{% aller %}
[exercices non corrigés](./exercices-non-corrigés)
{% endaller %}

> TBD : une fois qu'on a un algorithme qui fait ce qu'on veut on essaie de le faire le plus vite possible (en moins d'instruction possible)
> TBD égalité de mots binaires. max O(n) en moyenne O(2)
> 
<!-- TBD

- ajouter un projet de de code. avec tableaux numpy, split de valeurs, enlever le ramasse=miette etc pour bien calculer en moyenne en code
- tbd ajouter voir si for est pareil que while en pratique.
- tbd gagner un peu est non optimal par rapport à ganger un ordre de grandeur.
- tbd coder les calcul des boucles du cours et voir que effectivement les sommes sont proches.

- ajouter des exercices avec l'ordi avec plusieurs algos pour un même problème puis amélioration de la constantes multiplicative.

-->