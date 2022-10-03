---
layout: layout/post.njk
title: "Projet numérologie / partie 1 : front"

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Projet numérologie / partie 1 : front"
  parent: "Projet numérologie"
---

<!-- début résumé -->

Numérologie partie 1. On prépare notre site en créant tout ce qui est nécessaire et en le faisant fonctionner en *front*.

<!-- fin résumé -->

Avant de se lancer à corps perdu dans le développement et le code, vérifions que nous avons (enfin, surtout vous avez) tous les outils nécessaires :

1. et c'est le plus important **la bonne attitude** :
   * si vous ne connaissez rien : ne cédez pas à la facilité de copier/coller sans comprendre : c'est *bad karma* et ça vous rattrapera tôt ou tard. La magie — tout du moins en informatique — n'existe pas (et je suis le premier à le déplorer) : si ça fonctionne sans que vous savez au moins superficiellement pourquoi, c'est que ça n'a que l'air de fonctionner.
   * si vous connaissez déjà tout ça : faite-le tout de même cela vous permettra de suivre plus facilement les niveaux ultérieurs
2. **un cerveau** en état de marche : pour voir les correspondances, lire la doc, et poser des questions.
3. avoir **un éditeur de texte** fonctionnel. Nous utiliserons [vscode](https://code.visualstudio.com/) dans ce cours, téléchargez le et installez le.
4. un **navigateur internet** munis d'outils de développement. Tous les exemple seront fait avec [chrome](https://www.google.fr/chrome/).
5. Sachez ouvrir [une fenêtre terminal]({{"/tutoriels/terminal" | url}})
6. un interpréteur javascript. On utilisera [node](https://nodejs.org/en/).

## Installation de Node

{% details "sous Linux" %}
Vous pouvez utiliser [nodesource](https://github.com/nodesource/distributions/blob/master/README.md) pour installer node.
{% enddetails %}

{% details "sous Mac" %}
Comme dit dans le tuto d'installation, on utilise le gestionnaire de package [brew](https://brew.sh/).

Une fois celui ci installé, on tape dans un [terminal]({{"/tutoriels/terminal" | url}}) la commande : `brew install node`
{% enddetails %}

{% details "sous Windows" %}
Vous téléchargez la version courante de node : <https://nodejs.org/en/download/current/>.
{% enddetails %}

{% attention %}
Il existe 2 versions de [Node](https://nodejs.org/en/), la *LTS (long term support)* et la *current*. On choisira la version *current* qui est la plus récente. La version *LTS* est là pour des raisons de compatibilité.
{% endattention %}

## Niveaux

Cette partie est organisée en niveaux. Chaque niveau refait la partie en ajoutant à chaque fois des outils de développements/code de plus en plus perfectionnés. Il est recommandé de faire tous les niveaux.

1. [niveau 1](./niveau-1) : utilisation d'un éditeur de texte et bases du développement html/css/js
2. [niveau 2](./niveau-2) : ajoute d'outils de gestion de projets
3. [niveau 3](./niveau-3) : ajout de la gestion des sources avec l'application desktop de github et mise en production avec un logiciel de transfert de fichier
4. [niveau 4](./niveau-4) : ajout de la gestion des sources et mise en production sur un site distant avec le terminal.
