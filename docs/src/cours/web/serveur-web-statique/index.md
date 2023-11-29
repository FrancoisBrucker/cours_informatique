---
layout: layout/post.njk

title: Serveur web de fichiers statiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Les fichiers html, css et js que vous avec créés jusqu'à présent sont appelés ***fichiers statiques*** car ils ne peuvent être modifiés et sont chargés tels quels par le navigateur via une url. Cette url peut utiliser le protocole :

- [file](https://en.wikipedia.org/wiki/File_URI_scheme) si vous chargez un fichier de votre disque dur
- [http](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol) si vous utilisez votre page personnelle par exemple

De façon minimale, un serveur web est un programme qui ***écoute*** sur un port particulier de la machine et ***sert*** les fichiers d'un dossier précis du disque dur de la machine.

## Site statique

{% note "**Définition**" %}

Un ***site statique*** est un ensemble de fichiers html, css et js tous placés dans un dossier donné.

A l'intérieur de ce site, l'accès aux fichiers se fait de façon ***relative***.
{% endnote %}

Par exemple :

```
.
├── css
│   └── main.css
├── cv
│   └── index.html
├── img
│   └── gros_caillou.jpg
└── index.html
```

Que vous pouvez retrouver [là](./mon_super_site/index.html).

{% faire %}
Avec les outils de développement, regardez le code source du site et remarquez que tous les appels aux différents fichier du site sont bien relatifs.

{% endfaire %}

Si ce dossier est sur mon disque dur, je peux y accéder 
Par exemple supposons que mon site web est constitué `/users/fbrucker/mon_super_site`{.fichier} ou ses sous-dossiers. La page par défaut de mon site étant le fichier : `/users/fbrucker/mon_super_site/index.html`{.fichier}, je peux lire ce site depuis un navigateur en utilisant l'url : `file:///users/fbrucker/mon_super_site/index.html`.

Si je veux partager ce site, je peux zipper le dossier et l'envoyer par mail à une autre personne, ou le déposer sur le site de ma page perso de l'ecm.

## Serveur de fichiers statiques

Un serveur de fichier statique va être lié à un dossier de votre disque dur. A chaque url est associé un fichier de ce dossier. En reprenant l'exemple précédent :

1. mon serveur est sur ma machine locale, sur le port 8000 : `http://localhost:8000`
2. le dossier associé au serveur est le dossier `/users/fbrucker/mon_super_site`{.fichier}

L'url `http://localhost:8000/index.html` correspond au fichier `index.html` du dossier `/users/fbrucker/mon_super_site`{.fichier} et url `http://localhost:8000/css/main.css` correspond au fichier `main.css` du dossier `/users/fbrucker/mon_super_site/css/`{.fichier}.

Le serveur n'est qu'un intermédiaire entre les fichiers de votre disque dur et le navigateur.

{% info %}
C'est exactement ce qui se passe pour votre page perso. C'est le dossier `html` de votre dossier maison qui est utilisé.
{% endinfo %}

Il est très facile de créer un serveur web en python. Il suffit de se placer dans le dossier contenant votre site et de taper la commande :

```
python -m http.server 3456
```

Un serveur est crée à l'adresse <http://localhost:3456/> et il permet d'accéder aux fichiers via le protocole http.

{% info %}

- remplacez 3456 part le numéro de port que vous voulez utiliser
- remplacez `python` par `python3` si vous êtes sous Linux

{% endinfo %}

Il y a plusieurs intérêt à utiliser un serveur de site statique :

1. voir comment ce sera sur le serveur de page perso
2. s'assurer que tous vos fichiers sont accédé de façon relative
3. éviter les problèmes [CORS](https://fr.wikipedia.org/wiki/Cross-origin_resource_sharing) lorsque l'on chargera des fichiers depuis le site.

Cette façon de procéder est utilisée massivement par les bibliothèques de création de site comme <https://react.dev/> ou <https://vuejs.org/>.

{% faire %}
Téléchargez le ficher [mon_super_site.zip](./mon_super_site.zip) qui contient une archive compressé d'un site et créer un serveur de site statique pour le servir.
{% endfaire %}

## Utiliser <https://nodejs.org/>

On peut utiliser <https://nodejs.org/> pour installer des bibliothèques javascript ou css utiles.

L'intérêt de procéder ainsi est que :

1. vous contrôlez totalement ce qui est utilisé pour votre site
2. permet d'utiliser des outils comme [scss](https://sass-lang.com/) pour compiler votre css.

Pour cela, dans un terminal, placer-vous dans le dossier contenant votre site puis créez un projet node avec la commande :

```shell
npm init
```

Une fois que vous avez répondu aux questions (en appuyant juste sur la touche entrée si vous voulez), vous créez le fichier de configuration `package.json`{.fichier} qui contient les informations relatives à votre projet. En appuyant tout le temps sur la touche entrée j'ai obtenu le fichier suivant  :

```
{
  "name": "mon_super_site",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}

```

On peut maintenant installer un package javascript, comme <https://tabulator.info/> pour rendre notre table plus jolie :

```shell
npm install tabulator-tables
```

Le fichier `package.json` a maintenant changé, il contient les trois lignes suivantes en plus :

```
  "dependencies": {
    "tabulator-tables": "^5.5.2"
  }
```

Ainsi qu'un fichier `package-lock.json`{.fichier} qui contient un descriptif détaillé des bibliothèques installées.

Enfin, les bibliothèques téléchargées l'on été dans le dossier `node_modules/`{.fichier} lui aussi nouveau. Dans notre cas, seulement trois bibliothèques ont été installées avec une seule commandes, mais cela peut être beaucoup plus.

Pour utiliser tabulator comme dans l'exemple [tables html](https://tabulator.info/docs/5.5/data#table), il faut avoir accès :

- à la bibliothèque css qui est dans le dossier `node_modules/tabulator-tables/dist/css/tabulator.min.css`{.fichier}
- à la bibliothèque javascript qui est dans le dossier `node_modules/tabulator-tables/dist/js/tabulator.min.js`{.fichier}

{% info %}
Il n'y a pas de règle pour savoir quoi récupérer. Mais normalement, vous devriez trouver ce qu'il faut dans les dossiers js ou css et prenez les fichiers [minifiés](https://www.cloudflare.com/fr-fr/learning/performance/why-minify-javascript-code/) (moins lisible pour un humains mais plus léger pour traverser le réseau).

Parfois, la bibliothèque vient également avec son code source, vous avez alors deux dossiers, `src/`{.fichier} pour les sources et `dist`{.fichier} pour les fichiers utilisables.

{% endinfo %}

Le fichier `filmographie/index.html`{.fichier} devient :

```html
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <title>Filmographie concise de Kurt Russell</title>

    <link href="../node_modules/tabulator-tables/dist/css/tabulator.min.css" rel="stylesheet">
    <script type="text/javascript" src="../node_modules/tabulator-tables/dist/js/tabulator.min.js"></script>

    <link rel="stylesheet" href="../css/main.css">
  </head>
  <body>
    <h1>Filmographie concise de Kurt Russell</h1>
    <p>Un des plus grands acteurs de son temps (avec Jean-Claude Vandamme)</p>
<table id="table-cv">
  <thead>
    <tr>
      <th >Année</th><th>film ou série</th>
    </tr>

  </thead>
  <tbody>
    <tr>
      <td>2023</td><td>Monarch Legacy of Monsters</td>
    </tr>
    <tr>
      <td>2007</td><td>Boulevard de la mort</td>
    </tr>
    <tr>
      <td>1994</td><td>Stargate, la porte des étoiles</td>
    </tr>
    <tr>
      <td>1982</td><td>The Thing</td>
    </tr>
    <tr>
      <td>1981</td><td>New york 1997</td>
    </tr>
  </tbody>
</table>
<footer>
  <p>Revenir à l'<a href="../index.html">index</a></p>
</footer>

  <script>
    let table = new Tabulator("#table-cv", {
      layout:"fitDataStretch",
    });
  </script>
  </body>
</html>
```

{% faire %}
Modifier le site de la partie précédente pour utiliser les modules de node.
{% endfaire %}

## Compiler un site statique

> TBD sass; script node avec npx : `npm install sass` ; `npx sass`
> TBD webpack ?
