---
layout: layout/post.njk

title: Principes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Après avoir examiné les besoins qui impliquent l'utilisation d'un SCM, on en verra une implémentation possible sur une structure distribuée et l'usage qu'on peut en faire au quotidien.

## Besoins

{% aller %}
[Besoins](./besoins/){.interne}
{% endaller %}

## Structure distribuée

Pour que son accès soit facile, il faut que la structure de stockage soit sur le même ordinateur que celui ayant le répertoire de travail.

Si cette solution est idéal lorsque l'on est un unique développeur, elle devient plus complexe à mettre en œuvre si on est plusieurs à travailler sur le projet. Il faut :

1. en avoir une copie de la structure de stockage chez chaque participant,
2. permettre à plusieurs personnes de travailler sur le même fichier,
3. permettre le travail asynchrone entre les personnes : une personne va avancer à un endroit pendant qu'une autre travaille sur autre chose
4. pouvoir reprendre un projet existant avec une nouvelle équipe

Ceci implique que chaque copie soit synchronisée par un dépôt référent, un **_projet référent_** faisant autorité pour tous les participants. Mais comment faire ensuite pour que la synchronisation soit aisée ?

### Mauvaise implémentation

Avant d'exposer la solution adoptée par <https://git-scm.com/> et qui fait autorité actuellement, commençons par lister une série fausse bonne idées qui à été (et est malheureusement encore souvent) mis en place : un seul projet partagé assorti :

1. de règles de soumission de commits
2. d'un superviseur général qui doit tout valider avant

Cela ne fonctionnera jamais car aucune règle ne permettra de résoudre tous les cas. On Va passer un temps infini à les discuter et _in fine_ les personnes responsable de la création/vérification des règles feront en sorte qu'elles soient facile à vérifier plutôt qu'utile (voir l'administration en générale et la notre en particulier).

Enfin, en plus d'être inefficace, cela va induire de gros ralentissement car comme il faut tout vérifier on mettra en commun les changements peu souvent (genre une fois par mois) ce qui va générer d'énormes problèmes de synthèse des différentes versions et ralentira d'autant plus le processus.

### Bonne implémentation

La bonne implémentation consiste **à ne pas sacraliser la mise en commun**. Il faut le faire le souvent pour que tout le monde ait une version claire de l'ensemble **actuel** du projet.

La solution utilisée par [git](https://git-scm.com/) consiste à ne pas choisir de serveur distant avec des règles précise : tout participant possède l'intégralité de la structure de sauvegarde comme s'il était seul développeur. On ajoute enfin souvent un participant fictif, nommé **_origin_**, qui est la référence commune et est synchronisée à l'envie par les développeurs. Cette structure distribuée permet :

- que chaque développeur puisse faire ses propres commits en local,
- d'avoir une (ou plusieurs) branches partagée par tous les utilisateurs (comme `main`, `dev`, _etc_) et synchronisés souvent entre les utilisateur et _origin_ :
  - on appelle **_push_** les synchronisation des utilisateurs vers l'_origin_
  - on appelle **_pull_** les synchronisation de l'_origin_ vers un utilisateur
- de continuer un projet avec une nouvelle équipe, il suffit de copier _origin_

## Usage

{% aller %}
[Usages](./usages/){.interne}
{% endaller %}
