---
layout: layout/post.njk

title: Web
tags: ['cours', 'web', 'front', 'back']
authors:
    - "François Brucker"

date: 2026-01-08

eleventyNavigation:
    prerequis:
        - "/cours/coder-et-développer/ordinateur-développement/"

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"

---

<!-- début résumé -->

Cours de développement web. On y verra la partie front, le back, la gestion d'une API.

<!-- fin résumé -->

## URL ?

Différence entre exécuter un fichier soit et sur un serveur.

{% aller %}
[Bases de réseau](/cours/système-et-réseau/bases-réseau/)
{% endaller %}

## <span id="trinité"><span>  Trinité html/css/js

### Découverte d'html

1. Introduction avec les [outils de développement](./outils-de-développement/)
2. [Introduction à html](./html-introduction) chez soit dans un seul fichier
3. [Projet html](./projet-html)

### Découverte de css

1. [Introduction à css](./css-introduction)
2. [Unités et couleurs](./unités-couleurs)
3. [Sélecteurs css](./sélecteurs-css)
4. [modèle de boîtes](./modèle-boites)
5. [balise anonymes](./balises-anonymes)
6. [positionnement](./positionnement)
7. [Projet css](./projet-css)
8. flex + grid (TBD)

> - ajouter animations et fin css de ce cours <https://web.dev/learn/css/>{.externe}
> - TBD à présenter :
>   - flex + grid
>   - bootstrap

### Gestion des fichiers

{% lien %}
<https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files>{.externe}
{% endlien %}

Ayez :

1. un dossier spécifique où vous rangez tout votre site
2. à l'intérieur de ce dossier, le fichier `index.html`{.fichier} est l'entrée de votre site
3. ayez des dossiers spécifiques pour ranger les différents types de fichiers que vous utiliserez

{% note %}
Utilisez **toujours** des chemins relatifs lorsque vous référencez vos fichiers.
{% endnote %}

### Bibliothèques css

<https://getbootstrap.com/>{.externe}

Comment :

- cdn
- téléchargement des fichiers
- node_modules (npm pour gérer des paquets et utilisation de npm sans node pour le front)

Si vous avez des soucis avec l'exécution des scripts powershell :
<https://www.it-connect.fr/autoriser-lexecution-de-scripts-powershell/>{.externe}

Modifier votre page animal préféré avec bootstrap

### Découverte de Javascript

1. [Bases de javascript](./javascript-bases)
2. [Manipuler l'arbre DOM en javascript](./javascript-dom)
3. [gestion des événements](./javascript-événements)

{% faire %}
[Projet Numérologie](./projet-numérologie), faire [le niveau 1 de la partie 1](./projet-numérologie/partie-1-front/niveau-1/).
{% endfaire %}

> - à faire : partie 1 niveau 2 et changer la lib css par bootstrap. A présenter sur le site perso
> - éxo à présenter : js avec node. <https://www.w3schools.com/js/js_graphics_d3js.asp>{.externe}

## Projet front

{% aller %}
[Projet front](projet-front)
{% endaller %}

## <span id="serveur"><span> Serveur web

### Bases de réseau

Avant de vous langer dans la création de serveurs web, commençons par dégrossir un peut la notion de réseau et de protocole.

{% aller %}
Lisez jusqu'à port logiciel le cours sur [les Bases de réseau](/cours/système-et-réseau/réseau/)
{% endaller %}

{% faire %}
Avec le serveur local de la partie front, ouvrez [un Wireshark](https://www.wireshark.org/){.externe} et regardez le flux réseau sur le loopback.
{% endfaire %}

### Créer un serveur web

{% aller %}
[Serveur web](./serveur-web)
{% endaller %}

à faire : décathlon, faire un client/serveur : tous

## Gestion des données

### Lecture asynchrone

La lecture de donnée est un processus asynchrone et doit être traité avec des promesses :

{% aller %}
[Lecture asynchrone de fichiers](./lire-données)
{% endaller %}

La suite du projet numérologie qui intègre une route et échange des données avec le serveur.

{% faire %}
[Projet Numérologie partie 2](projet-numérologie/partie-2-serveur/).
{% endfaire %}

### <span id="données"><span> Gestion de données Serveur

{% aller %}

[côté serveur](./gestion-données-serveur)

{% endaller %}

{% aller %}

[utilisation de bases de données](./bases-de-données)

{% endaller %}

{% faire %}
[Projet Numérologie partie 3](./projet-numérologie/partie-3-données/).
{% endfaire %}

### <span id="données"><span> Gestion de données Clients

{% aller %}

1. [côté client](./gestion-données-client)
2. [cookies](./gestion-données-cookies)

{% endaller %}

## Projets

Les projets de cette partie ont vocation à :

- illustrer le cours
- apporter des bonnes pratique de développement
- montrer des astuces et autres utilisation adéquates de structures de code

### A vous : Décathlon

- règles :
  - sur le site du créateur : <https://www.knizia.de/wp-content/uploads/reiner/freebies/Website-Decathlon.pdf>{.externe}
  - en français : <http://www.jeuxprintandplay.fr/Fiches%20jeux/Fiche%20jeu%20Decathlon.html>{.externe}
- supports pour y jouer en vrai : <http://juegosrollandwrite.com/remake-reiner-knizias-decathlon/>{.externe}

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
> - pré-processeur : less /SCSS
> - post-processeur : postcss (exemple de tailwindcss)
> - packageur front.
> - générateur de front (eleventy)
> - angular/vue/...
