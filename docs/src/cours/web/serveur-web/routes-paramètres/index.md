---
layout: layout/post.njk

title: "Routes avec paramètres"

eleventyNavigation:
  key: "Routes avec paramètres"
  parent: "Serveur Web"
---

<!-- début résumé -->

Gestion des routes avec paramètres avec express.

<!-- fin résumé -->

Nous utiliserons ici la bibliothèque express pour montrer ces concepts, mais ils existent dans toute bibliothèque permettant de créer des serveurs webs.

Les routes que nous avons vus pour l'instant sont *statiques*, il faut créer une route pour chaque cas possible. Par exemple le site sous express suivant répond uniquement à 2 routes <http://127.0.0.1:3000/aurevoir> et <http://127.0.0.1:3000/bonjour> (le reste fait un 404) :

```javascript
import express from 'express'
const app = express()

const hostname = '127.0.0.1';
const port = 3000;

app.get('/bonjour/', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end("bonjour");

})

app.get('/aurevoir/', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end("au revoir");

})

app.use(function (req, res) {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end("N'existe pas");

})

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);
```

{% info %}
Si vous exécutez ce code, et utilisez les outils de développement pour voir le résultat de la requête <http://127.0.0.1:3000/aurevoir> par exemple, vos verrez que le navigateur chrome ajoute des choses au texte pour le transformer en html. Ce n'est **pas** le serveur qui le fait.
{% endinfo %}

Si on veut ajouter un prénom, il faut ajouter des routes. Par exemple si on veut dire saluer toutes les Carole :

```javascript

// ...

app.get('/bonjour/Carole', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end("bonjour Carole !");

})

app.get('/aurevoir/Carole', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end("au revoir Carole !");

})

// ...
```

Ceci n'est évidemment pas une solution acceptable si l'on veut dire bonjour à tout le monde sans avoir besoin de créer une route spécifique pour tous les prénoms du monde. Il faut pouvoir rendre nos urls paramétrables afin qu'elles puissent s'adapter au prénom de la route. Il y a plusieurs possibilités et nous allons en voir 2, les plus classiques. Supposons que l'on cherche à obtenir le code associé au prénom "François". On peut :

* encoder le prénom dans l'url : <http://localhost:3000/bonjour/françois>
* encoder le prénom dans une query : <http://localhost:3000/bonjour?prenom=françois>

Dans le premier cas, la demande est explicitée directement dans l'url, dans la seconde elle est encodée dans une demande.

## Encodage des paramètres dans l'url

{% lien "**Documentation**" %}
<https://expressjs.com/en/guide/routing.html#route-parameters>
{% endlien %}

Pour la route bonjour par exemple :

```javascript

// ...

app.get('/bonjour/:prenom', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end("bonjour " + req.params.prenom + " !");

})

// ...
```

Les différents paramètres sont placés dans le dictionnaire `req.params`{.language-}.

{% info %}
C'est triste mais il est impossible d'utiliser des variables accentuées. En remplaçant `:prenom`{.language-} par `:prénom`{.language-} le code ne fonctionne plus. C'est lié à la façon dont express gère les urls.

En revanche, la requête <http://127.0.0.1:3000/bonjour/François> fonctionne parfaitement, les paramètre étant eux bien traité en utf8.
{% endinfo %}

Notez que comme on a juste ajouté la route paramétrée, notre serveur sert bien les  deux routes <http://127.0.0.1:3000/bonjour/> **et** <http://127.0.0.1:3000/bonjour/François> !

{% exercice %}
Créez une route qui prend également en compte le nom de famille. On doit pouvoir effectuer des routes de style :

<http://127.0.0.1:3000/bonjour/Jimi/Hendrix>

{% endexercice %}
{% details "solution" %}

```javascript
// ...

app.get('/bonjour/:prenom/:nom', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end(`bonjour ${req.params.prenom} ${req.params.nom} ! `);

})

// ...
```

On a utilisé ici un propriété bien sympathique du javascript qui permet de [mettre des paramètres directement dans une chaîne de caractères](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Strings#concatenating_strings).
{% enddetails %}

## <span id="query"></span> Encodage des paramètres dans une query

{% lien "**Documentation**" %}
<https://en.wikipedia.org/wiki/Query_string>
{% endlien %}

Cette méthode, appelée [query string](https://en.wikipedia.org/wiki/Query_string), est utilisée par exemple par google maps ou encore amazon pour spécifier ses requêtes. Elle consiste à donner explicitement les paramètres dans la requête sous la forme d'un couple `clé=valeur`{.language}.

Dans notre ças, cela correspondrait à des routes du style :

* <http://localhost:3000/bonjour?prénom=François>
* <http://127.0.0.1:3000/bonjour?prénom=Sam junior>

{% note %}

* On entame la query par un `?`{.language-}
* on sépare les différents paramètres par des `&`{.language-}

{% endnote %}

Du côté de express, la query est mis dans le dictionnaire `req.query`{.language-}. Pour la route bonjour cela donne :

```javascript

// ...

app.get('/bonjour', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end("bonjour " + req.query.prénom + " !");

})

// ...
```

Plusieurs remarques :

* La route ci-dessus remplace notre route initiale : à ma connaissance, il n'y a aucun moyen de différentier les routes avec et sans query en express
* Si l'on appelle la route sans query <http://localhost:3000/bonjour>, le dictionnaire n'a pas de champ `prénom`{.language-}, il est donc `undefined`{.language-}
* on a pu mettre des accents aux paramètres ! C'est en effet des valeurs qui vont être interprétées par express (elle ne sont pas présente dans la création de la route avec `app.get`{.language-})

{% exercice %}
Créez une route qui prend également en compte le nom de famille. On doit pouvoir effectuer des routes de style :

<http://localhost:3000/bonjour?prénom=Harry&nom=Cover>

{% endexercice %}
{% details "solution" %}

```javascript
// ...

app.get('/bonjour', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end(`bonjour ${req.query.prénom} ${req.query.nom} ! `);

})

// ...
```

{% enddetails %}
