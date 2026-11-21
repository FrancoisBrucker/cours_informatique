---
layout: layout/post.njk

title: "Projet numérologie : partie 5 / postman"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Vérification des routes avec postman.

<!-- fin résumé -->

[Postman](https://www.postman.com/) est une application permettant de tester ses routes http, en particulier les routes POST que l'on ne peut pas tester directement avec un navigateur.

## Installation

{% lien "Téléchargement" %}
[postman](https://www.postman.com/downloads/)
{% endlien %}

{% info %}
Il n'est pas nécessaire de s'inscrire pour télécharger la version gratuite de postman.
{% endinfo %}

## Utilisation

L'utilisation est aisée pour les choses simples.

### Routes GET

#### Simple

![GET google](get-google.png)

* plusieurs onglets de requêtes
* résultats (cookes, headers http, body)

### Sans redirect

![GET google](get-numérologie-redirect.png)

Notez que notre route a suivi la redirection.

Pour supprimer cette feature, allez dans les préférences (l'engrenage en haut à droite) et mettez sur OFF "Automatically follow redirects"

![GET google](get-numérologie-sans-redirect.png)

Remettez l'option à ON car c'est ce que l'on veut habituellement.

### Paramètres

<http://127.0.0.1:3000/prénom/?valeur="François">

![GET paramètres](get-numérologie-paramètres.png)

Voyez que :

* on peut ajouter des paramètres dans l'entrée et l'url se met à jour automatiquement
* la réponse est directement formatée en json

### Routes POST

> TBD
