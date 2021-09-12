---
layout: page
title:  "Projet numérologie : niveau 2/partie 1/code js"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %})/[niveau 2]({% link cours/web/projets/numerologie/niveau-2/index.md %})/[partie 1]({% link cours/web/projets/numerologie/niveau-2/partie-1-front/index.md %})/[code js]({% link cours/web/projets/numerologie/niveau-2/partie-1-front/2-code_js.md %})
{: .chemin}

Code de la *logique métier* du projet. L'idée est de montrer comment on peut progresser en codant nous même, un item en amenant un autre à coder.

## todos initiaux

Il faut tout faire :

* [ ] associer un chiffre à un nom
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

## choix de la première tâche

> Quelle est la tâche la plus simple à réaliser dans nos todos ?
{: .note}

Le cœur du projet est d'associer un numéro à un nom, donc autant essayer de faire ça en javascript.

> On modifie le fichier *"numerologie/todo/todos.md"* pour refléter le fait qu'on travaille sur cet item :
{: .note}

* [X] associer un chiffre à un nom
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

Bon c'est pas encore très détaillé. Comment faire ça ?

1. déjà un nom c'est une chaine de caractère codée en utf-8
2. on peut prendre le numéro unicode/utf8 de chaque caractère et les sommer
3. il faut un chiffre donc comment passer d'un nombre à un chiffre ?
4. on peut sommer les chiffre du nombre pour obtenir un autre nombre strictement plus petit ($10.x + y < x + y$) et recommencer la procédure si ce n'est pas un chiffre.

Ajoutons nos réflexions à la todo list (fichier *"numerologie/todo/todos.md"*) :

```markdown
* [X] associer un chiffre à un nom
  * [ ] numéro unicode/utf8 d'un caractère
  * [ ] sommer des numéro des caractères d'une chaine de caractères
  * [ ] sommer les chiffre d'un nombre
  * [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter
```

> Au passage, vous avez vu comment on a mis des maths dans du markdown ? Lorsque vous transformerez le markdown en html, [Mathjax](https://www.mathjax.org/) rendra ces équations toutes jolies.

Quel est l'item le plus simple à résoudre ? A mon avis c'est lui :

* [X] associer un chiffre à un nom
  * [X] numéro unicode/utf8 d'un caractère
  * [ ] sommer des numéro des caractères d'une chaine de caractères
  * [ ] sommer les chiffre d'un nombre
  * [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

On va aller plus vite dans ce cours ensuite. Mais l(idée est toujours la suivante : dans votre listes de todos vous devez avoir un item qui vous semble le plus *facile* à résoudre. Si ce n'est pas le cas, c'est que vous items sont trop gros et qu'il faut les décomposer en unité plus fine.

> Que signifie *le plus facile à résoudre* ? C'est un item dont l'implémentation ne nécessite qu'une seule chose à faire, et que cette chose à faire est simple.

## Tache 1 : unicode d'un caractère

On utilise l'[implémentation du niveau 1]({% link cours/web/projets/numerologie/niveau-1/partie-1-front/2-code_js.md %}#tache-1) pour associer un nombre à un caractère unicode.

## Tache 2 : caractères et nombre

Ce qui nous permet de passer à l'item suivant :

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] sommer des numéro des caractères d'une chaine de caractères
  * [ ] sommer les chiffre d'un nombre
  * [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

Qu'on [implémente comme au niveau 1]({% link cours/web/projets/numerologie/niveau-1/partie-1-front/2-code_js.md %}#tache-2). Nos todos deviennent :

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [ ] sommer les chiffre d'un nombre
  * [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

On a bien progressé. La tâche qui semble la plus simple maintenant est de finaliser la partie consacrée à l'association d'un chiffre à un nom.

## Tache 3 : chiffres et nombre

Je choisis de faire :

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] sommer les chiffre d'un nombre
  * [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

Encore une fois on utilise l'[implémentation de niveau 1]({% link cours/web/projets/numerologie/niveau-1/partie-1-front/2-code_js.md %}#tache-3). Nous allons cependant modifier la façon dont on teste nos méthodes.

## test du code

La gestion des tests du niveau 1 n'est pas satisfaisante car elle mélange code et tests. Nous n'allons pas encore utiliser des bibliothèques dédiées aux tests (c'est le boulot des niveaux suivants), mais nous allons faire en sorte de pouvoir effectuer des tests :

* sans modifier le code,
* sans avoir à supprimer/commenter les tests ensuite.

Ceci nous permettra déjà de pouvoir ajouter ds tests sans y réfléchir de façon fluide et sans modifier le code. Ce qui sera utile lorsque le code sera déjà en production (ce qui est le but de tout code) ou si nous sommes plusieurs à coder sur le même projet (ce qui est la norme).

### méthode

On va procéder comme si l'on importait du javascript dans une page web : on va lire le fichier de code sous la forme d'une longue chaine de caractère et l'évaluer dans l'interpréteur. On pourra ensuite utiliser les fonctions comme si on venait de les taper.

> On ne peut pas utiliser d'import classique de fichiers ici, car il faut que le fichier de code soit dans un format spécial, ce qui n'est pas le cas ici.

#### lecture d'un fichier texte

La lecture de fichiers se fait de façon aisé avec node en utilisant la bibliothèque [`fs`](https://nodejs.org/api/fs.html#fs_file_system). On va utiliser : [`fs.readFileSync()`](https://nodejs.org/api/fs.html#fs_fs_readfilesync_path_options).

> La plupart des méthodes et fonctions de node sont asynchrones, c'est à dire que l'on attend pas que la méthode soit fini pour continuer l'exécution de notre code. Nous n'allons pas faire ça ici car ça complique (même si c'est mieux) le fonctionnement.

Testons ça dans un node :

```javascript
> contenu_du_fichier = fs.readFileSync("./numerologie.js")
<Buffer 6e 6f 6d 20 3d 20 22 6d 6f 6e 64 65 22 0a 0a 63 6f 6e 73 6f 6c 65 2e 6c 6f 67 28 22 62 6f 6e 6a 6f 75 72 20 22 20 2b 20 6e 6f 6d 20 2b 20 22 20 21 22 ... 1 more byte>
>
```

Bon ben c'est pas ce qu'on voulait. Un fichier est évalué comme un [fichier binaire](https://fr.wikipedia.org/wiki/Fichier_binaire) par défaut... On recommence en précisant qu'on veut du texte :

```javascript
> contenu_du_fichier = fs.readFileSync("./numerologie.js", {encoding:'utf8'})
[... snip ...]
>
```

> à la place de `[... snip ...]` vous devriez voir le contenu de votre fichier.

C'est une pratique courante en javascript de déclarer tous les paramètres en 1 fois, ici l'encodage du fichier, avec un [objet](https://developer.mozilla.org/fr/docs/Learn/JavaScript/Objects/Basics) (qui ressemble furieusement à un dictionnaire si vous venez de python).

> Il n'y a pas de différence fondamentale entre fichier binaire et texte, ce n'est que l'interprétation qui change. Dans un cas, les bits sont des nombres, de l'autre on associe ces nombres au caractères utf-8.

#### évaluation d'un fichier

> commentez nos précédents tests pour qu'ils ne soient pas évalués.
{: .note}

Puis on peut utiliser [eval](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/eval) :

Dans un nouveau node :

```javascript
> contenu_du_fichier = fs.readFileSync("./numerologie.js", {encoding:'utf8'})
[... snip ...]
> eval(contenu_du_fichier)
undefined
> somme("123")
6
> 
```

### un fichier de test

On va déporter les tests du fichier de code à un fichier de test :

* créez un nouveau dossier *"numerologie/tests/"*
* créez un fichier *"numerologie/tests/tests_numerologie.js"* où l'on pourra recopier nos tests.

Le fichier *"numerologie/tests/tests_numerologie.js"* :

```javascript
fs = require('fs')

eval(fs.readFileSync("../numerologie.js", {encoding:'utf8'}))

// test de somme(nombre)
console.log(somme(132))

// avec un chiffre : charAt != charCodeAt
console.log(somme(4))
console.log("4".charCodeAt(0))
console.log("4".charAt(0))

// conversion chaine de caracteres et nombre
console.log(typeof "4".charAt(0))
console.log(parseInt("4".charAt(0)))
console.log(typeof parseInt("4".charAt(0)))
// fin de test de somme(nombre)
```

On peut maintenant supprimer vos tests de *"numerologie/numerologie.js*. On pourra exécuter nos tests facilement dans terminal en se plaçant dans le dossier *"numerologie/tests"* puis en exécutant la commande : `node tess_numerologie.js`.

Plusieurs remarques :

* on a été obligé d'importer la bibliothèque `fs`. Dans un interpréteur node elle est importée par défaut, pas lorsque l'on exécute le fichier. Retenez d'un import node que l'on utilise [`require`](https://nodejs.org/en/knowledge/getting-started/what-is-require/) et que l'**on importe quelque chose** : le résultat de l'import doit être placé dans une variable
* on importe depuis un fichier dans le dossier *"tests"*. Le fichier *"numerologie/numerologie.js"* étant dans le dossier parent, on utilise la [notation *"../*"]({% post_url tutos/systeme/2021-08-24-fichiers-navigation %}#block-.-..).
* on a combiné la lecture et l'eval en une seule ligne.

## Tache 4 : somme itérative

On peut terminer cette partie en faisant l'item :

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

On procède [comme au niveau 1]({% link cours/web/projets/numerologie/niveau-1/partie-1-front/2-code_js.md %}#tache-4), en ajoutant les tests à notre tout nouveau fichier *"numerologie/tests/tests_numerologie.js"*.

## todos finaux

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

La partie javascript semble terminée pour l'instant. On peut s'attaquer à ce qui semble le plus simple, la page web.