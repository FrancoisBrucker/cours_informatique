---
layout: layout/post.njk

title: Projet front

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les fichiers html, css et js que vous avec créés forment un tout que l'on nomme ***le front*** (par opposé au *back* que l'on verra plus tard) et qui est exécuté sur un navigateur. Tous les fichiers crées sont ***statiques*** car ils ne peuvent être modifiés : ils sont chargés tels quels par le navigateur via une url. Cette url peut utiliser le protocole :

- [file](https://en.wikipedia.org/wiki/File_URI_scheme) si vous chargez un fichier de votre disque dur
- [http](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol) si vous utilisez votre page personnelle par exemple

## Site statique

{% note "**Définition**" %}

Un ***site statique*** est un ensemble de fichiers html, css et js tous placés dans un dossier donné, nommé ***dossier racine***. Le point d'entrée du site est le fichier `index.html`{.fichier} placé dans le dossier racine.

A l'intérieur de ce site, l'accès aux fichiers se fait de façon ***relative***.
{% endnote %}

Par exemple :

```
mon_super_site
├── css
│   └── main.css
├── cv
│   └── index.html
├── img
│   └── gros_caillou.jpg
└── index.html
```

Que vous pouvez retrouver [là](./mon_super_site/index.html). La racine du site est le dossier nommé `mon_super_site`{.fichier}.

{% faire %}
Avec les outils de développement, regardez le code source du site et remarquez que tous les appels aux différents fichier du site sont bien relatifs.

{% endfaire %}

Si le dossier racine est `/users/fbrucker/mon_super_site`{.fichier}, je peux accéder au point d'entrée depuis un navigateur en utilisant l'url : `file:///users/fbrucker/mon_super_site/index.html`.

Tous les liens étant fait de façon relative, je peux aisément partager ce site en distribuant directement le dossier et tous ses sous-dossiers et fichiers (en compressant le dossier racine par exemple) ou en déposant le dossier racine dans le dossier `~/html`{.fichier} sur une machine de l'ecm, pour y accéder via ma page perso.

{% faire %}
Téléchargez le ficher [mon_super_site.zip](./mon_super_site.zip) qui contient une archive compressé du site et utilisez le protocole file pour consulter le site.
{% endfaire %}

## Dépendances

{% aller %}
[Gestion des dépendances](gestion-dépendances)
{% endaller %}

## Serveur de fichiers statiques

{% aller %}
[Serveur de fichier statiques](serveur-statique)
{% endaller %}
