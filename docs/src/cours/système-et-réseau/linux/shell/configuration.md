---
layout: layout/post.njk

title: Fichiers de configuration

eleventyNavigation:
  order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Lorsqu'un shell est crée il va lire ses fichiers de configuration qui permettent de le personnaliser.

On va ici se concentrer sur les fichiers de configuration de bash. Chaque shell va avoir sa façon de faire, faites-y attention si vous changez de shell où êtes sous mac qui par défaut a le shell zsh.

{% lien %}
Fichiers de configurations de zsh](https://scriptingosx.com/2019/06/moving-to-zsh-part-2-configuration-files/)
{% endlien %}

> TBD <https://www.youtube.com/watch?v=Yva_nTXzTTw>

## Fichiers de configurations de bash

{% lien %}
[dotfiles de bash](http://mywiki.wooledge.org/DotFiles)
{% endlien %}

Plusieurs fichiers sont lus lors de l'exécution du shell :

1. au login sur une nouvelle machine :
   1. exécution du fichier `/etc/profile`
   2. **si** un fichier `.bash_profile` existe dans votre home **alors** il est exécuté
   3. **sinon si** un fichier `.bash_login` existe dans votre home **alors** il est exécuté
   4. **sinon si** un fichier `.profile` existe dans votre home **alors** il est exécuté
2. pour des exécutions non login (c'est à dire pour des enfants du shell bash de login) :
3. lecture du fichier `.bashrc` de votre home

- Le fichier `.profile` est un standard POSIX préférez ce fichier aux autres pour mettre votre configuration de login.
- le fichier `.bashrc` n'est **pas** au login, il est d'usage de le lire à la fin du `.profile`

{% exercice %}
Que fait le fichier `/etc/profile` avec les fichiers du dossier `/etc/profile.d` ?
{% endexercice %}
{% details "solution" %}
Il va les exécuter un à un.
{% enddetails %}

## Que mettre dans les fichiers de conf

- on place dans le `.profile` les éléments qui sont transmis aux enfants donc essentiellement les variables d'environnements, en particulier [la gestion du `$PATH`](https://opensource.com/article/17/6/set-path-linux).
- le fichier `.bashrc` contient tous les éléments qui ne sont pas transmis aux shell enfants, comme les alias ou les définitions de fonctions,

### `.profile`{.fichier} minimal

Ci-après un fichier `.profile`{.fichier} minimal :

```sh#
if [ -r ~/.bashrc ]; then
    . ~/.bashrc
fi

export PATH=~/.local/bin:${PATH}

```

Les 3 premières lignes vérifient que le fichier `.bashrc`{.fichier} existe avant de l'exécuter dans le même shell.

Puis il ajoute une commande au path en définissant et créant la variable d'environnement `PATH`.

### `.bashrc`{.fichier} minimal

```sh#
export MAILDIR=~/Maildir

alias ll="ls -la"
```

Qui définie une variable d'environnement puis un alias.

{% lien %}
[les alias en bash](https://debian-facile.org/doc:programmation:bash:alias)
{% endlien %}

Créons quelques alias :

{% exercice %}
Le fichier `.bashrc`{.fichier} crée un alias `ll`. À quoi cela correspond-t-il ?
{% endexercice %}
{% details "corrigé" %}
à Chaque fois que l'on va taper la commande `ll`, le shell la remplacera par `ls -la`.
{% enddetails  %}

{% exercice %}
Créez dans un shell les deux alias suivant :

- `cd..` pour `cd ..`
- `cd...` pour `cd ../..`.

{% endexercice %}

## Fichiers de configurations des applications

{% lien %}
[Où sont rangés les fichiers de configuration](https://wiki.archlinux.org/title/XDG_Base_Directory)
{% endlien %}

Les application vont eux aussi avec des fichiers de configurations. La plupart des applications vont créer un dossier à leur nom dans votre `$HOME/.config`

Si vous avez des exécutables à vous, rangez les dans : `$HOME/.local/bin`, et n'oubliez pas d'ajouter ce dossier à votre PATH (comme on l'a fait dans l'exemple du `.profile`{.fichier}).

L'organisation des ses fichiers de préférence, appelés les _dotfiles_ est un réel sujet. La plupart d'entre nous ont un projet github contenant nos fichiers de conf pour pouvoir les déplacer facilement d'une machine à l'autre :

{% lien %}
[gestion des dotfiles](https://www.youtube.com/watch?v=5oXy6ktYs7I)
{% endlien %}
