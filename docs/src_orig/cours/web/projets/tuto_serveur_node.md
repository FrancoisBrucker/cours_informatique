---
layout: page
title:  "Numérologie partie 2 - niveau 2. Mise en production sur un serveur distant (ovh1 en 3A)"
category: Projets
tags: tuto node ovh
authors:
- "Lucie Danard"
- "Anaïs Merliot"
---


## Étape 1 : Récupérer les fichiers du projet numérologie
Créez un dossier *numerologie* et reproduisez la structure suivante : 

### structure du projet

```text
.
├── back
│   └── numerologie.js
├── index.js
├── package-lock.json
├── package.json
└── static
    ├── index.html
    └── main.css
```

### fichiers

[Lien vers les contenus des fichiers](https://francoisbrucker.github.io/cours_informatique/cours/web/projets/numerologie/partie-2-serveur/5-structures.html)


## Étape 2 : Utiliser express

### gestionnaire de package

Pour gérer notre site, on va utiliser le module pour node [express](https://expressjs.com/fr/). 
Pour l'installer, comme pour installer les autres packages node, on peut utiliser npm (**n**ode **p**ackage **m**anager), qui est livré avec node.

#### npm init

Pour commencer, `npm` doit pouvoir gérer vos modules. Pour cela, il faut lui laisser créer un fichier de configuration nommé *"package.json"*. Pour cela, tapez dans un terminal placé à la racine de notre projet :

```shell
npm init
```

Répondez aux questions (ou tapez sur entrée). Lorsque le programme est fini, vous trouverez un fichier *"package.json"* à la racine de votre projet.

Chez moi, il ressemble à ça :

```json
{
  "name": "numerologie",
  "version": "1.0.0",
  "description": "de la numérologie",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "Lucie Danard",
  "license": "ISC"
}

```

Il ne contient pour l'instant que des informations générales quant au projet. Nous allons bientôt y ajouter des modules.

> Le [json](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation) est un format texte pour sauvegarder des données structurée. C'est un format génial qui sert tout autant pour les fichiers de configurations que le transfert de données par le web.

#### ajout d'un module

Pour cela, tapez dans un terminal placé à la racine de notre projet :

```shell
npm add --save express
```

> N'oubliez pas `--save`, sinon le module sera installé mais la dépendance ne sera pas ajoutée au fichier *"package.json"* ce qui est tarte.
{.attention}

Cette commande a ajouté une dépendance à notre fichier *"package.json"* :

```json
"dependencies": {
    "express": "^4.17.1"
  }
```

A créer un fichier *"package-lock.json"* qui contient la liste de tous les modules installés et un (gros) dossier *"node_modules"* qui contient les modules installés.

> Il y a plus de 50 modules installés alors que l'on a demandé d'installer que le module `express`, car il a lui même des dépendances et ses dépendances d'autres dépendances, etc.

La différence entre *"package.json"* et *"package-lock.json"* est que le premier décrit les versions possibles (nous, toutes les versions ultérieures à 4.17.1) alors que *"package-lock.json"* décrit la version effectivement installée (la 4.17.1). Cette méchanique permet de mettre à jour nos modules en supprimant le dossier *"node_module"* et le fichier *"package-lock.json"* et en tapant la commande `npm install`.

#### sauvegarde et installation du projet

Le dossier *"node_module"* n'est pas un module à sauver, on peut installer toutes les dépendances avec la commande `npm install` :

* grâce au fichier *"package-lock.json"* : la commande `npm --install` sait exactement quels modules installer
* le fichier *"package.json"* donnant les dépendances générales de notre projet.

## Étape 3 : Tester le projet en local

Ça y est en principe ça marche ! Pour vérifier que votre projet fonctionne en local, exécutez le fichier index.js en tapant dans le terminal :

```shell
node index.js
```

et allez vérifier le résultat dans le navigateur à l'adresse : http://localhost:3000. Vous remarquerez que 3000 correspond au port rentré dans le fichier index.js, donc si vous en avez mis un autre, il faut modifier l'adresse en conséquence.

## Étape 4 : Mettre en production sur l’ovh

### 1. Trouver et changer le port

#### Rappel: Connexion à l'ovh avec sa clé Ssh

> Se connecter à sas1 avec un agent: ```ssh identifiant@sas1.centrale-marseille.fr -A```
> <br/> Récuppèrer la clé SSh: ```ssh -add```
> <br/> Regarder ce que contient l'agent: ```ssh -add -l```
> <br/> Se connecter à l'ovh avec un agent:  ```ssh  herbearomatique@ovh1.ec-m.fr -A ```

<br/> Une fois connecté, on pourra faire régulièrement des ls, afin de savoir quels fichiers on a dans le répertoire.
<br/> Le numéro du port se trouve dans le fichier **readme**, pour le lire : ```cat readme.txt```.

<br/>Chez moi cela ressemble à :

```text
Tomcat instance port = 10033            <-- java.herbearomatique.ovh1.ec-m.fr
Tomcat shutdown port = 10133

Gunicorn (Django) port = 10233          <-- django.herbearomatique.ovh1.ec-m.fr

Gunicorn (Flask) port = 10333           <-- flask.herbearomatique.ovh1.ec-m.fr

Node.js port = 10433                            <-- node.herbearomatique.ovh1.ec-m.fr

PHP port = 10533                                <-- herbearomatique.ovh1.ec-m.fr pour les fichiers en .php seulement
```

<br/> Lire le port correspondant au serveur node (ici 10433) et le remplacer dans le fichier *index.js* (à la place de 3000).

### 2. Exporter le projet sur l’ovh

<br/>On utilise [git et github](https://francoisbrucker.github.io/cours_informatique/cours/git_et_github/ "Voir git").

#### Pour exporter
<br/>On utilise pour exporter la totalité du projet: ```git add --all``` ou un fichier en particulier : ```git add <nomfichier>```.
<br/>Ensuite on commit et push le projet sur github : ```git commit -am “<commentaire>” ``` et ```git push```.
 
#### Pour importer
<br/> On se place dans le dossier <b>node</b> de l’ovh, et on clone le projet: ```git clone <lien github ssh>```.
>Attention: ne pas oublier de se connecter à l'ovh avec son agent contenant la clé Ssh.



# Étape 5 : Lancer le démon

Pour lancer le serveur node sur l'ovh, et que celui-ci ne s'arrête pas quand vous éteignez votre machine, il faut lancer un démon. Pour commencer, placez-vous au bon endroit, c'est-à-dire à la racine du projet numérologie. Si vous lancez la commande '''ls''', vous devriez voir le fichier index.js. Ensuite vous pouvez lancer le démon avec la commande :

```shell
/usr/bin/screen -d -m -S node node index.js
```
C'est bon, votre serveur est en prod ! Vous pouvez vérifier que tout va bien en vous connectant à l'adresse <node.herbearomatique.ovh1.ec-m.fr>.

> Si vous avez une erreur dans les 500, cela signifie qu'il y a un problème avec le serveur (la mise en prod probablement, si tout marchait en local). Si vous avez une erreur 404 en revanche, c'est probablement parce que certains fichiers de votre projet ne sont pas trouvés par le serveur.

Si vous voulez tuer le démon, vous pouvez procéder de la façon suivante :
    
```shell
 screen -X -S node quit
```

et pour voir les screen en marche :

```shell
 screen -ls
```

# Bonus : Gestion des processus

Dans cette partie, vous allez pouvoir visualiser et arrêter les processus en cours.
Par exemple, commencez par vous connecter sur l'ovh (pour rappel ```ssh  herbearomatique@ovh1.ec-m.fr -A ```)

Pour visualiser tous les processus en cours :

```shell
ps aux
```

Vous remarquez que la première colonne correspond au nom de l'utilisateur, et la deuxième donne le numéro d'identification du processus.

Pour visualiser les processus de quelqu'un (par exemple stevia) :


```shell
ps aux | grep stevia
```

Chez moi cela renvoie ça :

```shell
root     1438186  0.0  0.2  14652  8968 ?        Ss   10:27   0:00 sshd: stevia [priv]
stevia   1438192  0.0  0.1  14652  6032 ?        S    10:27   0:00 sshd: stevia@pts/0
stevia   1438193  0.0  0.1  10776  5916 pts/0    Ss   10:27   0:00 -zsh
stevia   1438605  0.0  0.0  10428  3524 pts/0    R+   10:34   0:00 ps aux
stevia   1438606  0.0  0.0   6832   648 pts/0    S+   10:34   0:00 grep --color=auto stevia
stevia   2252952  0.0  0.2  15252  8108 ?        Ss   sept.30   0:00 /lib/systemd/systemd --user
stevia   2252953  0.0  0.0 167576   732 ?        S    sept.30   0:00 (sd-pam)
stevia   2913276  0.0  0.0   7564  2136 ?        Ss   oct.08   0:00 /usr/bin/SCREEN -d -m -S node node index.js
stevia   2913277  0.0  0.5 629340 23404 pts/11   Ssl+ oct.08   0:00 node index.js
```

On peut arrêter un processus, mais pas n'importe lequel !! On ne peut stopper que les siens (donc pas le root). Pour tuer un processus, on le désigne par son numéro. Par exemple, la commande suivante détruit le processus de connection à l'ovh, et donc me déconnecte.

```shell
kill 1438192
```