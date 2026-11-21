---
layout: layout/post.njk

title: Serveur de fichiers statiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Un serveur de fichier statique va être lié à un dossier de votre disque dur. A chaque url est associé un fichier de ce dossier. En reprenant l'exemple précédent :

1. mon serveur est sur ma machine locale, sur le port 8000 : `http://localhost:8000`
2. le dossier associé au serveur est le dossier `/users/fbrucker/mon_super_site`{.fichier}

L'url `http://localhost:8000/index.html` correspond au fichier `index.html` du dossier `/users/fbrucker/mon_super_site`{.fichier} et url `http://localhost:8000/css/main.css` correspond au fichier `main.css` du dossier `/users/fbrucker/mon_super_site/css/`{.fichier}.

Le serveur n'est qu'un intermédiaire entre les fichiers de votre disque dur et le navigateur.

{% info %}
C'est exactement ce qui se passe pour votre page perso. C'est le dossier `html` de votre dossier maison qui est utilisé.
{% endinfo %}

Il est très facile de créer un serveur web en python. Il suffit de se placer dans le dossier contenant votre site et de taper la commande :

```shell
python -m http.server 3456
```

Un serveur est crée à l'adresse <http://localhost:3456/> et il permet d'accéder aux fichiers via le protocole http.

{% info %}

- vous pouvez remplacez 3456 part le numéro de port que vous voulez utiliser dns la commande `python`
- remplacez `python` par `python3` si vous êtes sous Linux

{% endinfo %}

Il y a plusieurs intérêt à utiliser un serveur de site statique :

1. voir comment ce sera sur le serveur de page perso
2. s'assurer que tous vos fichiers sont accédés de façon relative
3. éviter les problèmes [CORS](https://fr.wikipedia.org/wiki/Cross-origin_resource_sharing) lorsque l'on charge des fichiers depuis le site (on le verra lorsque l'on traitera de la gestion des donnée).

Cette façon de procéder est utilisée massivement par les bibliothèques de création de site comme <https://react.dev/> ou <https://vuejs.org/>.

{% faire %}
Utilisez le site de la partie précédente (archive [mon_super_site.zip](./mon_super_site.zip)) pour créer un serveur de site statique sur le port 8080 de votre machine pour le servir.
{% endfaire %}
