---
layout: layout/post.njk
title: "Javascript : événements"

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Javascript : événements"
  parent: "Web"
---

<!-- début résumé -->

Gestion des événements en javascript.

<!-- fin résumé -->

## Un timer

{% chemin "**Documentation :**" %}
<https://developer.mozilla.org/en-US/docs/Web/API/setInterval>
{% endchemin %}

Pas à proprement parlé un événement, mais le principe que nous utiliserons ici sera identique pour eux.

{% faire %}
Créez un fichier `timer.html`{.fichier} et copiez/collez-y le code suivant :

```html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Magie javascript : un timer</title>
    </head>
    <body>
        <h1> Compteur</h1>
        <p id="compte"></p>
        <script>
            setInterval(() => {
                color = "#" + Math
                    .floor(Math.random() * 0xffffff)
                    .toString(16)
                document
                    .getElementById("compte")
                    .innerHTML += '<span style="color:' + color + ';\">coucou ! </span>'
            }, 1000)
        </script>
    </body>
</html>
```

Que fait l'exécution de ce [fichier](./timer) ?
{% endfaire %}

Un timer exécute la fonction en paramètre toute les secondes.

## Un événement

{% chemin "**Documentation :**" %}

* <https://developer.mozilla.org/fr/docs/Web/API/Element#%C3%A9v%C3%A8nements>
* <https://developer.mozilla.org/fr/docs/Web/API/HTMLElement#%C3%A9v%C3%A8nements>

{% endchemin %}

Il existe de nombreux événements que l'on peut associer à un `Element`{.language-} ou à un `HTMLElement`{.language-}. La façon la plus simple de les utiliser est d'associer une fonction à la propriété associé.

Par exemple, en regardant la [documentation de l'événement `click`](https://developer.mozilla.org/fr/docs/Web/API/Element/click_event), on voit que la propriété associées est `onclick`.

{% faire %}
Créez un fichier `événement-click.html`{.fichier} contenant le code suivant :

```html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Magie javascript : un événement</title>
    </head>
    <body>
        <h1> Compteur</h1>
        <p>En cliquant sur le nombre, on l'augmente.</p>
        <p id="compte">0</p>
        <script>
            compte = 0
            document
                .getElementById("compte")
                .onclick = () => {
                    compte += 1;
                    document
                        .getElementById("compte")
                        .innerHTML = compte;
                }
        </script>
    </body>
</html>
```

Ouvrez [le](./événement-click) avec votre navigateur et comprenez le.
{% endfaire %}

{% info %}
On a utilisé le fait que les variable sont par défaut globales en javascript (on modifie la variable compte)
{% endinfo %}

{% exercice %}
Créez un fichier html qui change la couleur d'un paragraphe de lorem ipsum lorsque la souris passe dessus, et qui redevient à la normal, une fois que la souris n'est plus sur le paragraphe.
{% endexercice %}
{% details "Solution :" %}
[Ce fichier fonctionne](./événement-hover) :

```html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Magie javascript : hover</title>
    </head>
    <body>
        <p id="lorem">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec viverra, elit a tristique sollicitudin, tortor mauris imperdiet lacus, id egestas quam eros sed diam. Nulla dolor neque, bibendum eu egestas quis, semper a odio. Proin venenatis diam quam. Nulla posuere mauris id tincidunt commodo. Duis turpis est, scelerisque ut suscipit sit amet, rhoncus sit amet quam. In hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur in malesuada ligula. Pellentesque a risus at ex congue feugiat. In velit nulla, aliquet eget bibendum sed, vestibulum quis turpis. Mauris nisl turpis, condimentum eu augue vel, malesuada finibus elit. Maecenas massa nisl, malesuada non dictum vel, pellentesque sed massa. Integer vel consectetur purus, non fringilla velit. Phasellus convallis elementum posuere.</p>
        <script>
            document
                .getElementById("lorem")
                .onmouseover = () => {
                    document
                        .getElementById("lorem")
                        .style
                        .color = "red"
                };
            document
                .getElementById("lorem")
                .onmouseleave = () => {
                    document
                        .getElementById("lorem")
                        .style
                        .color = ""
                }
        </script>
    </body>
</html>
```

{% enddetails %}

## Des fonctions associées à un événement

{% chemin "**Documentation :**" %}
<https://developer.mozilla.org/en-US/docs/Web/Events/Event_handlers>
{% endchemin %}

Dans les cas complexe, avoir une unique fonction associée à un événement est limitant. Pour avoir plusieurs fonctions associées à un même événement, on utilise la méthode [`addEventListener`{.language-}](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) pour ajouter une fonction et [`removeEventListener`{.language-}](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/removeEventListener) pour le supprimer.
