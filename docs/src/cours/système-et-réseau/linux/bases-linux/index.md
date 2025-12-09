---
layout: layout/post.njk

title: Bases Linux

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Linux à proprement parler ne concerne que [le noyau](https://fr.wikipedia.org/wiki/Noyau_Linux), dont le rôle est la gestion du matériel et la bonne entente entre processus. C'est pourquoi on parle souvent de **_Distribution Linux_** qui contient :

- le noyau Linux
- logiciels
- des outils de configurations

Par exemple les distributions GNU/Linux où [GNU](https://www.gnu.org/) fournit tous les outils et logiciels utilisées par le noyau Linux pour créer un système d'exploitation complet. Il existe de nombreuses distributions Linux, elles se distinguent par leur gestion des logiciels à installer via un [gestionnaire de paquets](https://fr.wikipedia.org/wiki/Gestionnaire_de_paquets) qui gère les dépendances (nombreuses) entre les différents paquets :

- [apt](https://fr.wikipedia.org/wiki/Advanced_Packaging_Tool) et paquets d'extension `.deb`{.fichier} pour [la distribution Debian](https://www.debian.org/index.fr.html)
- [rpm](https://en.wikipedia.org/wiki/RPM_Package_Manager) et paquets d'extension `.rpm`{.fichier} pour [la distribution Redhat](https://www.redhat.com/fr)
- [pacman](https://fr.wikipedia.org/wiki/Pacman_(Arch_Linux)) pour [la distribution Arch](https://archlinux.org/)

De ces trois distributions majeures et générales vont découler nombres d'autres plus spécialisées utilisant le même gestionnaire de paquets. Par exemple :

- [Ubuntu](https://www.ubuntu-fr.org/) pour Debian
- [Fedora](https://www.fedoraproject.org/fr/) pour Redhat
- [Manjaro](https://manjaro.org/) pour Arch

Pour connaître sa distribution :

```shell
❯ uname -a
Darwin so-high.local 25.1.0 Darwin Kernel Version 25.1.0: Mon Oct 20 19:26:04 PDT 2025; root:xnu-12377.41.6~2/RELEASE_ARM64_T8122 arm64

```

La plupart des distributions Linux suivent une règle : KISS (Keep It Simple, Stupid). Chaque commande fait une seule chose simple comme lister des fichiers ou compter le nombre de lignes. La complexité et l’intelligence ne viennent pas des commandes : c’est la combinaison de ces commandes bêtes qui fait quelque chose d’intelligent.

Autre chose à noter : il faut que le terminal devienne notre meilleur ami ! C’est l’outil principal qu’on utilise en permanence. Il faut se familiariser avec et apprendre à naviguer avec.

## Système de Fichier

### Arborescence système Linux

{% lien %}
[hiérarchie-fichiers](fhiérarchie-fichiers){.interne}
{% endlien %}

### Droits

{% lien %}
[fichiers et droits](fichiers-droits){.interne}
{% endlien %}

## TBD : refactor

> TBD Dans ce qui suit des choses simples qui peuvent rester dans bases et des choses bien plus compliquées qui doivent passer dans shell par exemple


1. [commandes](./commandes){.interne}
2. [process](process){.interne}
3. [exercices](exercices){.interne}

## Bibliographie

- très didactique. Deux séries de vidéos :
  - <https://www.youtube.com/watch?v=EYRWohJeCkk&list=PLQqbP89HgbbbD0WSKRR90R5yjmTpSNNIl>
  - <https://www.youtube.com/watch?v=M5dZHdN-Aac&list=PLQqbP89HgbbY23Ab_vXGfLXHygquD7cAs>
- <https://ubuntu.com/tutorials/command-line-for-beginners#1-overview>
- <https://www.youtube.com/watch?v=sAD4dq_jDTA&list=PLShDm2AZYnK1SdG3dufPdCqk08sOahUBP>
- <https://www.youtube.com/watch?v=QlWKQAh7MKc&list=PLTXMX1FE5Hj6QRdYfuLsTdwCDDISV9TtB>
- <https://www.youtube.com/watch?v=k89LskKoc1E&list=PL6tu16kXT9Po1kDfJXv0XDSatvGhbC3_X&index=1>
