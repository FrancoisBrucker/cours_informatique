---
layout: layout/post.njk

title: ssh
authors: 
  - "Herbelleau Romain"
  - "Laurent Léo"
  - "Dégeorges Laurie"
  - "François Brucker"


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Installation et utilisation (basique) de ssh.

<!-- fin résumé -->

## Installation

la commande `ssh` doit être Doit être installée par défaut :

```sh
$ ssh                
usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface] [-b bind_address]
           [-c cipher_spec] [-D [bind_address:]port] [-E log_file]
           [-e escape_char] [-F configfile] [-I pkcs11] [-i identity_file]
           [-J destination] [-L address] [-l login_name] [-m mac_spec]
           [-O ctl_cmd] [-o option] [-P tag] [-p port] [-Q query_option]
           [-R address] [-S ctl_path] [-W host:port] [-w local_tun[:remote_tun]]
           destination [command [argument ...]]

```

### Agent

La seule chose à possiblement faire est de mettre en place le [ssh-agent](https://en.wikipedia.org/wiki/Ssh-agent). L'agent est un démon permettant de gérer sos clés pour vous.

Pour savoir si vous avez un agent ssh opérationnel, tapez la commande :

```sh
ssh-add -l
```

Si cette commande répond :

```sh
$ ssh-add -l
Could not open a connection to your authentication agent.

```

C'est que vous n'avez pas d'agent. Il faut lancer l'agent à la connexion de chaque shell. Via la commande :

```sh
eval "$(ssh-agent -s)"
```

Si vous ne voulez pas le faire dans chaque terminal, la façon la plus simple est d'ajouter la ligne précédente à la à la fin de votre `~/.profile`{.fichier} (s'il n'existe pas créez le).

{% info %}
Si vous voulez plus d'options vous pouvez aussi copier-coller le contenu de ce lien : [ajout ssh-agent](https://gist.github.com/gabetax/3756756)
{% endinfo %}

### Sous windows sans WSL

1. <https://davidaugustat.com/windows/windows-11-setup-ssh>
2. old w10 : https://learn.microsoft.com/fr-fr/windows-server/administration/openssh/openssh_keymanagement

Les dernières versions de windows viennent avec tout ssh d'installé. Il faut juste faire en sorte que l'Agent ssh soit lancé au démarrage (on suit le tuto de [gestion des clés OpenSSH](https://docs.microsoft.com/fr-fr/windows-server/administration/openssh/openssh_keymanagement)). Ouvrez un fenêtre **powershell en mode administrateur** (clique droit sur le drapeau, puis choisissez *powershell (admin)*), puis tapez les commandes :

```
# Set the sshd service to be started automatically
Get-Service -Name ssh-agent | Set-Service -StartupType Automatic

# Now start the sshd service
Start-Service ssh-agent
```

L'agent fonctionne différemment sous windows que sous un système unix. Mais normalement, il devrait être reconnu, en particulier par git.

## ssh, c’est quoi ?

{% lien %}

[ssh en 10min](https://www.youtube.com/watch?v=3-MDtASgSo8)

{% endlien %}

**Secure Shell (SSH)** est à la fois un programme informatique et un protocole de communication sécurisé. Le protocole de connexion impose un échange de clés de chiffrement en début de connexion. Par la suite, tous les segments TCP sont authentifiés et chiffrés. Il devient donc impossible d'utiliser un sniffer pour voir ce que fait l'utilisateur. Il se comporte comme [tls](../tls){.interne} pour les connexions entre ordinateurs.

{% lien %}

- [ssh handshake](https://info.support.huawei.com/info-finder/encyclopedia/en/SSH.html)
- [chiffrements utilisés](https://bash-prompt.net/guides/bash-ssh-ciphers/)
{% endlien %}

On utilise ssh pour garantir de l'authenticité et des ordinateurs sur lesquels on se connecte et des utilisateur qui s'y connecte. Il y aura ainsi essentiellement 2 jeux de clés asymétriques :

1. la paire de clé identifiant l'ordinateur sur lequel un utilisateur veut se connecter
2. la paire de clé identifiant l'utilisateur

{% lien %}

1. [ssh en 5 parties](https://www.youtube.com/watch?v=QGixbJ9prEc&list=PLQqbP89HgbbYIarPqOU8DdC2jC3P3L7a6)
2. [ssh crash course](https://www.youtube.com/watch?v=hQWRp-FdTpc)
3. [deep dive](https://tusharf5.com/posts/ssh-deep-dive/)

{% endlien %}

## Connexion

Supposons que je veuille me connecter à une machine distante dont je connais le nom : `roucas100.etu.ec-m.fr` (cette machine n'est accessible que si vous êtes déjà sur le réseau de l'école centrale méditerranée).

{% note "**Connection depuis l'extérieur**" %}
Si vous n'êtes pas initialement connecté sur le réseau de l'école, remplacez `roucas100.etu.ec-m.fr` par `sas1.ec-m.fr` qui est kl'ordinateur accessible depuis internet.
{% endnote %}

Je dois me connecter en tant qu'utilisateur de cette machine. Pour cela la connection s'effectue toujours en utilisant le schéma d'une URL : `identifiant@machine`. Dan sle cs présent :

```sh
ssh fbrucker@roucas100.etu.ec-m.fr
```

Si c'est la première fois que je me connecte à cette machine, `ssh` me montre la clépublique de la machine `roucas100` et me demande de l'identifier :

```sh
$ ssh fbrucker@roucas100.etu.ec-m.fr
The authenticity of host 'roucas100.etu.ec-m.fr (147.94.25.100)' can't be established.
ED25519 key fingerprint is SHA256:Jf65ebUXhQ1w6+zcCnL8R9cvBMEI8yDvcR+GxtvSHZg.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? 
```

On voit que la clé est de type [ED25519](https://fr.wikipedia.org/wiki/EdDSA) qui est un chiffrement par courbe elliptique (celle d'Edwards tordue). Si je peux certifier que c'est bien la machine sur laquelle je veux m'identifier, je tape `yes` et peut taper mon mot de passe pour me connecter.

> TBD : <https://medium.com/risan/upgrade-your-ssh-key-to-ed25519-c6e8d60d3c54>

Si la clé de la machine change cela peut-être à cause d'une attaque de type *man in the middle* et ssh refuse de se connecter :

```sh
$ ssh fbrucker@roucas100.etu.ec-m.fr
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:Jf65ebUXhQ1w6+zcCnL8R9cvBMEI8yDvcR+GxtvSHZg.
Please contact your system administrator.
Add correct host key in /users/home3/fbrucker/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /users/home3/fbrucker/.ssh/known_hosts:32
Host key for roucas100.etu.ec-m.fr has changed and you have requested strict checking.
Host key verification failed.

```

La liste des ordinateurs connus ainsi que leur clé publique (sur lesquels on s'est déjà connecté) est stockée dans le fichier : `~/.ssh/known_hosts`.

## Identification des utilisateurs

Il est très utile de laisser ssh nous identifier sans avoir à taper de mots de passe, via notre couple de clé publique/privée.

### Générer une clé

```sh
ssh-keygen
```

{% attention %}
Comme vous allez vous servir de cette clé pour vous connecter automatiquement à des ordinateurs distant, Il ***faut*** mettre une passphrase sécurisée à votre clé.
{% endattention %}

Si vous suivez les comportement par défaut, vous aller créer deux fichier dans votre dossier `~/.ssh`{.fichier} :

- `id_rsa` qui contient votre clé privée
- `id_rsa.pub` qui contient votre clé publique

{% faire %}
Regardez les droits de ces deux fichiers ainsi que du dossier `~/.ssh`.
{% endfaire %}

> TBD : [ssh et RSA](https://www.vidarholen.net/contents/blog/?p=24)

### Hash de la clé

{% lien %}
[randomart](https://blog.benjojo.co.uk/post/ssh-randomart-how-does-it-work-art)
{% endlien %}

```sh
ssh-keygen -lv
```

### Stocker sa clé dans l'agent

Le rôle de l'agent est de stocker votre clé.

Ajouter la :

```sh
ssh-add
```

L'agent vous demandera de taper votre passphrase pour déchiffrer votre clé, puis l'ajoutera à son trousseau. Et voilà. Votre clé est chargée. vérifiez le en tapant :

```sh
ssh-add -l
```

Vous n'aurez plus besoin de taper cette passphrase tant que l'agent sera actif. C'est à dire jusqu'au reboot de votre machine. En démarrant une nouvelle session et en affichant la liste des identités représentées par l'agent avec `ssh-add -l`, vous obtenez donc le message suivant :

```
the agent has no identities
```

Il faut donc récupérer votre clé ssh là où vous l'avez laissée. Rien de nouveau ici, c'est simplement une routine à prendre.

### Connexion avec agent

Pour que vous puissiez vous connecter à une machine via vos clés, il faut que votre clé publique soit disponible sur la machine distante, dans le fichier `~.ssh/authorized-keys`{.fichier}. Chaque ligne de ce fichier contient une clé publique qui est autorisée à se connecter.

Connectez vous sur `roucas100.etu.ec-m.fr` et ajoutez (ou créez) une ligne au fichier  `~.ssh/authorized-keys`{.fichier} contenant votre clé publique :

```
cat id_rsa.pub >> ~/.ssh/authorized_keys
```

Vous pouvez ensuite vous déconnecter, puis vous reconnecter sans avoir besoin de taper un mot de passe.

{% faire %}
Faire cette procédure pour vous connecter sans mot de passe.
{% endfaire %}

### Stockage des clés

Il est de coutume de stocker ses clés sur un ordinateur accessible de l'internet. Il est alors possible d'y accéder depuis de multiple ordinateurs sans avoir à dupliquer la clé.

Pour cela, il fut pouvoir se connecter sur la machine distance en *emportant l'agent avec soit*. Ceci se fait en ajoutant l'option `-A` à la connection ssh. Le principe est alors le suivant :

1. accès à l'ordinateur possédant les clés avec **notre propre** agent : `ssh -A identifiant@sas1.ec-m.fr`
2. ajout de la clé depuis cette machine : `ssh-add`
3. retour chez soit en se déconnectant de la machine : `exit`
4. connection à un autre ordinateur où notre clé est autorisée : `ssh identifiant@ovh1.ec-m.fr`

## Copie de fichiers


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

## Amusons-nous avec la redirection de ports

### Une redirection de port

```
              22               22
so-high ---------  sas1  --------- roucas100.etu
```

La commande `ssh -L4000:roucas100.etu:22 fbrucker@sas1.ec-m.fr` depuis ma machine nommée so-high demande à :

1. faire une connexion ssh (depuis le port 22) sur le sas
2. que cette connexion fasse un lien entre :
   - le port 4000 de so-high
   - le port 22 de roucas100.etu

Ceci est possible puisque sas1 "voit" roucas100.etu et so-high.

En laissant cette connexion ouverte, dans un autre terminal on peut maintenant se connecter directement sur le port 22 de roucas100.etu (c'est à dire le démon ssh de roucas100.etu) en utilisant le port 4000 de so-high :

```
ssh -p4000 fbrucker@localhost
```

### Plusieurs redirection de port

On suppose que la première redirection est faite :

```
ssh -L4000:roucas100.etu:22 fbrucker@sas1.ec-m.fr`
```

Le port 4000 de so-high est le port 22 de roucas100.etu (via la connexion sas puisqu'il est impossible d'aller directement de l'un à l'autre)

On peut maintenant ramener un autre port de roucas100.etu sur notre machine, par exemple le port 9090 :

```
ssh -L9090:localhost:9090 -p4000 fbrucker@localhost
```

On effectue une connexion sur le port 4000 de localhost (qui est du coup aussi le port 22 de roucas100.etu) et on demande de faire une redirection du port 9090 sur cette machine sur notre machine locale.

Attention, il y a deux fois marqué `localhost` mains ce nest pas le même :

1. le deuxième localhost correspond à la machine qui se connecte, ici so-high
2. le premier localhost correspond à la machine connectée, ici roucas100.etu

Supposons que l'on ait un service uniquement accessible depuis roucas100.etu sur le port 9090. Par exemple une écoute de port (que vous aurez lancé depuis un autre terminal connecté sur roucas100.etu) :

```
nc -l -p 9090 127.0.0.1
```

On peut maintenant directement y accéder avec `nc 127.0.0.1 9090`
