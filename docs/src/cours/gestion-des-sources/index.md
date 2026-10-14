---
layout: layout/post.njk

title: Gestion du code source
tags: ["cours", "projet"]
authors:
  - François Brucker
eleventyNavigation:
  prerequis:
    - "/cours/système/interagir-avec-système/fichiers-dossiers/"
resume: "Comment gérer les sources d'un projet avec git et github."

date: 2026-01-03

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Comment gérer le code source d'un projet des principes au repository github.

{% lien "**Introductions**" %}

- [Qu'est ce que la gestion des sources avec github ?](https://www.youtube.com/watch?v=w3jLJU7DT5E){.externe}
- [Utilité de git pour tous](https://www.atlassian.com/fr/git/tutorials/why-git){.externe}

{% endlien %}

La gestion du code source (**_SCM_** pour _Source Control Management_) est bien sûr utilisée massivement en informatique, mais les méthodes et techniques mises en œuvre fonctionnent pour tout projet où l'on doit utiliser/produire des documents qui sont modifiés au cours du temps. C'est un cadeau fait par les informaticiens au monde (ne le détruisez pas comme la gestion de projet agile...).

Un des bénéfices d'une gestion des documents bien comprise est que l'on peut :

- **archiver** et retrouver facilement toutes les évolutions d'un projet,
- travailler sur **plusieurs versions** d'un projet en même temps.

Mais surtout : **ne pas avoir peur** de modifier, tester et expérimenter des nouveautés.

Ces bénéfices sont incommensurables lorsque l'on travaille à plusieurs sur un projet et sont très utiles même pour un projet solo.

## Principes 

### <span id="dépot"></span>Dépôt des sources

Déposer le code source pour qu'il puisse être utilisé par d'autres. 

{% aller %}
[Dépôt des sources](./besoins-dépôt/)
{% endaller %}

### Gestion du code source

Gérer les évolutions de son code.

{% aller %}
[Gestion de l'évolution du code source](./évolution-code/)
{% endaller %}
 
## Git chez soit

{% lien %}

- [Linus Torvalds a crée git en 10 jours](https://www.youtube.com/shorts/rK3IOMr6eSs){.externe}  (et le 11ème il s'est reposé)
- [Une histoire de git en français](https://www.youtube.com/watch?v=LDy6Rv0kU1Q){.externe}

{% endlien %}

Les notions que l'on a vu précédemment suffisent pour un usage courant de la gestion des sources avec github. Si vous voulez :

- utiliser git avec votre éditeur de texte comme vscode
- ou si vous voulez utiliser git en ligne de commande pour contrôler toutes vos opérations

Il vous faudra installer le programme `git` en ligne de commande qui est l'outil utilisé par github. C'est mieux si vous avez installé ce logiciel sur votre ordinateur et que vous savez un petit peut vous en servir. Cette partie vous permettra d'installer git et de le configurer.

{% aller %}
1. [Configurer et initialiser ses projets git](./git-init)
2. [Projet git](./projet-git)

{% endaller %}


## Partager du code source

{% aller %}
1. [Partager du code source](./besoins-partage/)
2. [Authentification à l'origine](./github-authentification)
3. [Projet avec github desktop](./github-projet-remote)
{% endaller %}

## Résumé des commandes

{% aller %}
[principales commandes git](./commandes-git/)

{% endaller %}

## Misc

{% aller %}

1. [Outils](./outils)
2. [Bonnes pratiques](./bonnes-pratiques)
3. [Besoins de gestion de l'historique](./besoins-historique)

{% endaller %}


## Pour aller plus loin

Outre ce qu'on a vu au préalable l'usage d'un SCM au quotidien nécessite quelques connaissances supplémentaires qui permettent de que nous allons aborder maintenant.

### Sha

{% lien %}
<https://fr.wikipedia.org/wiki/SHA-1>{.externe}
{% endlien %}

À tout objet de git est associé un nombre écrit en hexadécimal correspondant à son hash avec [la fonction de hachage](/cours/algorithmie/structure-dictionnaire/fonctions-hash/) sha-1.

Ceci permet de retrouver de façon unique (au moins en probabilité et sûrement pour un projet donné) tout ce que stocke git.

> TBD projet voir le sha.

### Diff

> TBD faire un exemple avec la commande diff au terminal : deux fichiers (lignes ≠) et deux dossiers (deux fichiers ≠)
> TBD sous windows <https://learn.microsoft.com/fr-fr/troubleshoot/windows-client/shell-experience/how-to-use-windiff-utility>{.externe} ou <https://www.git-tower.com/blog/diff-tools-windows>{.externe}

On a déjà vu le diff des fichiers lors de nos commits et en particulier lorsque l'on a résolu un conflit de fusion. Cela vaut le coût de connaître le format utilisé :

{% lien %}

- [format diff](https://www.math.utah.edu/docs/info/diff_3.html){.externe}
- [résumé en français](https://www.linuxtricks.fr/wiki/diff-et-patch-sous-linux){.externe}

{% endlien %}

Notez que l'on peut faire nous même des diff au terminal :

{% lien %}

Commande diff au terminal :

- [tuto en français](https://www.youtube.com/watch?v=0JZCah5w7I8){.externe}
- [tuto en anglais (plus concis)](https://www.youtube.com/watch?v=-CiLU9-RAGk){.externe}

{% endlien %}

Les algorithmes utilisés pour faire un diff sont basés sur [le problème de l'alignement de séquences](/cours/algorithmie/design-algorithmes/programmation-dynamique/alignement-séquences/). Ils ne travaillent cependant sur des caractères mais sur des lignes. Si cela vous intéresse suivez les liens suivant pour une introduction :

{% lien %}

- <https://medium.com/@livajorge7/understanding-the-diff-algorithm-and-its-applications-in-software-development-fe094895d92a>{.externe}
- <https://ably.com/blog/practical-guide-to-diff-algorithms>{.externe}

{% endlien %}


<!-- TBD 

> TBD numéro de commit ?

peut-être mettre le projet avant la théorie ? Ou en même temps ? 

couper en parties

1. git bisect
2. interne
-->

<!-- 

## Porcelaine et plomberie de git

> TBD expliquer porcelaine/plomberie

### Porcelaine

{% aller %}
[Git porcelaine](./git-porcelaine)
{% endaller %}

### Plomberie

> TBD un tag c'est un objet. Commit, tree ou blob.
> TBD work-trees et stash
> TBD utiliser switch et pas checkout pour passer de branches en branches (checkout pour les commits particulier: headless ?)
> TBD : index = staging area.
> TBD diff format et différents algos
> TBD <https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things>{.externe}

> TBD reflog.
> TBD git sha. Intro : <https://medium.com/@jonathan_finch/git-commit-hash-number-theory-770f67ec492d>{.externe} et <https://graphite.dev/guides/git-hash>{.externe}. Mieux : <https://www.designgurus.io/answers/detail/how-do-i-get-the-hash-for-the-current-commit-in-git>{.externe}

Cette partie du cours s'adresse plus particulièrement aux informaticiens voulant utiliser git en ligne de commande et/ou à ceux voulant comprendre le fonctionnement précis de git.

### Github actions

> TBD :
>
> - permet de mettre en place du CI/CD : <https://www.youtube.com/watch?v=scEDHsr3APg>{.externe}
> - github actions <https://www.youtube.com/watch?v=p3W2XCD3smk>{.externe} 

-->

## Bibliographie

### Cours

- [Learning Git](https://github.com/gitlearningjourney/learning-git){.externe}
- [Version control with git 3rd edition](https://www.amazon.fr/Version-Control-Git-Collaborative-Development/dp/1492091197){.externe}
- [the book](https://git-scm.com/book/en/v2){.externe}

### Références

- <https://git-scm.com/>{.externe}
- <https://comprendre-git.com/fr/>{.externe}

### Misc

- <https://learngitbranching.js.org/>{.externe}
- <https://tonyg.github.io/revctrl.org/index.html>{.externe}
- <https://ohshitgit.com/>{.externe}
- - [s'entraîner avec des commandes git](https://git-school.github.io/visualizing-git/){.externe}

## Histoire

{% lien %}

- <https://www.atikteam.com/fr/blog/page/Gestion-de-sources-centralisee-vs-decentralisee>{.externe}
- <https://blog.tarynmcmillan.com/a-history-of-version-control>{.externe}

{% endlien %}

<!-- TBD

> - git rebase avec des merges : <https://www.jnielson.com/git-rebase-with-merges>{.externe}
> - git fetch. qu'est ce qui est fetch ? Tout ou juste des branches <https://stackoverflow.com/a/74355550>{.externe}
> - force-push : expliquer ce que c'est.
> - mettre la doc de chaque commande avec la description de git en ligne de commande dans la partie plomberie et porcelaine.
> - lister tous tous les commit de la base : <https://stackoverflow.com/a/4787030>{.externe}
> - rebase les différentes commandes ?
>
>   - detached head : <https://www.cloudbees.com/blog/git-detached-head>{.externe}
>   - tous les commits : `git reflog` même ceux pas dans une branche (detached head). On peut les retrouver puis cherry pick <https://stackoverflow.com/questions/9984223/what-happens-to-git-commits-created-in-a-detached-head-state>{.externe}
>   - commit non attaché à une branche (dangling commits): `git fsck --lost-found`
>   - `git cat-files <hash>` pour voir les parents
>
> - remote :
>   - branches.
>   - ssh / https
>   - fetch et push différents : <https://stackoverflow.com/questions/31747072/will-remote-url-for-fetch-and-push-be-different>{.externe}
>   - pas forcément github ou un autre provider. Un autre ordi fait l'affaire, même juste le sien : <https://www.reddit.com/r/git/comments/5giehg/is_it_possible_to_have_a_remote_thats_on_the_same/>{.externe}
> - merge :
>   - meilleur ancêtre commun <https://git-scm.com/docs/git-merge-base>{.externe} <https://stackoverflow.com/a/73171967>{.externe}
> - conflits : <https://githowto.com/resolving_conflicts>{.externe}
> - 3-way merge : <https://tonyg.github.io/revctrl.org/ThreeWayMerge.html>{.externe}
> - réécrire l'histoire : <https://www.atlassian.com/git/tutorials/rewriting-history>{.externe}
> - pour aller plus loin :
>   - squash commit ?
>   - stash : <https://www.atlassian.com/git/tutorials/saving-changes/git-stash>{.externe}, <https://www.youtube.com/watch?v=BSLzA8oCT7g>{.externe} pour les mdp, etc
>   - worktree <https://www.youtube.com/watch?v=ntM7utSjeVU>{.externe}
>   - sous-projet
>   - git vscode
>   - bisect : <https://www.youtube.com/watch?v=Q-kqm0AgJZ8>{.externe}
>   - cherry pick : <https://www.youtube.com/watch?v=i657Bg_HAWI>{.externe} (attention : <https://www.youtube.com/watch?v=WPCxtFkLa7g>{.externe})
>
>
> - pull --rebase sinon merge à repetition : <https://www.youtube.com/watch?v=xN1-2p06Urc>{.externe} ; <https://www.youtube.com/watch?v=DkWDHzmMvyg>{.externe}
> - merge conflict : <https://www.youtube.com/watch?v=DloR0BOGNU0>{.externe}
> - cherry-pick attention ! : <https://stackoverflow.com/questions/880957/pull-all-commits-from-a-branch-push-specified-commits-to-another/881014#881014>{.externe}
> - <https://www.reddit.com/r/git/comments/mq9wh2/is_there_any_way_to_permanently_remove_commits/>{.externe} et <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>{.externe}
> - uncompress utilitaire : `pigz` <https://stackoverflow.com/a/3178638>{.externe}
> - internals git commit <https://pawelszczygielski.pl/2021/02/23/git-how-to-commit-without-git-commit/>{.externe}
> - tree object format : <https://stackoverflow.com/questions/14790681/what-is-the-internal-format-of-a-git-tree-object>{.externe}
> - internal objects: <https://shafiul.github.io/gitbook/1_the_git_object_model.html>{.externe} <https://git-scm.com/book/en/v2/Git-Internals-Git-Objects>{.externe}. Faire le code en python et pas en ruby. <https://praneethreddybilakanti.medium.com/7-git-internals-548f8707436a>{.externe}
> - git tag object avec du code en python <https://stackoverflow.com/questions/10986615/what-is-the-format-of-a-git-tag-object-and-how-to-calculate-its-sha>{.externe}
> - git index format : <https://git-scm.com/docs/index-format>{.externe} ; `git ls-files --stage` (attention: different de staged ); `git diff-index HEAD` et filetype <https://unix.stackexchange.com/questions/450480/file-permission-with-six-octal-digits-in-git-what-does-it-mean>{.externe}. Que quelques possibilités. Donc peut-être juste les lister.
> - commit jamais vraiment perdu <https://andrewallison.medium.com/oops-i-lost-my-git-commits-heres-how-to-bring-them-back-from-the-dead-90b1a62f63d1>{.externe}. Faire test avec rebase et on les retrouve.
>
> biblio :
>
> - ~ et ^ pour les ancêtres <https://stackoverflow.com/questions/2221658/what-is-the-difference-between-head-and-head-in-git>{.externe}
>
> - cours (BIEN): <https://www.youtube.com/watch?v=rH3zE7VlIMs>{.externe}, <https://www.boot.dev/teachers/the-primeagen>{.externe}
>   internals (TROP BIEN le debut puis devient trop chiant) : <https://www.youtube.com/watch?v=fWMKue-WBok&list=PL9lx0DXCC4BNUby5H58y6s2TQVLadV8v7>{.externe}
> - <https://womanonrails.com/git-rebase-onto>{.externe}
> - <https://jwiegley.github.io/git-from-the-bottom-up/>{.externe}
> - <https://tutorial.gitlabpages.inria.fr/git/>{.externe}
> - <https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain>{.externe}
> - créer son propre sha : <https://git-scm.com/book/en/v2/Git-Internals-Git-Objects>{.externe} <https://gist.github.com/masak/2415865>{.externe} et <https://stackoverflow.com/questions/552659/how-to-assign-a-git-sha1s-to-a-file-without-git/552725#552725>{.externe}
> - <https://gitirc.eu/gitrevisions.html>{.externe}
> - interactive stage <https://www.youtube.com/watch?v=UJ5fpaeZWsI>{.externe} <https://www.youtube.com/watch?v=8st1NhaKDCA>{.externe}
 -->
