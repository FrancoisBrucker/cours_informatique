---
layout: layout/post.njk
title: Pseudo-code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[La définition générale d'un algorithme](../../bases-théoriques/définition){.interne} ne spécifie rien sur les instructions à utiliser, juste qu'elles doivent être décrites en un nombre fini de mots. Un **_pseudo-code_** est une proposition d'instructions possibles pour décrire un algorithme, compréhensibles par un humain.

Ce n'est cependant pas une langue car il n'y a pas de place pour l'ambiguïté ni l'invention : tout doit y être rigoureusement défini, et chaque étape élémentaire doit être réalisable en un temps fini par un humain :

{% info %}

Rappelez-vous les trois premières règles de la [définition d'un algorithme](../../bases-théoriques/définition/#règles-générales) qui sont faciles à respecter.

{% endinfo %}

Ce n'est pas non plus un langage informatique dont le but est d'être compris par un ordinateur.

Il est communément admis que tout algorithme peut être écrit en **_pseudo-code_** :

{% note "**Thèse de Church-Turing**" %}

Tout programme (et donc algorithme) peut s'écrire sous la forme d'un pseudo-code (et réciproquement).

{% endnote %}

Notez que cette affirmation n'est pas démontrée mais que toutes les tentatives (et il y en a eu) pour infirmer cette affirmation ont été des échecs.

{% lien %}
[Thèse de Church-Turing](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church).
{% endlien %}

La thèse de Church-Turing a été initialement formulée pour les Machines de Turing mais, nous le verrons pseudo-code et machines de Turing sont deux notions équivalentes.

<span id="règles"></span>
{% note "**Définition**" %}
Un pseudo-code est une succession de lignes qui seront exécutées **_en séquence_** les unes à la suite des autres. Chaque ligne est composée d'une instruction qu'il faut réaliser avant de passer à la ligne suivante.
{% endnote %}

Les langages de programmation classiques comme [python](https://www.python.org/), [java](https://www.java.com/fr/) ou encore [rust](https://www.rust-lang.org/fr) se transcrivent aisément en pseudo-code et réciproquement et peuvent donc être considérés comme équivalent :

- on utilisera le pseudo-code ou un langage très proche comme le python pour l'étude théorique des algorithmes dans ce cours
- on codera ces algorithme dans un langage dédié à être exécuté lorsque l'on voudra les tester. Dans le cadre de ce cours on utilisera le python.

## Éléments de pseudo-code

### Briques de base

Commençons par décrire la _grammaire de base_ du pseudo-code :

{% aller %}
[Briques de base](briques-de-base){.interne}
{% endaller %}

### Format

Le pseudo-code d'un programme va contenir, en plus de ses instructions, un nom, des entrées et souvent une sortie (son but). Par exemple :

<div id="problème-recherche"></div>

```text
Nom : recherche
Entrées :
    t : un tableau d'entiers
    x : un entier
Programme :
    pour chaque élément e de t:
        si e == x:
            Retour vrai
    Retour faux
```

ou de manière équivalente, en un mélange de python et de français :

```python/
def recherche(t, x):
    pour chaque élément e de t:
        si e == x:
            return vrai
    return faux
```

Ou encore, complètement en python :

<div id="fonction-recherche"></div>

```python/
def recherche(t, x):
    for e in t:
        if e == x:
            return True
    return False
```

### Fonctions

{% aller %}
[Fonctions](fonctions){.interne}
{% endaller %}

## Écrire du bon pseudo-code

{% aller %}
[Comment écrire du pseudo-code](style){.interne}
{% endaller %}
