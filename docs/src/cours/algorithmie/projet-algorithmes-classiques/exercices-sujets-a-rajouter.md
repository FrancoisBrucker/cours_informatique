---
layout: layout/post.njk

title: Algorithmes classiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD exos de mpci

> TBD <https://diplome.di.ens.fr/informatique-ens/annales.html>
> TBD <https://nstarr.people.amherst.edu/trom/intro-notsure.html> <https://www.gamepuzzles.com/3color.htm>
> TBD <https://www.inf.usi.ch/carzaniga/edu/algo19s/exercises.pdf>

> TBD bezout : <http://pascal.delahaye1.free.fr/cpge/informatique/cours%20projetes/cp04.pdf>

## Algorithmes arithmétique

- addition de listes de chiffres
- multiplications de listes de chiffres

(- [optimisation de Karastuba](https://fr.wikipedia.org/wiki/Algorithme_de_Karatsuba))

> TBD ajouter liste d'exercices / colles / tests

> TBD rendu de pièces par programmation dynamique

## Min et max d'un tableau d'entiers

> - **Utilité** : une optimisation élégante et une astuce utile à garder dans sa poche, car elle se retrouve dans plusieurs algorithmes optimaux classiques.
> - **Difficulté** : moyen

### Un algo

{% exercice %}
Donnez un algorithme avec $T.\mbox{\small longueur} - 1$ comparaisons permettant de trouver le minimum d'un tableau d'entier.

Que faut-il modifier pour trouver le maximum ?
{% endexercice %}
{% details "corrigé" %}
> TBD simple
{% enddetails %}

### Complexité du Problème

{% exercice %}
Montrer que si l'on cherche à trouver l'élément minimum d'un tableau d'entiers $T$ il faut au moins $T.\mbox{\small longueur} - 1$ comparaisons
{% endexercice %}
{% details "corrigé" %}
> TBD graphe connexe.
{% enddetails %}
On veut minimiser le nombre de comparaisons dans la recherche d'un élément min et max d'un tableau.

### Une astuce

{% exercice %}
Montrer que si l'on cherche à trouver à la fois le minimum et le maximum d'un tableau d'entiers $T$, on peut s'en sortir avec  $3/2 \cdot T.\mbox{\small longueur} - 1$ comparaisons.
{% endexercice %}
{% details "corrigé" %}
Si on fait les deux à la suite on a 2n comparaisons.

On commence par trier les éléments $T[i]$ et $T[i+1]$ pour tout $i$ ($n/2$ comparaisons)

Puis on cherche le min sur les $T[2i]$ ($n/2$ comparaisons) et le max sur les $T[2i +1]$ ($n/2$ comparaisons)

{% enddetails %}
