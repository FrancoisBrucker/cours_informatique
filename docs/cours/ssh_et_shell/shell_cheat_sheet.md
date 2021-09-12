---
layout: page
title:  "ShellCheatSheet"

category: cours
tags: 
author: Valentin Defrance
---

## Commandes de base

- `cd` : Changer de répertoire. Taper cd .. permet d'aller au répertoire supérieur.
- `pwd` : Imprime sur l'écran de la ligne de commandes le répertoire de travail, c'est-à-dire le répertoire ou le dossier que vous êtes actuellement.
- `ls` : Imprime tous les fichiers dans le répertoire de travail.
- `su` Entrez le mot de passe root: La commande SU donne à l'utilisateur la racine des privilèges.
- `apt-get [package]` : Appelle le Gestionnaire de paquets qui permet de télécharger des logiciels en paquets.
- `nano [file]` : Nano est un éditeur de texte de base qui fonctionne dans la Shell. Il vous permet d'éditer des documents avec les privilèges root si vous avez exécuté SU.
- `rm [file]` : Supprime le fichier spécifié.
- `man [commande]` : Affiche l'aide de cette commande.

## Manipulation de fichier et de dossier

- `cp` : copie de fichier
- `dir` : Affiche le contenu d'un répertoire
- `file` : Détermine le type du fichier
- `gzip` et `gunzip` : Compresse ou décompresse des fichiers
- `ls` : Affiche le contenu de répertoire
- `mv` : Déplace ou renomme des fichiers ou des dossiers
- `mkdir` : création de dossier
- `popd` : Restaure la valeur précédente du répertoire courant
- `pushd` : Sauve et change le répertoire courant
- `pwd` : Affiche le répertoire de travail (Print Working Directory)
- `rcp` : Effectue une copie entre deux ordinateurs
- `rm` : Supprime des fichiers
- `rmdir` : Supprime des dossiers
- `rsh` : Shell à distance
- `rsync` : Copie de fichier à distance en utilisant son propre protocole. Il peut être utilisé au travers de ssh ou de rsh.
- `scp` : Copie des fichiers entre deux machines au travers d'une connexion ssh
- `sync` : Synchronise les données entre le disque dur et la mémoire
- `tar` : Créateur d'archive (à l'origine pour cassette)
- `ln` : Créer un lien.
- `split` : Diviser un fichier.
- `cat` : Affiche ou concatène le contenu d'un ou plusieurs fichier
- `less` : Affiche le contenu d'une fichier à l'écran et permet de le parcourir
- `more` : Affiche le contenu d'une fichier à l'écran et permet de le parcourir

## vim

- `i` : insertion du texte juste avant la position courante du curseur ;
- `I` : insertion du texte juste au début de la ligne courante ;
- `a` : insertion du texte juste après la position courante du curseur ;
- `A` : insertion du texte à la fin de la ligne courante.
- `:w` pour enregistrer
- `:q` pour quitter
- `:wq` pour enregistrer et quitter
- `:x` pour enregistrer et quitter
- `:q!` ignorer les modifications

## Commandes de gestion des utilisateurs

- `su` : Entrez la session en tant que root ou un autre utilisateur.
- `su utilisateur` : En tant que root, entrer comme autre utilisateur.
- `passwd` : Modifier votre mot de passe.
- `who -a -H` : Affiche des informations de la part des utilisateurs connectés.
- `users` : Affiche des informations de la part des utilisateurs connectés au système.
- `id` : Affiche l'information de l'utilisateur actuel.
- `groups` : Affiche les groupes auxquels ils appartiennent à un utilisateur.
- `adduser utilisateur` : Créer un nouvel utilisateur.
- `adduser utilisateur groupe` : Ajouter un utilisateur existant à un groupe existant.
- `adduser --no-create-home utilisateur` : Créer un utilisateur sans répertoire (home).
- `addgroup groupe` : Créer un nouveau groupe.
- `deluser utilisateur` : Supprimer un utilisateur.
- `deluser utilisateur groupe` : Supprime un utilisateur d'un groupe.
- `deluser --remove-home utilisateur` : Supprime un utilisateur et son répertoire (home).
- `delgroup groupe` : Supprime un groupe.
- `usermod -l new_utilisateur` : Changer le nom de l'utilisateur.
- `usermod -d new_home -m utilisateur` : Changer le répertoire (home) d'un utilisateur.
- `groupmod -n new_nom grupo` : Changer le nom d'un groupe.

## Autres

- `clear` : Nettoyer l'écran.
- `reset` : Rétablir la Console.
- `pwd` : Affiche le répertoire courant.
- `hostname` : Affiche le nom du serveur.
- `Ctrl+C` : Fin d'un processus.
- `Ctrl+Z` : Suspend temporairement la mise en œuvre d'un programme.
- `Ctrl+S` : Arrêter le transfert de données à La console de gestion.
- `Ctrl+Q` : Resume, redémarrez le transfert de données.
