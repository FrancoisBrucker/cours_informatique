---
layout: page
title: "usage de github"
category: tutorial
tags: dev git
author: "François Brucker"
---

[github](https://github.com/) est un endroit où l'on peut stocker ses projets. Ces projets seront identiques aux projets que vous avez sur votre machine (un projet git contient tout le temps tout l'historique de celui-ci) mais leurs état sera la référence pour tous les contributeur du projet. On appelle cet endroit _origin_.

> A priori rien de différentie ce repository d'un autre, juste une convention qui déscide qu'un des repository d'un projet sera l'origin.

Vous pouvez très bien monitorer vos projet uniquement avec github et son [application desktop](https://desktop.github.com/) sans connaitre grand chose de git.

## Initalisation d'un projet

Il y a deux façon d'initialiser un projet sur github :

- le projet existe déjà sur github et je le _clone_ chez moi : [la doc github pour le cloning](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
- le projet existe en dehors de github et je veux le mettre sur github : [la doc d'import d'un projet dans github](https://docs.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line)
  origin

### clone : le projet exsite sur github

Vous allez cloner le projet du cours qui est là : <https://github.com/FrancoisBrucker/cours_informatique>.

On va le cloner de deux façons différentes, dont les usages vont être différent. Dans le premier, on utilisera l'application pour gérer nos fichier entre notre ordinateur et github, dans le second on utilsiera la ligne de commande et les clés ssh (usage plus avancé).

#### avec l'application desktop

Dans menu code, choisissez _Open with Github Desktop_ :

![usage github]({{ "/assets/cours/git/github-desktop-clone.png" | relative_url }}){:style="margin: auto;display: block}

Puis laisez vous guider.

Un dossier _"cours_informatique"_ a été créé. Regardez le fichier _.git/config_ de ce projet :

```text
[core]
  repositoryformatversion = 0
  filemode = true
  bare = false
  logallrefupdates = true
  ignorecase = true
  precomposeunicode = true
[submodule]
  active = .
[remote "origin"]
  url = https://github.com/FrancoisBrucker/cours_informatique.git
  fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
  remote = origin
  merge = refs/heads/master
```

Deux entrées permettent de lier github à votre projet :

- "origin" : qui est le dépôt origin de notre projet maintenant, sur [github](https://github.com/).
- "master" qui est la branche principale sur le projet origin.

> La méthode de récupération et de fusion sur le serveur remote origin utilise le protocole https.
> {: .attention}

#### avec un terminal

1. placez vous dans le dossier parent où vous voulez que votre projet soit
2. `git clone git@github.com:FrancoisBrucker/cours_informatique.git`

> vous puvez aussi trouver la ligne à cloner en choissant SSH dans le menu sous code (voir figure précédente)

Un dossier _"cours_informatique"_ a été créé. Regardez le fichier _.git/config_ de ce projet :

```text
[core]
  repositoryformatversion = 0
  filemode = true
  bare = false
  logallrefupdates = true
  ignorecase = true
  precomposeunicode = true
[remote "origin"]
  url = git@github.com:FrancoisBrucker/cours_informatique.git
  fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
  remote = origin
  merge = refs/heads/master
```

Deux entrées permettent de lier github à votre projet :

- "origin" : qui est le dépôt origin de notre projet maintenant, sur [github](https://github.com/).
- "master" qui est la branche principale sur le projet origin.

> La methode de récupération et de fusion sur le serveur remote origin utilise le protocole ssh (`git@github.com`).
> {: .attention}

### ajout d'un projet existant à github

Ajoutons un projet web à github :

1. créez un _repository_ sur github
2. on va ajouter à la main l'origin et le master dans le projet sur notre ordinateur. Pour moi, avec _my_test_project_ comme nom de projet ça donne (il suffit de copier/coller ce que nous donne github après la création du projet) :
   - `git remote add origin git@github.com:FrancoisBrucker/my_test_project.git`
   - on se place dans la branche de notre projet qui va être le master et on tape `git branch -M master` si elle ne s'appelle pas encore master.
3. on pousse tout notre projet sur github : `git push --set-upstream origin master`. Cette commande pousser tou notre projet sur github et place le master de l'origin par défaut. Il suffira ensuite de taper `git push` pour que ce soit équivalent à `git push origin master`.

## récupérer les données du serveur origin

On utilise la commande `git pull --rebase=merges origin master` pour récupérer la branche `master` sur le serveur `origin`.

> Si on a définit une branche par défaut on peut juste taper : `git pull --rebase=merges`, et si on a défini une méthode de fusion (comme dit dans la configuration), `git pull` suffit.

Pour que cette commande fonctionne il faut que l'`origin` soit plus loin en commit que vous et que n'ayez pas fait de modification par rapport son histoire (vous devez juste être en retard, pas autre part)

> N'oubliez pas `--rebase=merges`. En effet, `git pull` fera un merge par défaut, brisant la jolie linéarité de l'historique. Il faut, comme pour la synchronisation des branche faire un rebase. Je vous conseille la lecture de [cet article](https://delicious-insights.com/fr/articles/bien-utiliser-git-merge-et-rebase/) qui explique bien comment faire. L'article vous demande d'utiliser `--rebase=preserve` comme option mais cette commande est obsolète et remplacée par `--rebase-merges`qui fonctionne de la même manière.
> {: .attention}

Si vous avez suivi [nos conseils de configuration]({% link cours/git_et_github/index.md %}#configuration-git), on a fixé le comportement par défaut de `git pull` correctement, vous pouvez donc même taper uniquement `gt pull` et tout se fera correctement.

## envoyer ses données à l'origin

Pour envoyer ses données à l'origin il faut que vous soyez en avance sur lui. Donc que l'origin se trouve à un endroit du passé de votre historique. Il doit être en retard par rapport à vous, pas autre part.

Il y a alors deux façons de faire, que l'on soit un contributeur authentifié du projet (on utilise alors push sur la branche comme on le ferait en local) ou pas (on fait un push mais il faut demander la permission au propriétaire du projet de la publier. C'est ce que l'on appelle un _pull-request_)

### push

Si une _origin_ de notre projet est déterminée, `git push` envoie les derniers commits sur celle-ci.

### pull request

Si l'on a cloné un projet et que l'on est pas un de ses contributeur mais que l'on aimerait tout de même contribuer (comme vous devrez/pouvez le faire pour ce cours), vous pouvez faire une [pull request](http://thelia-school.com/faire-une-pull-request-sur-un-projet-thelia/faire-une-pull-request.html), c'est à dire envoyez vos modification au responsable du projet pour qu'il l'intègre s'il le veut au projet.

## synchronisation

Si l'origin et votre dossier local n'est pas synchronisé, il faut faire un rebase comme pour les branches pour la synchronisation puisse se faire.

## pour aller plus loin

Pour participer à un repo github/gitlab il y a quelques uses et coutûmes à respecter afin de permettre au mieux la relecture, l'ajout de fonctionnalités et la compréhension de chacun.
On en parle ici -> [github_bonnes_pratiques]({% link cours/git_et_github/github_gitlab_bonnes_pratiques.md %})
