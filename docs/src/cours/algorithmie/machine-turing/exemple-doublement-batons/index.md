---
layout: layout/post.njk
title: "Exemple du doublement de batons"

eleventyNavigation:
  order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Faire de l'arithmétique avec une machine de Turing. Comme on ne peut qu'écrire des 0 ou des 1, la façon la plus simple d'écrire les nombres est d'utiliser un [système unaire](https://fr.wikipedia.org/wiki/Syst%C3%A8me_unaire) : chaque entier $n$ est représenté par $n$ 1 successifs sur la machine.

## Problème

Nous voulons créer une machine de Turing qui prend en entrée un suite finie de $k$ `1` ($k$ _bâtons_) et rend comme sortie une suite de $2k$ `1` ($2k$ _bâtons_).

Cette machine fait l'opération _multiplier par 2 unaire_.

## Idée

Chaque baton en entrée doit être doublé, mais :

- comme une machine de Turing n'a pas de variable on ne peut pas utiliser de compteur de boucle
- que le nombre d'état est constant : on ne peut pas les utiliser pour faire un compteur de boucle ($n$ états ne permettraient que de traiter les nombre de taille au plus $n$)

Il faut pouvoir trouver une boucle principale d'action et avoir un moyen simple de vérifier les fins de boucle et de revenir en début de boucle si nécessaire.

L'idée est de fabriquer la sortie à droite de l'entrée en supprimant itérativement un bâton à l'entrée et d'en ajouter 2 à la sortie. Lorsque l'on aura supprimé tous les bâtons de l'entrée, il ne restera que la sortie et la machine s'arrêtera :

```
000①10000000000
0000①0000000000
00001⓪000000000
000010⓪00000000
0000101⓪0000000
00001011⓪000000
0000101①0000000
000010①10000000
00001⓪110000000
0000①0110000000
000⓪10110000000
0000①0110000000
00000⓪110000000
000000①10000000
0000001①0000000
00000011⓪000000
000000111⓪00000
0000001111⓪0000
000000111①00000
00000011①100000
0000001①1100000
000000①11100000
00000⓪111100000
0000⓪0111100000
00000⓪111100000
000000①11100000
```

Ou de façon animée avec 3 batons :

![doublement de bâtons](./turing_double_batons.gif)

## Création de la machine

On va exécuter notre machine et ajouter petit à petit des états qui vont permettre de réaliser notre schéma ci-dessus.

On va ici ne pas faire dans la dentelle et ajouter des états lorsque l'on en a besoin. Il existe sûrement une version plus optimisée de cette machine mais qui sera plus compliquée à trouver.

### Départ

On part de (START, 1) à droite tant que l'on rencontre des 1 :

```
000①10000000000 START
0000①0000000000 UN
00001⓪000000000 UN
...
```

On peut faire ça comme ça :

état | case | nouvel état | écriture | déplacement
-----|------|-------------|----------|------------
START|   1  |    UN       |     0    |  droite
  UN |   1  |    UN       |     1    |  droite

### Séparation entre entrée et sortie

On arrive au `0` qui doit séparer l'entrée de la sortie. On se décale vers la droite pour se placer en mode écriture.

```
...
00001⓪000000000 UN
000010⓪00000000 DEUX
...
```

Ceci peut se faire en ajoutant autant d'états que nécessaire :

état | case | nouvel état | écriture | déplacement
-----|------|-------------|----------|------------
  UN |   0  |  DEUX       |     0    |  droite

### Écriture de la sortie

On arrive au `0` qui doit être remplacé par deux 1 à la suite.

```
...
00001⓪000000000 UN
000010⓪00000000 DEUX
0000101⓪0000000 TROIS
00001011⓪000000 QUATRE
...
```

On peut faire ça directement avec 1 nouvel état :

état | case | nouvel état | écriture | déplacement
-----|------|-------------|----------|------------
DEUX |   0  |  TROIS      |     1    |  droite  
TROIS|   0  |  QUATRE     |     1    |  droite  

### On remonte la sortie

Il faut maintenant remonter l'entrée :

```
...
00001011⓪000000 QUATRE
0000101①0000000 CINQ
000010①10000000 CINQ
00001⓪110000000 CINQ
...
```

état  | case | nouvel état | écriture | déplacement
------|------|-------------|----------|------------
QUATRE|   0  |  CINQ       |     0    |  gauche  
CINQ  |   1  |  CINQ       |     1    |  gauche  

### On remonte l'entrée

```
...
00001⓪110000000 CINQ
0000①0110000000 SIX
000⓪10110000000 SIX
...
```

état  | case | nouvel état | écriture | déplacement
------|------|-------------|----------|------------
CINQ  |   0  |  SIX        |     0    |  gauche  
SIX   |   1  |  SIX        |     1    |  gauche  

### On recommence à START

On est arrivé juste à gauche de l'entrée, il suffit de se décaler à droite pour tout recommencer.

```
...
000⓪10110000000 SIX
0000①0110000000 START
...
```

état  | case | nouvel état | écriture | déplacement
------|------|-------------|----------|------------
SIX   |   0  |  START      |     0    |  gauche  

La machine va alors recommencer son cycle jusqu'à tomber sur un cas non prévu :

```
...
0000①0110000000 START
00000⓪110000000 UN
000000①10000000 DEUX
...
```

On a écrit des choses en sortie. Il faut donc se décaler jusqu'à obtenir un 0 :

état  | case | nouvel état | écriture | déplacement
------|------|-------------|----------|------------
DEUX  |   1  |  DEUX       |     1    |  droite

Ce qui permet de continuer comme si de rien n'était :

```
000000①10000000 DEUX
0000001①0000000 DEUX
00000011⓪000000 DEUX
000000111⓪00000 TROIS
0000001111⓪0000 QUATRE
000000111①00000 CINQ
00000011①100000 CINQ
0000001①1100000 CINQ
000000①11100000 CINQ
00000⓪111100000 CINQ
0000⓪0111100000 SIX
...
```

### On STOP si on a fini

Il nous reste plus qu'à gérer le stop :

```
...
0000⓪0111100000 START
00000⓪111100000 SEPT
000000①11100000 STOP
```

état  | case | nouvel état | écriture | déplacement
------|------|-------------|----------|------------
START |   0  |  SEPT       |     0    |  droite
SEPT  |   0  |  STOP       |     0    |  droite

## Machine finale

état  | case | nouvel état | écriture | déplacement
------|------|-------------|----------|------------
START |   0  |  SEPT       |     0    |  droite
START |   1  |    UN       |     0    |  droite
  UN  |   0  |  DEUX       |     0    |  droite
  UN  |   1  |    UN       |     1    |  droite
DEUX  |   0  |  TROIS      |     1    |  droite  
DEUX  |   1  |  DEUX       |     1    |  droite
TROIS |   0  |  QUATRE     |     1    |  droite  
QUATRE|   0  |  CINQ       |     0    |  gauche  
CINQ  |   0  |  SIX        |     0    |  gauche  
CINQ  |   1  |  CINQ       |     1    |  gauche  
SIX   |   0  |  START      |     0    |  gauche  
SIX   |   1  |  SIX        |     1    |  gauche  
SEPT  |   0  |  STOP       |     0    |  droite

Et maintenant la machine finale :

{% exercice %}
Écrivez la machine pour qu'elle soit exécutable sur <https://turingmachine.io/> et vérifiez qu'elle fonctionne bien avec 3 batons en entrée.
{% endexercice %}
{% details "solution" %}

> TBD ne marche pas. A changer...

```
blank: 0
start state: START
input: '111'
table:
  START:
    0: {
      write: 0,
      R: DEUX
    }
    1: {
      write: 0,
      R: UN
    }
  UN:
    0: {
      write: 0,
      R: SEPT
    }
    1: {
      write: 1,
      R: UN
    }
  DEUX:
    0: {
      write: 1,
      R: TROIS
    }
    1: {
      write: 1,
      R: DEUX
    }
  TROIS:
    0: {
      write: 1,
      R: QUATRE
    }
  QUATRE:
    0: {
      write: 0,
      L: CINQ
    }
  CINQ:
    0: {
      write: 0,
      L: SIX
    }
    1: {
      write: 1,
      L: CINQ
    }
  SIX:
    0: {
      write: 0,
      L: START
    }
    1: {
      write: 1,
      L: SIX
    }
  SEPT:
    0: {
      write: 0,
      R: STOP
    }

  STOP:
```

{% enddetails %}
