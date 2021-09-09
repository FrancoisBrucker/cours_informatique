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


Vscode à compris que c'était du javascript, il l'écrit dans la barre de status (la dernière ligne, en bleu, de la fenêtre vscode, voir [user interface](https://code.visualstudio.com/docs/getstarted/userinterface)).

> la barre de status est très utile, elle regroupe plein d'infos relative au fichier courant :
> * où on est : Ln 1; Col 1
> * l'[encodage des caractères](https://www.w3.org/International/questions/qa-what-is-encoding.fr) : UTF-8. Vous ne **devez jamais** avoir autre chose lorsque vous écrivez du texte. 
> * l'[encodage des fin de ligne](https://fr.wikipedia.org/wiki/Fin_de_ligne) : LF (sous unix/mac) ou CRLF (sous windows). On ne s'en occupe pas trop, vscode gère tout ça pour nous
> * le langage : ici javascript
> * d'autres trucs selon les extensions que vous avez ajouté.


#### écrire du javascript

fichier : *"mes_tests.js"*
```javascript
nom = "monde"

console.log("bonjour " + nom + " !")
```
> Puis sauvez le fichier (*Fichier > save*).
{: .note}

Ce qu'il y a de bien avec vscode c'est que toute commande est aussi appelable par son nom grâce à la [palette de commande](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) : *Affichage > Command Palette...*. Vous pouvez taper "save" par exemple pour voir toutes les commandes qui contiennent save, dont celle qui sauve des fichiers *File: Save*. C'est super utile pour trouver une commande dont ne peut que deviner le nom. 

> Les commandes de la palette de commande sont accessible si la ligne commence par un ">". S'il y a un "?" c'est l'aide et s'il n'y a retrouve des fichiers ouverts.

Par exemple, tapez dans la palette ">terminal". Il doit y avoir une commande qui s'appelle *Open new external terminal". Choisissez là et apuyez sur entrée. Un nouveau terminal s'ouvre directement dans le dossier de votre projet. Magique non ?

>On peut Maintenant exécuter notre fichier en tapant dans ce nouveau terminal : `node mes_tests.js`.
{: .note}


> On peut aussi ouvrir un terminal Directement dans node : *"affichage > terminal"*.
> Les menus du dessus du terminal (PROBLEMS, OUTPUT, DEBUG CONSOLE et TERMINAL) dans vscode sont des sorties d'autres processus dont on a pas besoin pour l'instant : on reste donc sur *TERMINAL*.
> 
>Vous pouvez la supprimer en cliquant sur la poubelle en haut à droite de la fenêtre et en recréer une autre : *"Terminal > new terminal"*, ou juste le fermer en appuyant sur la croix (vous ré-ouviriez ce terminal la prochaine fois).

#### vscode, les préférences

> <https://code.visualstudio.com/docs/getstarted/settings>
{: .note}


Personnellement, s'il y a bien une chose qui m'ennuie c'est de constamment sauver mes fichiers. Si je fait une modification de mes fichiers, c'est parce que j'en ai envie je ne vois pas l'intérêt de devoir sauver pour confirmer. Heureusement, vscode permet (comme tout éditeur qui se respecte) de faire ça en modifiant ses préférences :

> Allez dans les préférences de vscode : *icône engrenage > settings*.
{: .note}

Une fenêtre s'ouvre avec toutes les préférences. Il y a : 
* une barre de recherche
* deux panels : *User* et *Workspace*. Par défaut, on est positionné sur *User*.

Selon le pannel que vous choisissez vous allez changer les préférences pour ce workspace particulier (panel *Workspace*) ou pour tous les workspaces (panel *User*).

Dans le panel *User* choisissez *Text Editor > Files* puis cherchez *Auto Save*. On pet ensuite régler sur *afterDelay* puis changer le délais dans le champ *Auto Save Delay*. J'ai mis 1000, ce qui fait qu'après 1seconde de repos mon fichier est sauvé automatiquement. 

> On aurait pu aussi taper "auto save" dans la barre de recherche pour obtenir directement les champs possibles.

> Regardez les préférence d'Auto Save* dans le panel *Workspace*, il devrait toujours être sur *off*.
{: .note}

> Les divers extensions et modules sont installés soit dans le dossier de projet pour des préférences *Workspace* soit dans les dossiers de préférences du compte, comme indiqué dans [la doc](https://code.visualstudio.com/docs/getstarted/settings#_settings-file-locations).


### docs utiles 

On va ajouter petit à petit des dossiers à notre projet. Pour l'instant ajoutons y un dossier nommé "user stories" qui nous permettra de stocker toutes les infos non code de notre site et de comment on peut qu'il soit utilisé.

1. *menu Affichage > Explorer*
2. cliquez sur le nom de dossier du workspace ("numérologie")
3. une fois le dossier sélectionné, vous pouvez cliquer sur l'icône du dossier avec un petit +
4. écrivez "user stories" puis appuyez sur entrée.

Une fois le dossier crée, on va écrire les utilisation possible de notre site comme si on était un utilisateur. 

#### actions sur le site

> Créez un fichier nommé *"connaitre-son-numero.md"* à l'intérieur du dossier *"user stories'* (cliquez droit sur le nom du dossier, puis "new file")
{: .note}

Ce fichier va être écrit en [markdown]({% post_url tutos/2021-08-30-format-markdown %})


> Comme on va écrire en français, vous allez ajouter à vscode les extensions suivantes (*Menu affichage > extensions) : 
> * [french langage pack for visual studio code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-fr) pour écrire presque sans faute d'orthographes
> * [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) pour nos aider à écrire du markdown.
{: .note}

```markdown
# connaître son numéro

## page générale

1. je rentre mon nom dans un champ texte : François puis j'appuie sur la touche entrée.
2. En dessous du champ texte, on affiche alors Bonjour François, votre numéro est le X

X est écrit en gros au milieu de la page.

## page du numéro

<http://localhost/prénom/XXXX>

doit rendre le numéro associé à XXXX
```

> Remarquez quand vous tapez entrée après avoir écrit le premier item ça passe de suite à 2 ?

> Dans la palette de commande, regadez tout ce que l'on peut faire en tapant "markdown".
> Par exemple essayez : *Markdown All in One: Print current document to html*
{: . note}


Votre markdown a magiquement été transformé en un joli html que vous pouvez ouvrir avec votre navigateur préféré (c'est tellement beau que j'en ai les larmes aux yeux). Vous pouvez supprimer ce fichier html en lui cliquant droit dessus puis : *delete file*.

> Ces user stories sont important pour garder en mémoire le but qu'on se fixe. Il ne faut pas hésiter à en ajouter, les modifier au cours du projet.

#### todos

> Créez dans le dossier "user stories" un fichier todo.md
{: .note}

On va ajouter nos liste des taches à faire, et marquer ces tâches effectuées lorsqu'elles sont réalisées. Le projet sera fini lorsqu'il n'y aura plus de tâche dans le todo.

> On nettoiera de temps en temps le fichier en supprimant les lignes effectuée pour garder une taille raisonnable de fichier.

fichier todo.md
```markdown
# Todos

On mettra un 'X' dans la checkbox pour l'item courant
on ~~barrera~~ lorsque cette item sera réalisé

- [ ] associer un numéro à un nom
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter
```


Ce fichier va nous servir à driver nos actions dans le projet. On
* tests, 
* user stories
* code


#### js ? 

* nombre et objet

#### développement

#### code