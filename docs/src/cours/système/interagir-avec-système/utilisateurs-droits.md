---
layout: layout/post.njk

title: Utilisateurs et droits d'utilisation

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD pour l'instant OS = exécution de programmes en parallèle et accès aux devices 
> il reste 3 choses :
> 1. données
> 2. qui les utilise (séparer le système d'un utilisateur normal et plusieurs utilisateurs)
> 3. comment les utiliser : application et terminal

> TBD rester simple (au niveau de google). admin/root (sudo) vs reste.

Si tous les process du user mode pouvaient effectuer tous les appels systèmes sans restriction cela poseraient d'énormes problèmes de sécurité (un process pourrait accéder à toute la mémoire, en particulier celle réservée à d'autres process par exemple) c'est pourquoi chaque process n'a qu'un nombre restreint de possibilités (on appelle ceci [des droits](<https://fr.wikipedia.org/wiki/Droit_d%27acc%C3%A8s_(informatique)>)) gérés via la notion d'utilisateurs.


## Utilisateurs et groupes

Du point de vue du système d'exploitation un utilisateur est une entité permettant d'exécuter des processus. L'utilisateur qui se connecte à l'ordinateur au login est donc un parmi beaucoup d'autres, la plupart n'étant pas associé à une personne physique. Les utilisateurs sont ensuite placés dans des groupes, chaque groupe ayant des droits particuliers.

{% note %}
Un utilisateur peut utiliser uniquement les éléments (logiciel, fichier, dossier, ...) qui lui appartiennent ou qui appartiennent à ses groupes.
{% endnote %}

Il existe de nombreux groupes et utilisateurs utilisés par le système pour segmenter (et donc sécuriser) les utilisations. Parmi eux, un utilisateur et un groupe se détachent car ils ont plus de droit que les autres.

### Utilisateur `root`

L'utilisateur `root` est l'utilisateur lié au système d'exploitation. Il est le propriétaire des process (démons) et interfaces du système d'exploitation. Cet utilisateur a ainsi tous les droits (peut aller partout, réserver autant de mémoire qu'il veut, etc).

Comme **Tout** processus a un propriétaire, l'existence de cet utilisateur est garantie.

### Groupe des administrateurs systèmes

{% lien %}
[administrateur système](https://fr.wikipedia.org/wiki/Administrateur_syst%C3%A8me)
{% endlien %}

Le groupe des administrateurs systèmes permet de modifier des paramètres systèmes d'exécuter ou stopper des démons et d'installer de nouveaux logiciels. Ces utilisateurs ont moins de pouvoirs que root qui peut tout faire mais permettent d'administrer le système au quotidien.

Cela permet, si nécessaire, d'installer ou de configurer son système sans être connecté en tant que root en utilisant [la commande sudo](https://www.linuxtricks.fr/wiki/sudo-utiliser-et-parametrer-sudoers) sous Linux par exemple.


Les démons et les interfaces sont des process comme les autres. Ils sont cependant exécutés par un utilisateur spécial, souvent nommé [`root`](https://fr.wikipedia.org/wiki/Utilisateur_root), qui est le [super-utilisateur](https://fr.wikipedia.org/wiki/Utilisateur_root) et est le représentant utilisateur du système.

> TBD quatrième couche pour les OS.
> TBD ici fichiers système

1. utilisateurs
   - qui à le droit de faire quoi

