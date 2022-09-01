---
layout: layout/post.njk 

title: git rebase, la tronçonneuse magique
authors: 
    - "Fanis Michalakis"

eleventyNavigation:
  key: "git rebase, la tronçonneuse magique"
  parent: "Git dans les détails"
---

<!-- début résumé -->

Le but de ce tuto est de comprendre pourquoi et comment utiliser `git rebase`.

<!-- fin résumé -->

 Il s'agit d'une version allégée du déjà très digeste [article](https://www.miximum.fr/blog/git-rebase/) de Thibault Jouannic. Une bonne idée pourrait être de commencer par celui-ci, puis de lire le tuto originel pour approfondir.

Sommaire :

[Le pourquoi](./#pourquoi) |
[Le quoi](./#quoi) |
[Cas d'usage](./#usage) |
Récapitulatif des commandes |
[Sources et ressources](./#sources) |

## Pourquoi { #pourquoi }

Pourquoi donc s'embêter à utiliser une commande comme `rebase`, souvent perçue comme obscure, même pour certains vétérans du git, alors qu'il existe quelque chose de simple et de connu comme `git merge` ? Pour deux raisons principales, que nous détaillerons par la suite :

1. En fait, contrairement à ce qu'on peut penser, `git rebase` n'est pas obscure du tout
2. Et c'est même souvent mieux qu'une bonne vieille fusion, pour plein de raisons.

## Quoi { #quoi }

Tout d'abord, que fait exactement la commande `git rebase` ? Elle permet ni plus ni moins de prendre une branche, de la découper, puis de la recoller ailleurs. En général, on veut la recoller au bout de la branche `main`, avec la commande suivante :

```shell
git rebase master <ma branche>
```

Mais pourquoi donc s'embêter à faire ça ? Voyons sur un petit exemple : j'ai créée une branche `ma branche` à partir de `main`, et je souhaite maintenait amener les modifications effectuées dans `ma branche` sur `main`.

```shell
A---B---C---D ← main
     \
      E---F---G ← ma branche
```

Il y a en gros deux écoles qui s'affrontent dans un combat titanesque : merge vs rebase.

Les partisans du *merge* vont se contenter de fusionner `ma branche` dans `main` à l'aide de la commande :

```shell
git merge <ma branche>
```

Ce qui donne graphiquement quelque chose comme ça :

```shell
A---B---C---D---H ← main
     \         /
      E---F---G ← ma branche
```

De leur côté, les défenseurs du rebase préconisent d'agir en deux temps :

1. On découpe la branche `ma branche` là où elle est reliée à `main` (en B) et on la recolle à la fin (en H)
2. Ensuite, on peut "merger" de façon triviale `ma branche` dans `main`.

Graphiquement, le rebase donne ceci :

```shell
A---B---C---D ← main
             \
              E---F---G ← ma branche
```

Et à l'issue de la fusion :

```shell
A---B---C---D---E---F---G ← main
                         \
                          ma branche
```

On peut ensuite supprimer `ma branche`, devenue inutile, en utilisant :

```shell
git branch -d ma branche
```

On obtient donc un historique linéaire, clair, là où auparavant on aurait eu des diverticules :

```shell
A---B---C---D---E---F---G ← main
```

## Usage

Tout cela est bien joli, mais à quoi est-ce que ça sert de découper une branche pour la recoller à la fin avant de fusionner sur `main` ? Cela peut en effet sembler être une perte de temps, dans la mesure où les problèmes (notamment les conflits) qui se déclarent habituellement lors d'un merge se déclareront lors du rebase. Petit panorama de l'utilité du rebase.

### Un historique propre

En découpant les branches pour les recoller plus loin, `git rebase` permet de conserver un historique de modification plus clair, qu'on décide ensuite de fusionner la branche fille à `main` ou non.

On peut ainsi décider de fusionner une branche peu importante, comme une simple correction de bug par exemple, sans que celle-ci n'apparaisse comme une excroissance de la branche principale. Pour se faire, on commence par re-baser la branche de correction de bug (appelée *bug*) sur `main`, puis on merge, et enfin on supprime la branche :

```shell
git rebase master bug
git checkout master
git merge bug
git branch -d bug
```

Cela nous permet d'obtenir un bel historique bien plat au lieu de quelque chose de plus alambiqué et qui, à la longue, les corrections de bug se succédant, risque d'alourdir inutilement l'arbre de l'historique de version.

On pourrait aussi vouloir, pour certaines raisons, conserver dans l'historique la trace de branches passées et de leur existence. Autrement dit, on peut désirer qu'il soit visible que tel ou tel développement a été effectué sur une branche bien précise, avant d'être fusionné dans la branche principale. Dans ce cas, l'utilisation de `rebase` permet tout de même un historique plus clair (un arbre moins touffu), en particulier lorsque plusieurs branches existent en parallèle.

Imaginons que j'ai deux fonctionnalités, 1 et 2, qui évoluent en parallèle, chacune sur sa branche dérivée de `main`.

```shell
          F---G ← fonctionnalité 2
         /
A---B---E---H---I ← main
     \
      C---D ← fonctionnalité 1
```

L'une des deux fonctionnalités va être achevée (disons la 2), après tests je la merge dans master. Puis, vient le tour de la fonctionnalité 1. Ce qui donne quelque chose comme ça :

```shell
          F---G ← fonctionnalité 2
         /     \
A---B---E---H---I---L ← main
     \             / 
      C---D---J---K ← fonctionnalité 1
```

On a donc deux branches qui s'échappent du tronc et, visuellement, ça peut déjà sembler un peu brouillon. On va donc astucieusement utiliser rebase pour que, à la fin, les branches filles se succèdent les unes après les autres plutôt que se superposer :

```shell
A---B---E---H-------I---------------L ← main
             \     / \             / 
              F---G   C---D---J---K 
```

On conserve donc bien l'historique en branches, mais avec beaucoup plus de clarté. Pour se faire, on va à chaque fois se re-baser sur `main` avant de fusionner, comme on le faisait avant. Mais en plus, on va utiliser l'option de merge "no fast forward" (`--no-ff`) pour que git conserve la trace des branches dans l'historique :

```shell
git rebase master fonctionnalité1
git checkout master
git merge fonctionnalité1 --no-ff
git branch -d fonctionnalité1
git rebase master fonctionnalité2
git checkout master
git merge fonctionnalité2 --no-ff
git branch -d fonctionnalité2
```

### Corriger des erreurs

Git rebase permet également de réparer certaines boulettes, particulièrement celles que l'on a tendance à commettre tôt le matin ou tard le soir. L'une d'elles consiste par exemple à créer une nouvelle branche à partir d'une branche fille plutôt qu'à partir de master :

```shell
A---B---H---I ← main
     \
      C---D---G ← bug1
       \
        E---F ← bug2
```

Sans rebase, il faudrait donc d'abord terminer `bug2` et le fusionner dans `bug1`, avant de pouvoir espérer fusionner `bug1` (et donc `bug2`) dans master. Pas pratique du tout ! On va donc pouvoir utiliser rebase pour découper la petite brindille `bug2` pour la coller au bout de master. Ainsi, on peut maintenant traiter les branches et les fusionner dans l'ordre le plus opportun. L'option `--onto` nous permet même de spécifier l'endroit de `main` où l'on souhaite coller `bug2`.

```shell
git rebase bug1 bug2 --onto B
```

```shell
      E---F ← bug2
     /
A---B---H---I ← production
     \
      C---D---G ← bug1
```

Où B, pour rappel, est l'étiquette d'un commit (`e73f3d6` par exemple).

### Diviser pour mieux régner

Parfois, on peut se traîner pendant de longues semaines la branche d'une fonctionnalité particulièrement longue à développer. Pendant ce temps, la branche `main` a le temps de connaître de nombreuses évolutions, et on risque donc de passer toute une demi-journée à résoudre des conflits lors de la fusion de notre branche avec `main`. Sauf si ...

```shell
A---B---H---I--- … ---J---E---F ← main
      \
       C---D---G--- … ---H---I ← longue_fonctionnalite
```

Sauf si on a pris le temps, tous les matins par exemple, de re-baser notre branche sur `main` pour prendre en compte les dernières modifications et corriger régulièrement les conflits, plutôt que tous à la fois à la fin.

Après, il y a peut-être deux écoles, comme entre ceux qui préfèrent faire la vaisselle après chaque repas, et ceux qui donnent un bon coup à la fin de la semaine.

### Le jardinage de commits (rebase interactif)

Le rebase interactif (`git rebase -i`) est très utile dans le cadre de l'utilisation de commits atomiques, afin de réorganiser l'historique et de fusionner plusieurs commits entre eux. Pour plus de détails, voir le tuto détaillé sur les commits atomiques.

## Bibliographie

* Ce superbe [tuto](https://www.miximum.fr/blog/git-rebase/) réalisé par Thibault Jouannic, et sur lequel se base une bonne partie du présent tuto.
* <https://stackoverflow.com/questions/21364636/git-pull-rebase-preserve-merges> qui montre l'utilité de `git --rebase=merges` qui préserve les merges locaux s'il y en a.
