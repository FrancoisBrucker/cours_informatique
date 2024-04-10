---
layout: layout/post.njk
title: "Exercices gloutons : corrigé"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Glouton optimal

## Recouvrement

<https://algo.gricad-pages.univ-grenoble-alpes.fr/L3I-S5-algo/TD1-10-corrige.pdf>
> recouvrement de points par des intervalles exo 3
## réservation SNCF

### solution possible ?

### solution approchée

## Ordonnancement, la variante

> introduction à l'algorithmique p392

## Ordonnancement, le retour

> introduction à l'algorithmique p393

### Formalisation du problème

### Algorithme

### Dates de disponibilité

### Interruption de tâches


## Une quête d'essence

Une route comporte $n$ stations services numérotées dans l’ordre du parcours, de $0$ à $n-1$. La distance du départ de la station $i$ est de $d_i$ kilomètres et on considère que $d[0] = 0$.

Le but est d'atteindre la dernière station de la route avec un réservoir de $L$ litres d'essence, en considérant qu'un litre d'essence permet de faire 1 kilomètre.

### Admissibilité

Donnez une condition nécessaire et suffisante pour que l'automobiliste puisse parcourir toute la route jusqu'à la dernière station service.

### Algorithme

Écrivez un algorithme glouton qui donne le nombre minimum de stations auxquelles il faut mettre de l'essence dans le réservoir pour arriver à destination, en supposant que le réservoir est initialement vide. 

### Prix fluctuant 

## Glouton comme heuristique


