---
layout: page
title:  "Projet numérologie : niveau 1 - cours 1/code js"
category: cours
author: "François Brucker"
---


> TBD : en chantier
{: .note}


## structure du projet

### dossiers

* dossier : *"numerologie-niveau-1"* :
    * fichier : *"mes_tests.js"*
    * dossier : *"user stories"*
      * fichier : *"connaitre-son-numero.md"*
      * fichier : *"todo.md"*

### todos

Il faut tout faire :

- [ ] associer un chiffre à un nom
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter



## choix de la première tâche

> Quelle est la tâche la plus simple à réaliser dans notre todo ?

Le cœur du projet est d'associer un numéro à un nom, donc autant essayer de faire ça en javascript.

> On modifie le fichier todo/md pour refléter le fait qu'on travaille sur cet item : 
{: .note}

- [X] associer un chiffre à un nom
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter

Bon c'est pas encore très détaillé. Comment faire ça ? 

1. déjà un nom c'est une chaine de caractère codée en utf-8
2. on peut prendre le numéro unicode/utf8 de chaque caractère et les sommer
3. il faut un chiffre donc comment passer d'un nombre à un chiffre ?
4. on peut sommer les chiffre du nombre pour obtenir un autre nombre strictement plus petit ($10.x + y < x + y$) et recommencer la procédure si ce n'est pas un chiffre.


Ajoutons nos réflexions à la todo list (fichier *"todo.md"*) :

```markdown
- [X] associer un chiffre à un nom
    - [ ] numéro unicode/utf8 d'un caractère
    - [ ] sommer des numéro des caractères d'une chaine de caractères
    - [ ] sommer les chiffre d'un nombre
    - [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter
```

> Au passage, vous avez vu comment on a mis des maths dans du markdown ? Lorsque vous transformerez le markdown en html, [Mathjax](https://www.mathjax.org/) rendra ces équations toutes jolies.

> Quel est l'item le plus simple à résoudre ?
{: .note}

A mon avis c'est lui :

- [X] associer un chiffre à un nom
    - [X] numéro unicode/utf8 d'un caractère
    - [ ] sommer des numéro des caractères d'une chaine de caractères
    - [ ] sommer les chiffre d'un nombre
    - [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter

> On va aller plus vite dans ce cours ensuite. Mais lidée est tojours la suivante :
> dans votre todolist vous devez avoir un item qui vous semble *facile* à résoudre.
> Si ce n'est pas le cas, c'est que vous items sont trop gros et qu'il faut les décomposer en unité plus fine.

### tests js

On va commencer par faire des petits tests en js pour voir comment on peut résoudre notre tâche (trouver les bonnes méthodes à utiliser), puis un codera la fonction proprement dite.

On peut faire les tests dans un interpréteur node s'ils sont tout petit (on peut utiliser le node dans un terminal vscode par exemple), ou bien exécuter un programme de test. 

On va préférer la première option ici car il nous faut juste découvrir la méthode [`charCodeAt`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt) :
```javascript
fbrucker@emma cours/numerologie-niveau-1 » node             
Welcome to Node.js v16.9.0.
Type ".help" for more information.
> ('coucou').charCodeAt(1)
111
> ('你好').charCodeAt(0)
20320
```

> 'o' c'est de l'ascii et a donc gardé un petit nombre, '你' c'est un [sinogramme](https://unicode-table.com/fr/4F60/) de numéro unicode U+4F60 ce qui en décimal vaut `parseInt("4F60", 16)`
(qui est l'inverse de `(20320).toString(16)`, testez-le...)

> que vaut le code unicode de `꧁` ?
{: .note}


### code js

Fort de nos expérimentations, on peut maintenant écrire un fichier *"numerologie.js"* qui va rendre la somme de tos les code unicode de ses caractères le constituant.

> Je jette ici un voile pudique sur ce qu'est un "caractère" dans une chaine unicode. Cela peut vite être [très compliqué](https://fr.wikipedia.org/wiki/%C3%89quivalence_Unicode). 

Fichier *"numerologie-niveau-1/numerologie.js"* :

```javascript
function nombre(chaine) {
    var somme = 0
    for (var i=0; i < chaine.length; i++) {
        somme += chaine.charCodeAt(i)
    }
    return somme
}
```

### updade todo

Note todo devient : 

- [X] associer un chiffre à un nom
    - [X] ~~numéro unicode/utf8 d'un caractère~~
    - [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
    - [ ] sommer les chiffre d'un nombre
    - [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter


On a bien progressé.

## fin du code js

La tâche qui semble la plus simple maintenant est de finaliser la partie consacrée à l'association d'un chiffre à un nom.

Je choisis de faire : 

- [X] associer un chiffre à un nom
    - [X] ~~numéro unicode/utf8 d'un caractère~~
    - [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
    - [X] sommer les chiffre d'un nombre
    - [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter

### sommer les chiffres d'un nombre

On pourrait se la jouer matheuse et diviser le nombre par 10 autant de fois que nécessaire et en prenant les parties entières, mais faisons plutôt de la magie en jouant avec les conversions :

```javascript
function somme(nombre) {
    var somme = 0
    chaine = String(nombre)
    for (var i=0; i < chaine.length ; i++) {
        somme += parseInt(chaine.charAt(i))
    }
    return somme
}
```

> Comment marche ce code ?
{: .note}

Pour l'instant, on va tester ce code *à la sauvage*, c'est à dire en ajoutant du code à la fin de *"numerologie.js"* et en affichant le résultat à l'écran grâce à la fonction [`console.log`](https://nodejs.org/api/console.html#console_console_log_data_args).  

On peut alors ajouter le code suivant (qu'on enlèvera ensuite...) dans *"numerologie.js"* :

```javascript
// test de la fonction
console.log(somme("132"))

// avec un chiffre : charAt != charCodeAt
console.log(somme("4"))
console.log("4".charCodeAt(0))
console.log("4".charAt(0))

// conversion chaine de caracteres et nombre
console.log(typeof "4".charAt(0))
console.log(parseInt("4".charAt(0)))
console.log(typeof parseInt("4".charAt(0)))
```

> Les commentaires en javascript se font en mettant des `//` : le reste la ligne n'est pas évaluée.
>  C'est tellement pratique qu'il y a des raccourcis pour cela en vscode : *menu édition > comment line comment*.
> Pour trouver ce raccourci, je suis allé dans la palette de commande et j'ai tapé *comment* pour voir mes possibilités.

> Ce n'est **pas** de bonnes pratiques. Il faut dissocier le code des tests physiquement (dans des fichiers séparés) pour ne pas faire de bêtises en supprimant du code alors qu'on voulait supprimer des tests ou en oubliant de supprimer des tests lors de l'utilisation du code.
> On verra plus loin comment faire *un peu* mieux et dans les niveaux suivant comment faire bien.
{: .attention}



### test du code

Nous n'allons pas encore utiliser des bibliothèques dédiées aux tests (c'est le boulot des niveaux suivants), mais nous allons faire en sorte de pouvoir effectuer des tests de code :

* sans modifier le code,
* sans avoir à supprimer les tests ensuite.



On va procéder comme si l'on importait du javascript dans une page web : on va lire le fichier de code sous la forme d'une longue chaine de caractère et l'évaluer dans l'interpréteur. On pourra ensuite utiliser les fonctions comme si on venait de les taper. 

> On ne peut pas utiliser d'import classique de fichier ici, car il faut que le fichier de code soit dans un format spécial, ce qui n'est pas le cas ici.


#### lecture d'un fichier texte

La lecture de fichiers se fait de façon aisé avec node en utilisant la bibliothèque [`fs`](https://nodejs.org/api/fs.html#fs_file_system). On va utiliser : [`fs.readFileSync()`](https://nodejs.org/api/fs.html#fs_fs_readfilesync_path_options).

> La plupart des méthodes et fonctions de node sont asynchrones, c'est à dire que l'on attend pas que la méthode soit fini pour continuer l'exécution de notre code. Nous n'allons pas faire ça ici car ça complique (même si c'est mieux) le fonctionnement.

Testons ça dans un node : 
```javascript
> contenu_du_fichier = fs.readFileSync("./numerologie.js")
<Buffer 66 75 6e 63 74 69 6f 6e 20 6e 6f 6d 62 72 65 28 63 68 61 69 6e 65 29 20 7b 0a 20 20 20 20 76 61 72 20 73 6f 6d 6d 65 20 3d 20 30 0a 20 20 20 20 66 6f ... 635 more bytes>
>
```

Bon ben c'est pas ce qu'on voulait. C'est raté comme un fichier binaire par défaut... On recommence en précisant qu'on veut du texte : 

```javascript
> contenu_du_fichier = fs.readFileSync("./numerologie.js", {encoding:'utf8'})
'function nombre(chaine) {\n' +
  '    var somme = 0\n' +
  '    for (var i=0; i < chaine.length; i++) {\n' +
  '        somme += sommeFinale(chaine.charCodeAt(i))\n' +
  '    }\n' +
  '    return somme\n' +
  '}\n' +
  '\n' +
  'function somme(nombre) {\n' +
  '    var somme = 0\n' +
  '    chaine = String(nombre)\n' +
  '    for (var i=0; i < chaine.length ; i++) {\n' +
  '        somme += parseInt(chaine.charAt(i))\n' +
  '    }\n' +
  '    return somme\n' +
  '}\n' +
  '\n' +
  '// test de la fonction\n' +
  'console.log(somme("132"))\n' +
  '\n' +
  '// avec un chiffre : charAt != charCodeAt\n' +
  'console.log(somme("4"))\n' +
  'console.log("4".charCodeAt(0))\n' +
  'console.log("4".charAt(0))\n' +
  '\n' +
  '// conversion chaine de caracteres et nombre\n' +
  'console.log(typeof "4".charAt(0))\n' +
  'console.log(parseInt("4".charAt(0)))\n' +
  'console.log(typeof parseInt("4".charAt(0)))'
> 
```


> C'est une pratique courante en javascript de déclarer tous les paramètres en 1 fois, avec un [objet](https://developer.mozilla.org/fr/docs/Learn/JavaScript/Objects/Basics) (qui ressemble furieusement à un dictionnaire si vous venez de python). 

#### évaluation d'un fichier

> commentez nos précédent tests pour qu'ils ne soient pas évalués.
{: .note}

Puis on peut utiliser [eval](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/eval) : 

Dans un nouveau node :
```javascript
> contenu_du_fichier = fs.readFileSync("./numerologie.js", {encoding:'utf8'})
'function nombre(chaine) {\n' +
  '    var somme = 0\n' +
  '    for (var i=0; i < chaine.length; i++) {\n' +
  '        somme += sommeFinale(chaine.charCodeAt(i))\n' +
  '    }\n' +
  '    return somme\n' +
  '}\n' +
  '\n' +
  'function somme(nombre) {\n' +
  '    var somme = 0\n' +
  '    chaine = String(nombre)\n' +
  '    for (var i=0; i < chaine.length ; i++) {\n' +
  '        somme += parseInt(chaine.charAt(i))\n' +
  '    }\n' +
  '    return somme\n' +
  '}\n' +
  '\n' +
  '// // test de la fonction\n' +
  '// console.log(somme("132"))\n' +
  '\n' +
  '// // avec un chiffre : charAt != charCodeAt\n' +
  '// console.log(somme("4"))\n' +
  '// console.log("4".charCodeAt(0))\n' +
  '// console.log("4".charAt(0))\n' +
  '\n' +
  '// // conversion chaine de caracteres et nombre\n' +
  '// console.log(typeof "4".charAt(0))\n' +
  '// console.log(parseInt("4".charAt(0)))\n' +
  '// console.log(typeof parseInt("4".charAt(0)))'
> eval(contenu_du_fichier)
undefined
> somme("123")
6
> 
```

#### un fichier de test

On va déporter les tests du fichier de code à un fichier de test :

* créez un nouveau dossier *"numerologie-niveau-1/tests/*
* créez un fichier *"numerologie-niveau-/tests/tests_numerologie.js* où l'on pourra recopier nos tests.

fichier *"numerologie-niveau-1/tests/tests_numerologie.js* : 
```javascript
fs = require('fs')

eval(fs.readFileSync("../numerologie.js", {encoding:'utf8'}))

// test de la fonction
console.log(somme("132"))

// avec un chiffre : charAt != charCodeAt
console.log(somme("4"))
console.log("4".charCodeAt(0))
console.log("4".charAt(0))

// conversion chaine de caracteres et nombre
console.log(typeof "4".charAt(0))
console.log(parseInt("4".charAt(0)))
console.log(typeof parseInt("4".charAt(0)))
```

Plusieurs remarques :

* on a été obligé d'importer la bibliothèque `fs`. Dans un interpréteur node elle est importée par défaut, pas lorsque l'on exécute le fichier. Retenez d'un import node que l'on utilise [`require`](https://nodejs.org/en/knowledge/getting-started/what-is-require/) et que l'**on importe quelque chose** : le résultat de l'import doit être placé dans une variable
* on importe depuis un fichier dans le dossier *"tests"*. Le fichier *"numerologie.js"* étant dans le dossier parent, on utilise la [notation *"../*"]({% post_url tutos/systeme/2021-08-24-fichiers-navigation %}#block-.-..).
* on a combiné la lecture et l'eval en une seule ligne.

### somme itérative

- [X] associer un chiffre à un nom
    - [X] ~~numéro unicode/utf8 d'un caractère~~
    - [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
    - [X] ~~sommer les chiffre d'un nombre~~
    - [X] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter

On a juste à itérer les somme jusqu'à ce que sa valeur soit $< 10$.

fichier *"numerologie-niveau-1/numerologie.js"*, on ajoute la fonction `chiffreAssocie` :
```javascript
// ...

function chiffreAssocie(chaine) {
    valeur = nombre(chaine)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}
```

Et dans nos tests *"numerologie-niveau-1/tests/tests_numerologie.js* : 
```javascript
//test valeur 
console.log(nombre("coucou"))
console.log(chiffreAssocie("coucou"))
```


## la suite

- [X] associer un chiffre à un nom
    - [X] ~~numéro unicode/utf8 d'un caractère~~
    - [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
    - [X] ~~sommer les chiffre d'un nombre~~
    - [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter



On va maintenant s'occuper de la partie html dans la [partie suivante]({% link cours/web/projets/numerologie/niveau-1/cours-1-front/front_html_css.md %})