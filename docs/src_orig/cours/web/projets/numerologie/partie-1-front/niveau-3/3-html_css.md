---
layout: page
title:  "Projet numérologie : partie 1 / niveau 3 / html et css"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 1]({% link cours/web/projets/numerologie/partie-1-front/index.md %}) / [niveau 3]({% link cours/web/projets/numerologie/partie-1-front/niveau-3/index.md %}) / [html et css]({% link cours/web/projets/numerologie/partie-1-front/niveau-3/3-html_css.md %})
{.chemin}

## où sont les préférences de git ?

Les configurations de git sont rangées dans un dossier *".git"* à la racine de votre projet.

### rendre visible le dossier .git

Ce fichier est par défaut caché par vscode. Nous allons le rendre visible : 

1. allez dans les préférences
2. tapez `files.exclude` dans la barre de recherche.
3. assurez vous d'être dans l'onglet *workspace* pour ne changer que pour ce projet.
4. supprimez la ligne où il y a marqué `**/.git`.

Vous devriez voir apparaitre un dossier *.git* dans vscode. Si vous regardez le fichier *config* vous verrez les configurations de votre projet.

### création d'un fichier .gitignore

Notez qu'on a un commit d'avance car vscode a crée un dossier .vscode où il range les préférences du workspace. Nous ne voulons pas mettre ce fichier sur github, car chaque utilisateur va avoir ses propres préférences : ajouter ce fichier va imposer nos préférences aux autres. Ce n'est pas bien.

Plutôt que de tout le temps penser à ne pas commiter ce fichier, on va demander à git de ne jamais le regarder. Pour cela on crée un fichier nommé [*".gitignore"*](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files).

Créez un fichier *".gitignore"* à la racine de votre projet (vscode va crier un peu mais faites le tout de même). Dans ce fichier vous mettrez la ligne :

```text
.vscode
```

A partir de maintenant, tout le dossier *".vscode"* sera ignoré de git. On le voit dans l'application github. On a toujours 1 modification, mais c'est l'ajout du fichier *".gitignore".

> Commitez ce changement et pushez sur l'origin'.
{.note}

## les tâches

* [tâche 1 du niveau 1 de la partie front]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/3-html_css.md %}#tache-1), puis on commit le nouveau fichier.
* Faite la 1ère partie de la [tâche 2 du niveau 1 de la partie front]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/3-html_css.md %}#tache-2.1), puis on commit le nouveau fichier en changeant le message par défaut par : "ajout css".
* Faite la 2nde partie de la [tâche 2 du niveau 1 de la partie front]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/3-html_css.md %}#tache-2.2), puis on commit le nouveau fichier en changeant le message par défaut par : "déplace css dans main.css".
* [tâche 3 du niveau 1 de la partie front]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/3-html_css.md %}#tache-3), puis on commit le nouveau fichier en changeant le message par défaut par : "ajout lib pure-css".

## synchronisation avec l'origin

On est 4 commit plus loin que le serveur. On push sur l'origin.
