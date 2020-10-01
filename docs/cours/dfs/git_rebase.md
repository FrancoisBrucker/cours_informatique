---
layout: page
title:  "git rebase, la tronçonneuse magique"
category: tutorial
tags: dev git 
authors: "Fanis Michalakis"
---

## But

Le but de ce tuto est de comprendre pourquoi et comment utiliser `git rebase`. Il s'agit d'une version allégée du déjà très digeste [article](https://www.miximum.fr/blog/git-rebase/) de Thibault Jouannic. Une bonne idée pourrait être de commencer par celui-ci, puis de lire le tuto originel pour approfondir.

Sommaire :

[Le pourquoi](#pourquoi) |
[Le quoi](#quoi) |
[Cas d'usage](#usage) |
Récapitulatif des commandes |
[Sources et ressources](#sources) |

## Pourquoi

Pourquoi donc s'embêter à utiliser une commande comme `rebase`, souvent perçue comme obscure, même pour certains vétérans du git, alors qu'il existe quelque chose de simple et de connu comme `git merge` ? Pour deux raisons principales, que nous détaillerons par la suite :

1. En fait, contrairement à ce qu'on peut penser, `git rebase` n'est pas obscure du tout
2. Et c'est même souvent mieux qu'une bonne vieille fusion, pour plein de raisons.

## Quoi

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

## Usage

Tout cela est bien joli, mais à quoi est-ce que ça sert de découper une branche pour la recoller à la fin avant de fusionner sur *master* ? Cela peut en effet sembler être une perte de temps, dans la mesure où les problèmes (notamment les conflits) qui se déclarent habituellement lors d'un merge se déclareront lors du rebase. Petit panorama de l'utilité du rebase.

### Un historique propre

En découpant les branches pour les recoller plus loin, `git rebase` permet de conserver un historique de modification plus clair, qu'on décide ensuite de fusionner la branche fille à *master* ou non.

On peut ainsi décider de fusionner une branche peu importante, comme une simple correction de bug par exemple, sans que celle-ci n'apparaisse comme une excroissance de la branche principale. Pour se faire, on commence par rebaser la branche de correction de bug (appelée *bug*) sur *master*, puis on merge, et enfin on supprime la branche :

~~~ shell
git rebase master bug
git checkout master
git merge bug
git branch -d bug
~~~

Cela nous permet d'obtenir un bel historique bien plat au lieu de quelque chose de plus alambiqué et qui, à la longue, les corrections de bug se succédant, risque d'alourdir inutilement l'arbre de l'historique de version.

On pourrait aussi vouloir, pour certaines raisons, conserver dans l'historique la trace de branches passées et de leur existence. Autrement dit, on peut désirer qu'il soit visible que tel ou tel développement a été effectué sur une branche bien précise, avant d'être fusionné dans la branche principale. Dans ce cas, l'utilisation de `rebase` permet tout de même un historique plus clair (un arbre moins touffu), en particulier lorsque plusieures branches existent en parallèle.

Imaginons que j'ai deux fonctionnalités, 1 et 2, qui évoluent en parallèle, chacune sur sa branche dérivée de *master*.

~~~ shell
          F---G ← fonctionnalité 2
         /
A---B---E---H---I ← master
     \
      C---D ← fonctionnalité 1
~~~

L'une des deux fonctionnalités va être achévée (disons la 2), après tests je la merge dans master. Puis, vient le tour de la fonctionnalité 1. Ce qui donne quelque chose comme ça :

~~~ shell
          F---G ← fonctionnalité 2
         /     \
A---B---E---H---I---L ← master
     \             / 
      C---D---J---K ← fonctionnalité 1
~~~

On a donc deux branches qui s'échappent du tronc et, visuellement, ça peut déjà sembler un peu brouillon. On va donc astucieusement utiliser rebase pour que, à la fin, les branches filles se succèdent les unes après les autres plutôt que se superposer :

~~~ shell
A---B---E---H-------I---------------L ← master
             \     / \             / 
              F---G   C---D---J---K 
~~~

On conserve donc bien l'historique en branches, mais avec beaucoup plus de clarté. Pour se faire, on va à chaque fois se rebaser sur *master* avant de fusionner, comme on le faisait avant. Mais en plus, on va utiliser l'option de merge "no fast forward" (`--no-ff`) pour que git conserve la trace des branches dans l'historique :

~~~ shell
git rebase master fonctionnalite1
git checkout master
git merge fonctionnalite1 --no-ff
git branch -d fonctionnalite1
git rebase master fonctionnalite2
git checkout master
git merge fonctionnalite2 --no-ff
git branch -d fonctionnalite2
~~~

### Corriger des erreurs

Git rebase permet également de réparer certaines boulettes, particulièrement celles que l'on a tendance à commettre tôt le matin ou tard le soir. L'une d'elles consiste par exemple à créer une nouvelle branche à partir d'une branche fille plutôt qu'à partir de master :

~~~ shell
A---B---H---I ← master
     \
      C---D---G ← bug1
       \
        E---F ← bug2
~~~

Sans rebase, il faudrait donc d'abord terminer bug2 et le fusionner dans bug1, avant de pouvoir espérer fusionner bug1 (et donc bug2) dans master. Pas pratique du tout ! On va donc pouvoir utiliser rebase pour découper la petite brindille bug2 pour la coller au bout de master. Ainsi, on peut maintenant traiter les branches et les fusionner dans l'ordre le plus opportun. L'option `--onto` nous permet même de spécifier l'endroit de *master* où l'on souhaite coller *bug2*.

~~~ shell
git rebase bug1 bug2 --onto B
~~~

~~~ shell
      E---F ← bug2
     /
A---B---H---I ← production
     \
      C---D---G ← bug1
~~~

Où B, pour rappel, est l'étiquette d'un commit (`e73f3d6` par exemple).

### Diviser pour mieux régner

Parfois, on peut se traîner pendant de longues semaines la branche d'une fonctionnalité particulièrement longue à développer. Pendant ce temps, la branche *master* a le temps de connaître de nombreuses évolutions, et on risque donc de passer toute une demi-journée à résoudre des conflits lors de la fusion de notre branche avec *master*. Sauf si ...

~~~ shell
A---B---H---I--- … ---J---E---F ← master
      \
       C---D---G--- … ---H---I ← longue_fonctionnalite
~~~

Sauf si on a pris le temps, tous les matins par exemple, de rebaser notre branche sur *master* pour prendre en compte les dernières modifications et corriger régulièrement les conflits, plutôt que tous à la fois à la fin.

Après, il y a peut-être deux écoles, comme entre ceux qui préfèrent faire la vaisselle après chaque repas, et ceux qui donnent un bon coup à la fin de la semaine.

### Le jardinage de commits (rebase interactif)

sd

TODO once the commits atomiques tuto is finished and we know what is useful here.

## Sources

- Ce superbe [tuto](https://www.miximum.fr/blog/git-rebase/) réalisé par Thibault Jouannic, et sur lequel se base une bonne partie du présent tuto.