---
layout: layout/post.njk 

title: Git dans les détails

eleventyNavigation:
  key: "Git dans les détails"
  parent: "Gestion des sources"
---
{% prerequis "**Prérequis** :" %}

* [Utilisation du Terminal]({{ "/tutoriels/terminal-utilisation" | url }})
* [Naviguer dans un système de fichiers]({{ "/tutoriels/fichiers-navigation" | url }})

{% endprerequis %}
<!-- début résumé -->

Comment fonctionne git et ses utilisations en ligne de commande.

<!-- fin résumé -->

## projet git

{% chemin %}

[Projet git](projet-git)

{% endchemin %}

Où l'on rentre quand même pas mal dans les détails pour comprendre comment fonctionne ce (merveilleux) outils.

## Commandes indispensables

{% chemin %}

[Commandes](commandes)

{% endchemin %}

Les commandes indispensables à connaître pour gérer un projet `git` en lignes de commandes.

## rebase en détails

{% chemin %}

[Rebase en détails](rebase)

{% endchemin %}

Rebase vs merge. Comment et quand les utiliser.

## Commits atomiques

{% chemin %}

[Commits atomiques](commit-atomiques)

{% endchemin %}

Commenter des parties homogènes "en fonction" de code.

## Bibliographie

* [githug](https://github.com/Gazler/githug) apprenez git par l'exemple.
* initialisation git/github par défaut :
  * [doc officielle](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
  * [git et github](https://kbroman.org/github_tutorial/pages/first_time.html)
* guide général :
  * [sympa et en français](https://www.miximum.fr/blog/decouvrir-git/)
  * [guide de Karl Broman](https://kbroman.org/github_tutorial/). Très bien fait et va au but.
  * [pro git](https://git-scm.com/book/en/v2). Y'a tout. Peut-être parfois un peu t*rop. Mais si on a un problème il y a forcément la solution là dedans.
  * [git magic](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/fr/index.html). En français. Très intéressant à suivre également, il donne des infos différente du tuto de Karl Broman.
  * playlist YouTube :
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
