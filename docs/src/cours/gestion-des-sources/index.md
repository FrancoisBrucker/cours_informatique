---
layout: layout/post.njk

title: Gestion du code source
tags: ["cours", "projet"]
authors:
  - François Brucker
eleventyNavigation:
  prerequis:
    - "/cours/système-et-réseau/bases-système/bases/interactions/fichiers-navigation/"
resume: "Comment gérer les sources d'un projet avec git et github."

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Comment gérer le code source d'un projet des principes au repository github.

{% lien "**Introductions**" %}

- [Qu'est ce que la gestion des sources avec github ?](https://www.youtube.com/watch?v=w3jLJU7DT5E)
- [Utilité de git pour tous](https://www.atlassian.com/fr/git/tutorials/why-git)

{% endlien %}

La gestion du code source (**_SCM_** pour _Source Control Management_) est bien sûr utilisée massivement en informatique, mais les méthodes et techniques mises en œuvre fonctionnent pour tout projet où l'on doit utiliser/produire des documents qui sont modifiés au cours du temps. C'est un cadeau fait par les informaticiens au monde (ne le détruisez pas comme la gestion de projet agile...).

Un des bénéfices d'une gestion des documents bien comprise est que l'on peut :

- **archiver** et retrouver facilement toutes les évolutions d'un projet,
- travailler sur **plusieurs versions** d'un projet en même temps.

Mais surtout : **ne pas avoir peur** de modifier, tester et expérimenter des nouveautés.

Ces bénéfices sont incommensurables lorsque l'on travaille à plusieurs sur un projet et sont très utiles même pour un projet solo.

<!-- TBD 

> TBD numéro de commit ?

peut-être mettre le projet avant la théorie ? Ou en même temps ? 

couper en parties

1. terminal et rebase on pull
2. git bisect
3. interne
-->

## <span id="dépot"></span>Principes : gestion des sources comme un dépôt

Après avoir examiné les besoins qui impliquent l'utilisation d'un SCM, on en verra une implémentation possible sur une structure distribuée et l'usage qu'on peut en faire au quotidien.

### Besoins pour un dépôt

{% aller %}
[Besoins](./besoins-dépôt/){.interne}
{% endaller %}

### Structure distribuée

Pour que son accès soit facile, il faut que la structure de stockage soit sur le même ordinateur que celui ayant le répertoire de travail.

Si cette solution est idéal lorsque l'on est un unique développeur, elle devient plus complexe à mettre en œuvre si on est plusieurs à travailler sur le projet. Il faut :

1. en avoir une copie de la structure de stockage chez chaque participant,
2. permettre à plusieurs personnes de travailler sur le même fichier,
3. permettre le travail asynchrone entre les personnes : une personne va avancer à un endroit pendant qu'une autre travaille sur autre chose
4. pouvoir reprendre un projet existant avec une nouvelle équipe

Ceci implique que chaque copie soit synchronisée par un dépôt référent, un **_projet référent_** faisant autorité pour tous les participants.

Une bonne implémentation consiste **à ne pas sacraliser la mise en commun**. Il faut le faire le souvent pour que tout le monde ait une version claire de l'ensemble **actuel** du projet.

{% attention2 "**À retenir**" %}

Lorsque vous utilisez un projet en commun il faut avoir un dépôt commun mais ne faut pas en sacraliser la mise en commun avec des règles de soumission stricte ou un superviseur.

{% endattention2 %}

### Dépôt origin

Nous allons utiliser <https://github.com/> comme dépôt commun de nos projet. Le site fonctionne avec logiciel de gestion de sources [git](https://fr.wikipedia.org/wiki/Git). Il en existe d'autres, comme <https://gitlab.com/> par exemple.

{% aller %}
[Création d'un compte github](./github-compte){.interne}
{% endaller %}

### Projet Dépôt

{% aller %}
[Github come un drive](./github-drive){.interne}
{% endaller %}

## Principes : gestion des sources en local

### Besoins pour une gestion des sources locale

{% aller %}
[Besoins](./besoins-gestion-sources){.interne}
{% endaller %}

### Projet : gestion des sources

{% aller %}
[Projet uniquement avec github](./github-projet){.interne}
{% endaller %}

## Principes : gestion d'un dépôt distant

### Besoins pour l'utilisation d'un dépôt distant

{% aller %}
[Besoins](./besoins-origin){.interne}
{% endaller %}

### Projet : local et origine

{% aller %}
[Projet avec github desktop](./github-desktop){.interne}
{% endaller %}

## Usage courant

Outre ce qu'on a vu au préalable l'usage d'un SCM au quotidien nécessite quelques connaissances supplémentaires qui permettent de que nous allons aborder maintenant.

### Sha

{% lien %}
<https://fr.wikipedia.org/wiki/SHA-1>
{% endlien %}

À tout objet de git est associé un nombre écrit en hexadécimal correspondant à son hash avec [la fonction de hachage](/cours/algorithmie/structure-dictionnaire/fonctions-hash/){.interne} sha-1.

Ceci permet de retrouver de façon unique (au moins en probabilité et sûrement pour un projet donné) tout ce que stocke git.

> TBD projet voir le sha.

### Diff

> TBD faire un exemple avec la commande diff au terminal : deux fichiers (lignes ≠) et deux dossiers (deux fichiers ≠)
> TBD sous windows <https://learn.microsoft.com/fr-fr/troubleshoot/windows-client/shell-experience/how-to-use-windiff-utility> ou <https://www.git-tower.com/blog/diff-tools-windows>

On a déjà vu le diff des fichiers lors de nos commits et en particulier lorsque l'on a résolu un conflit de fusion. Cela vaut le coût de connaître le format utilisé :

{% lien %}

- [format diff](https://www.math.utah.edu/docs/info/diff_3.html)
- [résumé en français](https://www.linuxtricks.fr/wiki/diff-et-patch-sous-linux)

{% endlien %}

Notez que l'on peut faire nous même des diff au terminal :

{% lien %}

Commande diff au terminal :

- [tuto en français](https://www.youtube.com/watch?v=0JZCah5w7I8)
- [tuto en anglais (plus concis)](https://www.youtube.com/watch?v=-CiLU9-RAGk)

{% endlien %}

Les algorithmes utilisés pour faire un diff sont basés sur [le problème de l'alignement de séquences](/cours/algorithmie/design-algorithmes/programmation-dynamique/alignement-séquences/){.interne}. Ils ne travaillent cependant sur des caractères mais sur des lignes. Si cela vous intéresse suivez les liens suivant pour une introduction :

{% lien %}

- <https://medium.com/@livajorge7/understanding-the-diff-algorithm-and-its-applications-in-software-development-fe094895d92a>
- <https://ably.com/blog/practical-guide-to-diff-algorithms>

{% endlien %}

### Altération et modification de l'historique

{% aller %}
[Besoins de gestion de l'historique](./besoins-historique){.interne}
{% endaller %}

> TBD projet avec desktop voir <https://docs.github.com/en/desktop> partie managing commits.

### Authentification

{% aller %}
[Authentification à l'origine](./github-authentification){.interne}
{% endaller %}

### Github actions

> TBD :
>
> - permet de mettre en place du CI/CD : <https://www.youtube.com/watch?v=scEDHsr3APg>
> - github actions <https://www.youtube.com/watch?v=p3W2XCD3smk>

## Git

{% lien %}

- [Linus Torvalds a crée git en 10 jours](https://www.youtube.com/shorts/rK3IOMr6eSs)  (et le 11ème il s'est reposé)
- [Une histoire de git en français](https://www.youtube.com/watch?v=LDy6Rv0kU1Q)

{% endlien %}

Est l'outil utilisé par github. C'est mieux si vous avez installé ce logiciel sur votre ordinateur et que vous savez un petit peut vous en servir. Cette partie vous permettra d'installer git et de le configurer. On verra aussi comment créer et cloner un projet pour github.

### Connexion ssh à github

Nous allons utiliser des clés ssh pour se connecter à github, donc si vous ne l'avez pas encore fait :

{% aller %}
[Créer et utiliser une clé ssh](/cours/système-et-réseau/ssh/){.interne}
{% endaller %}

Puis renseignez **votre clé publique** dans [votre profil github](https://github.com/settings/keys).

### Installation et configuration

Les notions que l'on a vu précédemment suffisent pour un usage courant de la gestion des sources avec github. Si vous voulez :

- utiliser git avec votre éditeur de texte comme vscode
- ou si vous voulez utiliser git en ligne de commande pour contrôler toutes vos opérations

Il vous faudra installer le programme `git` en ligne de commande.

{% info %}
L'installation et la configuration de git n'est pas très technique. Cela vaut le coup de de le faire ne serait-ce que pour pouvoir utiliser les magnifiques plugins de vscode.
{% endinfo %}

{% aller %}
[Configurer et initialiser ses projets git](./git-init){.interne}
{% endaller %}

## Outils

### App

Outil tout en un pour utiliser github :

{% aller %}
<https://git-fork.com/>
{% endaller %}

### Git avec vscode

{% info "**Documentation**" %}
<https://code.visualstudio.com/docs/editor/versioncontrol#_git-support>
{% endinfo %}

vscode permet d'utiliser directement les commandes git et possède de nombreux plugins permettant, par exemples :

- d'utiliser github avec l'[extension github](https://code.visualstudio.com/docs/editor/github)
- de voir le graphe de dépendances avec l'extension [git-graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) (commande `git-graph.view` pour voir le graphe)
- de voir l'historique de modification d'un fichier avec l'extension [git-history](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) (cliquer droit sur un fichier puis `Git: view file history`)
- ...

### TUI

{% lien %}

- [lazy git](https://github.com/jesseduffield/lazygit) ([une courte vidéo de présentation](https://www.youtube.com/watch?v=CPLdltN7wgE)) : une excellente application pour git
- [gh-dash](https://github.com/dlvhdr/gh-dash) : pour github et les pull requests

{% endlien %}

## Bonnes pratiques

{% aller %}

[Bonnes pratiques](./bonnes-pratiques){.interne}

{% endaller %}

## Porcelaine et plomberie de git

> TBD expliquer porcelaine/plomberie

### Porcelaine

{% aller %}
[Git porcelaine](./git-porcelaine){.interne}
{% endaller %}

### Plomberie

> TBD un tag c'est un objet. Commit, tree ou blob.
> TBD work-trees et stash
> TBD utiliser switch et pas checkout pour passer de branches en branches (checkout pour les commits particulier: headless ?)
> TBD : index = staging area.
> TBD diff format et différents algos
> TBD <https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things>

> TBD reflog.
> TBD git sha. Intro : <https://medium.com/@jonathan_finch/git-commit-hash-number-theory-770f67ec492d> et <https://graphite.dev/guides/git-hash>. Mieux : <https://www.designgurus.io/answers/detail/how-do-i-get-the-hash-for-the-current-commit-in-git>

Cette partie du cours s'adresse plus particulièrement aux informaticiens voulant utiliser git en ligne de commande et/ou à ceux voulant comprendre le fonctionnement précis de git.

## Bibliographie

### Cours

- [Learning Git](https://github.com/gitlearningjourney/learning-git)
- [Version control with git 3rd edition](https://www.amazon.fr/Version-Control-Git-Collaborative-Development/dp/1492091197)
- [the book](https://git-scm.com/book/en/v2)

### Références

- <https://git-scm.com/>
- <https://comprendre-git.com/fr/>

### Misc

- <https://learngitbranching.js.org/>
- <https://tonyg.github.io/revctrl.org/index.html>
- <https://ohshitgit.com/>
- - [s'entraîner avec des commandes git](https://git-school.github.io/visualizing-git/)

## Histoire

{% lien %}

- <https://www.atikteam.com/fr/blog/page/Gestion-de-sources-centralisee-vs-decentralisee>
- <https://blog.tarynmcmillan.com/a-history-of-version-control>

{% endlien %}

<!-- TBD

> - git rebase avec des merges : <https://www.jnielson.com/git-rebase-with-merges>
> - git fetch. qu'est ce qui est fetch ? Tout ou juste des branches <https://stackoverflow.com/a/74355550>
> - force-push : expliquer ce que c'est.
> - mettre la doc de chaque commande avec la description de git en ligne de commande dans la partie plomberie et porcelaine.
> - lister tous tous les commit de la base : <https://stackoverflow.com/a/4787030>
> - rebase les différentes commandes ?
>
>   - detached head : <https://www.cloudbees.com/blog/git-detached-head>
>   - tous les commits : `git reflog` même ceux pas dans une branche (detached head). On peut les retrouver puis cherry pick <https://stackoverflow.com/questions/9984223/what-happens-to-git-commits-created-in-a-detached-head-state>
>   - commit non attaché à une branche (dangling commits): `git fsck --lost-found`
>   - `git cat-files <hash>` pour voir les parents
>
> - remote :
>   - branches.
>   - ssh / https
>   - fetch et push différents : <https://stackoverflow.com/questions/31747072/will-remote-url-for-fetch-and-push-be-different>
>   - pas forcément github ou un autre provider. Un autre ordi fait l'affaire, même juste le sien : <https://www.reddit.com/r/git/comments/5giehg/is_it_possible_to_have_a_remote_thats_on_the_same/>
> - merge :
>   - meilleur ancêtre commun <https://git-scm.com/docs/git-merge-base> <https://stackoverflow.com/a/73171967>
> - conflits : <https://githowto.com/resolving_conflicts>
> - 3-way merge : <https://tonyg.github.io/revctrl.org/ThreeWayMerge.html>
> - réécrire l'histoire : <https://www.atlassian.com/git/tutorials/rewriting-history>
> - pour aller plus loin :
>   - squash commit ?
>   - stash : <https://www.atlassian.com/git/tutorials/saving-changes/git-stash>, <https://www.youtube.com/watch?v=BSLzA8oCT7g> pour les mdp, etc
>   - worktree <https://www.youtube.com/watch?v=ntM7utSjeVU>
>   - sous-projet
>   - git vscode
>   - bisect : <https://www.youtube.com/watch?v=Q-kqm0AgJZ8>
>   - cherry pick : <https://www.youtube.com/watch?v=i657Bg_HAWI> (attention : <https://www.youtube.com/watch?v=WPCxtFkLa7g>)
>
>
> - pull --rebase sinon merge à repetition : <https://www.youtube.com/watch?v=xN1-2p06Urc> ; <https://www.youtube.com/watch?v=DkWDHzmMvyg>
> - merge conflict : <https://www.youtube.com/watch?v=DloR0BOGNU0>
> - cherry-pick attention ! : <https://stackoverflow.com/questions/880957/pull-all-commits-from-a-branch-push-specified-commits-to-another/881014#881014>
> - <https://www.reddit.com/r/git/comments/mq9wh2/is_there_any_way_to_permanently_remove_commits/> et <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>
> - uncompress utilitaire : `pigz` <https://stackoverflow.com/a/3178638>
> - internals git commit <https://pawelszczygielski.pl/2021/02/23/git-how-to-commit-without-git-commit/>
> - tree object format : <https://stackoverflow.com/questions/14790681/what-is-the-internal-format-of-a-git-tree-object>
> - internal objects: <https://shafiul.github.io/gitbook/1_the_git_object_model.html> <https://git-scm.com/book/en/v2/Git-Internals-Git-Objects>. Faire le code en python et pas en ruby. <https://praneethreddybilakanti.medium.com/7-git-internals-548f8707436a>
> - git tag object avec du code en python <https://stackoverflow.com/questions/10986615/what-is-the-format-of-a-git-tag-object-and-how-to-calculate-its-sha>
> - git index format : <https://git-scm.com/docs/index-format> ; `git ls-files --stage` (attention: different de staged ); `git diff-index HEAD` et filetype <https://unix.stackexchange.com/questions/450480/file-permission-with-six-octal-digits-in-git-what-does-it-mean>. Que quelques possibilités. Donc peut-être juste les lister.
> - commit jamais vraiment perdu <https://andrewallison.medium.com/oops-i-lost-my-git-commits-heres-how-to-bring-them-back-from-the-dead-90b1a62f63d1>. Faire test avec rebase et on les retrouve.
>
> biblio :
>
> - ~ et ^ pour les ancêtres <https://stackoverflow.com/questions/2221658/what-is-the-difference-between-head-and-head-in-git>
>
> - cours (BIEN): <https://www.youtube.com/watch?v=rH3zE7VlIMs>, <https://www.boot.dev/teachers/the-primeagen>
>   internals (TROP BIEN le debut puis devient trop chiant) : <https://www.youtube.com/watch?v=fWMKue-WBok&list=PL9lx0DXCC4BNUby5H58y6s2TQVLadV8v7>
> - <https://womanonrails.com/git-rebase-onto>
> - <https://jwiegley.github.io/git-from-the-bottom-up/>
> - <https://tutorial.gitlabpages.inria.fr/git/>
> - <https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain>
> - créer son propre sha : <https://git-scm.com/book/en/v2/Git-Internals-Git-Objects> <https://gist.github.com/masak/2415865> et <https://stackoverflow.com/questions/552659/how-to-assign-a-git-sha1s-to-a-file-without-git/552725#552725>
> - <https://gitirc.eu/gitrevisions.html>
> - interactive stage <https://www.youtube.com/watch?v=UJ5fpaeZWsI> <https://www.youtube.com/watch?v=8st1NhaKDCA>
 -->
