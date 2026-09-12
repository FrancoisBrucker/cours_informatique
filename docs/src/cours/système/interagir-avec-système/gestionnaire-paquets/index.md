---
layout: layout/post.njk

title: Gestionnaire de paquets
eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Sous Linux, Macos et depuis plus récemment sous windows, l'installation d'applications se fait via l'utilisation d'[un gestionnaire de paquets](https://fr.wikipedia.org/wiki/Gestionnaire_de_paquets).

## Windows

### Windows store

Le [Windows store](https://apps.microsoft.com/home?hl=fr-FR&gl=US) va contenir de nombreuses applications, dont certaines utiles pour le développement (comme le langage python par exemple). Cela vaut toujours le coup de vérifier si l'application que l'on cherche à installer n'y est pas mais la plupart des logiciel système n'y sont pas.


### Winget

Depuis quelque temps les logiciels systèmes sous windows peuvent s'installer via [winget](https://learn.microsoft.com/fr-fr/windows/package-manager/). Il fonctionne avec [le terminal](../terminal/bases/){.interne} et contient plein d'outils système.

Quelques commandes utiles :

- trouver une application 
  - spécifique : `winget search <app name>`
  - lister toutes les applications : `winget list`
- installer une application : `winget install <app ID>`
- supprimer an app: `winget uninstall <app ID>`
- Mettre à jour 
  - une application : `winget upgrade <app ID>`
  - toute les applications : `winget upgrade --all`

## Macos

### App store

L'[App store](https://www.apple.com/fr/app-store/) permet d'installer les outils génériques utiles pour l'utilisation de son mac. Cela vaut toujours le coup de vérifier si l'application que l'on cherche à installer n'y est pas mais la plupart des logiciel système n'y sont pas.

### Brew

{% lien "**Documentation**" %}
<https://brew.sh>
{% endlien %}

Lorsque l'on utilise son mac pour le développement, il faut souvent installer tout un tas de logiciels unix. Le logiciel brew vous permet de le faire avec [le terminal](../terminal/bases/){.interne}  sans soucis.

1. installez le en copiant/collant la ligne de commande demandée dans un terminal.
2. si vous avez un mac avec une puce M1, il vous faudra également taper la commande `echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> $HOME/.zprofile`
3. quittez l'application terminal ("menu du nom de l'application > quitter" ou  `cmd + Q`), puis la relancer pour que les fichiers de configuration soient à jour.

Vous pourrez ensuite utiliser des commandes comme `brew install python3` pour installer python ou encore `brew install wezterm` pour les plus geek d'entre nous.


{% attention2 "**À retenir**" %}

N'installez **aucun logiciel unix** sous mac à la main. Utilisez toujours [brew](https://brew.sh/index_fr) pour le faire.

{% endattention2 %}

## Linux


`apt` et `snap` sont deux applications permettant d'installer des applications via [le terminal](../terminal/bases/){.interne} avec un système d'exploitation Linux/Ubuntu :

- [apt](https://doc.ubuntu-fr.org/apt) pour les installations Ubuntu
- [snap](https://doc.ubuntu-fr.org/snap) pour les installations standalone

Pour utiliser ces gestionnaires, il vous faut avoir les droits administrateurs. Ceci se fait via la commande [sudo](https://doc.ubuntu-fr.org/utilisateurs/roschan/sudo) (une [petite blague d'informaticien](https://xkcd.com/149/) à propos de sudo). 

{% info %}
La commande `sudo` vous demandera votre mot de passe pour vérifier que c'est bien vous avant que la commande ne s'exécute.
{% endinfo %}



### apt


Par exemple, pour mettre à jour la liste des paquets installables , tapez dans un terminal :

```
sudo apt update
```

Si vous exécutez juste `apt update`, la commande refusera de s'exécuter car vous n'êtes pas le super-utilisateur (dont le nom est `root`) : vous n'avez pas le droit de modifier les fichiers nécessaire  à la mise à jour.

Une fois les paquets mis à jour, vous pouvez les mettre à jour en tapant dans un terminal :

```
sudo apt upgrade
```

{% info %}
Si vous avez tapez la commande précédente peu de temps après la commande précédente contenant sudo, vous n'avez pas eu besoin de taper votre mot de passe. C'est le fonctionnement normal de sudo, qui évite de devoir constamment taper son mot de passe si on enchaîne les commande avec `sudo`.
{% endinfo %}





On utilise apt pour l'installation de paquets liés à la distribution ubuntu : les paquets sont maintenus par des personnes liées à la distribution que vous utilisez, ou de confiance.

{% lien %}

- [le manuel](https://manpages.ubuntu.com/manpages/xenial/man8/apt.8.html)
- [un tuto pour utiliser apt](https://debian-facile.org/doc:systeme:apt:apt).
{% endlien %}

L'intérêt d'utiliser apt pour installer des applications et que les *dépendances* (c'est à dire les différentes application ou bibliothèques nécessaires à l'installation de son paquet) sont gérés automatiquement.

Il est de plus très facile de connaître l'ensemble des paquets installé et de les mettre à jour.

{% info %}
Vous verrez sûrement quelques tuto utiliser `apt-get` plutôt que `apt`.

La commande `apt` est sensée remplacer `apt-get` pour la plupart des instructions. Vous trouverez ci-aprèß deux lien qui montrent les différences, mais dans le doute utilisez `apt`.

- <https://aws.amazon.com/fr/compare/the-difference-between-apt-and-apt-get>
- <https://itsfoss.com/apt-vs-apt-get-difference/>

{% endinfo %}


### Snap

{% lien %}

- le store : <https://snapcraft.io/store>
- [un tutoriel](https://debian-facile.org/doc:systeme:snap)
{% endlien %}


L'outils snap permet d'installer des applications, souvent des application tierces non maintenues par les administrateurs de Ubuntu, en incluant directement toutes les dépendances.

Il n'y a donc pas de paquets supplémentaires à installer mais les applications sont souvent plus grosses puisque toutes les dépendances sont directement installées dans l'application (un peu comme une application Macos).
