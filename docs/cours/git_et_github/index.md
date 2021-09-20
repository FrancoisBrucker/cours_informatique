---
layout: page
title:  "Git et github : usages et explications"
tags: informatique graphes
author: "François Brucker"
---


Gestion de version. On verra un peu de théorie et surtout de la pratique pour l'utilisation de git et github au quotidien.

## installation

### github

[github](https://github.com/) est le site qui va nous permettre de conserver et partager vos projets.

Créez vous un compte en utilisant une adresse "pro", c'est ce compte qui pourra faire office de *book* sur votre cv. Ce compte github sera utilisé pour tout le cours et vous pourrez  placer vos projet personnels montrable à vos futurs employeurs. Donc utilisez une adresse mail de contact ainsi qu'une photo de profil et un nom présentable.

 > Utilisez une adresse, genre un gmail, qui pourra vous suivre tout au long de votre vie et de vos différents emplois.

Nous utiliserons essentiellement la ligne de commande, mais parfois, il est bon de pouvoir utiliser une application. Téléchargez et installez l'[application desktop](https://desktop.github.com/) de github.

### git

{% details Linux %}

> <https://git-scm.com/download/linux>

```shell
apt-get install git
```

{% enddetails %}

{% details Mac %}

> on utilise <https://brew.sh/>

```shell
brew install git
```

{% enddetails %}

{% details Windows %}

> <https://gitforwindows.org/>

Gardez les paramètres par défaut lors de l'installation à part pour le choix de l'éditeur par défaut. Remplacez *vim* par *notepad++* par exemple (si vous n'avez pas [notepad++](https://notepad-plus-plus.org/), installez le.)

{% enddetails %}

### clé ssh

Il peut être utile d'ajouter une clé une clé ssh à votre compte github. Cela permettra de télé-verser vos sources sans avoir besoin de taper son mot de passe.

Vous pouvez suivre ce [tutoriel]({% link cours/ssh_et_shell/ssh.md %}) pour créer votre clé ssh, puis [ajouter votre nouvelle clé à votre compte github](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

## configuration

### config minimale github

Créez vous un compte github si ce n'est déjà fait. Github va vous permettre de travailler en groupe et de montrer ce que vous savez faire, c'est un peu votre *book* de développeur.

Donc :

* utilisez votre nom/prénom ou un pseudo présentable
* utiliser une adresse mail que vous lisez
* ne mettez dessus que les projets que vous pourriez mettre sur votre cv.
  
Rien ne vous empêche d'avoir d'autres comptes github pour vos projets plus perso mais celui-là c'est votre vitrine légale numérique.

Pour que vous puissiez facilement avoir accès à ce compte,
[ajouter votre clé publique dans github](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).

Vous pourrez donner votre clé publique pour être ajouté comme contributeur d'un projet. C'est un moyen pratique de gérer les personnes d'un projet.

### Configuration minimale git {#configuration-git}

Vous allez travailler sur vos projets git à plusieurs. Il faut pouvoir à tout moment savoir qui a fait quoi sur le projet. Il est donc impératif que vos données personnelles soient à jour.

Renseigner ces infos de façon globale pour tout projet (vous pourrez changer ces infos pour chaque projet, mais mettez des infos corrects par défaut) :

```shell
git config --global user.name "Your name here"
git config --global user.email "your_email@example.com"
```

On va mettre vim comme éditeur par défaut pour renseigner les commit :

```shell
git config --global core.editor vim
```

> Vous n'utiliserez que très peu l'éditeur par défaut une fois que vous ferez vos commit avec l'option `-m`

On met de la couleur dans le terminal par défaut :

```shell
git config --global color.ui true
```

> Vous pouvez mettre votre [éditeur favori](https://docs.github.com/en/github/using-git/associating-text-editors-with-git) bien sur, mais `vim` sera toujours présent quelque soit l'endroit où au aurez besoin de faire un commit (genre un serveur distant). Il est donc bien d'avoir quelque notions de vim et de les utiliser de temps en temps, d'où cette configuration.

Pour éviter d'avoir un pager lors des `git log` :

```shell
git config --global pager.log false
```

Si l'on ne met pas cette option, les logs seront automatiquement passé à `more` par défaut pour paginer les résultats.

> On obtiendrait le même résultat sans utiliser la config ci-dessus en utilisant l'argument de git `--no-pager`, par exemple :`git --no-pager log`. Notez que `--no-pager` est un argument de git, pas de sa commande `log`, il est donc placé avant celle-ci.

On définie tout de suite la stratégie de fusion :

```shell
git config --global pull.rebase merges
```

Ceci nous permettra par défaut :

* de faire un rebase de l'origin sur votre branche locale
* de préserver les merge (fusion) de branches déjà présentes (et qui donc, si elles existent, ont une fonction *sémantique* dans votre projet)

Vous pourrez ensuite faire des `git pull` tout seul et ils seront rebasé par défaut et préserveront les merges existant. Le meilleur des deux monde en somme.

> ceci ne peut se faire qu'à partir de git 2.22. Mettez à jour votre git si nécessaire. On est (à l'heure où je tape ces caractères) à la version 2.32.0 de git.
{: .attention}

## usages

### qu'est que github

[usage github]({% link cours/git_et_github/usage_github.md %})

### qu'est ce que git

[usage de git]({% link cours/git_et_github/usage_git.md %}) où l'on rentre quand même pas mal dans les détails pour comprendre comment fonctionne ce (merveilleux) outils.

## commandes indispensables

[les commandes indispensables]({% link cours/git_et_github/git_commands.md %})

## git et github avec l'application

> TBD : un court tuto sur commet faire en reprenant les commandes indispensables
{: .note}

## mettre en production avec git

Pour mettre un site en production, il suffit de cloner son projet git et de pull les dernières versions du projet.

On a parfois une branche dédiée qui s'appelle production, mais souvent la branche master suffit.

## git avancé

* [git rebase, la tronçonneuse magique]({% link cours/git_et_github/git_rebase.md %})
* [les commits atomiques]({% link cours/git_et_github/git_commits_atomiques.md %})

## ressources

* [githug](https://github.com/Gazler/githug) apprenez git par l'exemple.
* initialisation git/github par défaut :
  * [doc officielle](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
  * [git et github](https://kbroman.org/github_tutorial/pages/first_time.html) 
* guide général :
  * [sympa et en français](https://www.miximum.fr/blog/decouvrir-git/)
  * [guide de Karl Broman](https://kbroman.org/github_tutorial/). Très bien fait et va au but.
  * [pro git](https://git-scm.com/book/en/v2). Y'a tout. Peut-être parfois un peu t*rop. Mais si on a un problème il y a forcément la solution là dedans.
  * [git magic](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/fr/index.html). En français. Très intéressant à suivre également, il donne des infos différente du tuto de Karl Broman.
  * playlist youtube :
    * [coding train playlist](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV). Sympa à écouter et faire. Passe pas mal de temps au début avec github.
    * [grafikart](https://www.youtube.com/watch?v=rP3T0Ee6pLU&list=PLjwdMgw5TTLXuY5i7RW0QqGdW0NZntqiP). En français s'il vous plait.
  * [version control with git](https://www.amazon.fr/Version-Control-Git-collaborative-development-ebook/dp/B008Y4OR3A). Un très bon livre qui explique en détail le fonctionnement de git. 
* commandes :
  * [toutes les commandes](https://git-scm.com/docs/git#_git_commands)
  * [commandes courante](https://www.hostinger.fr/tutoriels/commandes-git/)
  * [une cheat sheet](https://training.github.com/downloads/fr/github-git-cheat-sheet.pdf)
* misc :
  * du git en 3 parties [partie 1](https://www.daolf.com/posts/git-series-part-1/)
  * tout ce que vous avez toujours voulu savoir sur [rebase t quand l'utiliser](https://delicious-insights.com/fr/articles/bien-utiliser-git-merge-et-rebase)
