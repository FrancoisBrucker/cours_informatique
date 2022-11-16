---
layout: layout/post.njk

title: Lire des données
authors:
    - "François Brucker"


eleventyNavigation:
  key: "Lire des données"
  parent: "Web"
---

<!-- début résumé -->

Récupérer des données sur internet avec javascript.

<!-- fin résumé -->

## Asynchrone et promesse

La plupart des requêtes en javascript sont asynchrones. Lorsque C'est à dire que quand on va demander quelque chose qui prend du temps, à la place d'attendre que la fonction se termine avant de passer à autre chose on passe directement à l'instruction suivante avec la possibilité **une fois que la fonction se termine** d'exécuter une autre fonction. Ce mécanisme s'appelle une [promesse](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Using_promises).

```javascript

ma_longue_fonction()
  .then(response => {
    // exécuté lorsque la longue fonction s'arrête
    // le paramètre de cette fonction étant de retour de la longue fonction
  })
  .catch(error => {
    // si la longue fonction ne s'est pas bien exécutée
  })

```

Le côté sympathique des promesses c'est qu'elle [peuvent s'enchaîner](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#chaining) en exécutant une nouvelle promesse après qu'une se soit terminée :

```javascript
ma_longue_fonction()
  .then(response => {
    // ...

    return une_autre_longue_fonction()
  })
  .then(response => {
    // c'est le then de l'autre longue fonction

  })
  .catch(error => {
    // si la longue fonction ne s'est pas bien exécutée
  })

```

Il peut cependant parfois être utile d'écrire du code, *à l'ancienne*, c'est à dire un exécutant ligne à ligne notre code. Le javascript a une instruction pour cela : `await`{.language-}. Cette instruction attend que la promesse te temrine pour aller à la ligne d'après. Le code précédent s'écrirait (sans la gestion d'erreur) :

```javascript

response = await ma_longue_fonction()
response2 = await une_autre_longue_fonction(response)

```

{% attention %}
On ne peut pas utiliser `await` partout. On ne peut le faire qu'à l'intérieur d'une fonction taguée `async` : <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function>
{% endattention %}

## Fonction `fetch` en javascript

La fonction [fetch](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch) de javascript vous permet de récupérer des données et de les utiliser dans un script front.

### Lecture de données distantes

{% faire %}

Créez un fichier : `lire-données-url.html` est copiez/collez y le code suivant :

```html#

<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8"/>
    <title>Communes de PACA</title>
  </head>
  <body>
    <h1>Communes de PACA</h1>
    <script>
      data = null

      fetch('https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions/provence-alpes-cote-d-azur/communes-provence-alpes-cote-d-azur.geojson', {method: 'GET'})
        .then(response => {
          console.log(response.status)
          data = response
        })
        .catch(error => {
          console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
        })

        console.log(data)
    </script>    
  </body>
</html>

```

Exécutez [le](./projet-fetch/lire-données-url) pour voir les réponses dans la console.
{% endfaire %}
{% info %}
Si vous cherchez des coordonnées géographiques de la France, allez voir : <https://github.com/gregoiredavid/france-geojson>.

Le format de données utilisés est le format [geojson](https://fr.wikipedia.org/wiki/GeoJSON) qui est un format de données json adaptés aux coordonnées géographique.
{% endinfo %}

Le code précédent explicite le faite que `fetch`{.language-} est une instruction asynchrone qui s'exécute sous la forme d'une promesse : le `console.log` de la fin de l'instruction `fetch`{.language-} (ligne 22) rend toujours null puisqu'elle elle est exécutée *avant* la fin de l'instruction.

{% attention %}
Faire plusieurs choses en même temps produit des erreurs inattendues et difficile à déboguer.

Essayer de faire en sorte que ces processus parallèles soient indépendants.
{% endattention %}

### Lecture d'un fichier json

Les données sont reçues sous la forme d'un objet de type [Response](https://developer.mozilla.org/fr/docs/Web/API/Response). Lorsque nos données sont de type [json](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation) — **ce qui devrait toujours être le cas** — nous pouvons chaîner une autre promesse pur retrouver nos données, comme le montre le code suivant :

```html

<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8"/>
    <title>Communes de PACA</title>
  </head>
  <body>
    <h1>Communes du 13</h1>
    <script>
      fetch('https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements/13-bouches-du-rhone/communes-13-bouches-du-rhone.geojson', {method: 'GET'})
        .then(response => {
          console.log(response)
          return response.json()
        })
        .then(data => {
          console.log(data)
        })
        .catch(error => {
          console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
        })
    </script>
  </body>
</html>

```

{% note %}
Dans la mesure du possible essayer de ne transmettre des données que sous la forme de json ou de texte.

Le csv par exemple est beaucoup plus difficile à utiliser car il n'existe pas de conversion automatique comme pour le json.
{% endnote %}

On peut ensuite utiliser ces données dans la page :

{% exercice %}
Modifier le code précédent pour qu'il affiche une liste de toutes les communes des bouches du Rhône.

{% endexercice %}
{% info %}
Pour cela, vous pourrez noter que les données json contiennent un attribut `features` qui est une liste de dictionnaires ayant deux attributs `geometry` et `properties`. Cette dernière contenant le nom et le code postal de la ville :

```javascript
for (x of data.features) {
  console.log(x.properties)
}
```

{% endinfo %}
{% details "solution" %}

```html
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8"/>
    <title>Communes de PACA</title>
  </head>
  <body>
    <h1>Communes du 13</h1>
    <ul id="liste"></ul>
    <script>
      fetch('https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements/13-bouches-du-rhone/communes-13-bouches-du-rhone.geojson', {method: 'GET'})
        .then(response => {
          return response.json()
        })
        .then(data => {
          liste = document.getElementById("liste")
          for (x of data.features) {
            li = document.createElement('li')
            li.appendChild(document.createTextNode(x.properties.nom + ' (' + x.properties.code + ')'))
            liste.appendChild(li)
          }
        })
        .catch(error => {
          console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
        })
    </script>
  </body>
</html>
```

Disponible [ici](./projet-fetch/lire-données-url-json-liste)
{% enddetails %}

### Lecture d'un fichier texte

On convertit la réponse en texte :

```javascript
fetch('https://www.gutenberg.org/ebooks/14155.txt.utf-8', {method: 'GET'})
        .then(response => {
          return response.text()
        })
        .then(data => {
          console.log(data)
        })
        .catch(error => {
          console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
        })
```

### Fetch une image

La réponse de fetch est un *stream* c'est à dire un flux de données. Les données du flux sont récupérées par les commandes `.json()`{.language-} et `.texte()`{.language-} vues précédemment. Dans le cas où l'on récupère des fichiers non texte (une image, une vidéo, etc) on utilise [`.blob()`](https://developer.mozilla.org/en-US/docs/Web/API/Response/blob)

```html

<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8"/>
    <title>CORS mon ami</title>
  </head>
  <body>
    <h1>Fetch Ada</h1>
    <img id="mon_image"/>
    <script>
      fetch('https://upload.wikimedia.org/wikipedia/commons/0/0f/Ada_lovelace.jpg', {method: 'GET'})
        .then(response => {
          return response.blob()
        })
        .then(blob => {
          const objectURL = URL.createObjectURL(blob);
          console.log(objectURL)
          document.getElementById("mon_image").src = objectURL;
        })
        .catch(error => {
          console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
        })
    </script>
  </body>
</html>

```

Ceci ne peut marcher que pour des données que le serveur autorise à récupérer avec fetch, sinon vous aurez des des problèmes CORS (voir ci-après).

### Fetch de son compte ecm

Par défaut, un site n'autorise de récupérer des données par fetch que si la demande a été faite par un script issu du site lui-même.

{% note %}
Les règles de transmission de fichiers s'appellent : [CORS](https://developer.mozilla.org/fr/docs/Web/HTTP/CORS)
{% endnote %}

{% faire %}

1. créez un dossier `données` dans votre dossier `~/html` sur le sas1
2. placez un petit fichier texte à l'intérieur
3. lisez-le avec chrome, par exemple : <http://[mon site].perso.centrale-marseille.fr/données/petit_texte.txt>
4. essayez de le récupérer avec fetch

Vous devriez obtenir une erreur dans la console.
{% endfaire %}

Lorsque les données sont des fichiers d'un dossier, on peut ajouter à ce dossier un fichier `.htaccess` dont le contenu explicite les règles d'accès. 

{% faire %}

1. Créez un fichier `.htaccess` dans le dossier `~/html/données`
2. mettez la ligne : `Header always set Access-Control-Allow-Origin: "*"`
3. tentez à nouveau d'acceder au fichier

Vous devriez pouvoir voir le fichier maintenant.

{% endfaire %}

{% attention %}
La règle cors qu'on a rajouté permet à tout utilisateur de récupérer les données du dossier. Donc faites attentions à l'endroit ou vous mettez ce fichier et ce que vous rendez accessible.
{% endattention %}

{% info %}
Le comportement de votre dossier `~/html/visible` est aussi contrôlé par un fichier `.htaccess`. Jetez-y un coup d'œil !
{% endinfo %}

### Fetch en local impossible

Il est impossible de récupérer des données en local avec fetch. Vos données doivent être accessible via un serveur web.

Par exemple le fichier suivant est impossible à faire fonctionner, car les données ne snt **pas** sur un serveur :

```html
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8"/>
    <title>CORS mon ami</title>
  </head>
  <body>
    <h1>Petit texte (dans la console)</h1>
    <script>
      fetch('petit_texte.txt', {method: 'GET'})
        .then(response => {
          return response.text()
        })
        .then(texte => {
          console.log(texte)
        })
        .catch(error => {
          console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
        })
    </script>
  </body>
</html>
```

{% faire %}
Exécuter le [code précédent](projet-fetch/lire-données-blob). Vous devriez voir apparaître Ada.
{% endfaire %}

La seule façon de procéder est d créer un serveur web minimal.

## Créer un serveur minimal pour lire ses données

Il est très facile de créer un serveur web en python avec la commande :

```
python3 -m http.server
```

{% info %}
remplacez `python3` par `python` si vous êtes sous windows.
{% endinfo %}

Un serveur est crée à l'adresse <http://localhost:8000/> et il permet d'accéder aux fichiers via le protocole http.
