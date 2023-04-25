---
layout: layout/post.njk

title: Brew
tags: ['tutoriel', 'système', 'mac']
authors:
    - "François Brucker"

eleventyNavigation:
  prerequis:
      - '../terminal/'


eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: Tutoriels
---

<!-- début résumé -->

Installation de <https://brew.sh> sur un ordinateur mac

<!-- fin résumé -->

Lorsque l'on utilise le [terminal]({{ "/tutoriels/terminal" | url }}){.interne} avec son mac, il faut souvent installer tout un tas de logiciels unix (comme python par exemple).

Le logiciel <https://brew.sh> vous permet de faire ça sans soucis.

1. installez le en copiant/collant puis en appuyant sur la touche entrée la ligne de commande suivante dans un terminal : `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. si vous avez un mac avec une puce M1, il vous faudra également taper la commande `echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> $HOME/.zprofile`
3. quittez l'application terminal ("menu du nom de l'application > quitter" ou  `cmd + Q`), puis la relancer pour que les fichiers de configuration soient à jour.

{% info %}
* <https://github.com/Homebrew/discussions/discussions/446>
* qu'est-ce que `.zprofile`  : <https://unix.stackexchange.com/questions/71253/what-should-shouldnt-go-in-zshenv-zshrc-zlogin-zprofile-zlogout>
{% endinfo %}

Ensuite, vous pourrez utiliser des commandes comme `brew install python3` pour installer python ou encore `brew install tmux` pour les plus geek d'entre nous.
