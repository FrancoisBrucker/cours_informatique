---
layout: layout/post.njk 
title: Installation et configuration de Git

eleventyNavigation:
  key: "Installation et configuration de Git"
  parent: "Gestion des sources"
---
{% prerequis "**Prérequis** :" %}

* [Terminal]({{ "/tutoriels/terminal" | url }})
* [Naviguer dans un système de fichiers]({{ "/tutoriels/fichiers-navigation" | url }})

{% endprerequis %}

<!-- début résumé -->

Installation et configuration de git pour github.

<!-- fin résumé -->

{% info %}
On ne montrera pas ici comment utiliser git en ligne de commande.
{% endinfo %}

## Installation

### Git

{% details "sous Linux" %}

{% lien %}
<https://git-scm.com/download/linux>
{% endlien %}

```shell
apt-get install git
```

{% enddetails %}

{% details "Sous mac" %}

On utilise [brew]({{ "/tutoriels/brew" | url}}) :

```shell
brew install git
```

{% enddetails %}

{% details "Windows" %}

Le package <https://gitforwindows.org/> est très bien.

Gardez les paramètres par défaut lors de l'installation à part pour le choix de l'éditeur par défaut. Remplacez *vim* par *notepad++* par exemple (si vous n'avez pas [notepad++](https://notepad-plus-plus.org/), installez le) et surtout pour le choix des bibliothèques ssh à utiliser : choisissez **use external openssh** :

![openssh](git-install-windows.png)

{% enddetails %}

### Github cli

Vous pouvez aussi télécharger l'utilitaire de github pour la ligne de commande : [github CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).

{% info %}
CLI signifie Command Line Interface.
{% endinfo %}

Nous ne l'utiliserons pas ici, mais je vous invite à lire [sa documentation](https://cli.github.com/manual/), il permet d'interagir avec github uniquement à la ligne de commande sans cliquer sur aucun bouton, ce qui est plus rapide.

## Configuration

Vous allez travailler sur vos projets git à plusieurs. Il faut pouvoir à tout moment savoir qui a fait quoi sur le projet. Il est donc impératif que vos données personnelles soient à jour.

### Info personnelles

Renseigner ces infos de façon globale pour tout projet (vous pourrez changer ces infos pour chaque projet, mais mettez des infos corrects par défaut) :

{% faire "**Dans un terminal, tapez les commandes :**" %}

```shell
git config --global user.name "Your name here"
git config --global user.email "your_email@example.com"
```

{% endfaire %}

### Rebase comme fusion

On définie tout de suite la stratégie de fusion.

{% faire "**Dans un terminal, tapez la commande :**" %}

```shell
git config --global pull.rebase merges
```

{% endfaire %}

Ceci nous permettra par défaut :

* de faire un rebase de l'origin sur votre branche locale
* de préserver les merge (fusion) de branches déjà présentes (et qui donc, si elles existent, ont une fonction *sémantique* dans votre projet)

Vous pourrez ensuite faire des `git pull` tout seul et ils seront rebasés par défaut et préserveront les merges existant. Le meilleur des deux monde en somme.

### Branche par défaut

POur être cohérent avec github, on va dire que tout nouveau projet commence avec la branche `main`.

Par défaut c'est `master` (et ça [fait des histoires](https://www.theserverside.com/feature/Why-GitHub-renamed-its-master-branch-to-main)).

{% faire "**Dans un terminal, tapez la commande :**" %}

```shell
git config --global init.defaultBranch "main"
```

{% endfaire %}

### Éditeur de messages

On va mettre vim comme éditeur par défaut pour renseigner les commits.

{% faire "**Dans un terminal, tapez la commande :**" %}

```shell
git config --global core.editor vim
```

{% endfaire %}

Vous n'utiliserez que très peu l'éditeur par défaut une fois que vous ferez vos commit avec l'option `-m`.

{% info %}
Vous pouvez également mettre votre [éditeur favori](https://docs.github.com/en/github/using-git/associating-text-editors-with-git) bien sur, mais `vim` sera toujours présent quelque soit l'endroit où au aurez besoin de faire un commit (genre un serveur distant). Il est donc bien d'avoir quelque notions de vim et de les utiliser de temps en temps, d'où cette configuration.
{% endinfo %}

### Configurations optionnelles

On met de la couleur dans le terminal par défaut.

{% faire "**Dans un terminal, tapez la commande :**" %}

```shell
git config --global color.ui true
```

{% endfaire %}

Pour éviter d'avoir un pager lors des `git log`.

{% faire "**Dans un terminal, tapez la commande :**" %}

```shell
git config --global pager.log false
```

{% endfaire %}

Si l'on ne met pas cette option, les logs seront automatiquement passé à `more` par défaut pour paginer les résultats.

{% info %}

On obtiendrait le même résultat sans utiliser la config ci-dessus en utilisant l'argument de git `--no-pager`, par exemple :`git --no-pager log`. Notez que `--no-pager` est un argument de git, pas de sa commande `log`, il est donc placé avant celle-ci.

{% endinfo %}

## Initialiser un projet pour github

{% lien "**Documentation**" %}
<https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories>
{% endlien %}

### Cloner un projet existant

{% lien "**Documentation**" %}
<https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>
{% endlien %}

le projet existe déjà sur github et je le *clone* chez moi C'est dans le menu déroulant `clone` sur la page github du projet. Par exemple pour le [projet animaux](../projet-github-desktop#animaux) :
[cloner un projet](clone-1.png)

Il existe plusieurs façon de procéder :

* https
* ssh
* github CLI

La différence entre ces trois modes est le moyen d’authentification entre votre ordinateur et github.

Après chaque clonage vous aurez un dossier du nom de votre projet contenant :

* tous les fichiers de l'état du projet actuel
* un dossier caché `.git`{.fichier} contenant :
  * l'historique complet du projet
  * la configuration de `git` du projet

Lorsque je regarde tous les fichiers du dossier contenant le projet `animaux` j'obtiens par exemple :

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

{% info %}
J'ai utilisé le terminal pour le faire, mais vous pouvez très bien utiliser l'explorateur de fichier, à condition d'avoir activé [la vue des fichiers cachés]({{ "/tutoriels/fichiers-navigation" | url }}#fichier-cache)
{% endinfo %}

Selon la méthode de clonage utilisé, seule la méthode d'authentification dans le fichier de configuration changera.

{% note %}
A moins que vous n'ayez une clé ssh, utilisez le clonage utilisant le protocole `https`.
{% endnote %}

#### Clonage https

1. dans un terminal, placez vous dans un dossier où seront rangés vos projets github. Pour mon mac, j'ai choisi `~/Documents/git-projets/`{.fichier}
2. tapez la commande : `git clone [le nom du projet]`. Dans mon cas, le menu déroulant *"clone"* m'indique qu'il faut taper la commande : `git clone https://github.com/Test-cours-ecm/animaux.git`
3. j'ai maintenant un dossier animaux contenant la branche `main` du projet :

Le dossier `.git` contient l'entièreté du projet, en particulier son fichier de configuration `.git/config`

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

#### Clonage github CLI

Il faut d'abord s'identifier (`gh auth login`) avant de pouvoir cloner le repo : `gh repo clone Test-cours-ecm/animaux`.

Ensuite, tout se passe comme précédemment. L'intérêt d'utiliser le `github CLI` est de pouvoir gérer directement les spécificités de github comme les pull request par exemple.

#### Clonage ssh

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

{% lien "**Documentation**" %}
<https://docs.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line>
{% endlien %}

Le projet existe en dehors de github et je veux le mettre sur github. Par exemple :

1. un dossier `planètes`{.fichier} contenant un fichier `solaire.txt`{.fichier} :

  ```shell
  fbrucker@so-high git-projets » ls -la planètes 
  total 8
  drwxr-xr-x  3 fbrucker  staff   96 29 aoû 09:44 .
  drwxr-xr-x  4 fbrucker  staff  128 29 aoû 09:45 ..
  -rw-r--r--  1 fbrucker  staff   57 29 aoû 09:44 solaire.txt
  ```

2. on se place dans le dossier du projet `cd planètes`
3. on met en place le repo git avec la commande `git init --initial-branch="main"`
4. on fait le premier commit pour initialiser le projet :
   1. `git add solaire.txt` (on ajoute tous les fichiers au stage, ici il n'y a en a qu'un)
   2. `git commit -am"initial commit"` (on effectue le premier commit)

Si l'on regarde le fichier de configuration de git :

```shell
fbrucker@so-high git-projets/planètes ±main » cat .git/config               
[core]
  repositoryformatversion = 0
  filemode = true
  bare = false
  logallrefupdates = true
  ignorecase = true
  precomposeunicode = true
```

Il manque la partie remote et branch. On pourrait très bien juste recopier ces parties dans le fichier de configuration, mais faisons le avec des commandes git :

Ajout de github :

1. Créer un projet github qui va contenir notre projet git. Sur github, allez dans le menu utilisateur (à droite) puis choisissez *"your repositories"*. Cliquez ensuite sur new pour créer un nouveau projet. Ne créez pas de fichiers `readme`{.fichier} ou `.gitignore`{.fichier}, il faut que ce projet soit vierge pour accueillir sans merge notre projet.
2. sur notre ordinateur, on ajoute l'origin (suivez la doc). Dans mon cas : `git remote add origin https://github.com/Test-cours-ecm/planetes.git`
3. on envoie notre projet git sur github et on lui associe la branche main :`git push --set-upstream origin main`.

{% info %}
L'item 3 permet que la commande `git push` soit équivalente à la commande `git push origin main`.
{% endinfo %}

A la fin, le fichier de config du projet ressemble à ca :

```shell
fbrucker@so-high git-projets/planètes ±main » cat .git/config                    
[core]
  repositoryformatversion = 0
  filemode = true
  bare = false
  logallrefupdates = true
  ignorecase = true
  precomposeunicode = true
[remote "origin"]
  url = https://github.com/Test-cours-ecm/plan-tes.git
  fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
  remote = origin
  merge = refs/heads/main
```
