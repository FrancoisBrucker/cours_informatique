---
layout: page
title:  "Projet commentaires : partie 4"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 4]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/index.md %})
{.chemin}


> TBD
> A refaire.
> ne garder que la partie sqlite et faire attention à windows avec le changement de path
{.note}

## sqlite

Comme nous allons utiliser une base de données, on vous demande d'installer [sqlite](https://www.sqlite.org/index.html) sur votre système. C'est une base de données sql qui fonctionne sans serveur et sauve les données sur le disque. Ne l'utilisez en production que pour de *petites* applications ou pour vos tests. 

> Il se peu que si vous utilisez sqlite sous mac, le système vous empêche de l'exécuter. Dans ce cas là, allez dans *préférences > sécurité et confidentialité > général* et choisissez autoriser quand même à côté de la requête sqlite (vous devrez certainement déverrouiller le cadenas pour le faire).
{.attention}

### installation sqlite

{% details sous linux %}
`apt-get install sqlite3 libsqlite3-dev`
{% enddetails %}

{% details sous mac %}
`brew install sqlite`

N'oubliez pas d'installer [brew](https://brew.sh/index_fr), c'est super bien.
{% enddetails %}

{% details sous windows %}
Sur la page de [download de sqlite](https://www.sqlite.org/download.html) choisissez la section *Precompiled Binaries for Windows* et récupérez les tools.

Il faudra ensuite modifier le path pour qu'il intègre le chemin de votre fichier sqlite3.exe
<https://java.com/fr/download/help/path_fr.html>

{% enddetails %}

### on vérifie que ça fonctionne

Dans terminal, tapez la commande `sqlite3`. Vous devriez rentrer dans un interpréteur SQL.
Tapez ensuite `.exit` pour en sortir.

## plan

1. [modèle de données]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/1-modele.md %}) pour l'envoi
2. [intégration au serveur]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/2-db-config.md %})
3. [routes]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/3-routes.md %})
