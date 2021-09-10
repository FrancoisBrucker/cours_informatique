---
layout: page
title:  "Projet numérologie : niveau 1"
category: cours
author: "François Brucker"
---


> TBD : en chantier
{: .note}

## but du site

On aimerait pouvoir créer un site de numérologie qui associerait à chaque prénom un chiffre. Comme les publications scientifiques sur ce sujet (comme [là](https://www.parents.fr/prenoms/nos-conseils-prenoms/la-numerologie-des-prenoms-diaporama-307570), [ici](https://www.femmeactuelle.fr/horoscope2/numerologie/numerologie-prenom-19618) ou [encore ceci](https://www.evozen.fr/numerologie/expression)) sont discordantes, nous allons créer le nôtre.


> But : associer un chiffre à toute chaine de caractère en [unicode](https://unicode-table.com/fr/


## prérequis

Avant de se lancer à corps perdu dans le développement et le code, vérifions que nous avons tous les outils nécessaires.

### outils développement

* Il nous faut un éditeur de texte. J'utilise [vscode](https://code.visualstudio.com/), téléchargez le et installez le.
* Il nous faut du javascript. On utilisera [node](https://nodejs.org/en/) : téléchargez le et installez le en [suivant le tuto]({% link cours/web/js/bases.md %}#bloc-id-installation-node). 
* nous utiliserons le terminal, donc jetez un oeil au [tuto terminal]({% post_url tutos/systeme/2021-08-24-terminal %}) pour pouvoir le dégainer à l'envie.

## plan

En quatre parties et autant de cours

1. [un premier site entièrement en front]({% link cours/web/projets/numerologie/niveau-1/cours-1-front/index.md %})
2. on ajoute une partie back pour les calculs
3. on polie tout ça avec des routes différentes
4. on ajoute la possibilités de stocker des données

### back 

> TBD : requete post et get
> ne pas s'emèler les pinceaux avec le node_module du back et du front
{: .note}

### routes

 cookies ?

### données

sequilize et compagnie avec sqlite.