---
layout: page
title:  "Projet numérologie : partie 1 / niveau 3 / intégration html et js"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 1]({% link cours/web/projets/numerologie/partie-1-front/index.md %}) / [niveau 3]({% link cours/web/projets/numerologie/partie-1-front/niveau-3/index.md %}) / [html et css]({% link cours/web/projets/numerologie/partie-1-front/niveau-3/4-integration_html_js.md %})
{.chemin}

## business as usual

* [tâche 1 du niveau 1]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/4-integration_html_js.md %}#tache-1). Puis on commit avec le message "action clique bouton"
* [tâche 2 du niveau 1]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/4-integration_html_js.md %}#tache-2). Puis on commit avec le message "integration numerologie.js"
* [tâche 3 du niveau 1]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/4-integration_html_js.md %}#tache-2). Puis on commit avec le message "utilisation numerologie.js"

Regardez à chaque fois ce qui est commité.

## un rebase qui se passe mal

Histoire de ne pas vous quitter sur l'impression (fausse) que le développement à plusieurs sur un même projet peut se faire n'importe comment, on va vous montrer une fusion qui ne se passe pas automatiquement.

> Pour éviter les multiples fusions manuelles, on a l'habitude de faire en sorte que chaque tâche ne s'occupe pas de la même partie code. Mais il sera toujours nécessaire de fusionner à la main de temps en temps. Ne soyez donc pas pris au dépourvu quand ça arrivera.

### modification côté github

Sur github (*menu Repository > View on github*), modifiez le code de *"numerologie.js"* pour mettre les tests juste en dessous de chaque déclaration de fonction :

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

Et on commit avec le message "ajoute séparateur de tests"

### fusion

L'application desktop nous dit qu'on est à 4/1 : nous à +4 et le serveur à +1 depuis la dernière synchronisation.

Tentons le pull... Et c'est le drame :

![problème de rebase]({{ "/assets/cours/web/numerologie/partie-1-niveau-3-projet-rebase-soucis.png" | relative_url }}){:style="margin: auto;display: block}

Git vous laisse dans un état entre-deux : vous n'avez pas récupéré les données du serveur et git ne vous laissera rien faire avant que ce soit fait : donc avant que vous ayez réglé les soucis de fusion.

Il y a 1 conflit, git n'a pas réussi à fusionner le fichier tout seul. Si vous ouvrez *"numerologie.js"* dans vscode, vous verrez le soucis :

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
console.log('----------------')
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
>>>>>>> 889641d (ajoute séparateur de tests)

```

L'unique conflit est à la fin entre `<<<<<<<<` et `>>>>>>>>` :

```javascript
<<<<<<< HEAD
// fin de test de chiffreAssocie(chaine)
=======

console.log('----------------')
// fin de test de chiffreAssocie(chaine)
>>>>>>> 889641d (ajoute séparateur de tests)
```

 Chaque conflit est composé de la même manière :

* entre `<<<<<<<` et `========` une possibilité,
* entre `========` et `>>>>>>>`, l'autre possibilité.

Il faut que l'on choisisse une des possibilité en supprimant l'autre. Ici on veut choisir la seconde possibilité, on supprime donc la première et les `<<<<` et `>>>>` :

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
console.log('----------------')
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

vscode nous aide est on peut choisir une possibilité, il supprimera la seconde tout seul.

On peut maintenant sauver le fichier. et l'application desktop est contente puisque l'on a supprimer les conflit (on en avait qu'un seul) :

![fin du problème de rebase]({{ "/assets/cours/web/numerologie/partie-1-niveau-3-projet-rebase-soucis-fini.png" | relative_url }}){:style="margin: auto;display: block}

On peut finir le rebase. Nous sommes maintenant uniquement en avance de 4 commits sur le serveur, dont l'état actuel est cohérent avec ce que l'on sait (auparavent il avait divergé d'un commit). On *push origin*.

> malgré toutes nos modifications, nous n'avions qu'un seul conflit. L'algorithme de rebase de git est donc assez performant.

## pour aller plus loin

On utilise souvent git en ligne de commande. Vous pouvez poursuivre en lisant plus avant le [cours sur git]({% link cours/git_et_github/index.md %}) qui vous donnera les bases de ce merveilleux outils.
