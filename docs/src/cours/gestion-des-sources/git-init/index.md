---
layout: layout/post.njk
title: Installation et configuration de Git

eleventyNavigation:
  prerequis:
    - "/cours/système/interagir-avec-système/terminal/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Installation et configuration de git pour github.

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

On utilise [brew](/cours/système-et-réseau/bases-système/système-installation/brew/){.interne} :

```shell
brew install git
```

{% enddetails %}

{% details "Windows" %}

{% lien %}
<https://learn.microsoft.com/fr-fr/windows/package-manager/winget/>
{% endlien %}

```shell
winget install --id Git.Git -e --source winget
```

{% enddetails %}

### Github cli

Vous pouvez aussi télécharger l'utilitaire de github pour la ligne de commande : [github CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).

{% info %}
CLI signifie Command Line Interface.
{% endinfo %}

Nous ne l'utiliserons pas ici, mais je vous invite à lire [sa documentation](https://cli.github.com/manual/), il permet d'interagir avec github uniquement à la ligne de commande sans cliquer sur aucun bouton, ce qui est plus rapide.

### Vscode

Il existe de nombreux plugins possibles pour [l'éditeur vscode](https://code.visualstudio.com/). Nous en utiliserons 2, en plus du plugin par défaut :

- [git history](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory)
- [git ignore](https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore)

## Configuration

{% lien %}
[configuration de git](https://git-scm.com/book/fr/v2/Personnalisation-de-Git-Configuration-de-Git)
{% endlien %}

Vous allez travailler sur vos projets git à plusieurs. Il faut pouvoir à tout moment savoir qui a fait quoi sur le projet. Il est donc impératif que vos données personnelles soient à jour.

La configuration de git s'effectue à trois niveaux successifs :

1. au niveau du système. Le fichier par défaut est `/etc/gitconfig`{.fichier} sous unix.
2. au niveau du compte. Par défaut le fichier de configuration de git est `~/.gitconfig`{.fichier}.
3. au niveau de chaque projet. Par défaut le fichier de configuration de git est `.git/config`{.fichier} à la racine du projet

On mettra les informations générales dans le fichier de configuration du compte (identité et comportement général de git) avec la commande `git config --global <variable> <valeur>` et les informations spécifiques pouvant changer dans la configuration du projet (les origines par exemple) avec la commande `git config <variable> <valeur>`.

### Info personnelles

Renseigner ces infos de façon globale pour tout projet (vous pourrez changer ces infos pour chaque projet, mais mettez des infos corrects par défaut) :

{% faire "**Dans un terminal, tapez les commandes**" %}

```shell
git config --global user.name "Your name here"
git config --global user.email "your_email@example.com"
```

{% endfaire %}

### Rebase comme fusion par défaut

On définie tout de suite la stratégie de fusion.

{% faire "**Dans un terminal, tapez la commande**" %}

```shell
git config --global pull.rebase merges
```

{% endfaire %}

Ceci nous permettra par défaut :

- de faire un rebase de l'origin sur votre branche locale
- de préserver les merge (fusion) de branches déjà présentes (et qui donc, si elles existent, ont une fonction _sémantique_ dans votre projet)

Vous pourrez ensuite faire des `git pull` tout seul et ils seront rebasés par défaut et préserveront les merges existant. Le meilleur des deux monde en somme.

### Branche par défaut

Pour être cohérent avec github, on va dire que tout nouveau projet commence avec la branche `main`.

Par défaut c'est `master` (et ça [fait des histoires](https://github.com/github/renaming?tab=readme-ov-file)).

{% faire "**Dans un terminal, tapez la commande**" %}

```shell
git config --global init.defaultBranch "main"
```

{% endfaire %}

### Éditeur de messages

On va mettre vscode comme éditeur par défaut pour renseigner les commits.

{% faire "**Dans un terminal, tapez la commande**" %}

```shell
git config --global core.editor "code --wait"
```

{% endfaire %}

Vous n'utiliserez que très peu l'éditeur par défaut une fois que vous ferez vos commit avec l'option `-m`.

{% info %}
Par défaut l'éditeur est `vi`. Il sera toujours présent quelque soit l'endroit où au aurez besoin de faire un commit sur un système unix (genre un serveur distant). Attention cet éditeur fonctionne de façon totalement différente que ce dont on a l'habitude. 

{% endinfo %}

### Configurations optionnelles

On met de la couleur dans le terminal par défaut.

{% faire "**Dans un terminal, tapez la commande**" %}

```shell
git config --global color.ui true
```

{% endfaire %}

Pour éviter d'avoir un pager lors des `git log`.

{% faire "**Dans un terminal, tapez la commande**" %}

```shell
git config --global pager.log false
```

{% endfaire %}

Si l'on ne met pas cette option, les logs seront automatiquement passé à `more` par défaut pour paginer les résultats.

{% info %}

On obtiendrait le même résultat sans utiliser la config ci-dessus en utilisant l'argument de git `--no-pager`, par exemple :`git --no-pager log`. Notez que `--no-pager` est un argument de git, pas de sa commande `log`, il est donc placé avant celle-ci.

{% endinfo %}
