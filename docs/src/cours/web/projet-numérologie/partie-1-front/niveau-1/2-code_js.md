---
layout: layout/post.njk
title: "Projet numérologie / partie 1 : front / niveau 1 / code javascript"

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Projet numérologie / partie 1 : front / niveau 1 / code javascript"
  parent: "Projet numérologie / partie 1 : front / niveau 1"
---

<!-- début résumé -->

Code de la *logique métier* du projet.

<!-- fin résumé -->

## <span id="tache-1"></span> Tâche 1 : Unicode d'un caractère

Chaque caractère est associé à un nombre (les ordinateurs ne comprennent que les entiers). Le codage de caractère utilisé est [Unicode](https://fr.wikipedia.org/wiki/Unicode). Il est fait pour pouvoir écrire toutes les langues du monde.

{% info %}
L'[ensemble des caractères Unicode](https://unicode-table.com/fr/)
{% endinfo %}

Comme cela fait beaucoup de caractères, on utilise des encodages à tailles variables pour que le moindre bout de texte ne fasse des mégaoctets. Le standard est l'encodage [utf-8](https://fr.wikipedia.org/wiki/UTF-8) (on peut aussi le noter "utf8") : tous vos textes doivent être encodés en utf-8 (sinon c'est *bad karma*).

{% note %}
Ne confondez pas utf8 et Unicode. Même s'ils sont liés ce n'est pas la même chose. En particulier il existe d'autres façon d'encoder l’Unicode comme l'[utf-16](https://fr.wikipedia.org/wiki/UTF-16) par exemple.
{% endnote %}

Notez que l'usage veut que les nombre associé à chaque caractères soient écrit en [hexadécimal]((https://fr.wikipedia.org/wiki/Syst%C3%A8me_hexad%C3%A9cimal)) sur 4 digit précédé de `U+` pour indiquer que c'est un code Unicode : [U+00E9](https://unicode-table.com/fr/00E9/) correspond ainsi à 'é' et au nombre décimal 233.

On utilise la méthode [`charCodeAt`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt).

On va commencer par faire des petits tests en js pour voir comment on peut résoudre notre tâche (trouver les bonnes méthodes à utiliser), puis un codera la fonction proprement dite.

On peut faire les tests dans un interpréteur node s'ils sont tout petit (on peut utiliser le node dans un terminal vscode par exemple), ou bien exécuter un programme de test, le fichier `mes_tests.js`{.fichier} est là pour ça.

On va préférer ici la première option. Ouvrez un terminal (dans vscode par exemple) puis tapez la commande `node`. Vous devriez obtenir :

```shell
fbrucker@emma cours/numérologie-niveau-1 » node             
Welcome to Node.js v16.9.0.
Type ".help" for more information.
> 
```

Vous êtes dans l'interpréteur node et vous pouvez directement taper des instructions javascript :

```javascript
> ('coucou').charCodeAt(1)
111
> ('你好').charCodeAt(0)
20320
```

Le programme ci-dessus cherche le code Unicode de 'o' et de '你'. Est-ce correct ?

Pour cela il faut encore convertir notre nombre décimal en nombre [hexadécmal](https://fr.wikipedia.org/wiki/Syst%C3%A8me_hexad%C3%A9cimal).

{% faire %}
Testez la fonction [`parseInt`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/parseInt) pour convertir une chaîne de caractères en nombre (`parseInt("4F60", 16)` par exemple) et la méthode des nombres [`toString`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Number/toString) qui fait le contraire (`(20320).toString(16)` par exemple).
{% endfaire %}

## <span id="tache-2"></span> Tâche 2 : nombre associé à une chaîne de caractères

### code js de `nombre(chaîne)`{.language-}

Fort de nos expérimentations, on peut maintenant écrire un fichier `numérologie/numérologie.js`{.fichier} qui va rendre la somme de tous les code Unicode de ses caractères le constituant.

{% info %}
Je jette ici un voile pudique sur ce qu'est un "caractère" dans une chaîne Unicode. Cela peut vite être [très compliqué](https://fr.wikipedia.org/wiki/%C3%89quivalence_Unicode).
{% endinfo %}

Fichier `numérologie/numérologie.js`{.fichier} :

```javascript
function nombre(chaîne) {
    let somme = 0
    for (let i=0; i < chaîne.length; i++) {
        somme += chaîne.charCodeAt(i)
    }
    return somme
}
```

### test js de `nombre(chaîne)`{.language-}

Pour l'instant, on va tester cette fonction *à la sauvage*, c'est à dire en ajoutant du code à la fin de `numérologie.js`{.fichier} et en affichant le résultat à l'écran grâce à la fonction [`console.log`](https://nodejs.org/api/console.html#console_console_log_data_args).  

On peut alors ajouter le code suivant (que l'on commentera pour le conserver) à la fin de  `numérologie/numérologie.js`{.fichier} :

```javascript
// test de nombre(chaîne)

// est-ce 2x plus ?
console.log(nombre("cou"))
console.log(nombre("coucou"))

// chaque caractère :la somme est-elle correcte ?
for (let c of "cou") { 
    console.log(c + " : " + nombre(c))
}
// fin de test de nombre(chaîne)
```

Les commentaires en javascript se font en mettant des `//`{.language-} : le reste la ligne n'est pas évaluée. C'est tellement pratique qu'il y a des raccourcis pour cela en vscode : *menu Edition > Afficher/masquer les commentaires de lignes*.

{% info %}
Pour trouver ce raccourci, je suis allé dans la palette de commande et j'ai tapé *comment* pour voir mes possibilités.
{% endinfo %}

Il existe en javascript [deux façons de commenter du code](https://www.w3schools.com/js/js_comments.asp), le commentaire de bloc et le commentaire de lignes. Je préfère toujours utiliser le commentaire de ligne car c'est d'une part plus visible (chaque ligne est commentée) et on peut plus facilement dé-commenter un bout du commentaire. Comme en plus c'est faisable avec un unique raccourci clavier, c'est efficace.

{% info %}
Plutôt qu'utiliser la [façon standard de faire des boucles en javascript](https://www.w3schools.com/js/js_loop_for.asp) qui me rappelle trop le C/C++ et que j'ai envie d'oublier, j'ai utilisé [une façon de faire des boucle qui ressemble au python](https://www.w3schools.com/js/js_loop_forof.asp) que je préfère.
{% endinfo %}

## <span id="tache-3"></span> Tâche 3 : somme des chiffres d'un nombre

Maintenant qu'on a un nombre associé à une chaîne de caractère, il nous reste à réduire ce nombre à un chiffre. Plusieurs méthodes sont possibles. On va choisir ici de sommer les chiffres du nombre.

Pour faire ça, expérience prouve que les élèves choisissent (presque) toujours la méthode la plus compliquée en se la jouant matheuse :  diviser le nombre par 10 autant de fois que nécessaire et en prenant les parties entières.

Nous allons plutôt faire de la magie avec les conversions de types.

{% note %}
Cette somme n'est peut-être pas un chiffre, on réglera ce problème dans la partie suivante.
{% endnote %}

### code js de `somme(nombre)`{.language-}

Ajouter le code ci-après après la déclaration de la fonction `nombre(chaîne)`{.language-} `numérologie/numérologie.js`{.fichier} :

```javascript
// ...

function somme(nombre) {
    let somme = 0
    chaîne = String(nombre)
    for (let i=0; i < chaîne.length ; i++) {
        somme += parseInt(chaîne.charAt(i))
    }
    return somme
}

// ...
```

{% info %}
On a coutume de mettre des `// ...`{.language-} pour dire que le reste du code du fichier n'est pas changé. Ce n'est pas la peine de les copier/coller.
{% endinfo %}

### test de `somme(nombre)`{.language-}

{% note %}
Comment marche le code de `somme(nombre)`{.language-} ?
{% endnote %}

Plutôt que de réfléchir des heures pour tenter de comprendre, rien de tel qu'utiliser le code pour voir. Ca va bien plus vite et au moins on est sur du résultat.

Pour l'instant, on va utiliser ce code *à la sauvage*, c'est à dire en ajoutant du code à la fin de `numérologie.js`{.fichier} et en affichant le résultat à l'écran grâce à la fonction [`console.log`](https://nodejs.org/api/console.html#console_console_log_data_args).  

On peut alors ajouter le code suivant (qu'on enlèvera ensuite ou que l'on commentera pour le conserver) à la fin de `numérologie/numérologie.js`{.fichier} :

```javascript
// ...

// test de somme(nombre)
console.log(somme(132))

// avec un chiffre : charAt != charCodeAt
console.log(somme(4))
console.log("4".charCodeAt(0))
console.log("4".charAt(0))

// conversion chaine de caractères et nombre
console.log(typeof "4".charAt(0))
console.log(parseInt("4".charAt(0)))
console.log(typeof parseInt("4".charAt(0)))
// fin de test de somme(nombre)
```

## <span id="tache-4"></span> Tâche 4 : somme itérative

Si la somme des chiffre d'un nombre n'est pas un nombre, il faut recommencer l'opération jusqu'à obtenir un chiffre (la convergence est assurée car la somme des chiffre n'un nombre est strictement plus petite que lui s'il n'est pas lui même un chiffre).

### code js de `chiffreAssocie(chaîne)`{.language-}

Dans le fichier *"numérologie/numérologie.js"*, on ajoute la fonction `chiffreAssocie(chaîne)`{.language-} :

```javascript
// ...

function chiffreAssocie(chaîne) {
    valeur = nombre(chaîne)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}

// ...
```

### test js de `chiffreAssocie(chaîne)`{.language-}

On peut alors ajouter le code suivant (qu'on enlèvera ensuite ou que l'on commentera pour le conserver) dans `numérologie/numérologie.js`{.fichier} :

```javascript
// test de chiffreAssocie(chaîne)

//test valeur somme des chiffres
console.log(nombre("coucou"))
console.log(chiffreAssocie("coucou"))
// fin de test de chiffreAssocie(chaîne)
```
