---
layout: page
title: "PostCSS"
category: cours
tags: postcss
authors:
  - "Victoire Flesselles"
  - "William Templeton"
---
## Qu'est-ce que PostCSS?
<p align="center">
	<img src="./images/postcss.png">
</p>
### SASS, la partie émergée de l'iceberg
On a vu dans le cours sur SASS à quel point l'écriture du CSS peut être drastiquement améliorée:
+ Les variables permettent une cohérence à travers l'ensemble des fichiers `scss`, ce qui est pariculièrement utile pour le respect d'une charte graphique par exemple
+ Le nesting permet de rendre le code plus flexible et bien plus agréable à lire
+ L'utilisation de modules permet une structure plus explicite et facile à maintenir
+ Les mixins permettent de respecter le principe DRY 
+ Les opérateurs simplifient beaucoup le calcul de tailles pour une interface très fluide

SASS est un outil très utile, mais peu configurable. Si on remarque une difficulté dans l'écritude du code `css` ou `scss`, on est obligés de rester dans les clous du format pour résoudre le problème. 

À l'inverse, le javascript est hautement configurable et il existe des milliers de librairies téléchargeables en quelques instants permettant de réaliser des tâches complexes en toute simplicité. Comment rendre le CSS tout aussi modulaire et configurable ? 

C'est là qu'intervient [PostCSS](https://postcss.org/).
### Concept
PostCSS s'appuie sur Javascript pour moderniser le CSS. En tant que tel, PostCSS ne fait pas grand chose; pour configurer le CSS, il faut faire appel à des plugins qui apportent des fonctionnalités supplémentaires. On peut voir une similitude avec `npm`: ce sont les librairies installées par `npm` qui apportent toute la configurabilité au projet. PostCSS met à disposition une API qui offre la possibilité aux plugins d'analyser et modifier n'importe quel fichier CSS.

### Pourquoi l'utiliser ? 
PostCSS compte plus de [200 plugins](https://www.postcss.parts/). L'objectif principal est de permettre au développeur de gagner en efficacité et rapidité. Certains plugins permettent de détecter automatique des erreurs ou des maladresses (les linters), d'autres automatisent l'écriture de morceaux de code. Il existe même des plugins qui mimiquent exactement le comportement de SASS: PostCSS n'est pas une alternative à SASS mais bel et bien un outil bien plus puissant. Pour autant, il n'y a pas nécessairement de dépaysement: rien ne nous oblige à utiliser plus que les fonctionnalités de SASS par exemple, mais on se laisse toujours la porte ouverte à plus de fonctionnalités par la suite. 

Et si jamais on ne trouve pas son bonheur, PostCSS permet d'écrire ses propres plugins! La [documentation officielle](https://github.com/postcss/postcss/blob/master/docs/writing-a-plugin.md) explique le processus et même comment partager son module avec le reste de la communauté. 

Au-delà d'une utilisation individuelle, certains plugins permettent d'écrire un code plus homogène au sein d'une équipe. Par exemple, l'utilisation de linters et prefixers encouragent l'utilisation de mêmes conventions par les différents développeurs même s'ils ont des pratiques différentes. PostCSS s'intègre très facilement dans n'importe quel projet d'envergure.
## Application
On reprend le projet très basique de calculatrice du cours sur Webpack, après empaquetage. Pour rappel, la structure du projet est : 

~~~
.
├── dist
│   ├── index.html
│   ├── main.js
│   └── style.css
├── node_modules
├── package.json
├── package-lock.json
├── src
│   ├── index.js
│   ├── methods.js
│   ├── style.scss
│   └── variables.js
└── webpack.config.js
~~~	
et les différents fichiers sont : 

+ `index.html` : 

	~~~html
	<html>
		<head>
			<meta charset="utf-8"/>
			<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
			<title>Calculatrice</title>
			<link href="https://fonts.googleapis.com/css?family=Montserrat&display=swap" rel="stylesheet"/>
			<link rel="stylesheet" type="text/css" href="./style.css"/>
		</head>
		<body>
		<main>
				<h1 class="title">Calculatrice</h1>
				<div class="calculator">
					<section class="affichage">
						<textarea id="result" class="result"></textarea>
					</section>
					<section class="number-inputs">
						<input type="button" class="case case1" value="1"/>
						<input type="button" class="case case2"  value="2"/>
						<input type="button" class="case case3"  value="3"/>
						<input type="button" class="case case4" value="4" />
						<input type="button" class="case case5" value="5"/>
						<input type="button" class="case case6" value="6"/>
						<input type="button" class="case case7" value="7"/>
						<input type="button" class="case case8"  value="8"/>
						<input type="button" class="case case9"  value="9"/>
						<input type="button" class="case case0" value="0" />
						<input type="button" class="case casepoint"  value="."/>
					</section>
					<section class="operators">
						<input type="button" class="case case+"  value="+"/>
						<input type="button" class="case case-" value="-" />
						<input type="button" class="case case*"  value="*" o/>
						<input type="button" class="case casediv"  value="/"/>
					</section>
					<section class="bottom-rank">
						<input type="button" id="caseegal" class="case caseegal"  value="="/>
						<input type="button" id="casedel" class="case casedel"  value="C"/>	
					</section>
				</div>
			</main>
		</body> 
		<script src="./main.js"></script>    
	</html>
	~~~
	
+ `index.js` :

	~~~js
	import {numInputs, opInputs} from "./variables"
	import {insert, calcul, del} from "./methods";

	numInputs.forEach(input => {
	    input.addEventListener('click', ()=>{
		insert(input.value)
	    })
	});

	opInputs.forEach(input => {
	    input.addEventListener('click', ()=>{
		insert(input.value)
	    })
	});

	document.getElementById("caseegal").addEventListener('click', ()=>{
	    calcul();
	})

	document.getElementById("casedel").addEventListener('click', ()=>{
	    del();
	})
	~~~

+ `methods.js` :

	~~~js
	function insert(num) {
	    return document.getElementById("result").value += num;
	}
	function calcul() {
	    return document.getElementById("result").value = eval(document.getElementById("result").value);
	}
	function del() {
	    return document.getElementById("result").value = "";
	}

	export {insert, calcul, del}
	~~~

+ `variables.js` :

	~~~js
	var numInputs = document.querySelectorAll(".number-inputs input");

	var opInputs = document.querySelectorAll(".operators input");

	export {numInputs, opInputs}
	~~~

+ `style.scss` :

	~~~scss
	$main-width: 450px;

	body {
	    text-align: center;
	    padding: 0;
	    margin: 0;
	    min-height: 100vh;
	    font-family: "Montserrat", sans-serif;
	    background-color: #b8c6db;
	    background-image: linear-gradient(315deg, #b8c6db 0%, #f5f7fa 74%);
	}
	    main {
	    width: min-content;
	    margin: 0 auto;
	    display: flex;
	    flex-direction: column;
	    align-items: center;
	    .title {
		margin: 50px 0 10px;
		font-size: 3.5em;
		text-transform: uppercase;
		font-weight: lighter;
	    }
	    .calculator{
		width: $main-width;
		padding: 20px;
		background: #efefef;
		border-radius: .5rem;
		box-shadow: 10px 10px 40px rgba(0, 0, 0, 0.2);
		display: grid;
		grid-template-areas:
		                "result result"
		                "number-inputs operators"
		                "bottom-rank bottom-rank";
		grid-template-columns: 3fr 1fr;
		.case {
		    width: calc($main-width / 4 - 20px);
		    height: calc($main-width / 4 - 20px);
		    text-transform: uppercase;
		    margin: 10px;
		    background: #efefef;
		    border: none;
		    border-radius: .5rem;
		    color: #444;
		    font-size: 1rem;
		    font-weight: 700;
		    text-align: center;
		    outline: none;
		    cursor: pointer;
		    transition: .2s ease-in-out;
		    box-shadow: -6px -6px 14px rgba(255, 255, 255, .7),
		                -6px -6px 10px rgba(255, 255, 255, .5),
		                6px 6px 8px rgba(255, 255, 255, .075),
		                6px 6px 10px rgba(0, 0, 0, .15);
		    &:hover{
		        box-shadow: -2px -2px 6px rgba(255, 255, 255, .6),
		        -2px -2px 4px rgba(255, 255, 255, .4),
		        2px 2px 2px rgba(255, 255, 255, .05),
		        2px 2px 4px rgba(0, 0, 0, .1);
		    }
		    &:active{
		        box-shadow: inset -2px -2px 6px rgba(255, 255, 255, .7),
		        inset -2px -2px 4px rgba(255, 255, 255, .5),
		        inset 2px 2px 2px rgba(255, 255, 255, .075),
		        inset 2px 2px 4px rgba(0, 0, 0, .15);
		    }
		}
		.caseegal, .casedel, .case0 {
		width: calc($main-width / 2 - 20px);
		}
		.affichage{
		    grid-area: result;
		    .result {
		        resize: none;
		        height: 50px;
		        width: 100%;
		        padding: 20px 8px 0 8px;
		        text-align: right;
		        color: #444;
		        font-size: 1rem;
		        font-weight: 700;
		        border: solid 1px #efefef;
		        border-radius: .5rem;
		        box-shadow: inset -2px -2px 6px rgba(255, 255, 255, .7),
		        inset -2px -2px 4px rgba(255, 255, 255, .5),
		        inset 2px 2px 2px rgba(255, 255, 255, .075),
		        inset 2px 2px 4px rgba(0, 0, 0, .15);
		        &:focus{
		            outline: none;
		        }
		    }
		}
		.number-inputs {
		grid-area: number-inputs;
		display: flex;
		flex-wrap: wrap;
		}
		.operators{
		    grid-area: operators;
		}
		.bottom-rank{
		    grid-area: bottom-rank;
		    display: flex;
		}
	    }
	}
	~~~

+ `package.json` :

	~~~json
	{
	  "name": "calculatrice-postcss",
	  "version": "1.0.0",
	  "description": "",
	  "private":true,
	  "scripts": {
	    "test": "echo \"Error: no test specified\" && exit 1",
	    "build": "webpack"
	  },
	  "keywords": [],
	  "author": "",
	  "license": "ISC",
	  "devDependencies": {
	    "webpack": "^5.58.2",
	    "webpack-cli": "^4.9.0"
	  }
	}
	~~~

+ `webpack.config.js` :

	~~~js
	const path = require('path');

	module.exports = {
	  entry: './src/index.js',
	  output: {
	    filename: 'main.js',
	    path: path.resolve(__dirname, 'dist'),
	  },
	};
	~~~

### Installation
Il existe plusieurs façons d'installer PostCSS. Ici, nous allons nous appuyer sur Webpack.
1. Commençons par installer PostCSS ainsi que son loader: `npm install --save-dev postcss-loader postcss postcss-cli`
2. On modifie `webpack.config.js` pour utiliser le module `postcss-loader`:
	
	~~~js
	const path = require('path');

	module.exports = {
	  entry: './src/index.js',
	  output: {
	    filename: 'main.js',
	    path: path.resolve(__dirname, 'dist'),
	  },
	  module: {
	    rules: [
	      {
		test: /\.css$/,
		exclude: /node_modules/,
		use: [
		  {
		    loader: 'style-loader',
		  },
		  {
		    loader: 'css-loader',
		    options: {
		      importLoaders: 1,
		    }
		  },
		  {
		    loader: 'postcss-loader'
		  }
		]
	      }
	    ]
	  }
	};	
	~~~

3. On créé le fichier de configuration avec PostCSS: `postcss.config.js`

	~~~js
	module.exports = {
	    plugins: [
		
	    ]
	  }
	~~~

	C'est ici qu'on précisera les plugins qu'on utilise dans le projet.

4. On finit l'installation avec `npm run build`

5. Grâce au paquet `postcss-cli` qu'on a installé avec `npm`, on peut invoquer des commandes `postcss` depuis la ligne de commande. Ainsi, on peut écrire des scripts dans `package.json` pour se simplifier la vie. Profitons-en pour vérifier que tout se passe bien jusqu'à présent: ajoutons le script suivant à `package.json`:

	~~~json
	{
	  "name": "calculatrice-postcss",
	  "version": "1.0.0",
	  "description": "",
	  "private": true,
	  "scripts": {
	    "test": "echo \"Error: no test specified\" && exit 1",
	    "build": "webpack",
	    "css": "npx postcss src/style.scss -o dist/style.css --no-map --verbose"
	  },
	  "keywords": [],
	  "author": "",
	  "license": "ISC",
	  "devDependencies": {
	    "postcss": "^8.3.9",
	    "postcss-loader": "^6.2.0",
	    "webpack": "^5.58.2",
	    "webpack-cli": "^4.9.0"
	  },
	  "dependencies": {
	    "postcss-cli": "^9.0.1"
	  }
	}
	~~~

	On peut désormais lancer la commande `npm run css`: PostCSS prend notre fichier `style.scss` dans le répertoire `src/` et le transforme en `style.css` dans le répertoire `dist/`. PostCSS ne renvoit pas d'erreur, mais il précise aussi qu'il ne fait rien (c'est normal, on n'a pas installé de plugins). Il faut donc installer des plugins SASS pour que le fichier `style.css` soit exploitable.

### Exemple 1: Retour au SASS
Ici, on va détailler comment effectuer une transition de SASS vers PostCSS. Mais on pourrait très bien adapter ce qui suit pour des fichiers `css` classiques (attention à bien préciser qu'on écrit en PostCSS dans l'IDE, même si l'extension est en `.css`).

On installe le plugin qui nous intéresse. Ici, on utilise [PreCSS](https://github.com/csstools/precss), qu'on installe avec la commande `npm install --save-dev precss `. PreCSS nous met à disposition les mêmes fonctionnalités que SASS. 

On modifie `postcss.config.js` comme suit: 

~~~js
module.exports = {
    plugins: [
	require('precss')
    ]
  }
~~~

Puis il suffit de lancer `npm run css` et PostCSS compile notre fichier SASS en fichier CSS. Tout simplement! 

### Exemple 2: Utilisation d'un linter

#### Qu'est-ce qu'un linter ?
Un linter est un outil indispensable pour écrire du code propre. Il analyse en temps réel les erreurs ou maladresses dans notre code, ce qui permet d'avoir un code écrit dans les règles de l'art et nous évite de s'arracher les cheveux lors de la compilation. 

#### Installation
Ne nous en privons pas plus longtemps et installons le plugin [stylelint](https://github.com/stylelint/stylelint) pour garantir un beau code CSS. 

1. Lancer la commande `npm install --save-dev stylelint stylelint-config-sass-guidelines stylelint-webpack-plugin`, qui installe `stylelint` ainsi qu'une configuration de base pour les fichiers SASS. Si on utilisait des fichiers CSS classiques, on utiliserait alors la configuration `stylelint-config-standard`.
	
	On remarque aussi qu'on installe `stylelint-webpack-plugin`. En effet, on va plutôt utiliser `stylelint` _via_ Webpack plutôt que par PostCSS, mais les deux sont possibles. Il existe en fait plein de façons de lancer `stylelint`; ici, on présente une solution simple qui lint au moment du build.

2. Créer le fichier de configuration `.stylelintrc` et importer les règles standard téléchargées plus haut; on peut aussi remplacer des règles par les notre: 

	~~~c++
	{
	  "extends": "stylelint-config-sass-guidelines",
	    "rules": {
	    "indentation": "tab",
	    "number-leading-zero": null
	  }
	}
	~~~

3. On modifie `webpack.config.js` de la sorte:

	~~~js
	const path = require('path');
	const StylelintPlugin = require('stylelint-webpack-plugin');

	module.exports = {
	  entry: './src/index.js',
	  output: {
	    filename: 'main.js',
	    path: path.resolve(__dirname, 'dist'),
	  },
	  module: {
	    rules: [
	      {
		test: /\.css$/,
		exclude: /node_modules/,
		use: [
		  {
		    loader: 'style-loader',
		  },
		  {
		    loader: 'css-loader',
		    options: {
		      importLoaders: 1,
		    }
		  },
		  {
		    loader: 'postcss-loader'
		  }
		]
	      }
	    ]
	  },
	  plugins: [new StylelintPlugin()],
	};
	~~~	

4. La commande `npm run build` lint tous nos fichiers SASS avant l'empaquetage, et retourne les erreurs ou les non-respects de convention (ici, on voit qu'elles sont nombreuses!)

On décrit ici une configuration de base, mais on peut aller beaucoup plus loin. On peut rajouter des plugins qui lint selon des règles encore plus strictes et conventionnelles. On peut aussi automatiser le processsus avec des scripts `npm`, voire en combiner: linter avant de compiler, n'autoriser les commits que si le code passe tous les feux du linter, automatiser le linter, ...

Précisons aussi que des extensions dans la plupart des IDE existent et se basent sur `stylelint`, ce qui peut peut-être en faciliter l'usage. Cependant, ce n'est pas la meilleure pratique: il vaut mieux préciser et configurer les plugins dans des fichiers, puisque cela est bien plus rapide et reproduisible sur différentes machines. 
### Exemple 3: Utilisation d'Autoprefixer

#### Qu'est-ce qu'Autoprefixer ?
Il s'agit du plugin PostCSS le plus utilisé. Comme tous les langages de programmation, le CSS bénéficie de mise à jour régulières et de nouvelles fonctionnalités sont implémentées. Cependant, tous les navigateurs ne les adoptent pas à la même vitesse. Si on écrit un code trop moderne, les navigateurs les plus anciens ne le comprendront pas et il y aura des erreurs. L'expérience utilisateur risque fortement d'être dégradée. 

Pour ne pas inhiber ce développement progressif du langage, les navigateurs mettent à disposition des préfixes vendeurs. Ce sont des règles supplémentaires de CSS qui s'appliquent seulement aux navigateurs concernés et qui permettent d'implémenter des règles CSS encore expérimentales. Afin de s'assurer que notre code sera compris par chaque navigateur, il faut pour certaines propriétés inclure tous les préfixes vendeurs "au cas où".

Le problème est que chaque navigateur a ses propres préfixes vendeurs, et qu'il est difficile de retenir les propriétés qui nécessitent des préfixes vendeurs. Parfois même, on oublie simplement et on peut longuement chercher d'où vient la source du problème sur certains navigateurs (qui interprètent de toute façon le CSS de façons différentes). 

[Autoprefixer](https://github.com/postcss/autoprefixer) vient à la rescousse des développeurs frontends. Plus besoin de se soucier des préfixes vendeurs: on écrit simplement notre code, et le plugin les ajoute automatiquement lors du traitement du fichier CSS par PostCSS. Il garantit que tous les préfixes adéquats sont utilisés lorsque c'est nécessaire.

#### Installation
On va tout simplement utiliser Webpack à nouveau pour bénéficier de ce plugin PostCSS.

1. On lance la commande `npm install --save-dev autoprefixer`
2. On modifie `postcss.config.js` de la sorte: 

	~~~js
	module.exports = {
	    plugins: [
		require('precss'),
		require('autoprefixer')
	    ]
	  }
	~~~

3. On profite maintenant d'autoprefixer avec `npm run css`
