---
layout: layout/post.njk
title: "Javascript : DOM"

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Javascript : DOM"
  parent: "Web"
---

<!-- début résumé -->

Manipulation de l'arbre DOM en javascript.
<!-- fin résumé -->

## Accès aux éléments

{% faire %}
Créez un fichier `javascript-dom.html`{.fichier} et copiez/collez le contenu suivant :

```html
<html>
    <head>
        <title>Magie javascript</title>

    </head>
    <body>
        <style>
            body,
            html {
                margin: 0;
                padding: 0;

                background: skyblue;
                color: #FFFFFF;
                font-size: 2em;
                text-align: center;
            }
            .milieu {
                margin: 10px auto;
                height: 50px;
                width: 20px;
            }
            .color {
                background-color: olive;
            }
        </style>

        <h1> Enfin du web !</h1>
        <p> et on <strong>aime</strong> ça</p>
        <div id="mon_div" class="milieu"></div>
        <p>!</p>
        <script>
            document
                .getElementById("mon_div")
                .style
                .backgroundColor = "blue"
        </script>
    </body>
</html>
```

Ouvrez [le](./javascript_dom) avec votre navigateur.
{% endfaire %}
{% attention %}
On ne peut pas mettre le code avant la déclaration du div (ce n'est **pas** comme du css).

Testez le pour voir.
{% endattention %}

L'objet [`document`{.language}](https://developer.mozilla.org/fr/docs/Web/API/Document) est le point d'accès à l'arbre DOM. Il nous permet de récupérer les éléments de cet arbre.

Dans notre cas, nous récupérons un [HTMLElement](https://developer.mozilla.org/fr/docs/Web/API/HTMLElement) qui hérite de [Element](https://developer.mozilla.org/fr/docs/Web/API/Element). Un `HTMLElement` possède de nombreux attributs auxquels on peut accéder, comme le [style](https://developer.mozilla.org/fr/docs/Web/API/HTMLElement/style).

On peut aussi accéder aux éléments par :

* leur tag : [`document.getElementsByTagName("p")`{.language-}](https://developer.mozilla.org/fr/docs/Web/API/Document/getElementsByTagName)
* leurs classes : [`document.getElementsByClassName("milieu")`{.language-}](https://developer.mozilla.org/fr/docs/Web/API/Document/getElementsByClassName) (on peut mettre plusieurs classes en les séparant par des espaces)

{% info %}
Seul la méthode [`document.getElementById`{.language-}](https://developer.mozilla.org/fr/docs/Web/API/Document/getElementById) rend directement un élément. Les autres méthodes rendent un conteneur de type [HTMLCollection](https://developer.mozilla.org/fr/docs/Web/API/HTMLCollection) que l'on peut manipuler comme un tableau :

```js
var list = document.getElementsByTagName("p");
for (var i = 0; i < list.length; i++) {
    console.log(list[i]);
}
```

{% endinfo %}

{% faire %}
Dans la console du fichier [`javascript_dom.html`{.language-}](./javascript_dom), accédez aux éléments par leur nom et leurs classes.
{% endfaire %}

## Naviguer dans l'arbre

> TBD : arbre DOM : Node -> element -> HTMLElement

{% lien %}
<https://fr.javascript.info/dom-navigation>
{% endlien %}

On peut naviguer dans l'arbre DOM en parcourant ses [nœuds](https://developer.mozilla.org/fr/docs/Web/API/Node).

Notez qu'un élément possède aussi un attribut [children](https://developer.mozilla.org/fr/docs/Web/API/Element/children). La différence tient au fait que children ne contient **que** les fils qui sont eux-même des éléments. Pas les champs texte par exemple.

{% faire %}
Dans la console du fichier [`javascript_dom.html`{.language-}](./javascript_dom), Remarquez la différence entre `document.getElementsByTagName("p")[0].childNodes` et `document.getElementsByTagName("p")[0].children`

{% endfaire %}



## Modifier des éléments

{% info %}
Cela vaut le coup de jeter un coup d’œil aux attributs et méthodes des [`Element`](https://developer.mozilla.org/fr/docs/Web/API/Element) ou des [`HTMLElement`](https://developer.mozilla.org/fr/docs/Web/API/HTMLElement), ellent permettent de contrôler très finement et de connaître parfaitement l'arbre DOM.
{% endinfo %}

### style

Dans l'exemple précédent on a accédé au [style](https://developer.mozilla.org/fr/docs/Web/API/HTMLElement/style) d'un `HTMLElement`{.language-}.

On peut aussi directement accéder à n'importe quel attribut d'un `Element` avec les méthodes [`getAttribute`](https://developer.mozilla.org/fr/docs/Web/API/Element/getAttribute) et [`setAttributes`](https://developer.mozilla.org/fr/docs/Web/API/Element/setAttribute) qui nous permettent de changer tous les attributs.

### classes

`element.classList` qui rend une [liste](https://developer.mozilla.org/fr/docs/Web/API/DOMTokenList) permettant d'ajouter ou supprimer ue class

### texte

Attribut innerHtml ou innerText

{% faire %}
Dans la console du fichier [`javascript_dom.html`{.language-}](./javascript_dom), Remarquez la différence entre `document.getElementsByTagName("p")[0].innerText` et `document.getElementsByTagName("p")[0].innerHtml`
{% endfaire %}

## Créer des éléments

On peut *facilement* ajouter des éléments  à l'arbre DOM grace à la fonction [document.createElement](https://developer.mozilla.org/fr/docs/Web/API/Document/createElement) et à la méthode [appendChild](https://developer.mozilla.org/fr/docs/Web/API/Node/appendChild) des éléments.

{% faire %}
Ajoutez au fichier `javascript_dom.html`{.fichier} le code ci-après pour ajouter une liste dans le div :

```html
<script>
    liste_non_orientée = document.createElement('ul')
    tab = ["oui", "non", "peut-être", "je ne sais pas"]
    tab.forEach((cat) => {
        li = document.createElement('li')
        button = document.createElement('button')
        button.appendChild(document.createTextNode(cat))
        button.setAttribute("id", cat)
        button.setAttribute("class", "color")
        li.appendChild(button)
        liste_non_orientée.appendChild(li)
    })
    document
        .getElementById("mon_div")
        .appendChild(liste_non_orientée)
    document
        .getElementById("mon_div")
        .style
        .width = 'auto'
    document
        .getElementById("mon_div")
        .style
        .height = 'auto'
</script>
```

{% endfaire %}
