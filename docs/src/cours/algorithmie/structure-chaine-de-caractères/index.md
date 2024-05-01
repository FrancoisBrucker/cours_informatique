---
layout: layout/post.njk
title: "Structure chaine de caractères"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Une chaine de caractères est dans toute sa généralité définie comme un **_mot_** produit par un **_alphabet_** :

{% note "**Définition**" %}
- Un **_alphabet_** $\mathcal{A}$ est un ensemble fini
- un **_mot_** est une suite finie d'éléments de $\mathcal{A}$
- une **_lettre_** est un élément d'un mot
- un **_langage_** est un ensemble, possiblement infini de mots d'un alphabet

Le **_langage_** formé de tous les mots d'un alphabet $\mathcal{A}$ est noté $\mathcal{A}^\star$
{% endnote %}

On représentera par la suite de façon indistincte un mot par :

- la suite finie $m = (a_i)_{1\leq i \leq n}$
- la chaine de ses éléments concaténés : $m = a_1\dots a_n$
- un tableau $m = [a_1, \dots, a_n]$

En informatique, l'alphabet de prédilection est $\\{0, 1\\}$ mais a priori toutes les structures qu'on va définir vont fonctionner quelque soit l'alphabet. 

La notion de langage est au cour même de l'algorithmie, on effleurera le sujet dans la prochaine partie, et est un sujet inépuisable d'applications pratiques (trouver des gènes dansun génome, correcteur orthographique, etc) et de sujets d'examens (nous verrons un cas d'cole dans la troisième partie.

Nous verons également comment passer d'un alphabet binaire à un alphabet quelconque et comment à été résolu de façon pratique la représentation informatique de l'écriture d'une langue humaine.

## Structure algorithmique

### Langages et mots

{% aller %}
[Langages et mots](./langages-mots){.interne}
{% endaller %}

### Automates

{% aller %}
[Automates](./automates){.interne}
{% endaller %}

### Grammaires

> TBD : permet de compiler des programmes.

## Encodage

> TBD : pas implémentation (voir partie code pour utf8 et python). ici juste suite finie de caractère = mot = chaine de caractère
> ordre entre les caractères. facile pour nous mais peut etre un soucis pour les chinois
> implique ordre entre les mots
> en pratique pas que des 0 et des 1, des lettres.

>TBD : pas juste 1 nombre de taille fixe. On module la taille selon l'usage. Plus c'est utilisé plus c'est court. Comment faire ? C'est le principe de unicode

{% aller %}
[encodage](./encodage){.interne}
{% endaller %}

## Recherche de sous-mots

{% aller %}
[Problème de la recherche de sous-mots](./recherche-sous-mots){.interne}
{% endaller %}

## Autre problèmes

- Recherche de sous-séquence (pas collé)
- recherche de motifs 
- ...



