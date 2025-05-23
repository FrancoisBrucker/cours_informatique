---
layout: layout/post.njk

title: Algorithmes classiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Algorithmes classiques dont l'intérêt est à la fois esthétique (ce sont de jolis algorithmes),pratiques (ils mettent en oeuvre des techniques facilement réutilisables) et didactiques (trouver et prouver leurs fonctionnement vous fera progresser).

## Fibonacci

> - **Utilité** : à connaître car :
>   - exemple de transformation d'un algo de complexité exponentiel à linéaire.
>   - un algorithme dont la complexité vaut sa valeur dans le cas récursif simple
> - **Difficulté** : facile pour la création et la complexité de base

{% aller %}

[Suite de Fibonacci](./fibonacci){.interne}

{% endaller %}

## $X$ marks the spot

> - **Utilité** : crucial à comprendre
> - **Difficulté** : dur

Un robot se déplace sur une droite à la vitesse de 1 mètre par seconde. Il doit chercher un endroit particulier sur cette droite à $X$ mètres de 0, $X$ pouvant être **positif ou négatif** mais est entier. Cette endroit est inconnu pour le robot, mais s'il passe sur cet endroit il le reconnaîtra.

{% exercice %}
Donnez un algorithme en $\mathcal{O}(X)$ permettant au robot d'atteindre $X$ à partir de sa position initiale qui vaut $0$.
{% endexercice %}
{% details "corrigé" %}

Remarquer que l'on ne peut pas :

1. avancer uniquement dans une direction : il faut osciller
2. osciller en incrémentant d'un pas constant : on est de complexité au carré de $X$ (c'est facile à montrer)

L'idée est d'osciller autour de l'origine en puissances de 2 :

1. avancer de $2^0 = 1$ : position finale $+1$
2. reculer de $2^0 + 2^0$ : position finale $-1$
3. avancer de $2^0 + 2^1$ : position finale $+2$
4. reculer de $2^1 + 2^1$ : position finale $-2$
5. avancer de $2^1 + 2^2$ : position finale $+4$
6. reculer de $2^2 + 2^2$ : position finale $-4$
7. avancer de $2^2 + 2^3$ : position finale $+8$
8. reculer de $2^3 + 2^3$ : position finale $-8$
9. ...

Au pire, le robot arrivera sur la marque $X$ au bout de $2 \cdot \log_2(X)$ itérations.

Il aura effectué un déplacement d'au plus : $2 \cdot (X + X/2 + X/4 + \dots + 1)$ unités. Or $2 \cdot (X + X/2 + X/4 + \dots + 1) = 2\cdot X \cdot \sum_{i=0}^{i=\log_2(X)} 1/2^i = 2\cdot X \cdot(1- 1/2^{\log_2(X)}) = \mathcal{O}(X)$.

L'astuce de se déplacer par puissance de 2 permet de majorer la distance par $X$ car la série des $\sum 1/2^i$ qui est, on l'a vu, convergente. Il est crucial de connaître cette technique qui vous tirera de nombreux mauvais pas en algorithmie.

{% enddetails %}

## Tours de Hanoï

> - **Utilité** : classique parmi les classique. La preuve que la complexité est minimale est à connaître
> - **Difficulté** : moyen

{% aller %}
[Tours de Hanoi](./tours-hanoi){.interne}
{% endaller %}

## Compteur binaire

> - **Utilité** : algorithme à la base de nombreux autres algorithmes d'énumération. A connaître pour son énumération récursive.
> - **Difficulté** : moyen

{% aller %}
[Compteur binaire](compteur-binaire){.interne}
{% endaller %}

## Col de listes

> - **Utilité** : à connaître car un classique des concours (on le donne sans indications...)
> - **Difficulté** : moyen

{% aller %}
[Cols de listes et de matrices](cols){.interne}
{% endaller %}

## Tris

> - **Utilité** : tris pouvant être utile dans des cas particuliers et surtout à la base de nombreux pièges
> - **Difficulté** : moyen

Des tris utiles dans des cas spécifiques, et dont la complexité semble plus petite que $n\log(n)$. Connaître pourquoi ce n'est (bien sur) pas le cas.

{% aller %}
[Tris spéciaux](tris-spéciaux){.interne}
{% endaller %}

## Chaînes de caractères

> - **Utilité** : classique mais pas indispensable
> - **Difficulté** : facile avec les indications données

{% aller %}
[Chaines de caractères](./chaine-caracteres){.interne}
{% endaller %}

## pgcd

> - **Utilité** : une [knutherie](https://fr.wikipedia.org/wiki/Donald_Knuth) sympathique mais pas indispensable
> - **Difficulté** : moyen à dur

{% aller %}
[Calcul du pgcd](./pgcd){.interne}
{% endaller %}
