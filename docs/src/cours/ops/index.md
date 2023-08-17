---
layout: layout/post.njk

title: Ops
tags: ['cours', 'unix', 'système']
authors:
    - "François Brucker"

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: Cours
---

<!-- début résumé -->

Cours introduction à l'*ops* du dev**ops**.

<!-- fin résumé -->
{% prerequis %}

* [Avoir un système en état de marche]({{ '/tutoriels/installation-système'  }})
* [Savoir naviguer dans un système de fichiers]({{ '/tutoriels/fichiers-navigation'  }})
* [Savoir ouvrir une fenêtre terminal]({{ '/tutoriels/terminal'   }})
* [D'installez brew si vous êtes sous mac]({{ '/tutoriels/brew'   }})

{% endprerequis %}

Nous verrons dans ce cours quelques fondamentaux de ce que doit savoir un développeur s'il veut pouvoir comprendre et interagir avec son administrateur système et un serveur distant (unix).


1. [cryptographie](./cryptographie){.interne}
2. [ssh](./ssh){.interne}
3. shell : <http://luffah.xyz/bidules/Terminus/>
4. système unix
5. docker

> TBD remplir les blancs (c'est à dire quasi tout)
