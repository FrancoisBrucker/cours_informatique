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

Voilà par exemple comment récupérer votre clé 
si vous l'avez stockée sur le serveur sas1 :
~~~sh
 $ ssh -A identifiant@sas1.ec-m.fr
    # Entrez votre mot de passe pour vous connecter sur sas1
 $ ssh-add
    # Entrez votre phrase secrète pour décrypter et récupérer la clé
 $ exit
 $ ssh-add -l  # Pour vérifier qu'on a bien récupéré la clé
~~~

Vous pouvez maintenant utiliser votre clé ! 
Par exemple pour vous connecter au serveur ovh1.ec-m.fr :
~~~sh
 $ ssh mon_herbe@ovh1.ec-m.fr
~~~


## Copie sécurisée via le protocole SSH

Vous avez maintenant accès à votre propre espace sur ovh1 ! 

Une fois connecté, vous pouvez trouver le dossier `www`. 
C'est ici que vous allez mettre le contenu de votre site. 
Pour l'instant il contient juste le fichier `index.html`. 
Vous pouvez lire et modifier ce fichier directement via la console, 
mais ce n'est pas très pratique...

On va donc plutôt créer nos fichiers sur notre ordinateur, 
puis les copier et les envoyer au serveur ovh1.

Pour copier un fichier, il existe la commande `cp`. 
On l'utilise comme ça :
~~~sh
 $ cp [option] fichier_source fichier_destination
~~~
Si aucun fichier de ce nom n'existe à la destination, il sera créé. 
S'il existe déjà, il sera remplacé.

On peut également copier des dossiers. 
Vous en trouverez quelques utilisations de base 
dans [ce tuto](http://www.commandeslinux.fr/commande-cp/). 
On peut notamment retenir :
~~~sh
 $ cp -r source destination  # Copie récursive (pour copier des dossiers)
~~~
~~~sh
 $ cp -p source destination  # Copie en conservant les droits du fichier
~~~

Le problème de `cp`, c'est qu'on ne peut l'utiliser que localement 
pour faire une copie sur notre machine.

Pour copier un fichier vers un serveur (et inversement), on utilise 
donc la commande `scp`, signifiant *Secure Copy Protocol*. 
Cette copie utilise le protocole SSH pour assurer l'authenticité 
et la confidentialité du transfert. 

Elle s'utilise de la même manière que `cp` : 
~~~sh
 $ scp [option] fichier_source fichier_destination
~~~

Pour l'essayer, créez un index.html sur votre machine et copiez-le vers ovh1 
dans le dossier www/.

Depuis votre machine (sans être déjà connecté à ovh1), ça donne :
~~~sh
 $ scp chemin/index.html mon_herbe@ovh1.ec-m.fr:www/index.html
~~~

Si vous allez vérifier sur ovh1, 
votre fichier a bien remplacé l'ancien index.html . 
Incroyable.

## Copie et Compression de dossiers

Comme pour `cp`, vous pouvez utiliser `scp` pour copier des dossiers. 
Le problème, c'est que les copier tels quels prend du temps. On veut donc 
les compresser avant de les transférer. 
Dans le monde UNIX, on utilise les archives GNU tar avec la commande `tar`. 
Cette commande permet de concaténer plusieurs fichiers en un seul et même 
fichier. En l'utilisant sur un dossier, cela conserve sa structure et ses 
droits. La syntaxe est la suivante :

Pour créer l'archive d'un dossier :
~~~sh
 $ tar -cvf archive_dossier.tar dossier/
~~~
`c` signifie qu'on crée une archive. 
`v` désigne le mode "verbeux" (il affiche ce qu'il fait). 
`f` signifie qu'on utilise le fichier en paramètre.

Ensuite, pour extraire ce dossier :
~~~sh
 $ tar -xvf archive_dossier.tar
~~~
`x` signifie qu'on extrait l'archive.


Attention cependant : ici le fichier .tar **n'est pas encore compressé**. 
Pour le compresser, on va ici choisir Lzma, la méhode utilisée 
par 7zip.

Vous pouvez compresser votre archive manuellement avec la commande `xz` :
~~~sh
 $ xz archive_dossier.tar
~~~
Un fichier *archive_dossier.tar.xz* est alors créé. 
Pour le décompresser, on utilise :
~~~sh
 $ xz -d archive_dossier.tar.xz
~~~

Une autre méthode plus simple est de compresser lors de l'archivage `tar`, 
en rajoutant `J` en option :
~~~sh
 $ tar -Jcvf archive_dossier.tar.xz dossier/
~~~
Et idem lors de l'extraction. 

Pour tester par vous-même : Créez un petit projet contenant par exemple 
un fichier html, un fichier css et un fichier js, puis copiez-le vers ovh1 
en utilisant l'archivage et la compression !
