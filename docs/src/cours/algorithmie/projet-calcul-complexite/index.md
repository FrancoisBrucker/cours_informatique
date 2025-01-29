---
layout: layout/post.njk

title: "Projet : calcul de complexité"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Quelques exemples d'algorithme pour le calcul de la complexité. Nous allons reprendre les algorithmes que nous avons crée précédemment dans la partie [calcul et preuve d'algorithmes](../projet-itératif-récursif){.interne}.

{% aller %}
[Suite de Fibonacci](fibonacci){.interne}
{% endaller %}

{% aller %}
[Suppression de valeurs](suppression-valeurs){.interne}
{% endaller %}

{% aller %}
[Suppression des doublons](suppression-doublons){.interne}
{% endaller %}

## Matrice circulante

Nous allons créer [une matrice circulante](https://fr.wikipedia.org/wiki/Matrice_circulante).

Une matrice circulante $m$ à 

### Création et vérification

Pour une matrice circulante $m$, on a  $m_{i, j} = m_{i-1, j-1}$

### décalage

> TBD commencer par faire une fonction qui rend un tableau décalé.

### Matrice

> TBD niveau 2. On a un tableau de tableau. Donner une façon de faire avec deux création de tableau et une matrice carrée identité.
> puis une matrice triangulaire.
puis une matrice.

{% aller %}
[Triangle de Pascal](triangle-pascal){.interne}
{% endaller %}
