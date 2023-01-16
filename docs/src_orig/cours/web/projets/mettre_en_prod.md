---
layout: layout/post.njk 
title:  "Commandes pour lancer son projet sur le serveur"
category: cours
tags: informatique cours 
authors:
- "Saidy"
- "Vienney"
---

## Se connecter sur ovh

### Sur Linux ou macOS
  
~~~ shell
ssh VotreIdentifiantCentrale@sas1.ec-m.fr -A
~~~

Se connecter au serveur sas tout en récupérerant votre clé ssh :

~~~ shell
ssh VotreIdentifiantCentrale@sas1.ec-m.fr -A
~~~

Quitter le serveur sas :

~~~ shell
exit
~~~

Se connecter sur le serveur ovh :

~~~ shell
ssh VotrePlante@ovh1.ec-m.fr
~~~

### Sur Windows (PowerShell)

~~~ shell
ssh VotrePlante@ovh1.ec-m.fr
~~~

Créer un nouveau dossier pour le projet :

~~~ shell
mkdir nom_du_projet
~~~

Entrer dans le dossier nom_du_projet :

~~~ shell
cd nom_du_projet
~~~

## Récupérer le projet depuis GitHub et le mettre dans le dossier

- Aller sur la page GitHub du projet (le repository)
- Cliquez sur Code (en vert)
- Copier le lien disponible dans Clone -> SSH (Il suffit de cliquer sur
le petit bouton à droite du lien pour le mettre dans votre presse-papier.)
- Récupérez les fichiers :

~~~ shell
git clone VotreLienSSH
~~~

## Créer le dossier node

Regarder s'il y a un dossier "node" :
`cd /`
`ls`

Si c'est le cas, le supprimer :
`rm -rf node`

Créer un dossier node qui est lié au projet :
`ln -s nom_du_projet/nom_du_repository node`

## Installer les modules node.js

- Dans le dossier node (`cd node`) :
`npm install`

- dans le dossier node/static (`cd node/static`) :
`npm install`

## Récupérer votre port Node.js

Revenir à la racine (`cd /`) et regarder le fichier readme.txt (`cat readme.txt`).

Le port s'affiche à côté de "Node"

**Ecrire le code du port dans le fichier node.js du serveur (depuis la racine) :**

- Avec nano :

~~~ shell
nano node/server.js
~~~

- Avec vim :

~~~shell
vim node/server.js
~~~

- Quelques commandes pour Vim

~~~shell
:m! (pour sauvegarder)
:q! (pour quitter)
~~~

## Lancer votre projet sur le serveur

~~~ shell
node node/server.js
~~~

Votre page web est maintenant accesible à l'adresse :

VotrePlante.ovh1.ec-m.fr

Mais alors votre serveur node s'arrêtera quand vous quitterez ovh et la page ne sera plus sur le web.

**Lancer votre projet sur le serveur sans qu'il s'arrête quand vous quitter le serveur :**

- Solution 1:

~~~ shell
screen -d -m -S node node node/server.js
~~~

- Solution 2:

lancer le processus en arrière-plan :

~~~ shell
node node/server.js &
~~~

Vous pouvez maintenant quitter votre ovh :

~~~ shell
exit
~~~

Et vous pouvez constater que maintenant votre projet est toujours accessible sur le web à l'adresse :

VotrePlante.ovh1.ec-m.fr

### Pour gérer les screens

Pour afficher tous les screens existants, sur toutes les sessions :

~~~ shell
`VotrePlante@ovh1 ~/node (git)-[master] % ps aux`
~~~

Pour afficher les screens existants, uniquement sur votre session :

~~~ shell
VotrePlante@ovh1 ~/node (git)-[master] % ps
~~~

Pour afficher uniquement les screens de sa propre session :

~~~ shell
VotrePlante@ovh1 ~/node (git)-[master] % ps aux | grep VotrePlante
~~~

Pour tuer le screen  (gentiment) :

~~~ shell
VotrePlante@ovh1 ~/node (git)-[master] % kill 3031408
~~~

ou :  

~~~ shell
VotrePlante@ovh1 ~/node (git)-[master] % kill -13 3031408
~~~

Pour tuer le screen 3031408 (méchamment) :

~~~ shell
VotrePlante@ovh1 ~/node (git)-[master] % kill -9 3031408
~~~

Sinon, vous pouvez aussi utiliser un outil plus convivial pour faire ces opérations :

~~~ shell
top
~~~
