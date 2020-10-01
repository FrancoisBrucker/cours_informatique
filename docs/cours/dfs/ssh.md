---
layout: page
title:  "SSH"
category: cours
tags: combat web
---


# Zéro tracash, Zéro blablash, SSH

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

Pour plein d'info et d'explication sur le chiffrement des clés voir [ici]({% link cours/dfs/ssh_rsa.md %}) 
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
#### Où ranger sa clé ?

Il est préférable de se placer dans un dossier adapté au stockage de données sensibles, en général on stockera les clés dans .ssh.

Avec `$ ls -la` on peut voir tous les fichiers et leurs permissions. La ligne de .ssh devrait commencer par 
`drwx______`, `d` indique qu'il s'agit d'un dossier, les trois caractères suivants `rwx` que le *propriétaire* peut lire, 
écrire et exécuter son contenu et les tirets suivants que les autres utilisateurs n'ont aucun droit dessus (plus d'info sur les permissions [ici](https://www.linux.com/training-tutorials/understanding-linux-file-permissions/)). 


Pour les clés on se place donc dans .ssh puis on génère une paire de clés : 
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

## A chaque nouvelle session

A chaque fois que vous fermez votre session utilisateur 
(donc notamment lorsque vous éteignez votre ordinateur), 
votre agent ssh perd les clés publiques qu'il possédait. 
En démarrant une nouvelle session et en affichant la liste des identités 
représentées par l'agent avec `ssh-add -l`, 
vous obtenez donc le message suivant : 
~~~sh
the agent has no identities
~~~

Il faut donc récupérer votre clé ssh là où vous l'avez laissée. 
Rien de nouveau ici, c'est simplement une routine à prendre.


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

Aller sur http://node.ail.ovh1.ec-m.fr/ dans un navigateur et se connecter avec son identifiant Centrale.

Copier sa clé publique en entier (en 3 mots, commence par “ssh-rsa”, se termine par “@sas1.ec-m.fr”) et valider pour 
se voir attribuer notre propre herbe de Provence absolument authentique (malheureusement la farigoule n'est pas dans la liste).

On pourra ensuite accéder à ovh1 depuis le terminal :
~~~sh
  $ mon_herbe@ovh1.ec-m.fr
~~~

Serveur et Identifiant que l'on utilisera pour [la suite du cours]({% link cours/dfs/ssh_scp.md %}).

