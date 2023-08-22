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

1. [architecture d'un ordinateur](./architecture-ordinateur){.interne}
2. [installation Linux](installation-linux){.interne}
3. [base Linux](bases-linux){.interne}
4. [cryptographie](./cryptographie){.interne}
5. [ssh](./ssh){.interne}
6. shell : <http://luffah.xyz/bidules/Terminus/>
7. système unix
8. docker

> TBD remplir les blancs (c'est à dire quasi tout)
