---
layout: page
title:  "git : les commandes"
category: tutorial
tags: dev git 
---

## But

Les indispensables à connaître. Ce tuto comporte deux sections :
1. La section [Comment faire ...](#comment-faire-) qui donne la marche à suivre pour les opérations courantes,
2. La section [Cheatsheet](#cheatsheet), un tableau récapitulant les commandes les plus utiles et leurs variations (notamment les options qu'il est important de connaître).

L'idée est donc de pouvoir utiliser ce tuto de deux façons : soit avec une idée de ce qu'on veut faire, obtenir les différentes commandes à utiliser ; soit pour se rafraichir la mémoire sur une commande bien précise.


## Comment faire ...

### Initialiser un nouveau projet

**Description :** on va créer en local notre nouveau projet, créer un répertoire sur GitHub et lier les deux.

1. Création du répertoire sur Github
2. Création du répertoire en local
3. Initialisation de git
4. La liaison (pas dangereuse)

**Commandes :**

1. Pour cette première étape, on peut soit opérer depuis un [navigateur](https://github.com), soit en ligne de commande avec [GitHub CLI](https://cli.github.com/).

2. 
~~~ shell
cd <là où on veut mettre le dossier>
mkdir <monprojet>
~~~

3. 
~~~ shell
cd <monprojet>
git init
~~~

4. 
~~~ shell
git remote add origin https://github.com/USER/monprojet.git
~~~

### Récupérer (cloner) en local un projet existant

**Description :** on souhaite travailler sur un projet donc le code est disponible sur Github (ou équivalent). Pour ce faire, on va cloner le répertoire en local sur sa machine.

**Commandes :**

~~~ shell
git clone <url>
~~~

### Récupérer en local les modifications effectuées sur le répertoire distant

**Description :** Sur un projet informatique, il arrive souvent que plusieurs développeurs travaillent de concert (c'est d'ailleurs toute l'utilité d'un logiciel tel que git). Afin de rester syncrhonisé avec le travail des collègues, on est régulièrement amené à télécharger depuis le serveur commun les apports qu'ils y ont déposé.

**Commandes :**

Depuis la racine du projet (là où se trouve le dossier .git) :

~~~ shell
git pull
~~~

En général, l'url peut être trouvée sous le menu "Code" ou "Clone" sur la page principale d'un projet.

### Créer une nouvelle branche

**Description :** pour travailler sur un aspect particulier, qu'il s'agisse d'une résolution de bug ou de l'élaboration d'une nouvelle fonctionnalité, on veut créer une nouvelle branche. Cette nouvelle branche va dériver d'une branche-mère (en général, il s'agit de la branche *master*, aussi appelée *main*, et ce sera aussi le cas dans notre exemple).

**Commandes :**

~~~ shell
git checkout master
git branch ma_nouvelle_branche
git checkout ma_nouvelle_branche
~~~

Ou sous une forme plus condensée :

~~~ shell
git checkout master
git checkout -b ma_nouvelle_branche
~~~

L'option `-b` appliquée à la commande `checkout` permet en effet de créer la branche de destination si celle-ci n'existe pas.

### Pousser une branche (nouvelle) locale sur le serveur distant

**Description :** on a créé en local une nouvelle branche, qui n'existe pas encore sur le serveur distant. On souhaite créer la branche du même nom sur le serveur distant et pousser nos modifications dessus.

**Commandes :**

~~~ shell
git checkout <branche>
git push --set-upstream origin <branche>
~~~

Version condensée :

~~~ shell
git checkout <branche>
git push -u origin <branche>
~~~

### Pousser ses modifications sur le serveur

**Description :** on veut "enregistrer" les modifications apportées au code et les partager avec ses collaborateurs en les poussant sur le serveur. On peut décomposer la marche à suivre en deux grandes étapes :
1. On ajoute localement ses modifications à l'historique git, suivant la fréquence qui nous convient le mieux
2. On pousse tout ça sur le serveur.

La fréquence d'ajout des modifications au git est variable suivant les développeurs. Certains aiment faire un gros ajout (*commit*) une fois de temps en temps, quand d'autres sont partisans de *commits* dits atomiques (pour chaque modification), quitte à retravailler ensuite l'historique ensuite pour le rendre plus concis si besoin.

Concernant la fréquence d'envoi sur le serveur (*push*), la seule règle vraiment importante est de bien avoir en tête que, tant que du code n'est pas poussé, il n'existe que sur votre ordinateur. Et si celui-ci est endommagé ou perdu ... Un *push* régulier est donc gage d'esprit léger !

**Commandes :** 

1. L'ajout des modifications au git se fait en plusieurs étapes : on ajoute d'abord les modifications qui nous intéressent au *stage*, puis on les *commit*. On peut voir le *stage* comme une sorte de bassine où l'on dépose tous les fichiers que l'on veut sauver.

En général, on a pris soin de placer les fichiers qu'on ne veut de toute façon pas voir dans git dans le fichier .gitignore. Donc, souvent, on va vouloir tout ajouter dans le stage pour tout commit :

~~~ shell
git add .
git commit -am "mon_message_decrivant_le_commit"
~~~

Si l'on souhaite *commit* seulement un fichier (ou un groupe de fichiers) :

~~~ shell
git add fichier1.md fichier2.html
git commit -am "mon_message_de_commit"
~~~

*Note :* `git status`est très utile pour voir ce qui est dans le *stage* et ce qui n'y est pas encore. Abusez-en !

2. Une fois qu'on a *commit* nos changements, que tout est testé (mais c'est un autre sujet), etc., on va pouvoir pousser notre code sur le serveur. Rien de plus simple :

~~~ shell
git push
~~~

Si la branche sur laquelle on travaille existe aussi sur le serveur et que les deux branches sont liées, tout devrait bien se passer. Sinon, c'est qu'on a mal fait [ça](#pousser-une-branche-nouvelle-locale-sur-le-serveur-distant).

### Fusionner une branche

**Description :** on souhaite fusionner une branche dans sa branche d'origine (par exemple *master*), c'est-à-dire appliquer toutes les modifications portées par une branche dans sa branche d'origine.

Nous proposons ici une méthode consistant à utiliser `git rebase` conjointement à `git merge` pour obtenir un historique plus "propre" (i.e. plus linéaire). Pour plus détails, voir le tuto sur [git rebase]({% link cours/dfs/git_rebase.md %}).

**Commandes :**

Pour ne garder aucune trace de la branche (et obtenir ainsi un historique complètement linéaire, plat) :

~~~ shell
git rebase master branche
git checkout master
git merge branche
git branch -d branche
~~~

Pour conserver une trace de la branche (par exemple parce qu'elle est significante) mais conserver une certaines linéarité (dans l'enchaînement des branches notamment) :

~~~ shell
git rebase master branche
git checkout master
git merge branche --no-ff
git branch -d branche
~~~

## Cheatsheet

Par ordre alphabétique ;)

Commande | Effet | Option(s) |
--- | --- | --- | --- 
`git add <fichier>` | ajoute des fichiers au stage en vue de les commit | `git add .` pour ajouter tous les fichiers modifiés
`git branch` | affiche les branches existantes (en local, par défaut). La branche actuelle est mise en évidence par un astérisque | `-d <branche>` supprime la branche *branche* |
`git checkout <branche>` | change de branche pour aller sur "branche" | `-b <nouvelle branche>` pour créer une nouvelle branche et s'y placer |
`git clone <url>` | clone en local un répertoire distant |  |
`git commit` | publie les changements dans l'arbre git local | `-a` commit tous les changements présents dans le stage <br> `-m "mon_message"` permet d'écrire le message de commit sans passer par l'éditeur |
`git diff` | indique les différences entre le dernier commit et ce qui n'est pas encore mis dans le *stage* |  |
`git init` | initialise git pour le dossier où la commande est lancée |  |
`git log` | affiche l'historique git complet du projet | `--oneline` affiche les commits sous forme condensée pour plus de lisibilité <br> `--graph` représentation visuelle de l'arbre (avec les branches éventuelles) |
`git merge <branche>` | applique les modifications portées par "<branche>" à la branche mère dont elle est issue | `--no-ff` (*no fast forward*) permer de créer un commit de fusion dans tous les cas, même cas quand la fusion pourrait être résolue trivialement (*fast-forward*). Utile pour conserver l'historique des branches lors d'un *merge* suivant un *rebase* |
`git pull` | télécharge en local les modifications présentes sur le serveur (*a priori* ajoutées par d'autres développeurs) | `--rebase=preverse` permet de conserver les commits de fusion, utile pour garder une trace de l'existence de certaines branches |
`git push` | pousse sur le serveur les modifications locales |  |
`git rebase <ici> <branche>` | découpe la branche `branche` à sa base et la recolle `ici`. `ici` peut-être le nom d'une branche, auquel cas la branche `branche` est recollée à la fin de la branche `ici`, ou un numéro de commtit. Voir le tuto complet sur rebase ici. | X |
`git stash` | permet de mettre temporairement de côté les modifications en attente de *commit* afin de revenir au dernier *commit*. Les modifications ainsi mises de côté peuvent ensuite être réappliqués (éventuellement après que d'autres commits ont été effectués) ou supprimées. | `git stash list` pour lister les éléments mis de côté <br> `git stash apply` pour faire revenir les modifcations dans l'espace de travail <br> `git stash clear` pour abandonner complètemet les modifications mises de côté |
`git status` | affiche les fichiers prêts à être *commit* et ceux qui ne sont pas encore dans le *stage* |  |


## Sources et ressources

