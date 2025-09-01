---
layout: layout/post.njk
title: Pseudo-code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[La définition générale d'un algorithme](../bases-théoriques/définition){.interne} ne spécifie rien sur les instructions à utiliser, juste qu'elles doivent être décrites en un nombre fini de mots. Un **_pseudo-code_** est une proposition d'instructions possibles pour décrire un algorithme, compréhensibles par un humain.

Ce n'est cependant pas une langue car il n'y a pas de place pour l'ambiguïté ni l'invention : tout doit y être rigoureusement défini, et chaque étape élémentaire doit être réalisable en un temps fini par un humain :

{% info %}

Rappelez-vous les trois premières règles de la [définition d'un algorithme](../bases-théoriques/définition/#règles-générales){.interne} qui sont faciles à respecter.

{% endinfo %}

Ce n'est pas non plus un langage informatique dont le but est d'être compris par un ordinateur. Il est communément admis que tout algorithme peut être écrit en **_pseudo-code_** :

<span id="règles"></span>
{% note "**Définition**" %}
Un pseudo-code est une succession de lignes qui seront exécutées **_en séquence_** les unes à la suite des autres. Chaque ligne est composée d'une instruction qu'il faut réaliser avant de passer à la ligne suivante.
{% endnote %}

Avant de définir précisément le pseudo-code, notez la thèse (hypothèse) fondamentale de l'informatique :

{% note "**Thèse de Church-Turing**" %}

Tout programme (et donc algorithme) peut s'écrire sous la forme d'un pseudo-code (et réciproquement).

{% endnote %}
{% lien %}
[Thèse de Church-Turing](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church).
{% endlien %}

La thèse de Church-Turing a été initialement formulée pour les Machines de Turing mais (nous le verrons bien plus tard) pseudo-code et machines de Turing sont deux notions équivalentes. Notez que cette affirmation n'est pas démontrée mais que toutes les tentatives (et il y en a eu) pour infirmer cette affirmation ont été des échecs.

## Pseudo-code et langages de programmation

Les langages de programmation classiques comme [python](https://www.python.org/), [java](https://www.java.com/fr/) ou encore [rust](https://www.rust-lang.org/fr) se transcrivent aisément en pseudo-code et réciproquement. Ce sont deux notions équivalentes :

- on utilisera le pseudo-code pour l'étude théorique des algorithmes
- on codera ces algorithme dans un langage dédié à être exécuté lorsque l'on voudra les tester. Dans le cadre de ce cours on utilisera le python.

## Éléments de pseudo-code

### Briques de base

Commençons par décrire la _grammaire de base_ du pseudo-code :

{% aller %}
[Briques de base](briques-de-base){.interne}
{% endaller %}

### Algorithmes en pseudo-code

Un programme et un algorithme doivent posséder des paramètres d'entrées
En pseudo-code, un algorithme est une suite d'instructions qui, a partir de paramètres d'entrée, rend une sortie. Considérons par exemple la description de  l'algorithme de recherche d'un élément dans une liste :

```text
Nom : recherche
Entrées :
    T : un tableau d'entiers
    x : un entier
Programme :
    parcourir chaque élément de t jusqu'à trouver un élément dont la valeur est égale à la valeur de x.
    Si on trouve un tel élément, rendre "Vrai"
    Sinon rendre "Faux"
```

En pseudo-code, cela va donner ça :

<div id="problème-recherche"></div>

```pseudocode
algorithme recherche(T: [entier],
                     x: entier     # entier recherché dans t
                    ) → booléen:   # Vrai si x est dans t

    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux
```

Le programme est un bloc. La definition du bloc (jusqu'aux `:`{.language-}) est constitué :

1. du mot-clé `algorithme`{.language-} qui détermine la nature du bloc
2. suit le du nom du programme
3. puis ses paramètres d'entrées entre parenthèses. Chaque paramètre est décrit par son nom suivit de son type
4. enfin, le type de sortie de l'algorithme qu'on fait précéder d'une flèche.

Si on a besoin d'information supplémentaire pour qu'un lecteur puisse mieux comprendre le pseudo-code on peut ajouter des commentaires en les faisant commencer par un `#`{.languages-}.  Ne mettez pas trop de commentaires, normalement le pseudo-code et le nom des variables doit suffire. On a ici juste décrit ce que fait l'algorithme avec ses paramètres d'entrées.

{% lien %}
La description des types de paramètres est reprise du format python : <https://docs.python.org/fr/3.13/library/typing.html>
{% endlien %}

Terminons par un petit exercice :

<span id="algorithme-nombre-occurrences"></span>

{% exercice %}
Adaptez le pseudo code de l'algorithme `recherche(T: [entier], x: entier) → booléen){.language-} précédent pour créer l'algorithme :

```pseudocode
nombre(T: [entier], x: entier) → entier
```

Cet algorithme  rend le nombre de fois où `x`{.language-} est présent dans `T`{.language-}
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme nombre(T: [entier], x: entier) → entier:
    nb ← 0
    pour chaque e de T:
        si e == x:
            nb ← nb + 1
    rendre nb
```

{% enddetails %}

### Fonctions

Un algorithme est constitué uniquement d'instructions de base. Mais rien n'empêche de réutiliser des algorithmes déjà écrit en les appelant par leur nom. Ces algorithmes intermédiaires sont appelées **_fonctions_**.

{% aller %}
[Fonctions](fonctions){.interne}
{% endaller %}

## Écrire du bon pseudo-code

Un bon pseudo-code doit être compréhensible en tant que tel, sans commentaires.

Pour cela il faut :

- expliciter la signature de vos algorithme
- utiliser des noms de variables ou de fonctions explicites et utile à la compréhension
- séparer les différentes parties d'un algorithmes en fonctions au nom explicite.

Leurs noms importent peu, seuls leurs fonctions sont importantes. Vous pouvez donc utiliser les mots qui vous plaisent, du moment qu'ils sont compréhensible pour vous et — surtout — pour votre lecteur. Le plus souvent, on utilisera un mix de python et de français, ou d'anglais.

## Opérateurs utilisés en pseudo-code

> TBD ici abus de notation avec utilisation sans déclaration. Le maitre mot est clarté. Si cela alourdi de tout expliciter alors que c'est clair, on laisse mais si ça peut rendre confus on l'explicite (ici exemple vec +)
> 
Les op
> TBD ajouter soit comme mot clé qui définie des variables
> unaire : `soit`
> binaire := définition soit x un entier x := un entier y := 3x + 1. On utilisera uniquement pour définir des fonctions ou algorithme d'une ligne `AJOUTE_UN(x) := x + 1. (attention dans certains vieux manuel ou <- n'existe pas parfois := est utilisé comme <-)
> <- affectation
> = égalité (conséquence) 1 = cos2(x) + sin2(y)
> == test
> faire les différences entre
> x := y : on remplace x par y à chaque fois qu'on le voit
> x <- y : on affecte x à la valeur de y
> x = y : avec les définitions de x et y les 2 variables sont toujours égales (c'est une conséquence)
> x == y : vrai si la valeur de x vaut la valeur de y et faux sinon
>
> puis dire que l'on oublie souvent cette ligne lorsque le type est évident.
> Mais attention aux cas limite c = a + 1 ou c = c + 1.0 en C.
> en python le type d´pend des variables ou des opérateurs :

```python
>>> x = 1
>>> y = 3
>>> z = x + y
>>> type(z)
<class 'int'>
>>> z = 3 / 1
>>> type(z)
<class 'float'>
>>> z = 3 // 1
>>> type(z)
<class 'int'>
>>> x = 1.0
>>> z = x + y
>>> type(z)
<class 'float'>
>>> z = y + x
>>> type(z)
<class 'float'>
```

> TBD soyez explicite `x entier puis x = 2/3` que vaut x ? 1 ou 0 ? floor ou ceil.
> L'algorithmie ne dot pas souffrir d'interpretation.
> 