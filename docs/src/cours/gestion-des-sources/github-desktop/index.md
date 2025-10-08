---
layout: layout/post.njk
title: SCM avec l'application desktop

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Travailler depuis le site <ahttps://github.com/> uniquement est très limitant. Github est le lieu où est stocké du projet, l'outil qui fait tout fonctionner est [git](https://fr.wikipedia.org/wiki/Git). Avant d'utiliser la ligne de commande qui peut être intimidante, utilisant une application développée par github qui permet d'en utiliser les fonctions les plus courantes.

{% lien %}

<https://desktop.github.com/> et sa [documentation](https://docs.github.com/en/desktop)

{% endlien %}

On va reprendre le projet précédent pour créer son projet chez soit ainsi que l'origin en utilisant l'application desktop. Ceci vous permettra de savoir comment :

- faire un clone
- notion de gestion distribuée
- créer un nouveau projet
- l'index aussi nommé _stage_
- faire un rebase

## Installation

{% faire %}
[Télécharger l'application github desktop](https://desktop.github.com/download/) et installez là sur votre ordinateur.

{% endfaire %}

## Configuration

### Lier le compte github

Lors du premier lancement de l'application vous devriez avoir un fenêtre de ce genre :

![premier lancement](app-github-mac-premier-accueil-1.png)

Connectez vous à github pour associer votre login à l'application :

![premier lancement](app-github-mac-premier-accueil-2.png)

Ignorez les fenêtres si vous en avez et arrivez là :

![premier lancement](app-github-mac-premier-accueil-3.png)

### Préférences

Allez dans les préférences (`file > options` sous windows ; `github desktop > préférences` sous mac) et vérifiez que :

- _"Accounts"_ : pointe bien vers votre compte github
- _"Integration"_ :
  - external editor : mettez vscode (ou votre éditeur de code préféré)
  - shell : votre terminal préféré
- _"Git"_ : connaisse bien votre vrai nom (pas de pseudo) et une adresse mail où vous joindre.

{% info %}
On le rappelle, dans la gestion des sources il faut pouvoir contacter rapidement toute personne ayant fait un commit pour lui demander des explications ou de faire des corrections. Il faut donc pouvoir **toujours** identifier l'auteur par un nom et une adresse mail valide.

{% endinfo %}

Dans l'onglet de préférences git cliquez sur _"edit your global git config"_ :

![pref git](./desktop-pref-git.png)

Ceci va vous ouvrir l'éditeur que vous avez choisi dans les préférences integration avec le fichier de configuration global de git. Assurez vous d'avoir la préférence ci-dessous :

```text
[pull]
	rebase = merges
```

Qui va par défaut faire un rebase plutôt qu'un merge lorsque l'on récupère les modification de l'origine.

{% info %}
Mon fichier de configuration global de git ressemble à ça :

```text
[user]
	name = François Brucker
	email = francois.brucker@gmail.com
[core]
	editor = vim
[color]
	ui = true
[pager]
	log = false
[pull]
	rebase = merges
[filter "lfs"]
	process = git-lfs filter-process
	required = true
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
[init]
	defaultBranch = main

```

Nous y reviendrons lorsque l'on utilisera directement git en ligne de commande.
{% endinfo %}

## Projets

Puisque vous travailler sur votre ordinateur, il vous faudra également une application vous permettant de créer et modifier des fichiers texte. Je vous conseille d'utiliser vscode :

{% faire %}
Téléchargez et installer l'éditeur vscode : <https://code.visualstudio.com/>
{% endfaire %}
{% aller %}
[Prise en main de l'éditeur vscode](cours/coder-et-développer/bases-programmation/interpréteur/éditeur-vscode/prise-en-main/){.interne}.
{% endaller %}

### <span id="récupérer-projet"></span>Récupérer un projet

Commençons par récupérer le projet précédent et voir comment tout ça se passe dans l'application.

1. choisissez _"clone a project from the internet"_
2. vous devriez voir vos le projet dans l'onglet _"Github.com"_
3. en cliquant sur le bouton _"clone"_, votre projet va aller dans un dossier de votre ordinateur

Une fois cliqué sur _"clone"_ on se retrouve devant la fenêtre suivante :

![projet](app-github-mac-projet-1.png)

Remarquez qu'en cliquant sur _"history"_, on retrouve **tout** l'historique du projet :

![projet](app-github-mac-projet-2.png)

{% note %}

Un clone d'un projet contient toute l'histoire du projet, depuis le 1er commit.

{% endnote %}

La solution utilisée par [git](https://git-scm.com/) consiste à ne pas choisir de serveur distant avec des règles précises : tout participant possède l'intégralité de la structure de sauvegarde comme s'il était seul développeur. On ajoute enfin souvent un participant fictif, nommé **_origin_**, qui est la référence commune et est synchronisée à l'envie par les développeurs. Cette structure distribuée permet :

- que chaque développeur puisse faire ses propres commits en local,
- d'avoir une (ou plusieurs) branches partagée par tous les utilisateurs (comme `main`, `dev`, _etc_) et synchronisés souvent entre les utilisateur et _origin_ :
  - on appelle **_push_** les synchronisation des utilisateurs vers l'_origin_
  - on appelle **_pull_** les synchronisation de l'_origin_ vers un utilisateur
- de continuer un projet avec une nouvelle équipe, il suffit de copier _origin_.

Chaque membre d'un projet aura chez lui une copie complète du projet, avec tous les commit et toutes les branches.

Pour communiquer les changement effectué chez soit aux autre membre de l'équipe, une technique courante est de désigner un clone particulier qu'on nomme `origin` — c'est celui sur github — et qui sera le lieu où l'ou enverra nos modifications (`push`) et où l'on récupérera les dernières avancées des collaborateurs (`pull`)

{% info %}
Avoir un clone _"origin"_ n'est pas indispensable. On pourrait tout aussi bien directement récupérer des modification depuis le clone d'un collaborateur : le système est **distribué**.

Mais c'est tout de même vachement plus simple d'avoir un lieu où se concentre l’information avant d'être distribuée aux autres membres du projet.

{% endinfo %}

### <span id="nouveau-projet"></span> Nouveau projet

Créons un nouveau projet jouet :

1. choisissez de créer un nouveau projet dans la fenêtre principale : ![nouveau projet](app-github-nouveau-1.png) Je l'ai appelé `animaux`{.fichier}
2. l'application a cré un dossier `animaux`{.fichier} sur mon ordinateur : ![nouveau projet 2](app-github-nouveau-2.png)

Tout a été fait sur votre ordinateur. Rien n'a été mis sur github pour l'instant. Faisons le :

Dans la fenêtre cliquez sur publish your repository to github :

![publish](app-github-nouveau-3.png)

{% info %}
Si le projet n'est pas confidentiel, autant le laisser public. C'est bien pour les autres qui pourront s'en inspirer et cela fait votre "book" pour plus tard.
{% endinfo %}

Allez sur github pour voir que le projet est présent.

Vous voyez que l'application a mis un fichier (caché) `.gitattributes`{.fichier}, on ne s'en en occupe pas, c'est une optimisation que desktop fait pour nous.

{% info %}
Le fichier `.gitattributes`{.fichier} donne à git des règles pour [modifier automatiquement](https://buzut.net/cours/versioning-avec-git/normalisation-des-fichiers) des fichiers lorsqu'ils passent entre ses mains.

Par exemple, pour les fichiers texte, de gérer automatiquement les caractères _à la ligne_ qui sont [différents sous unix, max et windows](https://fr.wikipedia.org/wiki/Fin_de_ligne).
{% endinfo %}

#### Liste des fichiers à ignorer

Allez dans les préférences du projet `Repository > repository settings` puis choisissez l'onglet `ignored files` :

![pref projet](./desktop-gitignore.png)

Ceci vous permet de créer ou de modifier votre liste de fichiers à ignorer. Vous voyez sur la copie d'écran que j'ai ajouté aux fichiers ignorés :

- la poubelle du Macintosh (le dossier `.DS_Store` par exemple)
- les fichiers relatif à votre éditeur de texte (comme les fichiers `.vscode` où vscode range ses préférences),
- les fichiers temporaires et de log
- ...

{% lien %}
[une liste de fichiers courant à ignorer](https://gist.github.com/octocat/9257657)
{% endlien %}

> TBD faire un fichier TBD.txt que l'on met en `.gitignore`{.fichier}
> TBD ajouter des choses à faire.

#### Ajoutons des fichiers

Utilisons vscode pour _"ouvrir un dossier"_ puis choisir le dossier contenant notre projet.

Ajoutons y 3 fichiers :

- `poissons.txt`{.fichier}

  ```text
  Anchois
  Sardine
  Requin

  ```

- `mammifères.txt`{.fichier}

  ```text
  Chat
  Homme
  Girafe

  ```

- `oiseaux.txt`{.fichier}

  ```text
  Pinson
  Mouette
  Goéland

  ```

Dans l'application desktop on voit qu'il y a 3 changements par rapport à la position précédente :

![desktop-projet-1](desktop-projet-1.png)

Les 3 nouveaux fichiers sont sélectionnés. Le prochain commit prendra en compte ces 3 fichiers.

Faisons un commit. On voit que les 3 fichiers ont été pris en compte dans le commit. Il n'est plus nécessaire de commiter chaque fichier comme on l'avait fait en travaillant directement sur le site de github !

![desktop-projet-2](desktop-projet-2.png)

{% note %}
Choisir quels fichiers seront pris en compte pour le commit est ce que l'on appelle le _staging_
{% endnote %}

### Pousser l'historique sur github

Pour l'instant, nous n'avons travailler que chez nous. Rien n'a été mis sur github. Pour le faire, il suffit de cliquer sur le bouton _"push origin"_ pour le faire.

Faisons le.

Tout s'est bien passé, il n'y a pas eu de conflit. Créons un conflit pour voir comment le résoudre.

### Résolution de conflit

On va :

1. modifier sur le site de github un fichier
2. modifier le même fichier chez nous
3. tenter de pousser nos modifications sur le serveur.

#### situation sur github

On modifie le fichier `oiseaux.txt`{.fichier} :

```text
Pinson du nord
Mouette
Gabian
Hibou petit duc
```

Et on commit les changements :

```text
origin : A -> B
```

Vous pouvez faire toutes les modifications que vous voulez, , du moment qu'on supprime les références aux commits en conflit.

> TBD donner des exemple avec le conflit et les modification  on fait une union ou même on fait autre chose.

#### situation à la maison

On modifie le fichier `oiseaux.txt`{.fichier} pour mettre les oiseaux dans l'ordre alphabétique :

```text
Goéland
Mouette
Pinson

```

Et on commit les changements :

```text
nous : A -> C
```

#### Situation globale

On se retrouve dans la situation suivante, sur la même branche `main` :

```text
origin : A -> B
          \
nous   :    -> C
```

Sur l'application desktop, notre bouton de communication avec le serveur dit*"fetch origin"* :

![desktop-projet fetch](desktop-projet-3.png)

{% note %}
**_fetch origin_** signifie que l'application va chercher des infos sur l'état de l'origin c'est à dire sur github.
{% endnote %}

Cliquons sur ce bouton pour nous retrouver dans la situation suivante :

![potentiel conflit](desktop-projet-4.png)

On voit que github et nous différons tous deux d'un commit.

#### Résolution du problème

Nous pourrions faire comme précédemment et faire un _merge_ des deux histoires. On aurait du coup un historique comme ça :

```text
origin : A -> B --> D
          \     /
nous   :    -> C
```

Mais notre nouvelle branche n'est pas informative. Elle ne correspond à rien d'un point de vue sémantique. C'est juste une façon de rabouter les deux main ensemble. Pour ce genre de cas (c'est à dire 90% du temps) on préfère une autre solution : le **rebase**

{% note %}
A moins que les branches soient liées au [workflow](https://delicious-insights.com/fr/articles/bien-utiliser-git-merge-et-rebase/), on privilégiera toujours le rebase au merge
{% endnote %}

On va re-écrire notre histoire en fonction de l'origine, c'est à dire transformer ça :

```text
origin : A -> B
          \
nous   :    -> C
```

en ça :

```text
origin : A -> B
               \
nous   :         -> C'
```

Il faut transformer notre commit C en le commit C' qui pourra s'intégrer tout seul dans l'histoire de l'origine : cette opération s'appelle un rebase.

C'est exactement ce que va faire desktop lorsque l'on clique sur le bouton pull.

Une fenêtre apparaît pour dire qu'il y a un soucis. Ne prenez pas peur et fermez cette fenêtre. On arrive à cette fenêtre là :

![rebase 1](desktop-rebase-1.png)

On sait faire. Il suffit d'éditer le ficher dans vscode et de faire comme pour le merge dans le projet précédent. Le nouveau fichier `oiseaux.txt` devient :

```text
Goéland
Hibou petit duc
Mouette
Pinson du nord
```

On a régler un problème dans le rebase. COmme c'était le seul, desktop nous permet de continuer :

![rebase 2](desktop-rebase-2.png)

On clique sur le bouton _"continue rebase"_. Pour arriver à cette situation :

![rebase 3](desktop-rebase-3.png)

Il n'y a plus de conflit avec l'origin, puisque son commit d'avance a été intégré dans notre historique. Allez dans l'historique pour le voir :

![rebase 4](desktop-rebase-4.png)

Notre commit a été re-écrit pour tenir compte du commit de l'origin (qui est passé _avant_ le notre) :

![rebase 5](desktop-rebase-5.png)

On peut maintenant pousser nos changements sur github sans soucis en cliquant sur le bouton _"push origin"_

Il y a au final tous les commit sur github (victoire !)

![rebase 6](desktop-rebase-6.png)
