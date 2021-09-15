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

Les dernières versions de windows viennent avec tout ssh d'installé. Il faut juste faire en sorte que l'Agent ssh soit lancé au démarrage (on suit le tuto de [gestion des clés OpenSSH](https://docs.microsoft.com/fr-fr/windows-server/administration/openssh/openssh_keymanagement)). Ouvrez un fenêtre **powershell en mode administrateur** (clique droit sur le drapeau, puis choissser *pouwershel (admin)*), puis tapez les commandes :

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

### redirection de port

> TBD : redirection de port
{: .note}

## shell

Pour s'en sortir devant un terminal, qu'il soit en local ou à distance.

### unix

[shell]({% link cours/ssh_et_shell/le_shell.md %})

### powershell

> TBD : à faire et trier les refs
> * <https://docs.microsoft.com/fr-fr/powershell/scripting/overview?view=powershell-7.1>
> * <https://docs.microsoft.com/fr-fr/powershell/scripting/learn/remoting/ssh-remoting-in-powershell-core?view=powershell-7.1>
> * <https://docs.microsoft.com/fr-fr/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.1>
{: .note}
