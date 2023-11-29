---
layout: layout/post.njk
title: "Javascript : bases"

authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Ce cours, tente de donner des notions de javascript et de comment l'utiliser en console, en script ou dans un navigateur.

<!-- fin résumé -->

On considère que vous savez déjà programmer en python, on ne traitera donc pas tous les détails. Il existe pleins de tutos pour apprendre javascript :

{% lien "**Tutoriels généraux sur javascript**" %}

- Si vous ne deviez faire qu'un seul tutoriel : <https://developer.mozilla.org/fr/docs/Web/JavaScript> qui contient tout ce qu'il faut
- <https://fr.javascript.info/>
- <https://grafikart.fr/tutoriels/javascript> en revanche, je ne sais pas si tout est gratuit.
- <https://www.tutorialspoint.com/javascript/index.htm>

{% endlien %}
{% attention %}
Avant de choisir un tuto, Vérifier bien cependant qu'ils ne soient pas trop vieux, javascript a beaucoup évolué au cours des années.
{% endattention %}

[Javascript](https://fr.wikipedia.org/wiki/JavaScript) n'est **pas*- java. Ça n'a même rien à voir. C'est en revanche un langage de script objet (comme python) qui est peut être utilisé partout et que l'on retrouve souvent dans le web :

- *côté front* : c'est le navigateur qui exécutera le code javascript de la page sur l'[ordinateur client](https://fr.wikipedia.org/wiki/Client_(informatique)) (c'est à dire celui qui qui exécute le navigateur).
- *côté back* : C'est le [serveur](https://fr.wikipedia.org/wiki/Serveur_informatique) qui exécutera le code (c'est à dire celui qui possède la ressource que va chercher le navigateur). On utilise souvent <https://nodejs.org/> pour cela.

{% note %}
Ça n'a l'air de rien mais exécuter du code côté client et côté serveur ce n'est pas la même chose du tout. Dans un cas on a accès à l'ordinateur qui exécute le navigateur, dans l'autre à l'ordinateur qui possède le serveur sur lequel on va chercher les ressources.
{% endnote %}

Nous verrons ici ce que ça veut dire qu'exécuter du javascript et le strict nécessaire pour pouvoir faire illusion en soirée.

## L'interpréteur javascript

Tout comme python, javascript est un [langage interprété](https://fr.wikipedia.org/wiki/Interpr%C3%A8te_(informatique)). Chaque ligne de javascript est exécutée dans un programme appelé interpréteur.  Il en existe essentiellement deux :

- votre navigateur web
- celui de <https://nodejs.org/>

### Javascript dans un navigateur

{% info %}
La plupart du temps, c'est l'interpréteur de la [V8](https://fr.wikipedia.org/wiki/V8_(moteur_JavaScript)) qui est utilisé. Il existe plusieurs interpréteurs javascript, ils sont tous aussi valables les uns que les autres s'il respectent les spécifications du langage javascript appelé [ecmascript](https://fr.wikipedia.org/wiki/ECMAScript) (les évolutions de cette norme sont visible [là](https://www.w3schools.com/js/js_versions.asp) par exemple)
{% endinfo %}

#### Directement depuis la console

L'interpréteur est accessible via la . Vous pouvez la consulter grâce aux [outils de développement](../../outils-de-développement/){.interne} (*"... du menu > show console drawer"*, ou en appuyant sur la touche <esc> alors que la fenêtre des outils de développement est ouverte).

{% aller %}
[Console avec chrome](https://developer.chrome.com/docs/devtools/console/)
{% endaller %}

Il est indispensable de connaître cette méthode car elle permet d'accéder directement au javascript de la page pour analyse les composant de la page et/ou débeuguer son code.

#### Via la balise `<script></script>`{.language-}

{% faire %}

Créez une fichier `hello_javascript.html`{.fichier} avec le contenu suivant :

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" /> 
        <title>
            Test de javascript
        </title>
    </head>
    <body>
        <h1>regardez dans la console !</h1>

        <script>
            console.log("Bonjour monde !");
        </script>
    </body>
</html>
```

Puis ouvrez [le](./hello_javascript){.interne}. Ouvrez le dans un navigateur.

{% endfaire %}

Le fichier html précédent écrit dans la console javascript du navigateur. Vous voyez l'utilisation du javascript via la balise `<script></script>`{.language-}. On place généralement le code javascript à exécuter à la fin de la page comme ça il pourra avoir accès à tout le contenu de la page.

En effet, le code est exécuté au **moment où il est lu**. Si vous le placer au début de votre page, il sera exécuté avant que le contenu de la page ne soit affiché.

On utilise ce comportement lorsque l'on charge une bibliothèque javascript. On veut exécuter le code de cette bibliothèque avant toute chose, on la place donc dans le header. Par exemple pour utiliser le plugin <https://datatables.net/>, on ajoute dans les header du fichier html la ligne  :

```html
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>
```

Il y a donc deux façon d'inclure du javascript dans vos fichiers html via la balise script :

1. soit du code et dans ce cas là on l'ajoute **à la fin de la page** pour qu'il puisse utiliser tous les éléments définis dans la page
2. soit des bibliothèque et dans ce cas là on l'ajoute **au début de la page, dans les headers** pour qu'elle puisse être utilisée par tous les éléments de la page.

#### Attention aux erreurs

Tout comme python, un script javascript est exécuté ligne à ligne. **À la moindre erreur**, le script s'arrête.

Considérons le code suivant :

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

{% faire %}

1. Testez le code précédent et vérifiez que rien n'est écrit dans la console et qu'une croix rouge est apparue.
2. Corrigez la faute et exécutez le code.
3. Une fenêtre s'affiche. Elle est modale. Cela signifie que le code s'est mis en pause. `Hello world`{.language-} ne s'affiche qu'une fois que l'on a tapé OK.

{% endfaire %}

Il est **indispensable** d'exécuter le code javascript dans un html avec les outils de développement pour savoir quand il y a eu une erreur. Sans ça, il est impossible de dire si tout s'est bien passé.

Si vous tentez d'exécuter le code précédent dans un <https://nodejs.org/>, vous obtiendrez l'erreur : `Uncaught ReferenceError: window is not defined`. En effet, l'objet window c'est le navigateur. Il n'existe pas dans l'interpréteur <https://nodejs.org/>.

{% attention %}
l'utilisation de `window.alert`{.language-} est certes marrant, mais c'est une action modale (le code est en pause jusqu'à ce que l'on ait appuyé sur `OK`), on ne sait donc pas tout de suite si le code fonctionne ou pas. Il vaut mieux faire ses tests avec la console en utilisant la fonction `console.log()`{.language-}.
{% endattention %}

### Javascript avec <https://nodejs.org/>

{% note "installation" %}
Commencez par télécharger installer la version current de <https://nodejs.org/> : <https://nodejs.org/en/download/current>.
{% endnote %}

<https://nodejs.org/> s'utilise via le terminal. Si vous ne savez pas ce que c'est lisez le tutoriel suivant :

{% aller %}
[Utilisation du terminal](/tutoriels/terminal)
{% endaller %}

D'un terminal il vous suffit de taper `node` pour exécuter l'interpréteur :

```js
$ node                 
Welcome to Node.js v20.8.1.
Type ".help" for more information.
> console.log("Bonjour de node")
Bonjour de node
undefined
> x = 40 + 2
42
> 
```

{% info %}
Pour quitter l'interpréteur <https://nodejs.org/> vous pouvez :

- soit taper `ctrl+D`
- soit exécuter la commande `.exit`{.language-}

{% endinfo %}
Tout comme l'interpréteur python, <https://nodejs.org/> exécute ligne à ligne du code puis affiche son résultat. Dans l'exemple précédent on exécute deux commandes :

1. `console.log("Bonjour de node")`{.language-}
2. `x = 40 + 2`{.language-}

A chaque fois l'interpréteur <https://nodejs.org/> exécute la commande :

1. affiche à l'écran `"Bonjour de node"`
2. affecte à la variable `x` la somme 40 plus 2

***Puis*** affiche le résultat de la commande :

1. `undefined` car le retour de la fonction `console.log` n'est pas définit
2. `42` qui est la valeur de l'affectation

Ce comportement est différent de l'exécution de code javascript dans un fichier. Créez par exemple un fichier `exemple.js`{.fichier} contenant :

```js
console.log("Bonjour de node")
x = 40 + 2
```

Puis placez vous dans le dossier contenant ce fichier dans le terminal et exécutez la comande suite :

```sh
$ node exemple.js 
Bonjour de node
```

Vous ne verrez ni `undefined` ni `42`. Dans le mode exécution de fichier, <https://nodejs.org/> exécute le fichier ligne à ligne mais n'affiche pas le résultat des commandes.

{% info %}
L'interpréteur python fonctionne exactement de la même manière.
{% endinfo %}

## Langage

Faites vos différents essais avec <https://nodejs.org/>

### Variables et Fonctions

Utilisons la console javascript de notre navigateur.

#### Blocs

Les blocs de javascript sont distingués par des `{}`{.language-}.

#### Variables

Les variables se déclarent avec le mot-clé `let`{.language-} :

```js
let pi = 3.14

console.log(pi)
```

On peut modifier une variable en omettant `let`{.language-} :

```js
let pi = 3.14

console.log(pi)

pi = "trois virgule quatorze !"

console.log(pi)
```

C'est en revanche une erreur de redéclarer la même variable. Le code suivant va produire une erreur :

```js
let pi = 3.14
let pi = "trois virgule quatorze !"
```

Enfin, la [portée](https://fr.wikipedia.org/wiki/Port%C3%A9e_(informatique)) d'une variable est son bloc. Le code suivant est donc légitime (on redéfinie une nouvelle variable qui disparaît à la fin du bloc) et affichera 3.14 à l'écran :

```js
let pi = 3.14
{
  let pi = "po"
}
console.log(pi)

```

La documentation ci-après explicite tout ce qu'il y a à savoir sur les variables :

{% lien "**Documentation**" %}
<https://developer.mozilla.org/fr/docs/Learn/JavaScript/First_steps/Variables>
{% endlien %}

{% faire %}
Testez les différents types d'objets suivant dans la console en les mettant dans une variable
{% endfaire %}

- basiques :
  - nombres (3 et 3.14)
  - chaines de caractères ("ma chaîne")
- conteneurs :
  - tableaux : liste d’objets indicés par des entiers. S'utilise comme en python :
    - création d'un tableau : `let mon_tableau = [1, "trois", 2.71]`{.language-}
    - indice : `mon_tableau[1]`{.language-} rend "trois"
  - dictionnaires : comme en python sauf que les clés ne peuvent être que des chaînes de caractères. liste d’objet indicés par des chaines de caractères. Autre spécificité, il n'est pas nécessaire de mettre les `"`{.language-} lorsque l'on défini les clés.
    - `let mon_dict = {pi: 3.14, collègues: ["Pascal", "Manu", "Ronan"] }`{.language-}
    - clés : `mon_dict["collègues"] (rend ["Pascal", "Manu", "Ronan"])`{.language-}

{% note %}
Les dictionnaires ont une importance énorme en javascript et en web en général : il n'y a pas de différence entre un dictionnaire et un [objet](https://developer.mozilla.org/fr/docs/Learn/JavaScript/Objects/Basics). Pour s'en convaincre, regardez le type d'un dictionnaire avec l'opérateur [typeof](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Operators/typeof) : `typeof {a:1}`.
{% endnote %}

#### Constantes

Vous pouvez utiliser le mot clé `const`{.language-} plutôt que `let`{.language-} pour déclarer des constantes, c'est à dire des variables qui ne bougent pas.

Ceci est très pratique pour éviter les erreurs.

#### Fonctions

{% lien "**Documentation**" %}
<https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Functions>
{% endlien %}

```html
<!DOCTYPE html>

<html>
<head>
<title>fonction et variables en javascript</title>
<meta charset="utf-8" />
</head>

<body>
<script>
  // définition classique d'une fonction
  function du_texte(texte) {
      console.log(texte)
  }
  du_texte("coucou")

  // la variable texte_plus_entête est associé à l'objet function
  texte_plus_entête = function(texte) {
      console.log("Et ben : " + texte)
  }
  //on peut l'exécuter
  texte_plus_entête("zut alors")

  // de plus en plus fort, sans le mot-clé fonction :
  texte_plus_entête = (texte) => {
      console.log("Et ben : " + texte)
  }

  // que l'on peut aussi écrire, s'il n'y a qu'une seule instruction :
  texte_plus_entête = (texte) => console.log("Et ben : " + texte);


  let compteur = 0 //les variables sont globales
  let entête_texte = "S'il vous plait ? "
  function entête_dans_variable(texte) {
      console.log(entête_texte + texte)
      compteur += 1 //on change la variable globale
      console.log(`cette fonction a été appelée ${compteur} fois.`)
  }

  entête_dans_variable("Bonjour ! ")
  entête_dans_variable("Au revoir.")
</script>
</body>
</html>

```

Le bout de code ci-dessus montre plusieurs spécificités de javascript :

- plusieurs façon de créer des fonctions :
  - normale (crée une fonction nommée `ma_fct`) : `function ma_fct(params) {code}`{.language-}
  - anonyme (rend un objet fonction) :`function (params) {code}`, que l'on pourrait aussi écrire `(params) => {code}`{.language-}
- les commentaires javascript s'écrivent en commençant par `//`{.language-}
- les portées des variables font que l'on peut modifier une variables dans une fonction
- la construction automatique de chaines. `cette fonction a été appelée ${compteur} fois.`{.language-} est équivalent à la concaténation classique : `"cette fonction a été appelée " + compteur + " fois."`{.language-}

{% note %}
Beaucoup de choses en web sont asynchrones : on envoie une requête au serveur et on exécute le résultat lorsque l'on obtient la réponse du serveur. De là, beaucoup de fonctions ne sont utilisées qu'une seule fois. C'est ce qui explique que l'on utilise abondamment de fonction anonymes.
{% endnote %}

### Structures de contrôles

#### Instructions conditionnelles

https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#les_instructions_conditionnelles

javascript utilise deux forme d'égalité :

- `==` : javascript va tenter de convertir les objets dans un même type avant de tester l'égalité. Par exemple `42 == "42"`{.language-} sera vrai.
- `===` : javascript ne fait aucune conversion avant de tester l'égalité. Par exemple `42 == "42"`{.language-} sera faux.

{% attention %}
Contrairement à python, javascript vous laisse faire la ligne suivante qui ne fait habituellement pas ce qu'on veut :

```js
x=0
console.log(x)
if (x=1) {console.log("ah ben vla aut' chose")}
console.log(x)
```

Rappelez vous que  `=` est une **affectation**.

{% endattention %}

#### Les 2 types de boucles for et while

{% lien "**Documentation**" %}
<https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Loops_and_iteration>
{% endlien %}

Différence avec python :

- do while
- Le for à l'ancienne
- for in et for on

### Fonctions anonymes

En paramètres de fonctions et utilisées une seule fois. Très utiles pour la gestion des événements (on le verra) et les itérateurs [exemple](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
