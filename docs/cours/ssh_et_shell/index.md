---
layout: page
title:  "ssh et shell"
tags: informatique graphes
author: "François Brucker"
---


Clés ssh. Connexion à des serveurs distants.

## ssh

### installation

{% details sous Linux %}

A priori déjà installé

{% enddetails %}

{% details sous Mac %}

On l'installe avec [brew](https://brew.sh/) : 

```shell
brew install openssh
```

{% enddetails %}

{% details sous Windows %}

Il y a plusieurs choses à installer. Windows vient avec la partie client d'openssh déjà installée. Il nous reste à installer la partie serveur et faire en sorte que celui ci et l'agent se mettent en route à chaque démarrage.

On commence par installer *OpenSSH serveur*, en suivant le [tuto de microsoft](https://docs.microsoft.com/fr-fr/windows-server/administration/openssh/openssh_install_firstuse) :

   1. Ouvrez *Paramètres*, sélectionnez "*Applications > Applications et fonctionnalités*", puis *Fonctionnalités facultatives*.
   2. recherchez *OpenSSH client* et vérifiez qu'il est déjà installé
   3. recherchez *OpenSSH serveur* et installez le.

Puis on ouvre un powershell en mode administrateur (clique droit sur le menu *démarrer* (le drapeau windows en bas à droite de la barre des tâches) puis on choisit *powershell (en mode administrateur)*). Ensuite on copie colle les commandes qui vont lancer le service et faire en sorte qu'il s'exécutera à chaque lancement (partie *Démarrer et configurer OpenSSH Server* du [tuto](https://docs.microsoft.com/fr-fr/windows-server/administration/openssh/openssh_install_firstuse)) :

```shell
# Start the sshd service
Start-Service sshd

# OPTIONAL but recommended:
Set-Service -Name sshd -StartupType 'Automatic'

# Confirm the firewall rule is configured. It should be created automatically by setup.
Get-NetFirewallRule -Name *ssh*

# There should be a firewall rule named "OpenSSH-Server-In-TCP", which should be enabled
# If the firewall does not exist, create one
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```

Enfin, il faut lancer l'agent ssh et s'assurer qu'il sera démarré automatiquement à chaque démarrage  (on suit le tuto de [gestion des clés OpenSSH](https://docs.microsoft.com/fr-fr/windows-server/administration/openssh/openssh_keymanagement)):

```shell
# Set the sshd service to be started automatically
Get-Service -Name ssh-agent | Set-Service -StartupType Automatic

# Now start the sshd service
Start-Service ssh-agent
```

> L'agent fonctionne différemment sous windows que sous un système unix. Mais normalement, il devrait être reconnu, en particulier par git.

{% enddetails %}

### utilisations

1. [utilisation de ssh]({% link cours/ssh_et_shell/ssh.md %}) où vous apprendrez à créer vos clés et à les utiliser pour vous connecter sur l'ovh
2. [Copie sécurisée scp]({% link cours/ssh_et_shell/ssh_scp.md %}) où vous apprendrez à utiliser scp pour transférer votre site depuis le dév jusqu'à la prod.

> [Le chiffrement RSA]({% link cours/ssh_et_shell/ssh_rsa.md %}) est le fondement mathématiques du chiffrement utilisé par ssh.

> TBD : redirections de port
{: .note}

## shell

POur s'en sortir devant un terminal, qu'il soit en local ou à distance.

### unix

  [shell]({% link cours/ssh_et_shell/le_shell.md %})

### powershell

> TBD : à faire et trier les refs
> * <https://docs.microsoft.com/fr-fr/powershell/scripting/overview?view=powershell-7.1>
> * <https://docs.microsoft.com/fr-fr/powershell/scripting/learn/remoting/ssh-remoting-in-powershell-core?view=powershell-7.1>
> * <https://docs.microsoft.com/fr-fr/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.1>
{: .note}
