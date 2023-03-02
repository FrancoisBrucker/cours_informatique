---
layout: layout/post.njk 
title:  "Projet numérologie : partie 1 / niveau 4 / html et css"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numérologie/index.md %}) / [partie 1]({% link cours/web/projets/numérologie/partie-1-front/index.md %}) / [niveau 4]({% link cours/web/projets/numérologie/partie-1-front/niveau-4/index.md %}) / [html et css]({% link cours/web/projets/numérologie/partie-1-front/niveau-4/3-html_css.md %})
{.chemin}

## où sont les préférences de git ?

Les configurations de git sont rangées dans un dossier *".git"* à la racine de votre projet.

### rendre visible le dossier .git

Ce fichier est par défaut caché par vscode. Nous allons le rendre visible :

1. allez dans les préférences
2. tapez `files.exclude` dans la barre de recherche.
3. assurez vous d'être dans l'onglet *workspace* pour ne changer que pour ce projet.
4. supprimez la ligne où il y a marqué `**/.git`.

Vous devriez voir apparaitre un dossier *.git* dans vscode. Si vous regardez le fichier *config* vous verrez les configurations de votre projet. Pour moi, c'est ça :

```text
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = git@github.com:FrancoisBrucker/numérologie.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
```

### création d'un fichier .gitignore

Un `git status` nous dit des choses bizarres :

```text
Sur la branche main
Votre branche est à jour avec 'origin/main'.

Fichiers non suivis:
  (utilisez "git add <fichier>..." pour inclure dans ce qui sera validé)
	.vscode/

aucune modification ajoutée à la validation mais des fichiers non suivis sont présents (utilisez "git add" pour les suivre)
```

Un dossier *".vscode"* a été créé. C'est l'endroit où vscode stocke ses préférences pour le projet (le *workspace*). 

Ceci est problématique, on ne veut pas ajouter ce dossier à git car :

* chaque utilisateur peut avoir ses propres préférences pour vscode
* peut-être que tout le monde n'utilise pas vscode

Ajouter ce fichier va imposer nos préférences aux autres. Ce n'est pas bien.

Plutôt que de tout le temps penser à ne pas commiter ce fichier, on va demander à git de ne jamais le regarder. Pour cela on crée un fichier nommé [*".gitignore"*](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files).

Créez un fichier *".gitignore"* à la racine de votre projet (vscode va crier un peu mais faites le tout de même). Dans ce fichier vous mettrez la ligne :

```text
.vscode
```

Si vous refaite un `git status` on a :

```text
Sur la branche main
Votre branche est à jour avec 'origin/main'.

Fichiers non suivis:
  (utilisez "git add <fichier>..." pour inclure dans ce qui sera validé)
	.gitignore

aucune modification ajoutée à la validation mais des fichiers non suivis sont présents (utilisez "git add" pour les suivre)
```

Ce qui est normal : le dossier *".vscode"* n'est plus suivi, mais on a ajouté un fichier *".gitignore"* qui n'est pas encore suivi par le projet.

1. `git add --all`
2. `git commit -am"ajout d'un .gitgnore"`
3. `git push`

Et finalement `git status` nous dit que tout est ok. Ouf.

## les tâches

* [tâche 1 du niveau 1 de la partie front]({% link cours/web/projets/numérologie/partie-1-front/niveau-1/3-html_css.md %}#tache-1), puis on `git add --all`/`git commit -am"add index.html`
* Faite la 1ère partie de la [tâche 2 du niveau 1 de la partie front]({% link cours/web/projets/numérologie/partie-1-front/niveau-1/3-html_css.md %}#tache-2.1), puis on commit : `git commit -am"ajout css"`
* Faite la 2nde partie de la [tâche 2 du niveau 1 de la partie front]({% link cours/web/projets/numérologie/partie-1-front/niveau-1/3-html_css.md %}#tache-2.2), puis on `git add --all` / le nouveau fichier puis on commit le tout : `git commit -am"déplace css dans main.css"`.
* [tâche 3 du niveau 1 de la partie front]({% link cours/web/projets/numérologie/partie-1-front/niveau-1/3-html_css.md %}#tache-3), puis on commit : `git commit -am"ajout lib pure-css"`.

## synchronisation avec l'origin

On est 4 commit plus loin que le serveur (`git status`) :

```text
Sur la branche main
Votre branche est en avance sur 'origin/main' de 4 commits.
  (utilisez "git push" pour publier vos commits locaux)

rien à valider, la copie de travail est propre
```

 On push sur l'origin : `git push`
