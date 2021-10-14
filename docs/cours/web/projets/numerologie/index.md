---
layout: page
title:  "Projet numérologie"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %})
{: .chemin}

Ce projet vise à découvrir les bases du développement de serveur web. On ne présuppose aucune connaissance en html/css ou javascript, mais il pourra être utile de voir les tutoriels spécifiques du [cours général]({% link cours/web/index.md %}) après avoir rencontré les notions ici pour aller plus loin.

Le principe est de refaire plusieurs fois ce projet, en ajoutant petit à petit des notions de plus en plus perfectionnées de développement web.

## dépôt github

<https://github.com/FrancoisBrucker/numerologie>

## but du site

On aimerait pouvoir créer un site de numérologie qui associerait à chaque prénom un chiffre. Comme les publications scientifiques sur ce sujet (comme [là](https://www.parents.fr/prenoms/nos-conseils-prenoms/la-numerologie-des-prenoms-diaporama-307570), [ici](https://www.femmeactuelle.fr/horoscope2/numerologie/numerologie-prenom-19618) ou [encore ceci](https://www.evozen.fr/numerologie/expression)) sont discordantes, nous allons créer le nôtre.

> But : associer un chiffre à toute chaine de caractère en [Unicode](https://unicode-table.com/fr/)

## Plan

Ce projet va être séparé en trois parties :

1. [un premier site entièrement en front]({% link cours/web/projets/numerologie/partie-1-front/index.md %})
2. [on ajoute une partie back pour les calculs]({% link cours/web/projets/numerologie/partie-2-serveur/index.md %})
3. [Introductions aux tests unitaires et fonctionnels]()

## déploiement

> TBD
>
> * Local : différence entre fichier et via node.  [cors](https://developer.mozilla.org/fr/docs/Web/HTTP/CORS)
> * sur le serveur de l'école sans node (cyberduck/scp/git)
> * sur l'ovh : scp/git
