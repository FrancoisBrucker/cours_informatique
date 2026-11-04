---
layout: layout/post.njk

title: "Projet : mesurer des complexités"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Exercices du cours


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
> - ajouter des exercices avec l'ordi avec plusieurs algos pour un même problème puis amélioration de la constantes multiplicative.
