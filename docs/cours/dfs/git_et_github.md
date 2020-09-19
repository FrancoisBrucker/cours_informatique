---
layout: page
title:  "git et github"
category: tutorial
tags: dev git 
---

# But

Base de l'utilisation de git et de github comme *origin*.

Git est le logiciel de [gestion de versions](https://fr.wikipedia.org/wiki/Gestion_de_versions) actuel et [github)[https://github.com/] un moyen pratique de stocker et diffuser ses projets en utilisant git.

On va vous montrer ici comment utiliser les deux de concert. 

Ce n'est pas un cours avancé de git/github, mais il devrait vous permettre de vous en sortir et d'utiliser correctement ces deux outils complémentaires.

  - gestion de l'origin comme source. Dire que c'est une convention
  - origin -> changement dans la config.
  - rebase on pull
  - faire un merge qui merde
  - les branches (un peu)
  - revenir à une version précédente
  - diff outil pour le merge
  - dire que l'on commite souvent et une fois par jour à l'origin
  - github clé ssh
  -github organisation ?
  - si diff sur pas le même fichier ok. mais faut pas se force à le faire. Il y a le merge au pire.
  - .gitignore : toujours avoir un status propre à la fin d'un commit. Pas de truc "à la con"

# initialisation 

Commencer par installer `git` si ce n'est pas encore fait et créez vous un compte sur [github](https://github.com/). Ce compte github sera utilisé pour tout le cours et vous pourrez  placer vos projet personnels montrable à vos futurs employeurs. Donc utilisez une adresse mail de contact ainsi qu'une photo de profil et un nom présentable. 

## Configuration minimale git

Vous allez travailler sur vos projets git à plusieurs. Il faut pouvoir à tout moment savoir qui a fait quoi sur le projet. Il est donc impératif que vos données personnelles soient à jour.

Renseigner ces infos de façon globale pour tout projet (vous pourrez changer ces infos pour chaque projet, mais mettez des infos corrects par défaut) :

~~~ shell
git config --global user.name "Your name here"
git config --global user.email "your_email@example.com"
~~~

On va mettre vim comme éditeur par défaut pour renseigner les commit :

~~~ shell
git config --global core.editor vim
~~~

> **Nota Bene :** Vous n'utiliserez que très peu l'éditeur par défaut une fois que vous ferez vos commit avec l'option `-m`

On met de la couleur dans le terminal par défaut : 

~~~ shell
git config --global core.editor vim
~~~

> **Nota Bene :** 
> Vous pouvez mette votre [éditeur favori](https://docs.github.com/en/github/using-git/associating-text-editors-with-git) bien sur, mais `vim` sera toujours présent quelque soit l'endroit où au aurez besoin de faire un commit (genre un serveur distant). Il est donc bien d'avoir quelque notions de vim et de les utiliser de temps en temps, d'où cette configuration.

Pour éviter d'avoir un pager lors des `git log` :
~~~ shell
git config --global pager.log false
~~~

## config minimale github

[Ajouter votre clé publique dans github](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account) pour pouvoir y accéder sans mot de passe.

Vous pourrez donner votre clé publique pour être ajouté comme contributeur d'un projet. C'est un moyen pratique de gérer les personnes d'un projet.

# Un projet tuto

## But 

Utilisation courante de git/github grâce à un petit projet web. On suppose que vous avez fait la partie concernant l'initialisation de git et de github.

## création du projet git

Munissez vous d'un terminal et placez vous dans un dossier vierge :

~~~ shell
mkdir mon_projet_web
cd mon_projet_web 
~~~

On peut maintenant initialiser un projet git :

~~~ shell
git init
~~~

## le dossier *.git*

> [**Dans la doc**](https://git-scm.com/book/fr/v2/Les-tripes-de-Git-Plomberie-et-porcelaine) 


La commande précédente a initialisé `git` en créant un dossier caché *.git*. Git ne fonctionne que comme ça, tout est mis dans ce dossier. Chez moi, il ressemble à ça (j'ai utilisé la commande `tree -a` pour afficher l'arborescence et les fichiers cachés) :


~~~ shell
.
└── .git
    ├── HEAD
    ├── config
    ├── description
    ├── hooks
    │   ├── applypatch-msg.sample
    │   ├── commit-msg.sample
    │   ├── fsmonitor-watchman.sample
    │   ├── post-update.sample
    │   ├── pre-applypatch.sample
    │   ├── pre-commit.sample
    │   ├── pre-merge-commit.sample
    │   ├── pre-push.sample
    │   ├── pre-rebase.sample
    │   ├── pre-receive.sample
    │   ├── prepare-commit-msg.sample
    │   └── update.sample
    ├── info
    │   └── exclude
    ├── objects
    │   ├── info
    │   └── pack
    └── refs
        ├── heads
        └── tags

9 directories, 16 files

~~~

Le fichier de configuration est également décrit [dans ce post](https://www.daolf.com/posts/git-series-part-1/). En deux mots :
  - *HEAD* : la branche courant, pour l'instant **Master** (vérifiez le en lisant le fichier avec la commande `cat`)
  - *config* : le fichier de configuration. 
  - *description* : descriptiopn du projet, pas vraiment utilisé
  - *hooks/* : contient des scripts que l'on peu utiliser à chaque qu'une commande git particulieère est utilisée. C'est une utilisation avancée de git, qui permet par exemple de lancer tous les tests à chaque push, etc.
  - *info/exclude/* un *.gitignore* pour tout le projet.
  - *objects/* : contient votre projet actuel et passé en plein de petits bouts. Pour l'instant il n'y a rien.
  - *refs/* : contient les commit. Pour l'instant il n'y a rien.

## fonctionnement de git

Le but de git est de garder un historique d'un projet, en conservant les fichiers du projets et leurs modifications au cours du temps. Cet historique est composé de **commit** qui stock l'état d'un projet à un instant donné. Plus précisément il stocke la différence en l'état précédent et le nouvel état, formant un graphe direct et acyclique (si je jargonne)

Pour démarrer cet historique faisons notre premier commit. 

### premier commit 

Pour cela, il faut que l'on ait quelque chose à stocker.  Créons un petit fichier *index.html* à la racine de notre projet (donc ne soyez plus dans le dossier *.git*) :

~~~ html
<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>My homepage</title>
</head>
<body>
<h1>Hello World !</h1>
</body>
</html>
~~~

Pour faire un *commit* (stocker l'état d'un projet) il faut commencer par dire à git ce que l'on veut *"commiter*, ici notre fichier *index.html* :

~~~ shell
git add index.html
~~~

On place le fichier *index.html* courant dans le **stage** c'est à dire l'endroit où son mis les fichier qui seront inclus dans le *commit*. Pour voir tout ça, la commande `status` est super utile :


~~~ shell
git  status
~~~

Cette commande dit chez moi (et en couleur) :

~~~ shell
Sur la branche master

Aucun commit

Modifications qui seront validées :
  (utilisez "git rm --cached <fichier>..." pour désindexer)
	nouveau fichier : index.html
~~~

On a bien un nouveau fichier que l'on veut garder. On peut fait notre premier commit :


~~~ shell
git  commit
~~~

Cette commande va lancer l'éditeur que vous avez configuré (`vim` si vous avez suivi mes recommandations) et va vous demander de décrire votre commit. Cette étape est **obligatoire** et **très importante**, ne mettez donc pas de message fantaisiste : décrivez en une ligne ce que vous avez fait. 
Ici, par exemple : *"first commit"*. Sauvez et sortez de `vim`, vous avez fait votre premier commit. On le voit en tapant la commande `git status` (qui dit que tout est ok, que le stage est vide et que l'on a aucun fichier non suivi par git). 

La commande `git log` vous donne un historique des *commit* avec le nom, l'heure et le message. Chez moi ça donne :


~~~ shell
commit 3b8c0a8836050e58ec8cf8bd24f3d06b0bf39613 (HEAD -> master)
Author: François Brucker <francois.brucker@gmail.com>
Date:   Sat Sep 19 14:35:41 2020 +0200

    First commit !
~~~

### les objets

> [**Dans la doc**](https://git-scm.com/book/fr/v2/Les-tripes-de-Git-Les-objets-de-Git) 

Git va tout (oui tout) stocker dans le dossier `.git/objects` sous la forme d'un fichier compressé de nom égal à sa valeur de hash [SHA-1](https://fr.wikipedia.org/wiki/SHA-1) sur 40 octets.

> **Nota Bene :** Il est possible mais hautement improbable que 2 fichiers différents aient la même valeur de hash SHA-1. Dans ce cas là git sera perdu. Mais bon, que cela arrive c'st rare, et dans un même projet c'est encore plus rare.... Voir n'est pas encore arrivé.

Chez moi j'ai, avec la commande `tree objects` exécutée dans le dossier git :

~~~ shell
objects
├── 3b
│   └── 8c0a8836050e58ec8cf8bd24f3d06b0bf39613
├── 4b
│   └── 825dc642cb6eb9a060e54bf8d69288fbee4904
├── aa
│   └── e16b7870ad8867b12184215adf9063afc800c1
├── ab
│   └── 3401bd309f7e474cba48b2ecc06c09543a1e0d
├── info
└── pack
~~~

Ce dossier est la base de donnée de notre projet. Chaque objet est stocké avec une signature SHA-1 de 40 octets, les deux proemiers étant le nom du dossier, les 38 autres le nom du fichier.

Si je veux savoir ce qu'il y a dans le fichier *ab/3401bd309f7e474cba48b2ecc06c09543a1e0d* du dossier objet, je tape : `git cat-file -p ab3401bd309f7e474cba48b2ecc06c09543a1e0d` et j'obtiens :

~~~ html

<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>My homepage</title>
</head>
<body>
<h1>Hello World !</h1>
</body>
</html>
~~~

C'est notre fichier html ! Les autres objets correspondent à l'arborescence de projet (pour l'instant un unique nœud, notre commit) et le commit en lui même. Il aura un autre nom chez vous, mais chez moi c'est celui de nom *3b/8c0a8836050e58ec8cf8bd24f3d06b0bf39613* (c'est le numéro donné dans le commit). 

### Les références 

Le dossier référence contient les références des commits de toutes les branches et ou tags de notre projet. Nous n'avons qu'une seule branche, nommée *master* commit des différentes branches. En regardant ce qu'il y a dans le fichier `refs/heads/master` je retrouve bien le numéro de commit.

On peut accéder à tout dans git en utilisant ces numéro (en entier ou les premiers chiffres (4 ou 7), qui sont normalement suffisant). Par exemple si jeu veux voir le log de mon commit de numéro *3b8c0a8836050e58ec8cf8bd24f3d06b0bf39613*, je peux taper `git log 3b8c0a8836050e58ec8cf8bd24f3d06b0bf39613` ou `git log 3b8c`.

###  gestion des commit

#### .gitignore

exemple mac .DS_store, l'ide, le build, etc.

Doit être dans le commit.

#### avancer dans l'arbre

Modifions notre fichier *index.html* :

~~~ html
<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Ma maison page</title>
</head>
<body>
<h1>Hello World !</h1>
<h2>et bonjour Monde !</h2>
</body>
</html>
~~~


La commande `git status` nous donne ce qui a changé :

~~~ shell 

Sur la branche master
Modifications qui ne seront pas validées :
  (utilisez "git add <fichier>..." pour mettre à jour ce qui sera validé)
  (utilisez "git restore <fichier>..." pour annuler les modifications dans le répertoire de travail)
	modifié :         index.html

aucune modification n'a été ajoutée à la validation (utilisez "git add" ou "git commit -a")
~~~

Un fichier a été modifié. Comme on a pas de nouveaux fichiers, et que l'on veut juste mettre à jour les fichiers déjà suivis, on peut se passr de passr par le stage et tout faire en une seule fois (la commande `-a` permet de commiter tous les fichiers suivi et modifié qu'ils soient ou pas dans le stage et la commande -`m` permet d'ajouter le message sans passer par `vim`) :

`git commit -a -m"add french"`

On peut voir les logs (avec en prime deux nouvelles options, une de git pour ne pas avoir de pager une option de log pour  juste afficher  le message et le numéro du commit) : `git --no-pager log --pretty=oneline`. J'obtiens :

~~~ shell
11f5564cda69451538ff8036c1eb92834a585884 (HEAD -> master) add french
3b8c0a8836050e58ec8cf8bd24f3d06b0bf39613 First commit !
~~~


Je peux voir les différences pour les commit, je peux utiliser la commande `git log` en se concentrant sur un fichier, ici `index.html` : `git`

#### revenir en arrière

TBD : comme l'autre, on supprime le html, ou un autre turc pour le commit.

Puis revenir en arrière avec juste les façon de faire



-  `git checkout 3b8c` va créer une branche temporaire
- `git checkout 3b8c index.html` va reprendre le fichier html de 3b8c
- `git revert` : enlève juste le commit
- `git reset --hard`  (`git reflog`) revient en arrière. Attention supprime tout l'historique.

head~1 (avant dernier)


Si ce commit ne me plait pas, je peux revenir à un commit précédent en utilisant `git reset`. Si je veux revenir au commit initial : `git reset 3b8c`

[revenir en arrière](https://www.youtube.com/watch?v=ZY5A7kUR0S4)

[commande reset](https://delicious-insights.com/fr/articles/git-reset/)

## Les branches

### créations

### merge

## github

origin

### push

### pull

### rebase

## mettre en production

parfois branche prod (des versions différentes etc)

on se connecte sur l'ovh et pull (on a bien amené avec nous l'agent...). Parfois une clé qui a juste le droit de pull.

#### récap.


Commande qu'on a utilisé :

  - `git init`
  - `git add`
  - `git status`
  - `git commit`
  - `git log`
  - `git cat-file -p`
## ressources

  - initialisation git/github par défaut :
    - [doc officielle](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
    - [git et github](https://kbroman.org/github_tutorial/pages/first_time.html) 
  - guide général :
    - [guide de Karl Broman](https://kbroman.org/github_tutorial/). Très bien fait et va au but.
    - [pro git](https://git-scm.com/book/en/v2). Y'a tout. Peut-être parfois un peu trop. Mais si on a un problème il y a forcément la solution là dedans.
    - [git magic](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/fr/index.html). En français. Très intéressant à suivre également, il donne des infos différente du tuto de Karl Broman.
    - playlist youtube :
      - [coding train playlist](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV). Sympa à écouter et faire. Passe pas mal de temps au début avec github.
      - [grafikart](https://www.youtube.com/watch?v=rP3T0Ee6pLU&list=PLjwdMgw5TTLXuY5i7RW0QqGdW0NZntqiP). En français s'il vous plait.
    - [version control with git](https://www.amazon.fr/Version-Control-Git-collaborative-development-ebook/dp/B008Y4OR3A). Un très bon livre qui explique en détail le fonctionnement de git. 
  - commandes :
    - [toutes les commandes](https://git-scm.com/docs/git#_git_commands)
    - [commandes courante](https://www.hostinger.fr/tutoriels/commandes-git/)
    - [une cheat sheet](https://training.github.com/downloads/fr/github-git-cheat-sheet.pdf)
  - misc :
      du git en 3 parties [partie 1](https://www.daolf.com/posts/git-series-part-1/)
