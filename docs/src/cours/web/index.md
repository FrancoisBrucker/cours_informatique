---
layout: layout/post.njk

title: Web
tags: ['cours', 'web', 'front', 'back']
authors:
    - "François Brucker"

eleventyNavigation:
  key: "Web"
  parent: "Cours"
---

<!-- début résumé -->

Cours de développement web. On y verra la partie front, le back, la gestion d'une API.

<!-- fin résumé -->
{% prerequis %}

* [Avoir un système en état de marche]({{ '/tutoriels/installation-système'  }})
* [Savoir naviguer dans un système de fichiers]({{ '/tutoriels/fichiers-navigation'  }})
* [Installation et prise en main de l'éditeur de texte vsc]({{ '/tutoriels/vsc-installation-et-prise-en-main'  }})
* Il pourra de plus être très utile de :
  * [Savoir ouvrir une fenêtre terminal]({{ '/tutoriels/terminal'   }})
  * [D'installez brew si vous êtes sous mac]({{ '/tutoriels/brew'   }})

{% endprerequis %}

## <span id="trinité"><span>  Trinité html/css/js

### Découverte d'html

1. Introduction avec les [outils de développement](./outils-de-développement/){.interne}
2. [Introduction à html](./html-introduction){.interne} chez soit dans un seul fichier
3. Différence entre exécuter un fichier soit et sur un serveur : [Qu'est qu'une url ?](./anatomie-url){.interne}
4. [Projet html](./projet-html){.interne}

### Découverte de css

1. [Introduction à css](./css-introduction){.interne}
2. [Unités et couleurs](./unités-couleurs){.interne}
3. [Sélecteurs css](./sélecteurs-css){.interne}

> TBD :
>
> * animations
> * fontes (à refaire avec la nouvelle api)

### Gestion des fichiers

{% lien %}
<https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files>
{% endlien %}

Ayez :

1. un dossier spécifique où vous rangez tout votre site
2. à l'intérieur de ce dossier, le fichier `index.html`{.fichier} est l'entrée de votre site
3. ayez des dossiers spécifiques pour ranger les différents types de fichiers que vous utiliserez

{% note %}
Utilisez **toujours** des chemins relatifs lorsque vous référencez vos fichiers.
{% endnote %}

### Boîtes et positionnement

1. [modèle de boîtes](./modèle-boites){.interne}
2. [balise anonymes](./balises-anonymes){.interne}
3. [positionnement](./positionnement){.interne}

> TBD :
>
> * à présenter : flex + grid
> * exercice à présenter : design de page

### Bibliothèques css

* exercice à présenter

exercices : bibliothèque css. Utilisation avec un cdn.

* bootstrap
* lib à la mode en 2022
* ...

Comment :

* cdn
* téléchargement des fichiers (on verra plus tard comment faire mieux avec npm)
* node_modules (npm pour gérer des paquets et utilisation de npm sans node pour le front)

### Javascript

1. [Bases de javascript](./javascript-bases){.interne}
2. [Manipuler l'arbre DOM en javascript](./javascript-dom){.interne}
3. [gestion des événements](./javascript-événements){.interne}

{% faire %}
[Projet Numérologie](./projet-numérologie){.interne}, faire la partie 1.
{% endfaire %}

## <span id="serveur"><span> Serveur web

1. [Lire des données](./lire-données){.interne}
2. [Serveur web](./serveur-web){.interne}

{% faire %}
[Projet Numérologie partie 2](projet-numérologie/partie-2-serveur/){.interne}.
{% endfaire %}

à faire : décathlon, faire un client/serveur : tous

## <span id="données"><span> Gestion de données Serveur

1. [côté serveur](./gestion-données-serveur){.interne}
2. [utilisation de bases de données](./bases-de-données){.interne}

{% faire %}
[Projet Numérologie partie 3](./projet-numérologie/partie-3-données/){.interne}.
{% endfaire %}

## <span id="données"><span> Gestion de données Clients

1. [côté client](./gestion-données-client){.interne}
2. [cookies](./gestion-données-cookies){.interne}

## Projets

Les projets de cette partie ont vocation à :

* illustrer le cours
* apporter des bonnes pratique de développement
* montrer des astuces et autres utilisation adéquates de structures de code

### A vous : Décathlon

* règles :
  * sur le site du créateur : <https://www.knizia.de/wp-content/uploads/reiner/freebies/Website-Decathlon.pdf>
  * en français : <http://www.jeuxprintandplay.fr/Fiches%20jeux/Fiche%20jeu%20Decathlon.html>
* supports pour y jouer en vrai : <http://juegosrollandwrite.com/remake-reiner-knizias-decathlon/>

Choisissez un sport et faite toute la partie jet de dés côté serveur pour éviter la triche.
Ne stockez pas de données côté serveur.

Certains présenteront la fois d'après.

### Numérologie

{% aller %}
[Projet Numérologie](projet-numérologie)
{% endaller %}

Ce projet en 5 parties (dont les 3 premières sont des support applicatif du cours) vous montrent la création complète d'un petit site web avec une partie front, une partie back et des données.

### Commentaires

> TBD : à mettre en œuvre

## Pour aller plus loin

> TBD :
>
> * pré-processeur : less /SCSS
> * post-processeur : postcss (exemple de tailwindcss)
> * packageur front.
> * générateur de front (eleventy)
> * angular/vue/...
