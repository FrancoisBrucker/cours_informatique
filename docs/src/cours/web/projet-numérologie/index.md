---
layout: layout/post.njk
title: "Projet numérologie"

authors:
    - "François Brucker"

eleventyNavigation:
  key: "Projet numérologie"
  parent: "Web"
---

<!-- début résumé -->

Ce projet vise à découvrir les bases du développement de serveur web. On ne présuppose aucune connaissance en html/css ou javascript, mais il pourra être utile de voir les tutoriels spécifiques du [cours général]({{"/cours/web/" }}) après avoir rencontré les notions ici pour aller plus loin.

<!-- fin résumé -->

Le principe est de refaire plusieurs fois ce projet, en ajoutant petit à petit des notions de plus en plus perfectionnées de développement web.

## But du site

On aimerait pouvoir créer un site de numérologie qui associerait à chaque prénom un chiffre. Comme les publications scientifiques sur ce sujet (comme [là](https://www.parents.fr/prenoms/nos-conseils-prenoms/la-numérologie-des-prenoms-diaporama-307570), [ici](https://www.femmeactuelle.fr/horoscope2/numérologie/numérologie-prenom-19618) ou [encore ceci](https://www.evozen.fr/numérologie/expression)) sont discordantes, nous allons créer le nôtre.

{% note "**But**" %}
Associer un chiffre à toute chaîne de caractère en [Unicode](https://unicode-table.com/fr/)
{% endnote %}

Avant de se lancer à corps perdu dans le développement et le code, vérifions que nous avons (enfin, surtout vous avez) tous les outils nécessaires :

1. et c'est le plus important **la bonne attitude** :
   * si vous ne connaissez rien : ne cédez pas à la facilité de copier/coller sans comprendre : c'est *bad karma* et ça vous rattrapera tôt ou tard. La magie — tout du moins en informatique — n'existe pas (et je suis le premier à le déplorer) : si ça fonctionne sans que vous savez au moins superficiellement pourquoi, c'est que ça n'a que l'air de fonctionner.
   * si vous connaissez déjà tout ça : faite-le tout de même cela vous permettra de suivre plus facilement les niveaux ultérieurs
2. **un cerveau** en état de marche : pour voir les correspondances, lire la doc, et poser des questions.
3. avoir **un éditeur de texte** fonctionnel. Nous utiliserons [vscode](https://code.visualstudio.com/) dans ce cours, téléchargez le et installez le.
4. un **navigateur internet** munis d'outils de développement. Tous les exemple seront fait avec [chrome](https://www.google.fr/chrome/).
5. Sachez ouvrir [une fenêtre terminal]({{"/tutoriels/terminal" }})
6. un interpréteur javascript. On utilisera [node](https://nodejs.org/en/).

## Installation de Node

{% details "sous Linux" %}
Vous pouvez utiliser [nodesource](https://github.com/nodesource/distributions/blob/master/README.md) pour installer node.
{% enddetails %}

{% details "sous Mac" %}
Comme dit dans le tuto d'installation, on utilise le gestionnaire de package [brew](https://brew.sh/).

Une fois celui ci installé, on tape dans un [terminal]({{"/tutoriels/terminal" }}) la commande : `brew install node`
{% enddetails %}

{% details "sous Windows" %}
Vous téléchargez la version courante de node : <https://nodejs.org/en/download/current/>.
{% enddetails %}

{% attention %}
Il existe 2 versions de [Node](https://nodejs.org/en/), la *LTS (long term support)* et la *current*. On choisira la version *current* qui est la plus récente. La version *LTS* est là pour des raisons de compatibilité.
{% endattention %}

## Plan

Ce projet va être séparé en cinq parties :

1. [un premier site entièrement en front](./partie-1-front){.interne}
2. [on ajoute une partie back pour les calculs](./partie-2-serveur){.interne}
3. [gestion des données](./partie-3-données){.interne}
4. [jardinage du code pour le rendre plus propre](./partie-4-jardinage){.interne}
5. [Maintenance du site](./partie-5-maintenance){.interne}

## Déploiement

> TBD
>
> * Local : différence entre fichier et via node.  [cors](https://developer.mozilla.org/fr/docs/Web/HTTP/CORS)
> * sur le serveur de l'école sans node (cyberduck/scp/git)
> * sur l'ovh : scp/git
