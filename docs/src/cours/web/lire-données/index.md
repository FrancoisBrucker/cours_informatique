---
layout: layout/post.njk

title: Lire des données
authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Récupérer des données sur internet avec javascript.

<!-- fin résumé -->

## Gestion des fichiers

### Fichier avec node

{% aller %}
[Lire des fichiers avec node](fichiers-node){.interne}
{% endaller %}

### Fichier côté front

{% aller %}
[Lire des fichiers via le navigateur](fichiers-front){.interne}
{% endaller %}

## Données json

Lorsque l'on veut stocker ou transmettre des données, il faut les convertir au format texte. L'usage courant est de les écrire au format [json](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation). Ce format est facile à lire et ressemble aux dictionnaires de js ou de python.

### format json

{% aller %}
[description du format json](https://www.json.org/json-fr.html)
{% endaller %}

Des données écrites sous un format texte comme le json sont dites ***sérialisées***. On les ***désérialise*** pour les retransformer en js.

{% exercice %}
Dans une console node :

1. créez la variable `t`{.language-} contenant le tableau `[1, "deux", {x:1, y:3}]`{.language-} contenant un entier, une chaîne de caractères et un dictionnaire.
2. en utilisant la fonction [`JSON.stringify()`{.language-}](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify), sérialisez `t`{.language-} en une chaîne de caractères au format json que vous stockerez dans la variable `t_json`{.language-}
3. En utilisant l'opérateur [`typeof`{.language-}](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof) vérifiez bien que `t_json`{.language-} est bien une chaîne de caractères et non un objet comme `t`{.language-}, ces deux variables ne sont donc ***pas égale***
4. désérialisez `t_json`{.language-} en utilisant la fonction [`JSON.parse()`{.language-}](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse) et placez le résultat dans la variable `t2`{.language-}
5. vérifiez que `t2`{.language-} possède bien les mêmes valeurs que `t`{.language-}
{% endexercice %}
{% details "solution" %}

```shell
» node                        
Welcome to Node.js v21.1.0.
Type ".help" for more information.
> t = [1, "deux", {x:1, y:3}]
[ 1, 'deux', { x: 1, y: 3 } ]
> t_json = JSON.stringify(t)
'[1,"deux",{"x":1,"y":3}]'
> typeof t
'object'
> typeof t_json
'string'
> t2 = JSON.parse(t_json)
[ 1, 'deux', { x: 1, y: 3 } ]
> t
[ 1, 'deux', { x: 1, y: 3 } ]
```

{% enddetails %}
{% info %}
Contrairement à python, javascript ne possède pas de fonction permettant de tester l'égalité entre deux tableaux. La façon courante de [vérifier l'égalité entre deux tableaux](https://www.freecodecamp.org/news/how-to-compare-arrays-in-javascript/) est de vérifier que leur sérialisation est identique...
{% endinfo %}

### Utiliser des données json

La façon la plus simple d'utiliser des fichiers json avec node ou côté front est de charger le fichier texte, puis de le convertir en json en utilisant la fonction `JSON.parse`{.language-}

> TBD :

```shell
curl https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions/provence-alpes-cote-d-azur/communes-provence-alpes-cote-d-azur.geojson | jq '[.features[].properties ]'
```

> TBD exemple d'utilisation avec les communes du 13 (restriction du fichier raw)

## Charger des fichiers sans input

> TBD
>
> 1. problème CORS
> 2. faire fichier serveur statique
> 3. asynchrone. Mettre un await.
> TBD


> 1. format json
> 2. lire depuis son site et son serveur statique, sinon CORS
> 3. depuis une page web
> 4. depuis une page web que l'on maintient avec un fichier .htaccess

### fetch

> Asynchrone : await

> TBD directement en js sans utilisateur.
> TBD 1. problème CORS 2. faire fichier serveur statique 3. asynchrone. Mettre un await.
> TBD ici await d'abord
> TBD comme pour l'url pas totalement chargé au retour

### htaccess

> TBD depuis une page web que l'on maintient avec un fichier .htaccess

## Fonction `fetch` en javascript

La fonction fetch de javascript permet de charger tout un tas de choses, bien plus que juste des fichiers json :

{% aller %}
[Accès à une ressource distance avec fetch](fetch){.interne}
{% endaller %}
