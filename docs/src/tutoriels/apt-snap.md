---
layout: layout/post.njk

title: Apt et snap
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

Utilisation des gestionnaires de package `apt` et `snap`

<!-- fin résumé -->

`apt` et `snap` sont deux applications permettant d'installer des applications via le [terminal]({{ "/tutoriels/terminal" | url }}){.interne} avec un système d'exploitation Linux/Ubuntu.

On utilise en utilise deux, via le terminal :

* [apt](https://doc.ubuntu-fr.org/apt) pour les installations Ubuntu
* [snap](https://doc.ubuntu-fr.org/snap) pour les installations standalone

## Droits administrateurs

Pour utiliser ces gestionnaires, il vous faut avoir les droits administrateurs. Ceci se fait via la commande [sudo](https://doc.ubuntu-fr.org/utilisateurs/roschan/sudo) (une [petite blague d'informaticien](https://xkcd.com/149/) à propos de sudo). Par exemple, pour mettre à jour la liste des paquets installables, tapez dans un terminal :

```
sudo apt update
```

{% info %}
La commande `sudo` vous demandera votre mot de passe pour vérifier que c'est bien vous avant que la commande ne s'exécute.
{% endinfo %}

Si vous exécutez juste `apt update`, la commande refusera de s'exécuter car vous n'êtes pas le super-utilisateur (dont le nom est `root`) : vous n'avez pas le droit de modifier les fichiers nécessaire  à la mise à jour.

Une fois les paquets mis à jour, vous pouvez les mettre à jour en tapant dans un terminal :

```
sudo apt upgrade
```

{% info %}
Si vous avez tapez la commande précédente peu de temps après la commande précédente contenant sudo, vous n'avez pas eu besoin de taper votre mot de passe. C'est le fonctionnement normal de sudo, qui évite de devoir constamment taper son mot de passe si on enchaîne les commande avec `sudo`.
{% endinfo %}

## apt

On utilise apt pour l'installation de paquets liés à la distribution ubuntu : les paquets sont maintenus par des personnes liées à la distribution que vous utilisez, ou de confiance.

{% lien %}

* [le manuel](https://manpages.ubuntu.com/manpages/xenial/man8/apt.8.html)
* [un tuto pour utiliser apt](https://debian-facile.org/doc:systeme:apt:apt).
{% endlien %}

L'intérêt d'utiliser apt pour installer des applications et que les *dépendances* (c'est à dire les différentes application ou bibliothèques nécessaires à l'installation de son paquet) sont gérés automatiquement.

Il est de plus très facile de connaître l'ensemble des paquets installé et de les mettre à jour.

{% info %}
Vous verrez sûrement quelques tuto utiliser `apt-get` plutôt que `apt`.

La commande `apt` est sensée remplacer `apt-get` pour la plupart des instructions. Vous trouverez ci-aprèß deux lien qui montrent les différences, mais dans le doute utilisez `apt`.

* <https://aws.amazon.com/fr/compare/the-difference-between-apt-and-apt-get>
* <https://itsfoss.com/apt-vs-apt-get-difference/>

{% endinfo %}

## snap

{% lien %}

* le store : <https://snapcraft.io/store>
* [un tutoriel](https://debian-facile.org/doc:systeme:snap)
{% endlien %}

L'outils snap permet d'installer des applications, souvent des application tierces non maintenues par les administrateurs de Ubuntu, en incluant directement toutes les dépendances.

Il n'y a donc pas de paquets supplémentaires à installer mais les applications sont souvent plus grosses puisque toutes les dépendances sont directement installées dans l'application (un peu comme une application Macos).


