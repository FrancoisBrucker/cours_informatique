---
layout: page
title:  "Projet numérologie : niveau 1"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %})/[niveau 1]({% link cours/web/projets/numerologie/niveau-1/index.md %})
{: .chemin}

Numérologie niveau 1. On ne verra que le strict nécessaire pour pour faire fonctionner le code :

* utilisation basique d'un éditeur de texte performant, ici [vscode](https://code.visualstudio.com/),
* stricte minimum de html/css pour pouvoir mettre en oeuvre notre serveur web,
* on tentera de s'amuser en javascript sans rentrer trop dans les détails de fonctionnement.

## prérequis

Avant de se lancer à corps perdu dans le développement et le code, vérifions que nous avons (enfin, surtout vous avez) tous les outils nécessaires :

1. et c'est le plus important **la bonne attitude** :
   * si vous ne connaissez rien : ne cédez pas à la facilité de copier/coller sans comprendre : c'est *bad karma* et ça vous rattrapera tôt ou tard. La magie — tout du moins en informatique — n'existe pas (et je suis le premier à le déplorer) : si ça fonctionne sans que vous savez au moins superficiellement pourquoi, c'est que ça n'a que l'air de fonctionner.
   * si vous connaissez déjà tout ça : faite-le tout de même cela vous permettra de suivre plus facilement les niveaux ultérieurs
2. **un cerveau** en état de marche : pour voir les correspondances, lire la doc, et poser des questions.
3. avoir **un éditeur de texte** fonctionnel. Nous utiliserons [vscode](https://code.visualstudio.com/) dans ce cours, téléchargez le et installez le.
4. un **navigateur internet** munis d'outils de développement. Tous les exemple seront fait avec [chrome](https://www.google.fr/chrome/).
5. un interpréteur javascript. On utilisera [node](https://nodejs.org/en/). Suivez le [tutoriel pour l'installation]({% link cours/web/js/bases.md %}#bloc-id-installation-node).
6. Sachez ouvrir [une fenêtre terminal]({% post_url tutos/systeme/2021-08-24-terminal %})

## plan

En quatre parties et autant de cours :

1. [un premier site entièrement en front]({% link cours/web/projets/numerologie/niveau-1/partie-1-front/index.md %})
2. [on ajoute une partie back pour les calculs]({% link cours/web/projets/numerologie/niveau-1/partie-2-post-get/index.md %})
3. on polie tout ça avec des routes différentes
4. on ajoute la possibilités de stocker des données
