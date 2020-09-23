---
layout: page
title:  "git rebase, la tronçonneuse magique"
category: tutorial
tags: dev git 
authors: "Fanis Michalakis"
---

# But

Le but de ce tuto est de comprendre pourquoi et comment utiliser `git rebase`.

Sommaire :

[Le pourquoi](#pourquoi) |
[Le quoi](#quoi) |
[Cas d'usage](#usage) |
Récapitulatif des commandes |
[Sources et ressources](#sources) |

# Pourquoi

Pourquoi donc s'embêter à utiliser une commande comme `rebase`, souvent perçue comme obscure, même pour certains vétérans du git, alors qu'il existe quelque chose de simple et de connu comme `git merge` ? Pour deux raisons principales, que nous détaillerons par la suite :

1. En fait, contrairement à ce qu'on peut penser, `git rebase` n'est pas obscure du tout
2. Et c'est même souvent mieux qu'une bonne vieille fusion, pour plein de raisons.

# Quoi

Tout d'abord, que fait exactement la commande `git rebase` ? Elle permet ni plus ni moins de prendre une branche, de la découper, puis de la recoller ailleurs. En général, on veut la recoller au bout de la branche *master*, avec la commande suivante :

~~~ shell
git rebase master mabranche
~~~

Mais pourquoi donc s'embêter à faire ça ? Voyons sur un petit exemple : j'ai créée une branche *mabranche* à partir de *master*, et je souhaite maintenait amener les modifications effectuées dans *mabranche* sur *master*.

~~~ shell
A---B---C---D ← master
     \
      E---F---G ← mabranche
~~~

Il y a en gros deux écoles qui s'affrontent dans un combat titanesque : merge vs rebase.

Les partisans du *merge* vont se contenter de fusionner *mabranche* dans *master* à l'aide de la commande :

~~~shel
git merge mabranche
~~~

Ce qui donne graphiquement quelque chose comme ça :

~~~shell
A---B---C---D---H ← master
     \         /
      E---F---G ← mabranche
~~~

De leur côté, les défenseurs du rebase préconisent d'agir en deux temps :
1. On découpe la branche *mabranche* là où elle est reliée à *master* (en B) et on la recolle à la fin (en H)
2. Ensuite, on peut "merger" de façon triviale *mabranche* dans *master*.

Graphiquement, le rebase donne ceci :

~~~shell
A---B---C---D ← master
             \
              E---F---G ← mabranche
~~~

Et à l'issue de la fusion :

~~~shell
A---B---C---D---E---F---G ← master
                         \
                          mabranche
~~~

On peut ensuite supprimer *mabranche*, devenue inutile, en utilisant :

~~~shell
git branch -d mabranche
~~~

On obtient donc un historique linéaire, clair, là où auparavant on aurait eu des diverticules :

~~~shell
A---B---C---D---E---F---G ← master
~~~

# Usage

Tout cela est bien joli, mais à quoi est-ce que ça sert de découper une branche pour la recoller à la fin avant de fusionner sur *master* ? Cela peut en effet sembler être une perte de temps, dans la mesure où les problèmes (notamment les conflits) qui se déclarent habituellement lors d'un merge se déclareront lors du rebase. Petit panorama de l'utilité du rebase.

## Un historique propre

## Corriger des erreurs

## Diviser pour mieux régner

## Le rebase interactif

# Sources

- Ce superbe [tuto](https://www.miximum.fr/blog/git-rebase/) réalisé par Thibault Jouannic, et sur lequel se base une bonne partie du présent tuto.