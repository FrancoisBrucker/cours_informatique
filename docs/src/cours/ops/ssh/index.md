---
layout: layout/post.njk

title: ssh
authors: 
  - "Herbelleau Romain"
  - "Laurent Léo"
  - "Dégeorges Laurie"


eleventyNavigation:
  key: "ssh"
  parent: "Ops"
---

<!-- début résumé -->

Installation et utilisation (basique) de ssh.

<!-- fin résumé -->

> TBD homogénéiser et rationaliser. Des choses sont mieux dans le cours unix

[Ssh](https://fr.wikipedia.org/wiki/Secure_Shell){.interne} permet d'établir une communication réseau sécurisée. Il utilise par défaut l'algorithme [rsa](./rsa){.interne} pour crypter le flux de communication.

## Installation

{% details "sous Linux" %}

A priori déjà installé

{% enddetails %}

{% details "sous Mac" %}

On l'installe avec [brew](https://brew.sh/) :

```
brew install openssh
```

{% enddetails %}

{% details "sous Windows" %}

Les dernières versions de windows viennent avec tout ssh d'installé. Il faut juste faire en sorte que l'Agent ssh soit lancé au démarrage (on suit le tuto de [gestion des clés OpenSSH](https://docs.microsoft.com/fr-fr/windows-server/administration/openssh/openssh_keymanagement)). Ouvrez un fenêtre **powershell en mode administrateur** (clique droit sur le drapeau, puis choisissez *powershell (admin)*), puis tapez les commandes :

```
# Set the sshd service to be started automatically
Get-Service -Name ssh-agent | Set-Service -StartupType Automatic

# Now start the sshd service
Start-Service ssh-agent
```

L'agent fonctionne différemment sous windows que sous un système unix. Mais normalement, il devrait être reconnu, en particulier par git.

{% enddetails %}

## Zéro tracash, Zéro blablash, SSH

### Vérifiez que ça fonctionne

Ouvrez une fenêtre terminal et, en remplaçant login par votre login unix de l’école tapez la commande : `ssh-add -l`
Vous devriez avoir une phrase vous disant que l’agent n’a pas d’identité. Si vous n’avez pas d’agent installé (ou si vous l’avez stoppé) cela devrait vous dire qu’on arrive pas à se connecter à l’agent.

## ssh, c’est quoi ?

**Secure Shell (SSH)** est à la fois un programme informatique et un protocole de communication sécurisé. Le protocole de connexion impose un échange de clés de chiffrement en début de connexion. Par la suite, tous les segments TCP sont authentifiés et chiffrés. Il devient donc impossible d'utiliser un sniffer pour voir ce que fait l'utilisateur.

Avec ssh, l'authentification peut se faire sans l'utilisation de mot de passe ou de phrase secrète en utilisant la cryptographie asymétrique. Le protocole utilise deux clés complémentaires, la clé publique et la clé privée.
La clé publique est distribuée sur les systèmes auxquels on souhaite se connecter. La clé privée, qu'on prendra le soin de protéger par un mot de passe (elle est donc stockée cryptée), reste uniquement sur le poste à partir duquel on se connecte. L'utilisation de l’agent ssh permet de stocker le mot de passe de la clé privée pendant la durée de la session utilisateur.

Pour plein d'info et d'explication sur le chiffrement des clés voir [ici](../ssh_rsa){.interne}

## Générer une clé

### Et ne pas se la faire voler par des hackers malveillants

{% note "**TL;DR**" %}

```
accéder au serveur de Centrale :  # pour retrouver ses données où que l'on soit 
  $ ssh -A identifiant@sas1.ec-m.fr

# ne pas créer de clé si on en a déjà une !
créer sa clé : 
  $ cd .ssh  # facultatif mais les clés seront plus en sécurité dans un dossier protégé 
  $ ssh-keygen

ajouter la clé à son porte clé :
  $ ssh-add chemin/nom_de_la_clé
```

{% endnote %}

### Pour créer sa paire de clés

#### Où ranger sa clé ?

Il est préférable de se placer dans un dossier adapté au stockage de données sensibles, en général on stockera les clés dans .ssh.

Avec `$ ls -la` on peut voir tous les fichiers et leurs permissions. La ligne de .ssh devrait commencer par
`drwx______`, `d` indique qu'il s'agit d'un dossier, les trois caractères suivants `rwx` que le *propriétaire* peut lire, écrire et exécuter son contenu et les tirets suivants que les autres utilisateurs n'ont aucun droit dessus (plus d'info sur les permissions [ici](https://www.linux.com/training-tutorials/understanding-linux-file-permissions/)).

Pour les clés on se place donc dans `.ssh`{.fichier} puis on génère une paire de clés :

```
cd ~/.ssh
ssh-keygen
```

On lui donne un nom (ex: keyblade95) et une passphrase (à ne pas oublier) et tadaaa on a maintenant deux fichiers keyblade95 et keyblade95.pub.

*keyblade95.pub* est votre clé **publique** à donner à tous vos amis.

*keyblade95* est votre clé **privée** à ne montrer à personne sous aucun prétexte.

Il faut ensuite ajouter sa clé à son agent qui joue ici le rôle de porte clé :

```
ssh-add nom_de_la_clé
```

Rentrer la passphrase et la clé sera ajoutée. C'est tout simple.

On peut vérifier les clés ajoutées avec :

```
ssh-add -l
```

Et faire oublier toutes les clés connues de son agent avec :

```
ssh-add -D 
```

## A chaque nouvelle session

À chaque fois que vous fermez votre session utilisateur (donc notamment lorsque vous éteignez votre ordinateur),
votre agent ssh perd les clés publiques qu'il possédait. En démarrant une nouvelle session et en affichant la liste des identités représentées par l'agent avec `ssh-add -l`, vous obtenez donc le message suivant :

```
the agent has no identities
```

Il faut donc récupérer votre clé ssh là où vous l'avez laissée. Rien de nouveau ici, c'est simplement une routine à prendre.

## Authorized keys

### Reconnaître les machines qu’on connaît

Lorsque on se connecte à un serveur distant il est en général nécessaire de s'identifier, parfois plusieurs fois pour une seule ligne de commande ce qui est rapidement fastidieux.

Pour s'éviter des efforts inutiles il suffit d'enregistrer sa clé publique sur la machine distante qui pourra ensuite nous reconnaître.
Les clés enregistrées sont stockées dans un fichier nommé authorized_keys dans un dossier `.ssh`{.fichier} sur le serveur.

La commande suivante permet d'ajouter notre clé publique aux clés connues par une machine :

```
cat id_rsa.pub >> authorized_keys
```

Il est maintenant possible de se déconnecter et reconnecter au serveur ou faire des opérations plus complexes sans entrer systématiquement son mot de passe youpi !

## Assaisonner son cours d'info

![image?](seasonning.png)

Aller sur <http://node.ail.ovh1.ec-m.fr/> dans un navigateur et se connecter avec son identifiant Centrale.

Copier sa clé publique en entier (en 3 mots, commence par “ssh-rsa”, se termine par “@sas1.ec-m.fr”) et valider pour
se voir attribuer notre propre herbe de Provence absolument authentique (malheureusement la farigoule n'est pas dans la liste).

On pourra ensuite accéder à `ovh1.ec-m.fr` depuis le terminal :

```
ssh mon_herbe@ovh1.ec-m.fr
```

Serveur et Identifiant que l'on utilisera dans la suite.

## serveur ovh

Une fois connecté, vous pouvez trouver le dossier `www/`{.fichier}. C'est ici que vous allez mettre le contenu de votre site. Pour l'instant il contient juste le fichier `index.html`{.fichier}. Vous pouvez lire et modifier ce fichier directement via la console, mais ce n'est pas très pratique...

On va donc plutôt créer nos fichiers sur notre ordinateur, puis les copier et les envoyer au serveur ovh1.

Pour copier un fichier, il existe la commande `cp`. On l'utilise comme ça :

```
cp [option] fichier_source fichier_destination
```

Si aucun fichier de ce nom n'existe à la destination, il sera créé. S'il existe déjà, il sera remplacé.

On peut également copier des dossiers. Vous en trouverez quelques utilisations de base dans [ce tuto](http://www.commandeslinux.fr/commande-cp/). On peut notamment retenir :

```
cp -r source destination  # Copie récursive (pour copier des dossiers)
```

```
cp -p source destination  # Copie en conservant les droits du fichier
```

Le problème de `cp`, c'est qu'on ne peut l'utiliser que localement pour faire une copie sur notre machine.

Pour copier un fichier vers un serveur (et inversement), on utilise donc la commande `scp`, signifiant *Secure Copy Protocol*. Cette copie utilise le protocole SSH pour assurer l'authenticité et la confidentialité du transfert. Elle s'utilise de la même manière que `cp` :

```
scp [option] fichier_source fichier_destination
```

Pour l'essayer, créez un index.html sur votre machine et copiez-le vers `ovh1.ec-m.fr` dans le dossier www/.

Depuis votre machine (sans être déjà connecté à `ovh1.ec-m.fr`), ça donne :

```
scp chemin/index.html mon_herbe@ovh1.ec-m.fr:www/index.html
```

Si vous allez vérifier sur `ovh1.ec-m.fr`, votre fichier a bien remplacé l'ancien index.html.

> Incroyable.

## Copie et Compression de dossiers

Comme pour `cp`, vous pouvez utiliser `scp` pour copier des dossiers. Le problème, c'est que les copier tels quels prend du temps. On veut donc les compresser avant de les transférer. Dans le monde UNIX, on utilise les archives GNU tar avec la commande `tar`. Cette commande permet de concaténer plusieurs fichiers en un seul et même fichier. En l'utilisant sur un dossier, cela conserve sa structure et ses droits. La syntaxe est la suivante :

Pour créer l'archive d'un dossier :

```
tar -cvf archive_dossier.tar dossier/
```

* `c` signifie qu'on crée une archive.
* `v` désigne le mode "verbeux" (il affiche ce qu'il fait).
* `f` signifie qu'on utilise le fichier en paramètre.

Ensuite, pour extraire ce dossier :

```
tar -xvf archive_dossier.tar
```

* `x` signifie qu'on extrait l'archive.

{% attention %}
Ici le fichier .tar **n'est pas encore compressé**. Pour le compresser, on va ici choisir Lzma, la méthode utilisée par 7zip.
{% endattention %}

Vous pouvez compresser votre archive manuellement avec la commande `xz` :

```
xz archive_dossier.tar
```

Un fichier *"archive_dossier.tar.xz"* est alors créé. Pour le décompresser, on utilise :

```
xz -d archive_dossier.tar.xz
```

Une autre méthode plus simple est de compresser lors de l'archivage `tar`, en rajoutant `J` en option :

```
 tar -Jcvf archive_dossier.tar.xz dossier/
```

Et idem lors de l'extraction.

Pour tester par vous-même : Créez un petit projet contenant par exemple un fichier html, un fichier css et un fichier js, puis copiez-le vers `ovh1.ec-m.fr` en utilisant l'archivage et la compression !
