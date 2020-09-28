---
layout: page
title:  "SSH"
category: cours
tags: combat web
---


# Zéro tracash, Zéro blablash, SSH

Mettre des sites / refs / sources

L’étape numéro 1 est d’avoir la bonne console. Moi, j’utilise Ubuntu (WSL 2).

L’étape numéro 2 est d’avoir un agent ssh, c’est le maître des clefs. 
Vous trouverez toutes les informations necessaires pour installer WSL2 et l’agent sous windows ici : [installation_W10](https://francoisbrucker.github.io/cours_informatique/cours/dfs/installation_W10.html)

Si vous utilisez linux ou mac tout est déjà là (normalement)

Comparer les OS expliquer ce qu’est l’agent

### Vérifiez que ça fonctionne
Ouvrez une fenêtre powershell et, en remplaçant login par votre login unix de l’école tapez la commande : `ssh-add -l`
Vous devriez avoir une phrase vous disant que l’agent n’a pas d’identité. Si vous n’avez pas d’agent installé (ou si vous l’avez stoppé) cela devrait vous dire qu’on arrive pas à se connecter à l’agent.
 
## SSH, c’est quoi ?
**Secure Shell (SSH)** est à la fois un programme informatique et un protocole de communication sécurisé. Le protocole de connexion impose un échange de clés de chiffrement en début de connexion. Par la suite, tous les segments TCP sont authentifiés et chiffrés. Il devient donc impossible d'utiliser un sniffer pour voir ce que fait l'utilisateur.
Avec SSH, l'authentification peut se faire sans l'utilisation de mot de passe ou de phrase secrète en utilisant la cryptographie asymétrique. Le protocole utilise deux clés complémentaires, la clé publique et la clé privée.
La clé publique est distribuée sur les systèmes auxquels on souhaite se connecter. La clé privée, qu'on prendra le soin de protéger par un mot de passe (elle est donc stockée cryptée), reste uniquement sur le poste à partir duquel on se connecte. L'utilisation de l’agent ssh permet de stocker le mot de passe de la clé privée pendant la durée de la session utilisateur.
 


## Générer une clé

### Et ne pas se la faire voler par des hackers malveillants

**TL;DR**
~~~sh
accéder au serveur de Centrale :  # pour retrouver ses données où que l'on soit 
  $ ssh -A identifiant@sas1.ec-m.fr

créer sa clé :
  $ cd .ssh  # facultatif mais les clés seront plus en sécurité dans un dossier protégé 
  $ ssh-keygen

ajouter la clé à son porte clé :
  $ ssh-add chemin/nom_de_la_clé
~~~
### Pour créer sa paire de clés
Où ranger sa clé ?

Il est préférable de se placer dans un dossier adapté au stockage de données sensibles, les dossiers cachés sont ceux dont le nom commence par un point.

On peut les voir avec la commande : 
~~~sh
  $ ls -a
~~~
Pour les clés on se place dans .ssh puis on génère une paire de clés : 
~~~sh
  $ cd .ssh
  $ ssh-keygen
~~~

On lui donne un nom (ex: keyblade95) et une passphrase (à ne pas oublier) et tadaaa on a maintenant deux fichiers keyblade95 et keyblade95.pub.

*keyblade95.pub* est votre clé **publique** à donner à tous vos amis.

*keyblade95* est votre clé **privée** à ne montrer à personne sous aucun prétexte.

Il faut ensuite ajouter sa clé à son agent qui joue ici le rôle de porte clé : 
~~~sh
  $ ssh-add nom_de_la_clé
~~~
Rentrer la passphrase et la clé sera ajoutée. C'est tout simple.

On peut vérifier les clés ajoutées avec :

~~~sh 
  $ ssh-add -l
~~~

Et faire oublier toutes les clés connues de son agent avec : 
~~~sh
  $ ssh-add -D 
~~~

## Authorized keys
### Reconnaître les machines qu’on connaît

Lorsque on se connecte à un serveur distant il est en général nécessaire de s'identifier, parfois plusieurs fois pour une seule ligne de commande ce qui est rapidement fastidieux. 

Pour s'éviter des efforts inutiles il suffit d'enregistrer sa clé publique sur la machine distante qui pourra ensuite nous reconnaitre.
Les clés enregistrées sont stockées dans un fichier nommé authorized_keys dans un dossier .ssh sur le serveur.

La commande suivante permet d'ajouter notre clé publique aux clés connues par une machine :
~~~sh 
  $ cat id_rsa.pub >> authorized_keys
~~~
Il est maintenant possible de se déconnecter et reconnecter au serveur ou faire des opérations plus complexes sans entrer systématiquement son mot de passe youpi !

## Assaisonner son cours d'info
![image?]({{"images/seasonning.png"}})

Aller sur http://node.ail.ovh1.ec-m.fr/ et se connecter avec son identifiant Centrale.

Copier sa clé publique en entier (en 3 mots, commence par “ssh-rsa”, se termine par “@sas1.ec-m.fr”) et valider pour recevoir votre propre herbe de Provence absolument authentique (malheureusement la farigoule n'est pas dans la liste).

On pourra ensuite accéder à ovh1 avec :
~~~sh
  $ mon_herbe@ovh1.ec-m.fr
~~~

Serveur et Identifiant que l'on utilisera pour la suite des cours.


explication encryption : https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work

DES MATHS


scp  : copier un dossier d’un ordi vers un autre
changement de port redirection
prendre une clé usb, copier les fichiers.
Aller sous le cri, brancher la clé sur le troisième serveur de la deuxième rangée.





cp : copier un fichier (sur une même machine)
cp -r => récursif
cp -p => garde les droits
cp [option] source destination

scp : commande pour transfert de fichiers via connexion ssh
s pour secure

monde UNIX: archives tar (mieux que zip car conserve les droits ?)

bsdtar cvf /tmp/node_ssh_keys.tar node.ssh.keys
/!\ fichier tar n’est pas encore compressé

xz /tmp/node_ssh_keys.tar
=> devient /tmp/node_ssh_keys.tar.xz
désormais compressé

bsdtar cf - node_ssh_keys | ssh herbe@ovh1.ec-m.fr “cd /tmp: tar xJf -”

tar      c        v         x           f
       créer   voir  extraire  utilise
                                      fichier en paramètres


scp fichier_source fichier_destination:www/


TL;DR
Mise en page Markdown : 

# en debut de ligne pour h1 ( plusieurs ## pour h2..3… )

Pour des lignes de code dans le shell
~~~sh
code
code 
code
~~~

[titre du lien](http:...)

les trucs entre `gnau` sont en gris très visible dans un paragraphe (attention c’est pas des apostrophes alt gr + 7 sur mon clavier)
les trucs entre ** ** sont en gras
les trucs entre * * sont en itallique

les tirets 
permettent
de faire 
des liste 
en markdown


