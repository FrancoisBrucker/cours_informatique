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

Ce projet vise à découvrir les bases du développement de serveur web. On ne présuppose aucune connaissance en html/css ou javascript, mais il pourra être utile de voir les tutoriels spécifiques du [cours général]({{"/cours/web/" | url}}) après avoir rencontré les notions ici pour aller plus loin.

<!-- fin résumé -->

Le principe est de refaire plusieurs fois ce projet, en ajoutant petit à petit des notions de plus en plus perfectionnées de développement web.

## dépôt github

<https://github.com/FrancoisBrucker/numerologie>

## but du site

On aimerait pouvoir créer un site de numérologie qui associerait à chaque prénom un chiffre. Comme les publications scientifiques sur ce sujet (comme [là](https://www.parents.fr/prenoms/nos-conseils-prenoms/la-numerologie-des-prenoms-diaporama-307570), [ici](https://www.femmeactuelle.fr/horoscope2/numerologie/numerologie-prenom-19618) ou [encore ceci](https://www.evozen.fr/numerologie/expression)) sont discordantes, nous allons créer le nôtre.

{% note "**But :**" %}
Associer un chiffre à toute chaîne de caractère en [Unicode](https://unicode-table.com/fr/)
{% endnote %}

## Plan

Ce projet va être séparé en trois parties, un jardinage final du code puis une introduction aux tests unitaires :

1. [un premier site entièrement en front](./partie-1-front)
2. [on ajoute une partie back pour les calculs](./partie-2-serveur)
3. [gestion des données](./partie-3-donnees)
4. [jardinage](./partie-4-jardinage) du code pour le rendre plus propre
5. [Introductions aux tests unitaires et aux tests fonctionnels](./partie-5-tests)

## déploiement

> TBD
>
> * Local : différence entre fichier et via node.  [cors](https://developer.mozilla.org/fr/docs/Web/HTTP/CORS)
> * sur le serveur de l'école sans node (cyberduck/scp/git)
> * sur l'ovh : scp/git
