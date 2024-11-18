---
layout: layout/post.njk

title: Web
tags: ['cours', 'web', 'front', 'back']
authors:
    - "François Brucker"

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
[Qu'est qu'une url](./anatomie-url){.interne}
{% endaller %}

## <span id="trinité"><span>  Trinité html/css/js

### Découverte d'html

1. Introduction avec les [outils de développement](./outils-de-développement/){.interne}
2. [Introduction à html](./html-introduction){.interne} chez soit dans un seul fichier
3. [Projet html](./projet-html){.interne}

### Découverte de css

1. [Introduction à css](./css-introduction){.interne}
2. [Unités et couleurs](./unités-couleurs){.interne}
3. [Sélecteurs css](./sélecteurs-css){.interne}
4. [modèle de boîtes](./modèle-boites){.interne}
5. [balise anonymes](./balises-anonymes){.interne}
6. [positionnement](./positionnement){.interne}
7. [Projet css](./projet-css){.interne}
8. flex + grid (TBD)

> - ajouter animations et fin css de ce cours <https://web.dev/learn/css/>
> - TBD à présenter :
>   - flex + grid
>   - bootstrap

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

### Bibliothèques css

<https://getbootstrap.com/>

Comment :

- cdn
- téléchargement des fichiers
- node_modules (npm pour gérer des paquets et utilisation de npm sans node pour le front)

Si vous avez des soucis avec l'exécution des scripts powershell :
<https://www.it-connect.fr/autoriser-lexecution-de-scripts-powershell/>

Modifier votre page animal préféré avec bootstrap

### Découverte de Javascript

1. [Bases de javascript](./javascript-bases){.interne}
2. [Manipuler l'arbre DOM en javascript](./javascript-dom){.interne}
3. [gestion des événements](./javascript-événements){.interne}

{% faire %}
[Projet Numérologie](./projet-numérologie){.interne}, faire [le niveau 1 de la partie 1](./projet-numérologie/partie-1-front/niveau-1/){.interne}.
{% endfaire %}

> - à faire : partie 1 niveau 2 et changer la lib css par bootstrap. A présenter sur le site perso
> - éxo à présenter : js avec node. <https://www.w3schools.com/js/js_graphics_d3js.asp>

## Projet front

{% aller %}
[Projet front](projet-front){.interne}
{% endaller %}

## <span id="serveur"><span> Serveur web

### Bases de réseau

Avant de vous langer dans la création de serveurs web, commençons par dégrossir un peut la notion de réseau et de protocole.

{% aller %}
Lisez jusqu'à port logiciel le cours sur [les Bases de réseau](/cours/système-et-réseau/réseau/){.interne}
{% endaller %}

{% faire %}
Avec le serveur local de la partie front, ouvrez [un Wireshark](https://www.wireshark.org/) et regardez le flux réseau sur le loopback.
{% endfaire %}

### Créer un serveur web

{% aller %}
[Serveur web](./serveur-web){.interne}
{% endaller %}

à faire : décathlon, faire un client/serveur : tous

## Gestion des données

### Lecture asynchrone

La lecture de donnée est un processus asynchrone et doit être traité avec des promesses :

{% aller %}
[Lecture asynchrone de fichiers](./lire-données){.interne}
{% endaller %}

La suite du projet numérologie qui intègre une route et échange des données avec le serveur.

{% faire %}
[Projet Numérologie partie 2](projet-numérologie/partie-2-serveur/){.interne}.
{% endfaire %}

### <span id="données"><span> Gestion de données Serveur

> TBD parler d'une requête http : header/type/body
> TBD fetch : dire que c'est une fonction distante et donc asynchrone ; lier json / faire un await puis un then en v2 et dire que l'on essaie de faire ça en vrai

{% aller %}

[côté serveur](./gestion-données-serveur){.interne}

{% endaller %}

{% aller %}

[utilisation de bases de données](./bases-de-données){.interne}

{% endaller %}

{% faire %}
[Projet Numérologie partie 3](./projet-numérologie/partie-3-données/){.interne}.
{% endfaire %}

### <span id="données"><span> Gestion de données Clients

{% aller %}

1. [côté client](./gestion-données-client){.interne}
2. [cookies](./gestion-données-cookies){.interne}

{% endaller %}

## Projets

Les projets de cette partie ont vocation à :

- illustrer le cours
- apporter des bonnes pratique de développement
- montrer des astuces et autres utilisation adéquates de structures de code

### A vous : Décathlon

- règles :
  - sur le site du créateur : <https://www.knizia.de/wp-content/uploads/reiner/freebies/Website-Decathlon.pdf>
  - en français : <http://www.jeuxprintandplay.fr/Fiches%20jeux/Fiche%20jeu%20Decathlon.html>
- supports pour y jouer en vrai : <http://juegosrollandwrite.com/remake-reiner-knizias-decathlon/>

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
