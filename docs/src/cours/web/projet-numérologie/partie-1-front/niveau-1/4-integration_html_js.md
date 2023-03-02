---
layout: layout/post.njk
title: "Projet numérologie / partie 1 : front / niveau 1 / intégration html et js"

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Projet numérologie / partie 1 : front / niveau 1 / intégration html et js"
  parent: "Projet numérologie / partie 1 : front / niveau 1"
---

<!-- début résumé -->

Lier le code js et la page html
<!-- fin résumé -->

## <span id="tache-1"></span> Tache 1 : cliquer sur le bouton

Pour l'instant, lorsque vous cliquez sur le  bouton, il n'y a l'air de rien se passer. En fait si, il s'est passé quelque chose la première fois que vous avez cliquez dessus : un `?` s'est ajouté à la fin de l'url et on *voit* que la page se recharge.

{% note %}
La gestion par défaut des formulaires html est archaïque. On va faire comme si elle n'existait pas.
{% endnote %}

Nous allons utiliser le javascript pour gérer le click sur ce bouton. Pour cela, on a plusieurs choses à faire/comprendre :

1. trouver le bouton
2. greffer du code qui s'exécutera lorsque l'on cliquera sur le bouton
3. trouver où se trouve le texte à récupérer

Pour récupérer des objets de l'arbre DOM, le plus simple est de les identifier de façon unique en utilisant un identifiant. Une balise peut en effet avoir deux types d'attributs spéciaux :

### Identifiants de balises

* des *classes* avec attribut `class="class1 class2 ..."`{.language-}. Les différentes classes d'une balise sont séparée par des espaces (une classe ne peut donc **pas** posséder d'espaces dans son nom)
* un identifiant avec l'attribut `id="identifiant"`{.language-}. Cet identifiant doit être unique.

{% note %}
Un identifiant sert lorsque l'on veut choisir une balise particulière au sein d'un ensemble de balises.
{% endnote %}

Nous voulons :

* récupérer le texte de l'input
* savoir quand on clique sur le bouton

Modifions donc leur code dans le fichier `numérologie/index.html`{.fichier} en leur ajoutant des identifiants :

```html
<!-- ... -->

<form class="pure-form">
    <label>Prénom :</label>
    <input type="text" id="form-input"/>

    <button type="submit" id="form-button" class="pure-button pure-button-primary">Envoi</button>
</form>

<!-- ... -->
```

{% info %}
Voyez comment les [commentaires html](https://www.w3schools.com/html/html_comments.asp) sont différents des autres commentaires.
{% endinfo %}

### Console javascript

Ouvrez les [outils de développement](https://developer.chrome.com/docs/devtools/open/) de chrome et choisissez le panel [*console*](https://developer.chrome.com/docs/devtools/console/).

Cette console est l'interpréteur javascript de la page. On peut y écrire du javascript comme dans du node, mais l'intérêt principal est qu'il possède des objets et des attributs permettant de manipuler l'arbre DOM :

```javascript
document.querySelector("#form-input").value
```

Et vous y découvrirez la valeur de votre input, qui est vide (`''`{.language-}) si vous n'avez rien tapé dans ce champ.

{% faire %}
Changez la valeur de l'input et vérifiez que la ligne précédente donne un autre résultat
{% endfaire %}

Comment avons-nous réalisé ce prodige ?

* [`document.querySelector`{.language-}](https://developer.mozilla.org/fr/docs/Web/API/Document/querySelector) qui permet de retrouver un élément de l'arbre DOM par son identifiant (il faut mettre un `#`{.language-} devant l'identifiant)
* l'attribut [`value`{.language-} d'un input](https://developer.mozilla.org/fr/docs/Web/HTML/Element/Input#value) qui donne sa valeur.

Il faut maintenant réussir à faire ça lorsque l'on clique sur un bouton.

### Événements

{% lien "**Documentation**" %}
<https://developer.mozilla.org/fr/docs/Learn/JavaScript/Building_blocks/Events>
{% endlien %}

Dès qu'il se passe quelque chose sur la page, un évènement est lancé. Ici, pour le bouton, c'est lorsque l'on clique dessus. On va donc se greffer à cet évènement. Tapez dans la console :

```javascript
document.querySelector("#form-button").addEventListener("click", (event) => {
    console.log(document.querySelector("#form-input").value)
    event.preventDefault()
})
```

{% faire %}
Vous pouvez ensuite cliquer sur le bouton pour voir le code s'exécuter.
{% endfaire %}

Le code se comprend comme ça :

1. on récupère (comme avant) le bouton.
2. on ajoute une fonction qui fa être exécuté lors de l'évènement "click"

La notation [`(param) => {code}`{.language-} crée une fonction javascript](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Functions#utiliser_une_expression_de_fonction_fl%C3%A9ch%C3%A9e_).

La ligne `event.preventDefault()`{.language-} est importante, elle empêche le comportement par défaut de l'évènement click qui recharge la page. Supprimez cette ligne pour voir le résultat.

### Integration dans l'html

Le code qu'on a placé dans la console va être ajouté à notre html. Ici, on place le code javascript à la fin du `<body></body>`{.language-} pour que les balises existent quand on va les chercher avec `querySelector`{.language-}.On intègre ce code grâce à la balise `<script></script>`{.language-}.

{% info %}
Le javascript se place à l'opposé du style css.
{% endinfo %}

Le fichier html `numérologie/index.html`{.fichier} est alors :

```html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>
        
        <link rel="stylesheet" href="https://unpkg.com/purecss@2.0.6/build/pure-min.css" integrity="sha384-Uu6IeWbM+gzNVXJcM9XV3SohHtmWE+3VGi496jvgX1jyvDTXfdK+rfZc8C1Aehk5" crossorigin="anonymous">
        
        <link href="main.css" rel="stylesheet">

    </head>
    <body>
        <div class="main">
            <form class="pure-form">
                <label>Prénom :</label>
                <input type="text" id="form-input"/>
            
                <button type="submit" id="form-button" class="pure-button pure-button-primary">Envoi</button>
            </form>
            <div class="pure-g">
                <div class="pure-u-1-3"></div>
                <div class="pure-u-1-3"><p>7</p></div>
                <div class="pure-u-1-3"></div>
            </div>

        </div>
        <script>
            document.querySelector("#form-button").addEventListener("click", (event) => {
                chaine = document.querySelector("#form-input").value;
                console.log(chaine);
                event.preventDefault();
            })
        </script>
    </body>
</html>
```

Dès que vous cliquerez sur le bouton, la valeur sera envoyée dans la console.

{% faire %}
Testez le !
{% endfaire %}

## <span id="tache-2"></span> Tâche 2 : chargement et utilisation de fichier javascript

On ne veut pas juste afficher le prénom dans la console, on veut lui associé le chiffre calculé en [partie 2](../2-code_js). Il faut donc charger nos fonctions javascript dans le html.

Cela se fait simplement avec l'attribut `src`{.language-} de la balise `<script></script>`{.language-} qui contient un chemin relatif vers un fichier javascript :

```html
<script src="./numérologie.js"></script>
```

{% attention %}
Il ne faut rien mettre d'autre dans script si on charge un fichier
{% endattention %}

Après cette ligne dans le html, la fonction `chiffreAssocie`{.language-} sera connue. Cela donne le fichier `numérologie/index.html`{.fichier} suivant, qui commence par charger notre fichier dans une balise script, puis l'utilise dans une autre (c'est possible car l'interpréteur javascript est commun à la page) :

```html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>
        
        <link rel="stylesheet" href="https://unpkg.com/purecss@2.0.6/build/pure-min.css" integrity="sha384-Uu6IeWbM+gzNVXJcM9XV3SohHtmWE+3VGi496jvgX1jyvDTXfdK+rfZc8C1Aehk5" crossorigin="anonymous">
        
        <link href="main.css" rel="stylesheet">

    </head>
    <body>
        <div class="main">
            <form class="pure-form">
                <label>Prénom :</label>
                <input type="text" id="form-input"/>
            
                <button type="submit" id="form-button" class="pure-button pure-button-primary">Envoi</button>
            </form>
            <div class="pure-g">
                <div class="pure-u-1-3"></div>
                <div class="pure-u-1-3"><p>?</p></div>
                <div class="pure-u-1-3"></div>
            </div>

        </div>
        <script src="./numérologie.js"></script>
        <script>
            document.querySelector("#form-button").addEventListener("click", (event) => {
                chaine = document.querySelector("#form-input").value;
                console.log(chaine);
                event.preventDefault();
            })
        </script>
    </body>
</html>
```

Par défaut, on a mis un chiffre de `"?"`{.language-} puisque le prénom est vide au chargement.

## <span id="tache-3"></span> Tâche 3 : modification du html

Il nous reste à changer le chiffre lorsque l'on appuie sur le bouton. Il faut pouvoir modifier le contenu du paragraphe. Pour cela :

* on donne un identifiant unique au paragraphe à modifier
* on regarde la doc pour savoir quelle attribut modifier : ici c'est [textContent](https://developer.mozilla.org/fr/docs/Web/API/Node/textContent)

Le fichier html `numérologie/index.html`{.fichier} final est alors :

```html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>
        
        <link rel="stylesheet" href="https://unpkg.com/purecss@2.0.6/build/pure-min.css" integrity="sha384-Uu6IeWbM+gzNVXJcM9XV3SohHtmWE+3VGi496jvgX1jyvDTXfdK+rfZc8C1Aehk5" crossorigin="anonymous">
        
        <link href="main.css" rel="stylesheet">

    </head>
    <body>
        <div class="main">
            <form class="pure-form">
                <label>Prénom :</label>
                <input type="text" id="form-input"/>
            
                <button type="submit" id="form-button" class="pure-button pure-button-primary">Envoi</button>
            </form>
            <div class="pure-g">
                <div class="pure-u-1-3"></div>
                <div class="pure-u-1-3"><p id="chiffre">7</p></div>
                <div class="pure-u-1-3"></div>
            </div>

        </div>
        <script src="./numérologie.js"></script>
        <script>
            document.querySelector("#form-button").addEventListener("click", (event) => {
                chaine = document.querySelector("#form-input").value;
                chiffre = chiffreAssocie(chaine);
                document.querySelector("#chiffre").textContent = chiffre;
                event.preventDefault();
            })
        </script>
    </body>
</html>
```
