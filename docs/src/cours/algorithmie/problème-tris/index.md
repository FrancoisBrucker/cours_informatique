---
layout: layout/post.njk

title: Problème du tri

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% prerequis %}

Parties [bases](/cours/coder-et-développer/#bases){.interne} et [développer](/cours/coder-et-développer/#développer){.interne} du [cours de développement](/cours/coder-et-développer){.interne}.

{% endprerequis %}

Étude du problème du tri et implémentation de quelques algorithmes pour *voir* les différentes façon de trier et leurs complexités.

Les informaticiens adorent [les algorithmes de tris](https://fr.wikipedia.org/wiki/Algorithme_de_tri). Pas parce qu'ils aiment l'ordre — loin de là — mais parce qu'il existe des millions de façons différentes de trier.

{% info %}
Les algorithmes de tri que nous verrons dans cette partie nous permettrons non seulement de mettre en oeuvre tout ce que nous avons vu sur les techniques de preuves et de calcul de complexités, mais également d'apprendre de nouveaux outils, comme le master theorem.
{% endinfo %}

Commençons par définir le problème :

{% note "**Problème**" %}

- **nom** : tri
- **données** : un tableau d'entiers
- **réponse** : un tableau contenant les valeurs du tableau en entrée triées selon l'ordre croissant

{% endnote %}

## Reconnaissance

Commençons par travailler sur un problème connexe au problème du tri, celui de savoir si un tableau d'entiers est trié ou non. Le problème du tri présuppose en effet que l'on sache ce qu'est un tableau trié et, en creux, qu'on puisse vérifier (rapidement) qu'un tableau est trié ou non.

{% aller %}
[Reconnaissance d'un tableau trié](./reconnaissance){.interne}
{% endaller %}

Pouvoir vérifier qu'une solution à un problème en est vraiment une est un point crucial en algorithmie. Nous y reviendrons intensivement lorsque nous parlerons de classes de problèmes.

## Algorithmes Tris simples

Deux Algorithmes simples pour trier un tableau.

### Tri par sélection

Le plus simple des algorithmes de tri, pour s'échauffer.

{% aller %}
[Tri par sélection](./algorithme-sélection){.interne}
{% endaller %}

### Tri par insertion

Son implémentation va nécessiter d'utiliser une nouvelle technique, le placement de sentinelles, et démontrer ses complexités va demander un peu de travail car son nombre d'instructions est très variable selon le tableau donné en paramètre.

{% aller %}
[Tri par insertion](./algorithme-insertion){.interne}
{% endaller %}

## Complexité du problème du tri

{% aller %}
[Complexité du problème](./complexité-problème){.interne}
{% endaller %}

## Algorithmes de tris optimaux

### Tri fusion

Le tri fusion utilise une technique de création d'algorithme classique nommée *diviser pour régner* et nous utiliserons le très utile master Theorem pour en calculer la complexité.

{% aller %}
[Algorithme du tri fusion](./algorithme-fusion){.interne}
{% endaller %}

### Tri de python

L'algorithme [timsort](https://en.wikipedia.org/wiki/Timsort) est l'algorithme utilisé par python pour trier des listes :

```python

T = [1, 3, 2, 6, 4, 5]
T.sort()

print(T)

```

Ce tri est **in place** et est un mix entre le tri fusion et le tri par insertion. C'est un tri très efficace puisque :

{% note "**Complexités du timsort**" %}
Pour un tableau de taille $n$, l'algorithme [timsort](https://en.wikipedia.org/wiki/Timsort) a :

- une complexité de $\mathcal{O}(n\ln(n))$
- une complexité min de $\mathcal{O}(n)$
- une complexité en moyenne de $\mathcal{O}(n\ln(n))$

{% endnote %}

{% info %}
Ne perdez donc pas de temps à recoder un algorithme de tri : utilisez celui de python !
{% endinfo %}

## Cas du tri rapide

Le tri rapide est, malgré sa simplicité apparente, le plus difficile à implémenter proprement et pour en calculer la complexité. Il vous apprendra à avoir une intuition de la complexité d'un algorithme.

{% aller %}
[Algorithme du tri rapide](./algorithme-rapide){.interne}
{% endaller %}

## Implémentations

Projet de développement pour voir les tris se trier.

{% aller %}
[Implémentation des algorithmes](./implémentation-tris){.interne}
{% endaller %}
