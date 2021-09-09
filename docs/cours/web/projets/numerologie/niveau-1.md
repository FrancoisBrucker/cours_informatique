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

On va lister :
* les user stories (def)
* tests fonctionnels
* les tests unitaires

## prérequis

Avant de se lancer à corps perdu dans le développement et le code, vérifions que nous avons tous les outils nécessaires.

### outils développement

* Il nous faut un éditeur de texte. J'utilise [vscode](https://code.visualstudio.com/), téléchargez le et installez le.
* Il nous faut du javascript. On utilisera [node](https://nodejs.org/en/) : téléchargez le et installez le en [suivant le tuto]({% link cours/web/js/bases.md %}#bloc-id-installation-node). 
* nous utiliserons le terminal, donc jetez un oeil au [tuto terminal]({% post_url tutos/systeme/2021-08-24-terminal %}) pour pouvoir le dégainer à l'envie.

### projet

Nous allons préparer le projet dans lequel nous allons coder. 

1. Commencez par créer le dossier *"numerologie-niveau-1"*
2. das vscode, choisissez : "*Fichier > open*" puis naviguez jusqu'à votre dossier *"numerologie-niveau-1"*. 
3. On vous demande si vous faites confiances aux auteurs, puisque c'est vous dites oui.

#### vscode le tour du propriétaire

Nous venons de créer un nouveau projet, que vscode appelle un [workspace](https://code.visualstudio.com/docs/editor/workspaces#_how-do-i-open-a-vs-code-workspace). Sur la gauche de la fenêtre, le menu du haut vous permets de choisir :
* les fichiers et sous-dossiers de votre workspace (pour l'instant il n'y a rien)
* de chercher du texte dans votre projet
* la gestion de source avec [git](https://fr.wikipedia.org/wiki/Git)
* le debogage
* les extensions installées. 

Le menu du bas : 
* ma gestion des compte
* les préférences


Vous avez aussi une fenêtre d'ouverte qui s'appelle welcome. Vous pouvez la fermer en cliquant sur la croix à droite de son nom.

Créons un nouveau fichier *"fichier > New File"*, et sauvons le tout de suite : *"fichier > enregistrer"* avec le nom *"mes_tests.js"*. 

> Lorsque l'on code et que vous ne voulez pas avec de problème, les noms de fichier doivent êtres sans espaces et sans accents.


Vscode à compris que c'était du javascript, il l'écrit dans la barre de status (la dernière ligne, en bleu, de la fenêtre vscode).

> la barre de status est très utile, elle regrope plein d'infos relative au fichier courant :
> * où on est : Ln 1; Col 1
> * l'[encodage des caractères](https://www.w3.org/International/questions/qa-what-is-encoding.fr) : UTF-8. Vous ne **devez jamais** avoir autre chose lorsque vous écrivez du texte. 
> * l'[encodage des fin de ligne](https://fr.wikipedia.org/wiki/Fin_de_ligne) : LF (sous unix/mac) ou CRLF (sous windows). On ne s'en occupe pas trop, vscode gère tout ça pour nous
> * le langage : ici javascript
> * d'autres trucs selon les extensions que vous avez ajouté.


#### écrire du javascript

> TBD
{: .note}


### docs utiles 

* tests, 
* user stories
* code


#### js ? 

* nombre et objet

#### développement

#### code


## niveau 2

* type= module et serveur de base

On va automatiser :

* les user stories
* les tests


mettre sur l'ovh
