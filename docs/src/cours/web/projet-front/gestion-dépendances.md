---
layout: layout/post.njk

title: Gestion des dépendances

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Pour gérer les dépendances de votre site front (les bibliothèques css ou javascript utilisées), on a jusqu'à présent utilisé des [CDN](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_diffusion_de_contenu). Mais lorsque l'on veut :

1. contrôlez totalement ce qui est utilisé pour votre site
2. utiliser des outils comme [scss](https://sass-lang.com/) pour compiler notre css.

Il est conseillé de télécharger directement les bibliothèque chez soit.

Ceci pose cependant des problèmes de gestion des dépendances :

- on doit pouvoir savoir exactement ce que l'on a installé
- on doit pouvoir gérer les versions des bibliothèques installées
- on doit pouvoir uniquement gérer le projet de notre code (avec git par exemple) sans avoir besoin de sauvegarder le code de personnes tierces.

On utilise pour cela un outil de gestion de dépendances. Nous allons utiliser celui de <https://nodejs.org/>, nommé [npm](https://www.npmjs.com/).

## Projet <https://nodejs.org/>

Dans un terminal, placer-vous dans le dossier contenant votre site puis créez un projet node avec la commande :

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

Ainsi qu'un fichier [`package-lock.json`{.fichier}](https://docs.npmjs.com/cli/v10/configuring-npm/package-lock-json) qui contient un descriptif détaillé des bibliothèques installées.

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

L'intérêt principal de passer via l'installeur de package de node (`npm`) plutôt que de tout télécharger soit même est que le fichier `package.json`{.fichier} contient toutes les dépendances de votre projet. Pour partager le projet on a pas besoin d'intégrer' le dossier `node_modules/`{.fichier} qui peut être gros, il suffit de le reconstruire à partir du fichier `package.json`{.fichier} en utilisant, dans un terminal placé à la racine du site, la commande :

```shell
npm install
```

{% faire %}
Téléchargez l'archive [mon_super_site_node.zip](../mon_super_site_node.zip) qui contient le site sous la forme d'un projet node :

1. installez les dépendances
2. créez un serveur statique pour le servir
{% endfaire %}
{% info %}

Si vous n'installez pas les dépendance, le site ne peut fonctionner puisqu'il ne contient pas de dossier `node_modules/`{.fichier}.

{% endinfo %}

On conserve également parfois le fichier `package-lock.json`{.fichier} dans la distribution d'un projet node. Vois le lien suivant pour le pourquoi de son existence et son utilisation courante :

{% aller %}
[gestion du fichier](https://blog.boris.sh/blog/package-lock-les-mauvaises-pratiques-a-bannir-pour-un-projet-stable)
{% endaller %}

## Compiler un site statique

> TBD sass; script node avec npx : `npm install sass` ; `npx sass`
> TBD webpack ?
