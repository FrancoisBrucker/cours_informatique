---
layout: layout/post.njk
title: "bases du javascript"

authors:
  - "François Brucker"


eleventyNavigation:
  key: "bases du javascript"
  parent: "javascript"
---
{% prerequis "**Prérequis** :" %}

* [Avoir un système en état de marche]({{ '/tutoriels/installation-système' | url }})
* [Savoir naviguer dans un système de fichiers]({{ '/tutoriels/fichiers-navigation' | url }})
* [Installation et prise en main de l'éditeur de texte vsc]({{ '/tutoriels/vsc-installation-et-prise-en-main' | url }})
* Il pourra de plus être très utile de :
  * [Savoir ouvrir une fenêtre terminal]({{ '/tutoriels/terminal'  | url }})
  * [D'installez brew si vous êtes sous mac]({{ '/tutoriels/brew'  | url }})

{% endprerequis %}

<!-- début résumé -->

Premières utilisation de javascript.
<!-- fin résumé -->

[Javascript](https://fr.wikipedia.org/wiki/JavaScript) n'est **pas** java. Ça n'a même rien à voir. C'est en revanche un langage de script objet (comme python) qui est peut être utilisé partout et que l'on retrouve souvent dan le web :

* *côté front* : c'est le navigateur qui exécutera le code javascript de la page sur l'[ordinateur client](https://fr.wikipedia.org/wiki/Client_(informatique)) (c'est à dire celui qui qui exécute le navigateur).
* *côté back* : C'est le [serveur](https://fr.wikipedia.org/wiki/Serveur_informatique) qui exécutera le code (c'est à dire celui qui possède la ressource que va chercher le navigateur). On utilise souvent la bibliothèque <https://nodejs.org/en/> pour cela.

{% note %}
Ça n'a l'air de rien mais exécuter du code côté client et côté serveur ce n'est pas la même chose du tout. Dans un cas on a accès à l'ordinateur qui exécute le navigateur, dans l'autre à l'ordinateur qui possède le serveur sur lequel on va chercher les ressources.
{% endnote %}

Nous verrons ici ce que ça veut dire qu'exécuter du javascript et le strict nécessaire pour pouvoir faire illusion en soirée.

## L'interpréteur javascript

Tout comme python, javascript est un [langage interprété](https://fr.wikipedia.org/wiki/Interpr%C3%A8te_(informatique)). Chaque ligne de javascript est exécutée dans un programme appelé interpréteur.  Il en existe essentiellement deux :

* votre navigateur web
* celui de [node](https://nodejs.org/en/)

Nous allons présenter les deux.

{% info %}
La plupart du temps, c'est l'interpréteur de la [V8](https://fr.wikipedia.org/wiki/V8_(moteur_JavaScript)) qui est utilisé. Il existe plusieurs interpréteurs javascript, ils sont tout autant valable les uns que les autres s'il respectent les spécifications du langage javascript appelé [ecmascript](https://fr.wikipedia.org/wiki/ECMAScript) (les évolutions de cette norme sont visible [là](https://www.w3schools.com/js/js_versions.asp) par exemple)
{% endinfo %}

### Navigateur web

On exécutera le code depuis un fichier html. La sortie standard est la console, que vous pouvez voir avec les [outils de développement](../../outils-de-développement/) (*"... du menu > show console drawer"*, ou en appuyant sur la touche <esc> alors que la fenêtre des outils de développement est ouverte).

{% faire %}

fichier [`hello_javascript.html`](./javascript_files/hello_javascript.html). Ouvrez le dans un navigateur.

Créez une fichier `hello_javascript.html`{.fichier} avec le contenu suivant :

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" /> 
        <title>
            Test de javascript
        </title>
        <script>
            console.log("Bonjour monde !");
        </script>
    </head>
    <body>
        <h1>regardez dans la console !</h1>
    </body>
</html>
```

{% endfaire %}

Le fichier html précédent écrit dans la console javascript du navigateur. Vous voyez l'utilisation du javascript via la balise <script></script>

### node

[Node](https://nodejs.org/en/) est un interpréteur javascript puissant basé sur la V8 et qui contient des bibliothèques dédiées très pratiques lorsque l'on code en javascript.

<https://nodejs.dev/learn>

#### Installation de node { #bloc-id-installation-node }

{% details "sous Linux" %}
Vous pouvez utiliser [nodesource](https://github.com/nodesource/distributions/blob/master/README.md) pour installer node.
{% enddetails %}

{% details "sous Mac" %}
Comme dit dans le tuto d'installation, on utilise le gestionnaire de package [brew](https://brew.sh/).

Une fois celui ci installé, on tape dans un terminal la commande : `brew install node`
{% enddetails %}

{% details "sous Windows" %}
Vous téléchargez la version courante de node : <https://nodejs.org/en/download/current/>.
{% enddetails %}

{% attention %}
Il existe 2 versions de Node](https://nodejs.org/en/), la *LTS (long term support)* et la *current*. On choisira la version *current* qui est la plus récente. La version *LTS* est là pour des raisons de compatibilité.
{% endattention %}

#### utilisation de node

Une fois <https://nodejs.org/en/>, tapez `node` dans un terminal. Vous êtes dans un interpréteur javascript. Vous pouvez ensuite taper `console.log("bonjour monde !")`. Vous devriez obtenir quelque chose du genre :

```js
> console.log("coucou")
coucou
undefined
> 
```

La première réponse (`coucou`) correspond à l'action de `console.log` qui est d'afficher du texte, la seconde réponse (`undefined`) correspond au retour de `console.log`.

{% info %}
Utiliser l'interpréteur `node` dans un terminal est identique à utiliser l'interpréteur `python` par exemple. On tape des lignes qui sont interprétées lorsque l'on tape entrée.
{% endinfo %}

On peut aussi, tout comme pour python, exécuter un fichier. Par exemple le fichier *"hello.j"* :

```js
nom = "François"

console.log("bonjour " + nom + " !")
```

Qu'on pourra exécuter avec la commande : `node hello.js` dans un terminal se trouvant dans le dossier contenant le fichier *"hello.js"*.

Pour la bonne bouche, un petit exemple de javascript utilisant node un peu plus compliqué :

fichier *"hello_qui.js"* :

```js
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Quel est ton nom ? ', (answer) => {
  console.log(`Bonjour ${answer} !`);

  rl.close();
});
```

On a utilisé :

* l'import de la bibliothèque [readline](https://nodejs.org/api/readline.html#readline_readline) de node,
* [process.stdin](https://nodejs.org/api/process.html#process_process_stdin) et [process.stdout](https://nodejs.org/api/process.html#process_process_stdout) pour les entrées/sorties standard
* une fonction anonyme du type `() => {}` comme paramètre d'une fonction.
* les [construction de chaines de caractère avec `${}`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Template_literals)

## Langage

Tout comme python, un script javascript est exécuté ligne à ligne. A la moindre erreur le script s'arrête.

Testez le code suivant :

```html
<!DOCTYPE html>

<html>
<head>
<title>Hello World en javascript avec des erreurs</title>
<meta charset="utf-8" />
</head>

<body>
<script>
     window.allert("Hello World!"); //une erreur !
    console.log("Hello World!");
</script>
</body>

</html>
```

Rien n'est écrit dans la console et une croix rouge est apparu.

{% faire %}

1. corrigez la faute et exécutez le code.
2. une fenêtre s'affiche. Elle est modale. Cela signifie que le code s'est mis en pause. `Hello world` ne s'affiche qu'une fois que l'on a tapé OK.

{% endfaire %}

Il est **indispensable** d'exécuter le code javascript dans un html avec les outils de développement pour savoir quand il y a eu une erreur. Sans ça, il est impossible de dire si tout s'est bien passé.

Si vous tentez d'exécuter le code précédent dans un node, vous obtiendrez l'erreur : `Uncaught ReferenceError: window is not defined`. En effet, l'objet window c'est le navigateur. Il n'existe pas dans l'interpréteur node.

{% attention %}
l'utilisation de `window.alert` est certes marrant, mais c'est une action modale (le code est en pause jusqu'à ce que l'on ait appuyé sur `OK`), on ne sait donc pas tout de suite si le code fonctionne ou pas. Il vaut mieux faire ses tests avec la console en utilisant la fonction `console.log()`.
{% endattention %}

### fonctions et variables

Exécutez le code suivant dans un node. Appelons ce fichier *"fct.js"* :

```js
// définition classique d'une fonction
function du_texte(texte) {
    console.log(texte)
}
du_texte("coucou")

// la variable texte_plus_entete est associé à l'objet function
texte_plus_entete = function(texte) {
    console.log("Et ben : " + texte)
}
//on peut l'exécuter
texte_plus_entete("zut alors")

compteur = 0 //les variables sont globales
entete_texte = "S'il vous plait ? "
function entete_dans_variable(texte) {
    console.log(entete_texte + texte)
    compteur += 1 //on change la variable globale
    console.log(`cette fonction a été appelée ${compteur} fois.`)
}

entete_dans_variable("Bonjour ! ")
entete_dans_variable("Au revoir.")
```

> TBD fonction () => {}

Le bout de code ci-dessus montre plusieurs spécificités de javascript :

* plusieurs façon de créer des fonctions :
  * normale (crée une fonction nommée `ma_fct`) : `function ma_fct(params) {code}`
  * anonyme (rend un objet fonction) :`function (params) {code}`, que l'on pourrait aussi écrire `(params) => {code}`
* les commentaires javascript s'écrivent en commençant par `//`
* les variables sont globales par défaut (`i = 1`), `var` les rend locales (`var i = 1`)
* la construction automatique de chaines. `\`cette fonction a été appelée ${compteur} fois.\` ` est équivalent à la concaténation classique : `"cette fonction a été appelée " + compteur + " fois."`

{% note %}
Beaucoup de choses en web sont asynchrones : on envoie une requête au serveur et on exécute le résultat lorsque l'on obtient la réponse du serveur. De là, beaucoup de fonctions ne sont utilisées qu'une seule fois. C'est ce qui explique que l'on utilise abondamment de fonction anonymes.
{% endnote %}

### types d'objets

TBD : A tester dans la console.

* basiques :
  * nombres (3 et 3.14)
  * chaines de caractères ("ma chaine")
* conteneurs :
  * tableaux : liste d’objets indicés par des entiers. S'utilise comme en python :
    * création d'un tableau : `mon_tableau = [1, "trois", 2.71]`
    * indice : `mon_tableau[1]` rend "trois"
  * dictionnaires : comme en python sauf que les clés ne peuvent être que des chaînes de caractères. liste d’objet indicés par des chaines de caractères. Autre spécificité, il n'est pas nécessaire de mettre les `"` lorsque l'on défini les clés.
    * `mon_dict = {pi: 3.14, potes: ["Pascal", "Manu"] }`
    * clés : `mon_dict["potes"] (rend ["Pascal", "Manu"])`

{% note %}
Les dictionnaires ont une importance énorme en javascript et en web en général : il n'y a pas de différence entre un dictionnaire et un objet. Pour s'en convaincre, regardez le type d'un dictionnaire avec l'opérateur [typeof](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Operators/typeof) : `typeof {a:1}`.
{% endnote %}

### object

<https://developer.mozilla.org/fr/docs/Learn/JavaScript/Objects/Basics>

## gestion des dépendances

> TBD : à faire propre
{.note}

L'import de fichiers en javascript est différents de beaucoup d'autres langages. En gros :

> c'est le cirque.
{.attention}

### bibliothèques node

node_modules et npm/yarn

### importer dans un script

Il existe plusieurs façon d'importer des modules en javascript :

* la façon ecmascript avec les mots clés `import` et `export`
* la façon commonjs avec les mots clés `require` et `module.export`
* la façon web en lisant bêtement le fichier à importer dans l'interpréteur

On peut plus ou moins passer d'une version à l'autre mais c'est compliqué 

<https://redfin.engineering/node-modules-at-war-why-commonjs-and-es-modules-cant-get-along-9617135eeca1>

<https://adrianmejia.com/getting-started-with-node-js-modules-require-exports-imports-npm-and-beyond/>

<https://javascript.info/import-export>

#### ecmascript modules

import / export

<https://nodejs.org/api/esm.html#esm_modules_ecmascript_modules>

#### commonjs modules

require

<https://nodejs.org/api/modules.html#modules_modules_commonjs_modules>

### dans le web

* plusieurs balises script
* charger un fichier par le script
  * local
  * cdn
  * node_modules

<https://developer.mozilla.org/fr/docs/Web/HTML/Element/script>

{% attention %}
par d'import sauf si module
<https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements/import>
<https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Modules>
{% endattention %}
