---
layout: layout/post.njk
title: "Anatomie d'une url"

authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Notion d'url.

<!-- fin résumé -->

Une [URL](https://fr.wikipedia.org/wiki/Uniform_Resource_Locator) (Uniform Resource Locator) est un cas particulier d'[URI](https://fr.wikipedia.org/wiki/Uniform_Resource_Identifier).

Pour ce qui nous concernent, ces deux notions permettent de retrouver une ressource. La force d'une d'URI est son [schéma](https://fr.wikipedia.org/wiki/Sch%C3%A9ma_d%27URI), très souple qui s'adapte à de nombreuses situation

{% note "**Définition**" %}
Un [schéma d'URI](https://fr.wikipedia.org/wiki/Sch%C3%A9ma_d%27URI) est défini de la façon suivante :

```
<nom du schéma>://<domaine>/<chemin> [?<requête>] [#<fragment>]
```

* le **nom du schéma** : protocole d'accès aux données
* le **domaine** et le **chemin** permettent de retrouver la ressource
* requête et domaines sont facultatifs :
  * la **requête** est constitué d'éléments `clef=valeur` séparé par des `;`
  * le **fragment** est un mot
{% endnote %}

Dans le web on parle plutôt d'url qui sont une sous-classe des uri :

{% note "**Définition**" %}
Une [url (Uniform Resource Locator)](https://fr.wikipedia.org/wiki/Uniform_Resource_Locator) est un moyen de retrouver n'importe quelle élément du web. Elle est composée de 3 parties :

```shell
<protocole>://<serveur>[:port]/<ressource>[ ? <requête> ] [#<lien>]
```

{% endnote %}

Ce qui donne pour l'url <https://fr.wikipedia.org/wiki/Uniform_Resource_Locator> :

* le *protocole* est `https`
* le *serveur* est  `fr.wikipedia.org`
* la *ressource* est  `wiki/Uniform_Resource_Locator`

Le boulot d'un navigateur pour une url `protocole://serveur/ressource` donnée est alors :

1. de récupérer la `ressource` sur le `serveur` en utilisant le protocole `protocole`
2. d'interpréter la ressource récupérée pour l'afficher (c'est souvent du [html](https://fr.wikipedia.org/wiki/Hypertext_Markup_Language))

## Protocole

Le protocole d'une url est le moyen d'accéder à une ressource. Dans le web, il y a essentiellement 3 protocoles d'utilisé :

* [http](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol) : permet d'envoyer et de recevoir des fichiers. Généralement des fichiers textes. Exemple : <http://www.csszengarden.com/>
* [https](https://fr.wikipedia.org/wiki/HyperText_Transfer_Protocol_Secure): le même qu'avant mais de façon sécurisé (le "s" veut dire "secure"). Exemple : <https://www.google.com/>
* **file** : permet d'accéder à un fichier de l'ordinateur. Le chemin est alors le [chemin absolu]({{ "/tutoriels/fichiers-navigation" }}#absolu-relatif) vers votre fichier. Exemple : `file:///Users/fbrucker/Documents/web/exemple.html`

{% info %}
Il est plus difficile de créer un serveur web supportant le https que celui supportant le http. C'est pourquoi vos serveur à vous seront quasi-exclusivement non sécurisé.
{% endinfo %}

## Serveur

Le serveur est l'adresse internet de l'ordinateur sur lequel la ressource est stockée. Cela peut être :

* un nom comme `fr.wikipedia.org`
* une [adresse IP](https://fr.wikipedia.org/wiki/Adresse_IP) comme `62.40.98.186`
* Il n'y a pas de serveur lorsque l'on utilise le protocole file, c'est pourquoi les url utilisant le protocole file commencent toujours par `file:///`

{% info %}
Une machine ne comprenant que les nombres, à chaque nom est associé une adresse IP grâce à un annuaire que l'on appelle [DNS](https://fr.wikipedia.org/wiki/Domain_Name_System). A chaque adresse IP peut donc être associé un ou plusieurs noms.
{% endinfo %}

Parmi toutes les adresses et les noms, il en existe deux qui signifient **toujours** la machine actuelle :

* le nom : `localhost`
* l'adresse IP : `127.0.0.1`

{% note %}
Il n'est pas nécessaire d'être accordé au réseau pour résoudre l'adresse `localhost` et `127.0.0.1`. Elles sont souvent utilisées lorsque l'on crée ses propres serveur web
{% endnote %}

## Ressource

La ressource est ensuite déterminée par le serveur et est envoyée au demandeur, c'est à dire le navigateur.

Dans le cadre d'une page web, cette ressource sera pourra être :

* du [html](https://fr.wikipedia.org/wiki/Hypertext_Markup_Language) : la structure de la page
* du [css](https://fr.wikipedia.org/wiki/Feuilles_de_style_en_cascade) : le style de la page
* du [javascript](https://fr.wikipedia.org/wiki/JavaScript) : qui gère les interactions avec l'utilisateur
* une image
* des données décrite au format [json](https://www.json.org/json-fr.html)
* ...

## <span id="port"></span> Port

Dans le schéma d'une url, la machine sur sur laquelle on va chercher la ressource est identifiée par deux composantes, le serveur et le port :

```shell
<protocole>://<serveur>[:port]
```

En effet, une machine sur internet peut avoir plusieurs utilisations. Pour séparer chacune de ses utilisation, on associe un [un port](https://fr.wikipedia.org/wiki/Port_(logiciel)) à chacune d'elle : l'url est alors de la forme `protocole://serveur:port/ressource`).

Chaque protocole a cependant un port par défaut qui est utilisé s'il aucun port n'est précisé. Par exemple, le port par défaut du protocole https est le 443 et donc les urls `https://www.google.fr` et `https://www.google.fr:443` sont identiques.

{% faire %}
Essayez d'atteindre avec chrome les 2 urls : `https://www.google.fr` et `https://www.google.fr:443`. Que donne l'url  `https://www.google.fr:8080` ? A priori elle ne fonctionne pas car la roue tourne mais ne s'arrête pas.
{% endfaire %}

{% note %}

Chaque machine possède [$2^16$ port](https://fr.wikipedia.org/wiki/Port_(logiciel)) dont certains sont utilisés par le système (de 1 à 1023) et ne doivent pas être utilisé par les utilisateurs, les autres sont libres d'être utilisés pour nos serveurs.

[Liste ds port communément utilisés](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)

{% endnote %}

{% attention %}
Bien que libres certains ports sont usuellement utilisés par certains protocoles.
{% endattention %}
