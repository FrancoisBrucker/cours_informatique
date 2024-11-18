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

Récupérer des données sur internet avec javascript.

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

{% lien %}
[description du format json](https://www.json.org/json-fr.html)
{% endlien %}

Des données écrites sous un format texte comme le json sont dites **_sérialisées_**. On les **_désérialise_** pour les retransformer en js.

{% exercice %}
Dans une console node :

1. créez la variable `t`{.language-} contenant le tableau `[1, "deux", {x:1, y:3}]`{.language-} contenant un entier, une chaîne de caractères et un dictionnaire.
2. en utilisant la fonction [`JSON.stringify()`{.language-}](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify), sérialisez `t`{.language-} en une chaîne de caractères au format json que vous stockerez dans la variable `t_json`{.language-}
3. En utilisant l'opérateur [`typeof`{.language-}](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof) vérifiez bien que `t_json`{.language-} est bien une chaîne de caractères et non un objet comme `t`{.language-}, ces deux variables ne sont donc **_pas égale_**
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

Côté client, la façon la plus simple d'utiliser des fichiers json avec node ou côté front est de charger le fichier texte, puis de le convertir en json en utilisant [la fonction `JSON.parse`{.language-}](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse) (on va voir un exemple juste après en utilisant la fonction fetch de javascript).

### Charger des fichiers avec la fonction `fetch`{.language-}

> TBD problème de sécurité expliciter cors et htaccess

{% lien %}

- [problème CORS](https://grafikart.fr/tutoriels/cors-http-navigateur-1180)
- [fichier htaccess](https://www.mauricelargeron.com/parametrer-les-acces-a-son-serveur/)

{% endlien %}

La fonction fetch de javascript permet de charger tout un tas de choses, bien plus que juste des fichiers json :

{% aller %}
[Accès à une ressource distance avec fetch](fetch){.interne}
{% endaller %}
