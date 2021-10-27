---
layout: page
title: "Webpack"
category: cours
tags: packaging webpack front
authors:
  - "Victoire Flesselles"
  - "William Templeton"
---
## Pourquoi utiliser Webpack ?

### Un exemple
Partons d'un projet très simple de calculatrice qui réalise les opérations de base : `+`, `-`, `*`, `/`. La structure du projet est la suivante: 

~~~
.
├── index.html
├── css
│   └──style.css
├── js
│   └──index.js
└── scss
    └── style.scss
~~~
Les différents codes sources sont: 

+ `index.html` :

	~~~html
	<html>
		<head>
			<meta charset="utf-8"/>
			<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
			<title>Calculatrice</title>
			<link href="https://fonts.googleapis.com/css?family=Montserrat&display=swap" rel="stylesheet"/>
			<link rel="stylesheet" type="text/css" href="css/style.css"/>
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
		<script src="js/index.js"></script>    
	</html>
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

+ `index.js` :

	~~~js
	var numInputs = document.querySelectorAll(".number-inputs input");
	var opInputs = document.querySelectorAll(".operators input");
	
	function insert(num) {
	    return document.getElementById("result").value += num;
	}
	function calcul() {
	    return document.getElementById("result").value = eval(document.getElementById("result").value);
	}
	function del() {
	    return document.getElementById("result").value = "";
	}
	
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

Il suffit d'ouvrir `index.html` pour avoir le rendu. La compilation `scss -> css` a été vue dans le cours sur SASS.

Bien que le projet soit simple, on aimerait améliorer la structure du projet au cas où on souhaite ajouter de nouvelles fonctionnalités. Jusqu'à présent, tout le fonctionnement de la calculatrice est géré dans un seul fichier `index.js`. C'est un peu maladroit: plus notre projet prend de l'ampleur, plus notre fichier javascript devient long et difficile à maintenir. Il est plus judicieux de le diviser selon des fonctionnalités qui remplissent un objectif différent. On préfère donc le scinder selon:
+ la déclaration de variables
+ la définition des fonctions
+ l'attribution des fonctions aux éléments HTML

On adopte alors la structure suivante: 
~~~
.
├── css
│   └── style.css  
├── index.html
├── js
│   ├── index.js
│   ├── variables.js
│   └── methods.js
└── scss
    └── style.scss
~~~
où les trois fichiers `js` sont les suivants:
+ fichier `variables.js`:

	~~~js
	var numInputs = document.querySelectorAll(".number-inputs input");

	var opInputs = document.querySelectorAll(".operators input");
	~~~

+ fichier `methods.js`:

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
	~~~

+ fichier `index.js`:

	~~~js
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

Afin de s'assurer que le fichier `index.js` dispose des variables et méthodes nécessaires à son exécution, il faut nécessairement importer les fichier `js` dans `index.html` de la façon suivante:
~~~html
<script src="js/variables.js"></script>    
<script src="js/methods.js"></script>    
<script src="js/index.js"></script>   
~~~

Cette méthode est simple et à l'avantage d'être très comprensible: sur un fichier html, chaque balise `<script>` importe le fichier dont on a besoin pour faire fonctionner la page.

Mais elle est terriblement archaïque, et ce pour plusieurs raisons: 
+ Pour un très gros projet, il peut y avoir des centaines des fichiers et libraires javascript nécessaires au bon fonctionnement du site, et tout autant de pages `html`. Avec cette méthode, pour chaque page `html`, il faudrait faire un grand copié/collé (ce qui est mauvais signe) de toutes ces dépendances, sans se tromper dans l'ordre d'importation.
+ Chaque changement est laborieux: lorsqu'on ajoute une nouvelle librairie ou un nouveau fichier, ou même simplement renommer un fichier, il faut effectuer manuellement dans chacune des pages `html`
+ La logique de déclaration et d'importation est obscure et non optimisée. Avec une telle méthode, il n'est pas clair quel fichier a besoin de quelles méthodes et variables déclarées dans un certain fichier; souvent, dans le doute, toutes ces variables et fonctions sont déclarées alors que ce n'est pas toujours nécessaires. 

La solution serait d'importer un seul fichier `js` dans `index.html`, qui gère quels fichiers sont importés. Pour cela, les fichiers `js` doivent pouvoir faire appel aux autres, comme c'est le cas avec `node.js` avec la méthode `require`.

Cependant, importer des fichiers `js` via des `require` ou `import` n'est pas autorisé sur les navigateurs, puisque le javascript n'est censé que tourner sur le navigateur et n'a pas été concu pour accéder à des fichiers systèmes. On a pas ce problème avec node, qui tourne côté serveur (et a donc accès aux fichiers). 

Il faut donc regrouper les fichiers `js` et les compiler dans un seul paquet lisible par les navigateurs. C'est la qu'intervient les bundler comme [Webpack](https://webpack.js.org/) ou [Parcel](https://parceljs.org/).

## Webpack en bref
<p align="center">
	<img src="./images/webpack.png">
</p>
### Comment ça marche ? 

Webpack réalise une concaténation "intelligente" des fichiers en un seul et même fichier: chaque fichier indique ses dépendances, qui sont incluses dans un graphe global. Finalement, dans le fichier `html`, au lieu d'importer plusieurs modules et librairies entières, on n'a qu'une seule balise script qui prend en compte le fichier d'output de webpack.
Pour cela, Webpack fonctionne alors en deux étapes: 

#### Une étape de détermination des dépendances

Webpack part du fichier "entrée" spécifié dans la configuration, puis parcourt le fichier à la recherche de modules dépendant de cette entrée. Il parcourt ensuite chacun de ses modules à la recherche de modules qui en dépendent, construisant alors un graphe de dépendance. Ainsi de suite, jusqu'à ce que toute l'arborescence des dépendances soit épuisée.  

#### Une étape d'empaquetage

Webpack empaquete alors les fichiers dans un seul même fichier n'utilisant que le nécesaire à chaque module. Par exemple, si une seule fonction d'un module est utilisée, seule cette fonction sera compilée dans le fichier de sortie. Webpack ne modifie aucun code autres que les `import`/`export`. 

Le plus souvent, Webpack sert surtout à empaqueter des fichiers `js`, mais en réalité, tous types de fichiers peuvent être empaqueter par Webpack. On peut ainsi relier des fichiers `js`, `css`/`scss`, des images ou vidéos, ... et Webpack empaquetera tout dans un seul bundle qui chargera les fichiers selon le besoin. 

### Principes
Les concepts principaux sont détaillés dans la [documentation](https://webpack.js.org/concepts) officielle de Webpack.
#### Entry point
Un Entry Point indique avec quel module webpack doit commancer à construire son graphe de dépendance des modules. Il sélectionne uniquement ce dont il a besoin dans chaque module et librairie selon toutes ses dépendances. Dans le fichier de configuration de Webpack, on précise donc le chemin de ce fichier.

On peut vouloir avoir plusieurs points d'entrée, par exemple quand vous faites deux applications dans le même projet (app visiteur lambda et app admin). Dans ce cas là deux Output seront contruites, mais l'avantage est qu'en fonction de l'ordre de chargement des fichiers, les librairies en commun ne seront chargées qu'une seule fois. Webpack optimise ceci.

#### Output point
Le champ Output indique à webpack où mettre et comment nommer les bundles qu'il créé.
On peut set up plusieurs outputs.

#### Loaders
Comme indiqué dans la partie de l'empaquetage, les `import`/`export` sont les seules lignes de codes qui sont modifiées par Webpack pour produire un seul fichier recueillant tous les modules. Cepandant ces syntaxes ne sont pas supportées par tous les navigateurs. Ainsi, Webpack nécessite l'utilisation d'un transpiler pour l'adapter à tous les types de navigateurs.

#### Autres
Les 3 points précédants sont les points les plus importants à comprendre pour commencer la configaration de webpack. D'autres paramètres sont configurables comme Plugins, Mode ou Browser Compatibility. 

## Applications 
### Retour au projet de la calculatrice
Revenons à notre projet de calculatrice. Avec Webpack, on souhaite n'avoir qu'un seul fichier `js` de chargé dans notre fichier `index.html`. En termes de dépendance, `index.js` fera appel à `variables.js` et `methodes.js`. 

(on suivra le [guide officiel](https://webpack.js.org/guides/) de Webpack)

1. On commence par initialiser `npm` avec `npm init -y` (la balise `-y` permet de sauter les questions de npm, lorsqu'on veut rapidement initialiser), puis on install Webpack: `npm install webpack webpack-cli --save-dev`
2. Nous n'avons pas besoin d'un point d'entrée pour npm, puisque tout sera chargé dans un seul fichier `js` dans `index.html`. La documentation Webpack recommande de modifier le champ `private` pour éviter de publier involontairement du code probablement propriétaire dans npm. Le fichier `package.json` ressemble alors à : 
~~~json
{
  "name": "calculatrice-webpack",
  "version": "1.0.0",
  "description": "",
  "private":true,
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
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
3. Puisqu'on va empaqueter tous nos fichiers `js` en un seul, il faut faire la distinction entre les fichiers qui vont servir pendant le développement et ceux qui vont servir en production. C'est une question d'optimisation: cela évite de déployer des fichiers inutiles. On distingue alors les fichiers sources des fichiers de distribution. La structure du projet ressemble alors à :
~~~
.
├── dist
│   ├── index.html
│   └── style.css
├── node_modules
├── package.json
├── package-lock.json
└── src
    ├── index.js
    ├── methods.js
    ├── style.scss
    └── variables.js
~~~

4. Grâce à Webpack, on va pouvoir exporter les variables de `variables.js` et les fonctions de `methodes.js`, puis les importer dans `index.js`. Les 3 fichiers ressemblent désormais à :

	+ `variables.js` :

		~~~js
		var numInputs = document.querySelectorAll(".number-inputs input");

		var opInputs = document.querySelectorAll(".operators input");

		export {numInputs, opInputs}
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

5. Désormais, plus besoin d'importer les 3 scripts. Webpack va nous fournir un seul fichier de sortie, `main.js`, qui sera un fichier de distribution (donc localisé dans `dist/`). Le fichier `index.html` ressemble maintenant à :

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

6. On est prêt à empaqueter. Dans un terminal, on lance la commande suivante dans le répertoire source: `npx webpack`. Webpack donne en sortie le fichier `main.js` dans le répertoire `dist/`. 

	On remarque que toutes les fonctionnalités tiennent en une seule ligne, avec un code assez différent de ce qu'on a écrit. C'est la magie de Webpack: le fichier `main.js` est totalement optimisé et ce pour chaque navigateur, le but n'étant pas d'être humainement lisible.

	Notre projet est simple et on pourrait se contenter d'utiliser Webpack de la sorte. Mais s'il prend de l'ampleur, on sera rapidement limité avec cette méthode. Il est vivement recommandé d'utiliser un fichier de configuration qui permettra de spécifier ce qu'on attend de Webpack depuis un terminal. Le but est de gagner en flexibilité et en efficacité.

7. On créé un fichier `webpack.config.js` dans le répertoire source avec la configuration de base suivante: 

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

	On peut maintenant lancer Webpack avec la commande `npx webpack --config webpack.config.js`. Vu notre projet, cela n'a en apparence pas grand intérêt. Mais, à mesure que notre fichier de configuration grandit et devient complexe, la commande pour lancer Webpack sera toujours la même, alors qu'elle devriendrait indigeste si on souhaitait s'en passer.
	
8. On peut aller encore un peu plus loin en créant un script `npm` pour lancer l'empaquetage en une commande. La convention pour n'importe quel projet veut que la commande soit `npm run build`. Cela permet à tous les développeurs de s'approprier plus rapidement d'un projet et de le lancer avec une seule commande, sans se soucier d'options éventuelles. Ici, il suffit de modifier le fichier `package.json` de la sorte: 

	~~~json
	{
	  "name": "calculatrice-webpack",
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

Le [guide officiel](https://webpack.js.org/guides/) de Webpack permet d'aller bien plus loin: lier d'autres types de fichiers, maîtriser la sortie, ...

### Postcss
voir cours postcss

### Comment Réact utilise Webpack
Savoir comment React utilise Webpack pour contruire la page est un avantage pour comprendre Webpack lui-même.
Ce [tuto](https://freecodecamp.org/news/an-intro-to-webpack-what-it-is-and-how-to-use-it-8304ecdc3c60) vous mène à travers la construction (très simplifiée certes) d'une application React sans utiliser le `create-react-app CLI` qui fait tout le travail en arrière plan.

La puissance de Webpack permet de créer des pages web avec un seul fichier `html`. On peut utiliser une architecture en composants et écrire notre `html` directement dans du `js` pour l'injecter à l'endroit voulu dans la page. En faisant ainsi, on peut très facilement créer une pages à plusieurs onglets en ayant qu'un seul fichier `html`. Cette façon de procéder est à la base de nombreux framework fronts, notamment les plus connus: React, Angular et Vue. Et l'avantage principal est la rapidité des applications produites ainsi, car la page n'est pas rechargé à chaque fois qu'on veut changer d'onglet.

Ainsi à la fin de ce tutoriel on obtient un seul fichier `html` dans lequel on a une balise `<div>` dans le corps du fichier, et cette balise est le point d'injection du reste de l'application qui est codé dans des fichiers `js`.
## Parcel, une alternative à Webpack ?
Bien que Webpack soit le bundler le plus utilisé, il n'est pas le seul sur le marché. [Parcel](https://parceljs.org/) est une alternative récente. 

<p align="center">
	<img src="./images/parceljs.png">
</p>
### Intérêt
+ Le plus grand atout de Parcel est qu'il n'y a rien à configurer. Alors qu'on est rapidement amenés à configurer assez lourdement `webpack.config.js` pour prendre en compte toutes les spécificités du projet, Parcel le fait automatiquement en une seule ligne de commande: `parcel index.html`.
+ Comme le suggère la commande ci-dessus, Parcel se lance le plus souvent (car c'est le plus pratique) avec un fichier `html` comme cible. Parcel est capable de déduire du fichier quel fichier `js` est le point d'entrée et créé le bundle dans la foulée.
+ Parcel dispose d'un système de cache: bien que le premier empaquetage soit lent, ceux d'après sont très rapides;

### Inconvénients
+ On ne l'a pas exploré dans ce tuto, mais il vaut souvent mieux créer plusieurs bundles qui peuvent alors être chargés lorsque c'est nécessaire ou en parallèle, ce qui peut drastiquement réduire les temps de chargement. On parle de [code splitting](https://webpack.js.org/guides/code-splitting/). 
	Grâce au fichier de configuration de Webpack, le code splitting est totalement maîtrisé: on contrôle où vont les fichier `js`, `css`, etc. De l'autre côté, c'est Parcel qui automatise ce processus, mais pas nécessairement de la façon qu'on souhaiterait. Notamment, le dossier comprenant tous les bundle n'a qu'un seul niveau: tous les fichiers sont au même endroit, ce qui peut porter à confusion. 

+ Sûrement dû à son développement récent, Parcel n'est pas adopté ou supporté par la plupart d'outils tiers. Gatsby ou les frameworks front-ends Angular, React et Vue utilisent tous Webpack. Pour maîtriser ces technologies, mieux vaut donc utiliser Webpack. De la même façon, beaucoup plus de développeurs utilisent Webpack, ce qui signifie qu'il y a plus d'aide en ligne lorsqu'on rencontre un problème. 

### Quel bundler utiliser ?
Comme souvent lorsqu'on hésite entre deux outils similaires, c'est la nature du projet qui tranche. Pour les projets de petites tailles ou pour rapidement lancer un prototype, Parcel est parfait puisqu'il garantie aucune prise de tête. Pour les projets d'envergure, Webpack reste la référence. 
