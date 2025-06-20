---
layout: layout/post.njk

title: Gestion du code source
tags: ["cours", "projet"]
authors:
  - François Brucker
eleventyNavigation:
    prerequis:
        - "/cours/coder-et-développer/connaissances-système-minimales/fichiers-navigation/"
resume: "Comment gérer les sources d'un projet avec git et github."

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Comment gérer le code source d'un projet avec git et github.

{% lien %}

- [Qu'est ce que la gestion des sources avec github ?](https://www.youtube.com/watch?v=w3jLJU7DT5E)
- [Utilité de git pour tous](https://www.atlassian.com/fr/git/tutorials/why-git)

{% endlien %}

La gestion du code source (_Source Control Management_) est bien sûr utilisée massivement en informatique, mais les méthodes et techniques mises en œuvre fonctionnent pour tout projet où l'on doit utiliser/produire des documents qui sont modifiés au cours du temps. C'est un cadeau fait par les informaticiens au monde (ne le détruisez pas comme la gestion de projet agile...).

Un des bénéfices d'une gestion des documents bien comprise est que l'on peut :

- **archiver** et retrouver facilement toutes les évolutions d'un projet,
- travailler sur **plusieurs versions** d'un projet en même temps.

Mais surtout : **ne pas avoir peur** de modifier, tester et expérimenter des nouveautés.

Ces bénéfices sont incommensurables lorsque l'on travaille à plusieurs sur un projet et sont très utiles même pour un projet solo.

{% attention %}
Dire que l'on fait de la gestion des sources ou que l'on connaît [git](https://git-scm.com/) parce qu'on se sert de [github](https://github.com/) comme d'un drive est un mensonge et vous fera passer pour un rigolo.
{% endattention %}

## Principes

{% aller %}
[Principes](./principes){.interne}
{% endaller %}

## Github

> TBD voir les diff + format.

> 3. git
>     1. avec Github
>     1. idem avec Github desktop

<https://github.com/> est une interface au logiciel de gestion de sources [git](https://fr.wikipedia.org/wiki/Git). Il en existe d'autres, comme <https://gitlab.com/> par exemple.

{% info %}
L'[aide de github](https://docs.github.com/en/get-started) est très bien faite, n'hésitez pas à y jeter un coup d'œil.
{% endinfo %}

### <span id="compte-github"></span> Création du compte github

1. créez votre compte avec github
   - On crée ici votre compte github _pro_, ne mettez pas de bêtises
   - Utilisez une adresse mail pérenne (genre votre adresse pro gmail ou votre adresse ecm)
2. modifier son profile :
   1. Allez dans la modification du profile :
      - en haut à droite de la fenêtre puis _"Your profile"_
      - ou `https://github.com/<votre login>` en remplaçant `<votre login>` par votre login.
   2. Il **faut** mettre de bonnes info car lorsque vous modifiez le code vous êtes responsable de ce que vous modifiez. Il faut donc :
      - savoir qui a modifier le code et pourvoir le retrouver
      - votre compte github est aussi votre book. Il permet de savoir ce que vous avez fait.
      - Mettez donc au moins :
        - un vrai nom
        - une vrai photo (rechargez la page pour avoir la nouvelle photo)

### <span id="tuto-github"></span> Utilisation de github

On va aller un peu plus loin en voyant, directement avec le site les principales fonctionnalités de git.

{% aller %}
[Comment créer un projet uniquement avec github](./projet-github){.interne}
{% endaller %}

Vous avez vu les principales qualités d'un logiciel de gestion de sources :

- faire des commit
- gérer des branches
- fusionner des branches en résolvant des conflits
- voir l'historique du projet
- comment ajouter des membres à un projet

### <span id="utilisation-desktop-github"></span> Github desktop

Travailler depuis le site uniquement est très limitant. Github est le lieu où est stocké du projet, l'outil qui fait tout fonctionner est [git](https://fr.wikipedia.org/wiki/Git). Avant d'utiliser la ligne de commande qui peut être intimidante, utilisant une application développée par github qui permet d'en utiliser les fonctions les plus courantes.

{% lien %}

Il suffit d'aller sur cette page : <https://desktop.github.com/> pour télécharger puis installer l'application.

{% endlien %}

On va reprendre le projet précédent pour créer son projet chez soit ainsi que l'origin en utilisant l'application desktop.

{% aller %}
[Comment créer un projet avec l'application desktop](./projet-github-desktop){.interne}
{% endaller %}

Vous avez vu les principales qualités d'un logiciel de gestion de sources :

- faire un clone
- notion de gestion distribuée
- le stage
- faire un rebase

## Gérer ses sources

> TBD noms : Git flow ? Github flow ? Feature branches ? Push to prod ?
> 4. workflow :
>     1. github-flow : peut avoir plein de branches features en parallel mais une seule branche develop
>     2. git-flow (rigide et plein de branches) <https://leanpub.com/git-flow/read>
>     3. différences <https://www.youtube.com/watch?v=hG_P6IRAjNQ>
>     4. ci-cd extrême inverse <https://www.youtube.com/watch?v=v4Ijkq6Myfc> : beaucoup de tests automatisé pour vérifier bien que tout peut aller vite en prod. et être corrigé. La prod est le dernier endroit ou votre code est testé, certes, mais ça ne doit pas être le seul
>     5. dépend du projet et on s'adapte
>
>
> TBD refaire

{% aller %}
[Utiliser les bonnes pratiques lors d'un projet github](./bonnes-pratiques){.interne}
{% endaller %}

Pour participer à un repo github/gitlab il y a quelques us et coutumes à respecter afin de permettre au mieux la relecture, l'ajout de fonctionnalités et la compréhension de chacun.

## Git

> TBD expliquer porcelaine/plomberie
> TBD un tag c'est un objet. Commit, tree ou blob.
> TBD worktrees et stash
> TBD utiliser switch et pas checkout pour passer de branches en branches (chekout pour les commits particulier: headless ?)
> TBD : index = staging area.
> TBD diff format et différents algos

### Installation et configuration

{% aller %}
[Configurer et initialiser ses projets git](./git-init){.interne}
{% endaller %}

### Porcelaine

> - histoire ?

> 5. ligne de commandes
>     1. projet avec ligne de commande
>     2. outils (lazygit, vscode)
>
> Outils :

> - lazygit : <https://github.com/jesseduffield/lazygit> <https://www.youtube.com/watch?v=Ihg37znaiBo>
> - <https://www.git-tower.com/learn/git/faq/git-filter-repo>
> - github actions <https://www.youtube.com/watch?v=p3W2XCD3smk>

Les notions que l'on a vu précédemment suffisent pour un usage courant de la gestion des sources avec github. Si vous voulez :

- utiliser git avec votre éditeur de texte comme vscode
- ou si vous voulez utiliser git en ligne de commande pour contrôler toutes vos opérations

Il vous faudra installer le programme `git` en ligne de commande.

{% info %}
L'installation et la configuration de git n'est pas très technique. Cela vaut le coup de de le faire ne serait-ce que pour pouvoir utiliser les magnifiques plugins de vscode.
{% endinfo %}

#### Utilisation de git avec vscode

{% info "**Documentation**" %}
<https://code.visualstudio.com/docs/editor/versioncontrol#_git-support>
{% endinfo %}

vscode permet d'utiliser directement les commandes git et possède de nombreux plugins permettant, par exemples :

- d'utiliser github avec l'[extension github](https://code.visualstudio.com/docs/editor/github)
- de voir le graphe de dépendances avec l'extension [git-graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) (commande `git-graph.view` pour voir le graphe)
- de voir l'historique de modification d'un fichier avec l'extension [git-history](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) (cliquer droit sur un fichier puis `Git: view file history`)
- ...

### Plomberie

> TBD ajouter à la partie comment faire en vrai :
{% aller %}
[Cours détaillé sur le fonctionnement de Git](./git){.interne}
{% endaller %}

Cette partie du cours s'adresse plus particulièrement aux informaticiens voulant utiliser git en ligne de commande et/ou à ceux voulant comprendre le fonctionnement précis de git.

## Histoire

>TBD histoire de la gestion des sources :
>
> - <https://www.atikteam.com/fr/blog/page/Gestion-de-sources-centralisee-vs-decentralisee>
> - <https://blog.tarynmcmillan.com/a-history-of-version-control>
>
> TBD : à étoffer et à mettre en perspective

## TBD

> - mettre la doc de chaque commande avec la description de git en ligne de commande dans la partie plomberie et porcelaine.
> - lister tous tous les commit de la base : <https://stackoverflow.com/a/4787030>
> - rebase les différentes commandes ?
> - jouer avec le DAG des commits
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
>   - alignement, les algorithmes : dire que c'est comme l'alignement de séquence mais avec des lignes (ref)
>   - meilleur ancêtre commun <https://git-scm.com/docs/git-merge-base> <https://stackoverflow.com/a/73171967>

>   - conflits : <https://githowto.com/resolving_conflicts>
>   - 3-way merge : <https://tonyg.github.io/revctrl.org/ThreeWayMerge.html>
> - réécrire l'histoire : <https://www.atlassian.com/git/tutorials/rewriting-history>
> - pour aller plus loin :
>   - squash commit ?
>   - stash : <https://www.atlassian.com/git/tutorials/saving-changes/git-stash>,  <https://www.youtube.com/watch?v=BSLzA8oCT7g> pour les mdp, etc
>   - worktree <https://www.youtube.com/watch?v=ntM7utSjeVU>
>   - sous-projet
>   - git vscode
>   - bisect : <https://www.youtube.com/watch?v=Q-kqm0AgJZ8>
>   - cherry pick : <https://www.youtube.com/watch?v=i657Bg_HAWI> (attention : <https://www.youtube.com/watch?v=WPCxtFkLa7g>)
>
> TBD :
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
> - diff <https://medium.com/@livajorge7/understanding-the-diff-algorithm-and-its-applications-in-software-development-fe094895d92a> et <https://ably.com/blog/practical-guide-to-diff-algorithms>, <https://en.m.wikipedia.org/wiki/Diff> et <https://git-scm.com/docs/git-diff>
> - commit jamais vraiment perdu <https://andrewallison.medium.com/oops-i-lost-my-git-commits-heres-how-to-bring-them-back-from-the-dead-90b1a62f63d1>. Faire test avec  rebase et on les retrouve.
>
> biblio :
>
> - ~ et ^ pour les ancêtres <https://stackoverflow.com/questions/2221658/what-is-the-difference-between-head-and-head-in-git>
> - <https://github.com/gitlearningjourney/learning-git>
> - cours (BIEN): <https://www.youtube.com/watch?v=rH3zE7VlIMs>, <https://www.boot.dev/teachers/the-primeagen>
> internals (TROP BIEN le debut puis devient trop chiant) : <https://www.youtube.com/watch?v=fWMKue-WBok&list=PL9lx0DXCC4BNUby5H58y6s2TQVLadV8v7>
> - <https://womanonrails.com/git-rebase-onto>
> - <https://jwiegley.github.io/git-from-the-bottom-up/>
> - <https://tutorial.gitlabpages.inria.fr/git/>
> - <https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain>
> - créer son propre sha : <https://git-scm.com/book/en/v2/Git-Internals-Git-Objects> <https://gist.github.com/masak/2415865> et <https://stackoverflow.com/questions/552659/how-to-assign-a-git-sha1s-to-a-file-without-git/552725#552725>
> - <https://ohshitgit.com/>
> - <https://gitirc.eu/gitrevisions.html>
> - `git diff` <https://www.youtube.com/watch?v=F1van9nShjA>
> - diff / patch : fr <https://www.youtube.com/watch?v=0JZCah5w7I8> en (plux concis) <https://www.youtube.com/watch?v=-CiLU9-RAGk>
> - interactive stage <https://www.youtube.com/watch?v=UJ5fpaeZWsI> <https://www.youtube.com/watch?v=8st1NhaKDCA>
> - <https://learngitbranching.js.org/>
> - <https://git-school.github.io/visualizing-git/>
