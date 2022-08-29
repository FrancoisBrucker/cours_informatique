---
layout: layout/post.njk 
title: Git

eleventyNavigation:
  key: "Git"
  parent: "Gestion des sources"
---
{% prerequis "**Prérequis** :" %}

* [Utiliser le Terminal]({{ "/tutoriels/terminal-utilisation" | url }})

{% endprerequis %}

<!-- début résumé -->

Configuration et utilisation de git

<!-- fin résumé -->

## Installation

### git

{% details "sous Linux" %}

{% chemin %}
<https://git-scm.com/download/linux>
{% endchemin %}

```shell
apt-get install git
```

{% enddetails %}

{% details "Sous mac" %}

On utilise [brew]({{ "tutoriel/brew" | url}}) :

```shell
brew install git
```

{% enddetails %}

{% details "Windows" %}

Le package <https://gitforwindows.org/> est très bien.

Gardez les paramètres par défaut lors de l'installation à part pour le choix de l'éditeur par défaut. Remplacez *vim* par *notepad++* par exemple (si vous n'avez pas [notepad++](https://notepad-plus-plus.org/), installez le) et surtout pour le choix des bibliothèques ssh à utiliser : choisissez **use external openssh** :

![openssh](git-install-windows.png)

{% enddetails %}

### github cli

Vous pouvez aussi télécharger l'utilitaire de github pour la ligne de commande : [github CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).

{% info %}
CLI signifie Command Line Interface.
{% endinfo %}

Nous ne l'utiliserons pas ici, mais ej vous invite à lire [sa documentation](https://cli.github.com/manual/), il permet de faire beaucoup de choses uniquement à la ligne de commande, sans cliquer sur aucun bouton, ce qui peut être très pratique.

## Configuration

Vous allez travailler sur vos projets git à plusieurs. Il faut pouvoir à tout moment savoir qui a fait quoi sur le projet. Il est donc impératif que vos données personnelles soient à jour.

### Info personnelles

Renseigner ces infos de façon globale pour tout projet (vous pourrez changer ces infos pour chaque projet, mais mettez des infos corrects par défaut) :

```shell
git config --global user.name "Your name here"
git config --global user.email "your_email@example.com"
```

### Rebase comme fusion

On définie tout de suite la stratégie de fusion :

```shell
git config --global pull.rebase merges
```

Ceci nous permettra par défaut :

* de faire un rebase de l'origin sur votre branche locale
* de préserver les merge (fusion) de branches déjà présentes (et qui donc, si elles existent, ont une fonction *sémantique* dans votre projet)

Vous pourrez ensuite faire des `git pull` tout seul et ils seront rebasés par défaut et préserveront les merges existant. Le meilleur des deux monde en somme.

### Éditeur de messages

On va mettre vim comme éditeur par défaut pour renseigner les commit :

```shell
git config --global core.editor vim
```

Vous n'utiliserez que très peu l'éditeur par défaut une fois que vous ferez vos commit avec l'option `-m`.

{% info %}
Vous pouvez également mettre votre [éditeur favori](https://docs.github.com/en/github/using-git/associating-text-editors-with-git) bien sur, mais `vim` sera toujours présent quelque soit l'endroit où au aurez besoin de faire un commit (genre un serveur distant). Il est donc bien d'avoir quelque notions de vim et de les utiliser de temps en temps, d'où cette configuration.
{% endinfo %}

### Optionnel

On met de la couleur dans le terminal par défaut :

```shell
git config --global color.ui true
```

Pour éviter d'avoir un pager lors des `git log` :

```shell
git config --global pager.log false
```

Si l'on ne met pas cette option, les logs seront automatiquement passé à `more` par défaut pour paginer les résultats.

{% info %}

On obtiendrait le même résultat sans utiliser la config ci-dessus en utilisant l'argument de git `--no-pager`, par exemple :`git --no-pager log`. Notez que `--no-pager` est un argument de git, pas de sa commande `log`, il est donc placé avant celle-ci.

{% endinfo %}

## Initialiser un projet pour github

{% chemin "**Documentation :**" %}
<https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories>
{% endchemin %}

### Cloner un projet existant

{% chemin "**Documentation :**" %}
<https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>
{% endchemin %}

le projet existe déjà sur github et je le *clone* chez moi C'est dans le menu déroulant `clone` sur la page github du projet. Par exemple pour le [projet animaux](../projet-github-desktop#animaux) :
[cloner un projet](clone-1.png)

Il existe plusieurs façon de procéder :

* https
* ssh
* github CLI

La différence entre ces trois modes est le moyen d’authentification entre votre ordinateur et github.

Après chaque clonage vous aurez un dossier du nom de votre projet contenant :

* l'état du projet actuel
* un dossier `.git`{.fichier} contenant :
  * l'historique complet du projet
  * la configuration de `git` du projet

```shell
fbrucker@so-high git-projets/animaux ±main » ls -la
total 32
drwxr-xr-x   7 fbrucker  staff  224 29 aoû 08:57 .
drwxr-xr-x   3 fbrucker  staff   96 29 aoû 08:57 ..
drwxr-xr-x  12 fbrucker  staff  384 29 aoû 08:57 .git
-rw-r--r--   1 fbrucker  staff   66 29 aoû 08:57 .gitattributes
-rw-r--r--   1 fbrucker  staff   18 29 aoû 08:57 mammifères.txt
-rw-r--r--   1 fbrucker  staff   49 29 aoû 08:57 oiseaux.txt
-rw-r--r--   1 fbrucker  staff   23 29 aoû 08:57 poissons.txt
```

Selon la méthode de clonage utilisé, seul le fichier la méthode d'authentification dans le fichier de configuration changera.

#### clonage https

1. dans un terminal, placez vous dans un dossier où seront rangés vos projets github. Pour mon mac, j'ai choisi `~/Documents/git-projets/`{.fichier}
2. tapez la commande : `git clone [le nom du projet]`. Dans mon cas, le menu déroulant *"clone"* m'indique qu'il faut taper la commande : `git clone https://github.com/Test-cours-ecm/animaux.git`
3. j'ai maintenant un dossier animaux contenant la branche `main` du projet :

Le dossier `.git` contient l'entièreté du projet, en particulier son fichier de configuration :

```shell
fbrucker@so-high git-projets/animaux ±main » cat .git/config 
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = https://github.com/Test-cours-ecm/animaux.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
```

La seule chose à retenir ici est :

* github est identifié comme la branche `origin` et son protocole de communication est `https://`
* la branche `main` est disponible sur l'origin.

#### clonage github CLI

Il faut d'abord s'identifier (`gh auth login`) avant de pouvoir cloner le repo : `gh repo clone Test-cours-ecm/animaux`.

Ensuite, tout se passe comme précédemment.

#### clonage ssh

{% info %}
C'est la méthode à privilégier si vous êtes informaticien. C'est à dire que vous allez faire des commits tous les jours et jongler avec les repos de votre projet.

Sinon, vous pouvez ne pas utiliser cette méthode.
{% endinfo %}

MOntrons juste les différences de configuration entre les méthodes précédentes et celle-ci :

* Commande de clonage : `git clone git@github.com:Test-cours-ecm/animaux.git`
* Fichier de configuration :
  ```shell
  fbrucker@so-high git-projets/animaux ±main » cat .git/config
  [core]
    repositoryformatversion = 0
    filemode = true
    bare = false
    logallrefupdates = true
    ignorecase = true
    precomposeunicode = true
  [remote "origin"]
    url = git@github.com:Test-cours-ecm/animaux.git
    fetch = +refs/heads/*:refs/remotes/origin/*
  [branch "main"]
    remote = origin
    merge = refs/heads/main
  ```

On voit que le protocole d’authentification n'est **pas** `https://`, il faut avoir lié une clé ssh à son compte github.

> TBD : lien vers cours spécial avec ssh en prérequis

### Créer un nouveau projet et l'envoyer sur github

{% chemin "**Documentation :**" %}
<https://docs.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line>
{% endchemin %}

Le projet existe en dehors de github et je veux le mettre sur github.

Faisons le.

On commence par créer un dossier

1. si le projet n'est pas encore sous git, il faut l'initialiser avec la commande `git init`
2. 
> TBD un dossier puis taper `git init`
> voir ce que ça a fait.
> 