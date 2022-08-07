---
layout: page
title:  "anatomie d'une url"
category: tutorial
tags: web
authors : 
  - "François Brucker"
---




Une [url (Uniform Resource Locator)](https://fr.wikipedia.org/wiki/Uniform_Resource_Locator) est un moyen de retrouver n'importe quelle élément du web. Elle est composée de 3 parties : 
```
protocole://serveur/ressource 
```

Ce qui donne pour l'url <https://fr.wikipedia.org/wiki/Uniform_Resource_Locator> :
* le *protocole* est **`https`**
* le *serveur* est  **`fr.wikipedia.org`**
* la *ressource* est  **`wiki/Uniform_Resource_Locator`**

Le boulot d'un navigateur pour une url `protocole://serveur/ressource` donnée est alors :
1. de récupérer la `ressource` sur le `serveur` en utilisant le `protocole`
2. d'interpréter la ressource récupérée pour l'afficher (c'est souvent du [html](https://fr.wikipedia.org/wiki/Hypertext_Markup_Language))

> Ne confondez pas une [url ((Uniform Resource Locator))](https://fr.wikipedia.org/wiki/Uniform_Resource_Locator) avec une de ses deux soeurs que sont les [uri (Uniform Resource Identifier)](https://fr.wikipedia.org/wiki/Uniform_Resource_Identifier) et les [urn (Uniform Resource Name)](https://fr.wikipedia.org/wiki/Uniform_Resource_Name). Elles se ressemblent mais ne font pas la même chose.
{.attention}

## protocole

Le protocole d'une url est le moyen d'accéder à une ressource. Dans le web, il y a essentiellement 2 protocoles d'utilsé : 
* [http](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol) : permet d'envoyer et de recevoir des fichiers. Généralement des fichiers textes.
* [https](https://fr.wikipedia.org/wiki/HyperText_Transfer_Protocol_Secure) : le même qu'avant mais de façon sécurisé (le "s" veut dire "secure"). 

> Il est plus difficile de créer un serveur web supportant le https que celui supportant le http. C'est pourquoi vos serveur à vous seront quasi-exclusivement non sécurisé.


> TBD : envoyer vers un cours détaillé avec :
> * faire du telnet
> * RFC
> * autre protocole (genre envoyer un mail ?)
{.note}


## serveur

Le serveur est l'adresse internet de l'ordinateur sur lequel la ressource est stockée. Cela peut être : 
* un nom comme `fr.wikipedia.org`
* une [adresse IP](https://fr.wikipedia.org/wiki/Adresse_IP) comme `62.40.98.186`

> Une machine ne comprenant que les nombres, à chaque nom est associé une adresse IP grâce à un annuaire que l'on appelle [DNS](https://fr.wikipedia.org/wiki/Domain_Name_System). A chaque adresse IP peut donc être associé un ou plusieurs noms.

Parmi toutes les adresses et les noms, il en existe deux qui signifient **toujours** la machine actuelle :
* le nom : `localhost`
* l'adresse IP : `127.0.0.1`

> Ce n'est pas la peine d'être accordé au réseau pour résoudre l'adresse `localhost` et `127.0.0.1`. Elles sont souvent utilisées lorsque l'on crée ses propres serveur web (on le verra dans la partie [back]({% link cours/web/back/index.md %}) du cours)


Enfin, une machine sur internet peut avoir plusieurs utilisations. Pour séparer chacune de ses utilisation, on associe un [un port](https://fr.wikipedia.org/wiki/Port_(logiciel)) à chacune d'elle : l'url est alors de la forme `protocole://serveur:port/ressource`). 

Chaque protocole a cependant un port par défaut qui est utilisé s'il aucun port n'est précisé. Par exemple, le port par défaut du protocole https est le 443 et donc les urls `https://www.google.fr` et `https://www.google.fr:443` sont identiques. 


> Essayez d'atteindre avec chrome les 2 urls : `https://www.google.fr` et `https://www.google.fr:443`. Que donne l'url  `https://www.google.fr:8080` ? A priori elle ne fonctionne pas car la roue tourne mais ne s'arrête pas.



> TBD : envoyer vers un cours détaillé avec : 
> * port
> * login
> * numéro ou nom avec dns traceroute
> * démon
{.note}

## ressource

La ressource est ensuite déterminée par le serveur et est envoyée au demandeur, c'est à dire le navigateur. 

Dans le cadre d'une page web, cette ressource sera pourra être : 
* du [html](https://fr.wikipedia.org/wiki/Hypertext_Markup_Language) : la structure de la page
* du [css](https://fr.wikipedia.org/wiki/Feuilles_de_style_en_cascade) : le style de la page
* du [javascript](https://fr.wikipedia.org/wiki/JavaScript) : qui gère les interactions avec l'utilisateur
* une image

Mais cela peut être ce que l'on veut. 


> TBD : envoyer vers un cours détaillé avec : 
> * autre type de fichier
> * curl
> * un serveur en python avec des fichiers en chroot.
> * header
> * post/get
{.note}