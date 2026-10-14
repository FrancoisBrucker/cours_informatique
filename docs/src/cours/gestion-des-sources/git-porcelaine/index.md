---
layout: layout/post.njk

title: Git porcelaine

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD à jardiner et réorganiser. Des redites, des choses qui manquent et peut-être des choses à mettre en plomberie
>
> TBD utiliser `git diff` <https://www.youtube.com/watch?v=F1van9nShjA>{.externe} et ref : <https://git-scm.com/docs/git-diff>{.externe}
>
> TBD utiliser tous les usages vue dans les parties précédentes (même add/reset -p)

> TBD utiliser gh pour s'authentifier et créer un repo git. <https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-using-git>{.externe} et <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github#authenticating-with-the-command-line>{.externe}
>

Comment fonctionne git et ses utilisations en ligne de commande.

## Rebase en détails

{% aller %}

[Rebase en détails](./rebase)

{% endaller %}

Rebase vs merge. Comment et quand les utiliser.

## Commits atomiques

{% aller %}

[Commits atomiques](./commit-atomiques)

{% endaller %}

Commenter des parties homogènes "en fonction" de code.

## Bibliographie

> TBD à jardiner

{% lien %}

- initialisation git/github par défaut :
  - [doc officielle](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup){.externe}
  - [git et github](https://kbroman.org/github_tutorial/pages/first_time.html){.externe}
- guide général :
  - [sympa et en français](https://www.miximum.fr/blog/decouvrir-git/){.externe}
  - [guide de Karl Broman](https://kbroman.org/github_tutorial/){.externe}. Très bien fait et va au but.
  - [pro git](https://git-scm.com/book/en/v2){.externe}. Y'a tout. Peut-être parfois un peu t\*rop. Mais si on a un problème il y a forcément la solution là dedans.
  - [git magic](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/fr/index.html){.externe}. En français. Très intéressant à suivre également, il donne des infos différente du tuto de Karl Broman.
  - playlist YouTube :
    - [coding train playlist](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV){.externe}. Sympa à écouter et faire. Passe pas mal de temps au début avec github.
    - [grafikart](https://www.youtube.com/watch?v=rP3T0Ee6pLU&list=PLjwdMgw5TTLXuY5i7RW0QqGdW0NZntqiP){.externe}. En français s'il vous plait.
  - [version control with git](https://www.amazon.fr/Version-Control-Git-collaborative-development-ebook/dp/B008Y4OR3A){.externe}. Un très bon livre qui explique en détail le fonctionnement de git.
- commandes :
  - [toutes les commandes](https://git-scm.com/docs/git#_git_commands){.externe}
  - [commandes courante](https://www.hostinger.fr/tutoriels/commandes-git/){.externe}
  - [une cheat sheet](https://training.github.com/downloads/fr/github-git-cheat-sheet.pdf){.externe}
- misc :
  - du git en 3 parties [partie 1](https://www.daolf.com/posts/git-series-part-1/){.externe}
  - tout ce que vous avez toujours voulu savoir sur [rebase t quand l'utiliser](https://delicious-insights.com/fr/articles/bien-utiliser-git-merge-et-rebase){.externe}

{% endlien %}
