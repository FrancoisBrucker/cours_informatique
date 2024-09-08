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
- la chaîne de ses éléments concaténés : $m = a_1\dots a_n$
- un tableau $m = [a_1, \dots, a_n]$

En informatique, l'alphabet de prédilection est $\\{0, 1\\}$ mais a priori toutes les structures qu'on va définir vont fonctionner quelque soit l'alphabet.

La notion de langage est au cour même de l'algorithmie, on effleurera le sujet dans la prochaine partie, et est un sujet inépuisable d'applications pratiques (trouver des gènes dans un génome, correcteur orthographique, etc) et de sujets d'examens (nous verrons un cas d'école dans la troisième partie).

Nous verrons également comment passer d'un alphabet binaire à un alphabet quelconque et comment à été résolu de façon pratique la représentation informatique de l'écriture d'une langue humaine.

## Encodage

> TBD : pas implémentation (voir partie code pour utf8 et python). ici juste suite finie de caractère = mot = chaine de caractère
> ordre entre les caractères. facile pour nous mais peut etre un soucis pour les chinois
> implique ordre entre les mots
> en pratique pas que des 0 et des 1, des lettres.

>TBD : pas juste 1 nombre de taille fixe. On module la taille selon l'usage. Plus c'est utilisé plus c'est court. Comment faire ? C'est le principe de unicode

{% aller %}
[encodage](./encodage){.interne}
{% endaller %}

## Structure algorithmique

### Langages et mots

> TBD mots et décideur

## Langages et algorithmes

<div id="décideur"></div>
{% note "**Définition**" %}
Un **_décideur_** est un programme de :

$$f: \\{0, 1\\}^\star \rightarrow \\{0, 1 \\}$$

{% endnote %}

{% note "**Définition**" %}
On appelle **_langage_** d'un décideur $d$ l'ensemble $d^{-1}(1)$.

On dira qu'un décideur $d$ **_accepte le langage_** $L$ si $L = d^{-1}(1)$ et qu'un langage $L$ est **_décidable_** s'il existe un algorithme pour l'accepter.
{% endnote %}

Tout langage n'est bien sur pas décidable. On a vu qu'il était impossible de savoir _a priori_ si un programme va s'arrêter ou pas ([l'algorithme STOP n'existe pas](../../bases-théoriques/arrêt-rice/#algorithme-STOP){.interne}). Le langage composé des pseudo-codes associés aux algorithmes — c'est à dire les programmes qui s'arrêtent — n'est donc pas décidable. En revanche, le langage composé des pseudo-codes, est décidable (on peut facilement vérifier si un texte respecte les règles syntaxiques associé à un pseudo-code).

{% exercice %}
Montrez que l'ensemble des palindromes d'un alphabet $\mathcal{A}$ est décidable.
{% endexercice %}
{% details "corrigé" %}

```python
def palindrome(mot):
    for i in range(len(mot)):
        if mot[i] != mot[len(mot) - 1 - i]:
            return False
    return True

```

{% enddetails %}

> même distinction entre programme et algorithme : langages reconnaissable si programme (ne s'arrête pas forcément).

### Automates

{% aller %}
[Automates](./automates){.interne}
{% endaller %}

### Grammaires

> TBD : permet de compiler des programmes.

## Problèmes algorithmique associés

### Recherche de sous-mots

{% aller %}
[Problème de la recherche de sous-mots](./recherche-sous-mots){.interne}
{% endaller %}

### Recherche de sous-séquences

> TBD

### Recherche de motifs

> TBD
