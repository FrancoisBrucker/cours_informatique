---
layout: page
title:  "Projet numérologie : partie 1 / niveau 1 / intégration html et js"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 1]({% link cours/web/projets/numerologie/partie-1-front/index.md %}) / [niveau 4]({% link cours/web/projets/numerologie/partie-1-front/niveau-4/index.md %}) / [html et css]({% link cours/web/projets/numerologie/partie-1-front/niveau-4/4-integration_html_js.md %})
{: .chemin}

## business as usual

* [tâche 1 du niveau 1]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/4-integration_html_js.md %}#tache-1). Puis on commit : `git commit -am"action clique bouton"`
* [tâche 2 du niveau 1]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/4-integration_html_js.md %}#tache-2). Puis on commit : `git commit -am"integration numerologie.js"`.
* [tâche 3 du niveau 1]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/4-integration_html_js.md %}#tache-2). Puis on commit : `git commit -am"utilisation numerologie.js"`

On fini pas pousser le tout sur le serveur : `git push`

On a (presque) terminé cette partie de projet.

## un rebase qui se passe mal

Histoire de ne pas vous quitter sur l'impression (fausse) que le développement à plusieurs sur un même projet peut se faire n'importe comment, on va vous montrer une fusion qui ne se passe pas automatiquement.

> Pour éviter les multiples fusions manuelles, on a l'habitude de faire en sorte que chaque tâche ne s'occupe pas de la même partie code. Mais il sera toujours nécessaire de fusionner à la main de temps en temps. Ne soyez donc pas pris au dépourvu quand ça arrivera.

### modification côté github

Sur github, dans la page de prijet, modifiez le code de *"numerologie.js"* pour mettre les tests juste en dessous de chaque déclaration de fonction :

```javascript
function nombre(chaine) {
    var somme = 0
    for (var i=0; i < chaine.length; i++) {
        somme += chaine.charCodeAt(i)
    }
    return somme
}

// test de nombre(chaine)

// est-ce 2x plus ?
console.log(nombre("cou"))
console.log(nombre("coucou"))

// chaque caractère :la somme est-elle correcte ?
for (c of "cou") { 
    console.log(c + " : " + nombre(c))
}
// fin de test de nombre(chaine)

function somme(nombre) {
    var somme = 0
    chaine = String(nombre)
    for (var i=0; i < chaine.length ; i++) {
        somme += parseInt(chaine.charAt(i))
    }
    return somme
}

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

function chiffreAssocie(chaine) {
    valeur = nombre(chaine)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}

// test de chiffreAssocie(chaine)

//test valeur somme des chiffres
console.log(nombre("coucou"))
console.log(chiffreAssocie("coucou"))
// fin de test de chiffreAssocie(chaine)
```

Puis commitez vos changements (en cliquant sur le bouton vert).

### modification sur l'ordinateur

Dans le projet local, pour le même fichier *"numérologie"*, on garde les tests en fin de fonction, et on ajoute des séparateur entre chaque test :

```javascript
function nombre(chaine) {
    var somme = 0
    for (var i=0; i < chaine.length; i++) {
        somme += chaine.charCodeAt(i)
    }
    return somme
}

function somme(nombre) {
    var somme = 0
    chaine = String(nombre)
    for (var i=0; i < chaine.length ; i++) {
        somme += parseInt(chaine.charAt(i))
    }
    return somme
}

function chiffreAssocie(chaine) {
    valeur = nombre(chaine)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}

// test de nombre(chaine)

// est-ce 2x plus ?
console.log(nombre("cou"))
console.log(nombre("coucou"))

// chaque caractère :la somme est-elle correcte ?
for (c of "cou") { 
    console.log(c + " : " + nombre(c))
}
console.log('----------------')
// fin de test de nombre(chaine)


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

console.log('----------------')
// fin de test de somme(nombre)

// test de chiffreAssocie(chaine)

//test valeur somme des chiffres
console.log(nombre("coucou"))
console.log(chiffreAssocie("coucou"))

console.log('----------------')
// fin de test de chiffreAssocie(chaine)
```

Et on commit : `git commit -am"ajoute séparateur de tests"`

### fusion

On fait un `git fetch` pur retrouver l'état du serveur, puis un `git status`qui nous donne :

```text
Sur la branche main
Votre branche et 'origin/main' ont divergé,
et ont 1 et 1 commits différents chacune respectivement.
  (utilisez "git pull" pour fusionner la branche distante dans la vôtre)

rien à valider, la copie de travail est propre
```

Tentons le pull (`git pull`) pour synchroniser nos branches comme tout à l'heure... Et c'est le drame :

```text
Fusion automatique de numerologie.js
CONFLIT (contenu) : Conflit de fusion dans numerologie.js
error: impossible d'appliquer 9b0e873... ajoute séparateur de tests
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
Impossible d'appliquer 9b0e873... ajoute séparateur de tests
```

Git vous laisse dans un état entre-deux : vous n'avez pas récupéré les données du serveur et git ne vous laissera rien faire avant que ce soit fait : donc avant que vous ayez réglé les soucis de fusion.

Un git status nous indique que c'est *"numérologie.js"* le problème (dans un cas réel vous pouvez avoir plusieurs fichiers impacté, il faudra alors les corriger un à un).

*"numérologie.js"* ressemble à ca dans le vscode :

```javascript
function nombre(chaine) {
    var somme = 0
    for (var i=0; i < chaine.length; i++) {
        somme += chaine.charCodeAt(i)
    }
    return somme
}

<<<<<<< HEAD
=======
function somme(nombre) {
    var somme = 0
    chaine = String(nombre)
    for (var i=0; i < chaine.length ; i++) {
        somme += parseInt(chaine.charAt(i))
    }
    return somme
}

function chiffreAssocie(chaine) {
    valeur = nombre(chaine)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}

>>>>>>> 9b0e873 (ajoute séparateur de tests)
// test de nombre(chaine)

// est-ce 2x plus ?
console.log(nombre("cou"))
console.log(nombre("coucou"))

// chaque caractère :la somme est-elle correcte ?
for (c of "cou") { 
    console.log(c + " : " + nombre(c))
}
console.log('----------------')
// fin de test de nombre(chaine)

<<<<<<< HEAD
function somme(nombre) {
    var somme = 0
    chaine = String(nombre)
    for (var i=0; i < chaine.length ; i++) {
        somme += parseInt(chaine.charAt(i))
    }
    return somme
}
=======
>>>>>>> 9b0e873 (ajoute séparateur de tests)

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

console.log('----------------')
// fin de test de somme(nombre)

function chiffreAssocie(chaine) {
    valeur = nombre(chaine)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}

// test de chiffreAssocie(chaine)

//test valeur somme des chiffres
console.log(nombre("coucou"))
console.log(chiffreAssocie("coucou"))
<<<<<<< HEAD
// fin de test de chiffreAssocie(chaine)
=======

console.log('----------------')
// fin de test de chiffreAssocie(chaine)
>>>>>>> 9b0e873 (ajoute séparateur de tests)

```

 Chaque conflit est composé de la même manière :

* entre `<<<<<<<` et `========` une possibilité,
* entre `========` et `>>>>>>>`, l'autre possibilité.

Il faut que l'on choisisse une des possibilité en supprimant l'autre.

Notre fichier a trois conflits :

```javascript
<<<<<<< HEAD
=======
function somme(nombre) {
    var somme = 0
    chaine = String(nombre)
    for (var i=0; i < chaine.length ; i++) {
        somme += parseInt(chaine.charAt(i))
    }
    return somme
}

function chiffreAssocie(chaine) {
    valeur = nombre(chaine)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}

>>>>>>> 9b0e873 (ajoute séparateur de tests)
```

où on a ajouté du code dans le commit du serveur (Incoming change) par rapport à ce qu'on a en local (Current Change).

et

```javascript
<<<<<<< HEAD
function somme(nombre) {
    var somme = 0
    chaine = String(nombre)
    for (var i=0; i < chaine.length ; i++) {
        somme += parseInt(chaine.charAt(i))
    }
    return somme
}
=======
>>>>>>> 9b0e873 (ajoute séparateur de tests)
```

Où l'on retouve la fonction somme en local alors qu'elle n'est plus à cet endroit côté serveur

et

```javascript
<<<<<<< HEAD
// fin de test de chiffreAssocie(chaine)
=======

console.log('----------------')
// fin de test de chiffreAssocie(chaine)
>>>>>>> 9b0e873 (ajoute séparateur de tests)
```

où on a une ligne de plus dans le commit du serveur (*Incoming change*) par rapport à ce 
qu'on a en local (*Current Change*).

Nous allons ici toujours choisir la même version, ici celle du serveur, (dans des cas réels, on peut avoir à réfléchir pour remettre d'aplomb un fichier modifié par de nombreuses personnes). On supprime donc la première possibilité et les `<<<<` et `>>>>` :

On obtient au final le code :

```javascript
function nombre(chaine) {
    var somme = 0
    for (var i=0; i < chaine.length; i++) {
        somme += chaine.charCodeAt(i)
    }
    return somme
}

function somme(nombre) {
    var somme = 0
    chaine = String(nombre)
    for (var i=0; i < chaine.length ; i++) {
        somme += parseInt(chaine.charAt(i))
    }
    return somme
}

function chiffreAssocie(chaine) {
    valeur = nombre(chaine)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}

// test de nombre(chaine)

// est-ce 2x plus ?
console.log(nombre("cou"))
console.log(nombre("coucou"))

// chaque caractère :la somme est-elle correcte ?
for (c of "cou") { 
    console.log(c + " : " + nombre(c))
}
console.log('----------------')
// fin de test de nombre(chaine)


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

console.log('----------------')
// fin de test de somme(nombre)

function chiffreAssocie(chaine) {
    valeur = nombre(chaine)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}

// test de chiffreAssocie(chaine)

//test valeur somme des chiffres
console.log(nombre("coucou"))
console.log(chiffreAssocie("coucou"))

console.log('----------------')
// fin de test de chiffreAssocie(chaine)
```

Où il n'y a plus de conflits : on peut commit : `git commit -am"rebase"`.

Un `git status` nous informe qu'on peut continuer le rebase avec la commande : `git rebase --continue`. Un dernier `git status` nous indique que c'est ok. On peut maintenant push sur le serveur : `git push` pour synchroniser le serveur avec notre nouvelle version.

 > Félicitations, vous venez de survire à votre premier rebase qui se passe mal.
