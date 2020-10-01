---
layout: page
title: "Webpack"
category: cours
tags: packaging webpack front
author: Adèle Bourgeix & Maxime Vivier
---
# Pourquoi Webpack ?

Webpack permet à la fois : 
+ d'écrire et charger des modules sous n'importe quel format dans le navigateur. 
+ d'optimiser l'utilisation des ressources et assets (css, images...). Le "Lazy Loading" est ce qui permet d'optimiser la navigation dans une application en ne chargeant que ce que l'utilisateur va voir. Certains blocks ne seront même peut-être pas chargés, ce qui joue énormément sur les performances.

# Comment ça marche ? 

Pour faire simple, Webpack réalise une concaténation "intelligente" des fichiers en un seul et même fichier: chaque fichier indique ses dépendances, qui sont incluses dans un graphe global. 
Pour cela, Webpack fonctionne alors en deux étapes. 

## Une étape de détermination des dépendances

Webpack part du fichier "entrée" spécifié dans la configuration, puis parcourt le fichier à la recherche de modules dépendant de cette entrée. Il parcourt ensuite chacun de ses modules à la recherche de modules qui en dépendent, construisant alors un graphe de dépendance. Ainsi de suite, jusqu'à ce que toute l'arborescence des dépendances soit épuisée.  

## Une étape d'empaquetage

Webpack empaquete alors les fichiers dans un seul même fichier n'utilisant que le nécesaire à chaque module. Par exemple, si une seule fonction d'un module est utilisée, seule cette fonction sera compilée dans le fichier de sortie.

Webpack ne modifie aucun code autres que les import/export. En revanche, comme certains browsers peuvent avoir du mal à interpréter ces instructions, il est nécessaire d'avoir un "transpiler" comme Babel. Il s'utilise en le précisant comme loader dans la configuration webpack.

# Et comment on utilise Webpack ?

## Tutoriel 

Webpack propose un tutoriel simple pour pouvoir comprendre le fonctionnement du bundling. L'idée de ce tutoriel est d'abord d'importer le module lodash directement dans le fichier de départ index.html via une balise script.

En utilisant Webpack, on importe directement le module dans le fichier script d'entrée dit "source" et au moment de compiler, Webpack créée en sortie un fichier bundle.js dit de "distribution" qui compile le script source avec les fonctions du module lodash qui sont utilisées.

 
[Ici le tutoriel](https://webpack.js.org/guides/getting-started/ )

Le tuto est simple et permet d'appréhender les concepts concrètement en utilisant webpack, et le tout en 10-15 minutes.

## Ce que l'on obtient à la fin du tutoriel
A la fin du tutoriel de Webpack, on a un fichier de configuration webpack qui nous amène à build le fichier js final contenant toutes les dépendances du fichier initial. Et celui-ci est simplement appelé dans le fichier html.
Finalement, dans le fichier html, au lieu d'importer plusieurs modules et librairies entières, on n'a qu'une seule balise script qui prend en compte le fichier d'output de webpack.

## Paramétrer le fichier de configurations 

Depuis la version 4 de Webpack, une configuration préalable n'est pas nécessaire mais il est possible de paramétrer un fichier de configuration pour pouvoir changer les fichiers d'entrée et sortie et aussi spécifier les "loaders" pour chaque type de ressource rencontré.


> **Nota Bene**: les loaders permettent de spécifier à Webpack comment traiter la ressource en
 fonction de son type (c'est à dire la nature de son extension).


~~~
const path= require('path');

module.exports = {
	entry: './src/index.js', 
	output: { 
		filename: 'main.js',
		path: path.resolve(__dirname, 'dist'),
		},
	module: {
		rules : [ 
			{test:  /\.txt$/, use: 'raw-loader' }
			]
		}
	};
~~~

#### Entry point
Un Entry Point indique avec quel module webpack doit commancer à construire son graphe de dépendance des modules. Il sélectionne uniquement ce dont il a besoin dans chaque module et librairie selon toutes ses dépendances. Dans le fichier de configuration de webpack on précise donc le chemin de ce fichier.

 On peut vouloir avoir plusieurs points d'entrée, par exemple quand vous faites deux applications dans le même projet (app visiteur lambda et app admin). Dans ce cas là deux Output seront contruites, mais l'avantage est qu'en fonction de l'ordre de chargement des fichiers, les librairies en commun ne seront chargées qu'une seule fois. Webpack optimise ceci.

#### Output point
Le champ Output indique à webpack où mettre et comment nommer les bundles qu'il créé.
En fait ainsi on peut set up plusieurs output.
~~~
module.exports = {
	entry: {
		app: './src/app.js',
		search: './src/search.js'
	},
	output: {
		filename: '[name].js',
		path: __dirname + '/dist'
	}
};
~~~

#### Loaders
La configuration dans le code ci-dessus spécifie que pour chaque fichier ".txt" rencontré, le loader qui doit être utilisé est le "raw-loader".

Comme indiqué dans la partie de l'empaquetage, les `import`/`export` sont les seules lignes de codes qui sont modifiées par Webpack pour produire un seul fichier recueillant tous les modules. Cepandant ces syntaxes ne sont pas supportées par tous les browsers donc Webpack nécessite l'utilisation d'un transpiler pour l'adapter à tous les types de browsers.

C'est donc dans l'objet module que tu précises le loader pour l'importation de chaque type de fichier que tu utilises.
Voici un exemple avec différents types de fichiers
~~~
module.exports = {
	module: {
		rules: [
			{ test: /\.css$/, use: 'css-loader' },
			{ test: /\.ts$/, use: 'ts-loader' },
			{ test: /\.txt$/, use: 'raw-loader' }
		]
	}
};
~~~

#### Autres
Les 3 points précédants sont les points les plus importants à comprendre pour commencer la configaration de webpack.
Et chacun de ces points a plus de spécifités que tu peux découvrir dans la documentation de webpack.

D'autres paramètres sont configurables comme Plugins, Mode ou Browser Compatibility. La [documentation](https://webpack.js.org/concepts) sur ces concepts se suffit à elle-même.

## Comment React l'utilise
Savoir comment React utilise webpack pour contruire la page est un avantage pour comprendre webpack lui-même.
Ce [tuto](https://freecodecamp.org/news/an-intro-to-webpack-what-it-is-and-how-to-use-it-8304ecdc3c60) vous mène à travers la construction (ultra simplifié certes) d'une application React sans utiliser le create-react-app CLI qui fait tout le travail en background. Ce tuto est aggrémenté de nombreuses explications claires.

La puissance de webpack quand il créé son graphe de dépendances, permet de créé des pages web avec un seul fichier html. On peut utiliser une architecture en composants et écrire notre html directement dans du JS pour l'injecter à l'endroit voulu dans la page. En faisant ainsi on peut très facilement créer une pages à plusieurs onglets en ayant qu'un seul fichier html. Cette façon de procéder est à la base de nombreux framework fronts, notamment les plus connus React Angular et Vue. Et l'avantage principal est la rapidité des applications produites ainsi, car la page n'est pas rechargé à chaque fois qu'on veut changer d'onglet.

Ainsi à la fin de ce tutoriel on obtient un seul fichier html dans lequel on a une balise `<div>` dans le corps du fichier, et cette balise est le point d'injection du reste de l'application qui est codé dans des fichiers JS.

