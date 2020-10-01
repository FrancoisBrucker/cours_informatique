---
layout: page
title:  "Copie sécurisée"
category: cours
tags: combat web
---

# Copie sécurisée via le protocole SSH 
  
Pour créer sa clé et s'identifier sur ovh1 voir [le début du cours]({% link cours/dfs/ssh.md %}). 

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
