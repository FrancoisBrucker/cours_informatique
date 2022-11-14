---
layout: page
title:  ""
category: cours
tags: combat web
authors: 
  - "Baptiste Mahé"
  - "Maxime Vivier"
---

![Vue.js Logo](../../assets/vuejs_logo.png)

## Qu'est-ce que c'est ?

[Vue.js](https://v3.vuejs.org) est un framework de dévelopement web basé sur la **componentization** comme [React](https://fr.reactjs.org) ou [Angular](https://angular.io). La particularité de Vue est qu'il se veut facile à maitriser et à intégrer à des projets divers tout en restant capable de créer des single-page applications complexes. \
La dernière majeure version **Vue.js 3.0** est sortie le 18 septembre 2020 avec pour nom de code **One Piece**. Cette release change énormément de choses dans l'utilisation et le fonctionnement global du framework. Dans ce tuto on ne s'intéressera qu'à cette version.

## Installation

Il existe 3 manières différentes d'implémenter Vue dans vos projets :

### 1. L'importer comme un "Content Delivery Network" package

Cela signifie que votre applications ira directement téléchager la version de Vuejs spécifiée au runtime. Pour cela il suffit de rajouter cette ligne dans votre html :

```html
<script src="https://unpkg.com/vue@next"></script>
```

Cette pratique rapide est assez efficace pour du prototypage mais elle est déconseillée sur le long terme.

### 2. L'importer comme package npm

Pour un import un peu plus *propre* on peut utiliser le Node Package Manager (ajouter lien vers tuto Node pas ecore écrit). Pour cela on va lancer la commande suivante dans le dossier `root` du projet :

```shell
npm install vue@next # avec npm directement
# OU
yarn add vue@next # en passant par yarn
```

Cette commande va installer la dernière version de Vue.js dans le dossier node_modules ainsi que toutes ses dépendances.

### 3. Utiliser le CLI (Command Line Interface) officiel de Vue

Vue nous offre une [CLI](https://cli.vuejs.org/guide) avec beaucoup de fonctionnalités trés itéressantes pour le développement d'applications web basées sur le framework :

- génération de composants Vuejs
- local server avec hot-reload
- lint-on-save
- ...

Il faut d'abord installer le CLI globalement sur notre machine pour pouvoir l'utiliser directement depuis n'importe où :

```shell
npm install -g @vue/cli @vue/cli-service-global # avec npm directement
# OU
yarn global add @vue/cli @vue/cli-service-global # en passant par yarn
```

Pour tester l'installation on peut executer la commande suivante :

```shell
vue --version
```

Pour utiliser le CLI avec Vue 3.0 il nous faut `@vue/cli 4.5` ou supérieur.

## Les débuts, initialisation d'un projet Vue.js

Parmis les 3 méthodes si-dessus nous allons utilisé la 3ème pour la suite de ce tuto. Assurez-vous d'avoir bien installé le CLI.

Pour initialiser un projet Vue.js à l'aide du CLI :

```shell
vue create my-first-vue-project
```

Une fois cette commande exécutée on va choisir `Default (Vue 3 Preview) ([Vue 3] babel, eslint)` pour le type de projet et `NPM` pour le management des packages. \
On peut ensuite naviguer dans le projet créé par le CLI :

```shell
cd my-first-vue-project
```

On remarque 2 choses à l'intérieur du dossier :

- un repo `git` a été initialisé
- un projet `node` a aussi été initialisé

Si l'on regarde dans le `README.md` on peut voir les différentes commandes possibles dans le repo avec le CLI. \
Essayons d'abord de servir notre porjet en local avec la commande :

```shell
npm run serve
```

Si l'on va avec notre navigateur à l'addresse indiquée `http://localhost:8080`, on peut voir notre toute première application Vue.js exécutée !

![Vue Screen](../../assets/vue-project-capture.png)

Nous allons maintenant regarder dans les fichiers généré par le CLI pour comprendre comment la page que l'on a sous les yeux fonctionne.

### Tout d'abord le dossier `public`

On peut y voir 2 fichiers :

- favicon.ico : l'icône vue affichée dans l'escpace tab de notre browser.
- index.html : le fichier HTML qui est rendu dans notre borwser.

Dans ce fichier html on peut déjà voir certaines lignes intéréssantes dans le `head`:

```html
<link rel="icon" href="<%= BASE_URL %>favicon.ico">
<title><%= htmlWebpackPlugin.options.title %></title>
```

Ces lignes nous permettent de définir l'icône et le titre de l'application dans la zone de tab du site. \
Il s'agit pour l'instant que de code html simple avec un peu de WebPack rien à voir avec Vue.js...

Ensuite on peut s’intéresser au `body` de notre page html :

```html
<div id="app"></div>
<!-- built files will be auto injected -->
```

Cette `div` avec un **id** "app" est en réalité la `div` qui va contenir toute notre application. Vue.js va injecter nos composants Vue dans cette `div`.

### Ensuite le dossier `src`

Le fichier `main.js` est le fichier qui va nous permettre injecter notre application dans la `div` app de l'`index.html` que l'on vient de voir. \
On y retrouve le code suivant :

```javascript
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```

La fonction `createApp` est une fonction native de Vue qui permet de build l'application. Son paramètre doit être un composant Vue définie dans `App.vue`. Cette fonction renvoi un objet `App` sur lequel on execute la méthode `mount` qui va nous permettre d'indiquer sur quel composant nous souhaitons monter notre application. Ici le `#app` signifie que l'on souhaite monter notre application sur un élément avec un `id` égale à `app` donc notre `div` de toute à l'heure.

Allons donc voir comment est défini notre composant `App` dans `App.vue`!

```vue
<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Welcome to Your Vue.js App" />
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";

export default {
  name: "App",
  components: {
    HelloWorld,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

On remarque 3 parties différentes dans la définition du composants :

- `<template>` : La définition HTML du template du composant, de quelles balises HTML ce composant est-il composée (tiens, tiens, tiens une balise HelloWorld...).
- `<script>` : La définition logique du composant.
- `<style>` : Des règles CSS qui vont être appliquées au composant.

Nous voila donc devant le grand intéret de Vue : **1 COMPOSANT = 1 FICHIER** \
Mais cela signifie aussi jongler entre 3 languages différents dans un même fichier : le **html** pour le template, le **js** pour le script et le **css** pour les styles.

En regardant d'un peu plus près on peut voir que notre `<template>` comporte un élément HTML que l'on connait pas : `<HelloWorld msg="Welcome to Your Vue.js App" />`. On peut voir dans le script que cet élément est importé depuis le fichier `components/HelloWorld.vue`. \
**Encore un composant Vue !** Et oui, comme dans React et Angular les composants Vue, une fois bien défénis, peuvent être utilisés comme des balises HTML de base.

Allons découvrir ce qu'il y a dans notre fichier  `components/HelloWorld.vue` !

```vue
<template>
  <div class="hello">
    {% raw %}<h1>{{ msg }}</h1>{% endraw %}
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
    <h3>Installed CLI Plugins</h3>
    <ul>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener">babel</a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank" rel="noopener">eslint</a></li>
    </ul>
    <h3>Essential Links</h3>
    <ul>
      <li><a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank" rel="noopener">Forum</a></li>
      <li><a href="https://chat.vuejs.org" target="_blank" rel="noopener">Community Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank" rel="noopener">Twitter</a></li>
      <li><a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a></li>
    </ul>
    <h3>Ecosystem</h3>
    <ul>
      <li><a href="https://router.vuejs.org" target="_blank" rel="noopener">vue-router</a></li>
      <li><a href="https://vuex.vuejs.org" target="_blank" rel="noopener">vuex</a></li>
      <li><a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank" rel="noopener">vue-devtools</a></li>
      <li><a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">awesome-vue</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
```

On retrouve nos 3 parties `template`, `script` et `style` comme pour App. \
On remarque néanmoins certaines particularités dans ce composant :

- On peut voir la propriété `msg` du composant qui est un example de propagation d'information entre composants. Nous avons vu dans `App.vue` quand on a déclaré l'élément `HelloWorld` l'assignation `msg="Welcome to Your Vue.js App"` qui signifie que l'on passse le **string "Welcome to Your Vue.js App"** depuis le composant `App` au composant `HelloWorld`. Du côté du composant `HelloWord` on définit `props: { msg: String }` dans le `script`. On utilise ensuite cette propriété dans le template de HelloWorld `<h1>{{ msg }}</h1>`, on affiche le string dans une balise `h1`.
- On voit l'attribut `scoped` dans la définition des styles. Cela signifie que les règles CSS définies ici ne seront appliquées que dans le composant `HelloWorld` et pas dans le reste de l'application.

Le reste des éléments dans le template de ce composant correspond aux éléments affichés dans notre browser (liens GitHub et réseaux sociaux).

## La fin, Builder l'application Vue

Comme on a pu le remarquer les fichiers `.vue` ne sont pas des fichiers `.js`, `.html` ou `.css` de base or les navigateurs ne lisent que ces fichiers là. Il faut donc **compiler** notre application avant de la mettre sur un serveur. \
Pour compiler notre application nous allons utiliser le super **CLI** de Vue avec la commande (à executer dans le fichier *root* du projet):

```shell
npm run build
```

Le **CLI** va générer notre application compilée dans le dossier `dist` de notre projet. Il suffit maintenant de copier le contenu de ce dossier sur le server (et bien faire servir l'`index.html`) pour avoir notre application *up and running* comme on dit dans le jargon !

**ATTENTION** : Par défault le cli de vue va avoir un *publicPath* égale à `'/'` ce qui souvent ne va pas fonctionner avec notre intégration sur le serveur (sauf si le `index.html` se trouve à la racine du server ce qui arrive rarement...). Pour palier à ce problème il va falloir indiquer au cli un publicPath vide `''` pour notre `build`. Pour cela on va créer un nouveau fichier (attention aux tipos !) `vue.config.js` à la racine de notre projet vue et y écrire :

```js
module.exports = {
  publicPath: ''
}
```

Une fois cela fait on peut exécuter la commande `npm run build` et build notre site pour l'envoyer où on veut sur le server (l'`index.html` va chercher les sources par rapport à son PATH **relatif** et non depuis **la racine du server**).

Cette petite présentation de Vue est terminée, pour poursuivre votre formation avec ce framework nous vous proposons la création d'une application todolist dans [ce tuto]({% link cours/dfs/todolist_vuejs.md %}).
