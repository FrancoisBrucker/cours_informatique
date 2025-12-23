---
layout: layout/post.njk

title: ssh

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD voir comment les connexion ne peuvent pas se faire via un docker.

> TBD refaire avec ici juste ssh login et scp. Pour se connecter et copier
> TBD montrer comment ça marche avec vscode et -J
>
> 1. création de la clé
> 2. accéder à ses clés publiques et privées dans le dossier caché .ssh
> 3. sert d'identification à github ou de connexion à une machine distante
> 4. nécessité d'un agent
> 5. un sas et l'option -J

{% info %}
On supposera ici que vous êtes étudiant de l'ecm et que vous avez accès aux salles unix de l'école via un login et un mot de passe.
{% endinfo %}

## Connexion sécurisée

> TBD port 22 de la machine
> ssh login@machine
> scp <chemin relatif local> login@machine:<chemin relatif distant> (ou le contraire)

> TBD chiffrement symétrique rapide
> TBD est-on certain de la machine sur laquelle on se connecte ?

> TBD d'une machine à l'autre dans une salle : `$ uname -n`
> TBD d'une machine au sas : `$ uname -n`
> TBD schéma entrée via le sas : seul port ouvert est le 22 celui de ssh.

## Identification

### Machine distante

> `~/.ssh/known_hosts`{.fichier}

### Se créer une paire de clé

### Utiliser la clé pour se connecter

> TBD `~/.ssh/authorized_keys`{.fichier}
> TBD on voit qu'il demande la passphrase et plus le mot de passe du login

## Agent

Utilisation (basique) du logiciel ssh. On va voir deux usages important :

- se connecter à une machine distante sur le réseau en assurant un chiffrement de la transmission
- permettre de s'identifier via une paire de clé publique/privée.

## Client

La client ssh est une commande nommée  `ssh` accessible via le terminal :

```sh
$> ssh
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

C'est que vous n'avez pas d'agent, il va vous falloir en créer un.

#### Création sous windows/wsl

{% lien %}
<https://davidaugustat.com/windows/windows-11-setup-ssh>
{% endlien %}

Les dernières versions de windows viennent avec tout ssh d'installé. Il faut juste faire en sorte que l'Agent ssh soit lancé au démarrage (on suit le tuto de [gestion des clés OpenSSH](https://docs.microsoft.com/fr-fr/windows-server/administration/openssh/openssh_keymanagement)).

{% faire %}
Ouvrez un fenêtre **powershell en mode administrateur** (clique droit sur le drapeau, puis choisissez _powershell (admin)_), puis tapez les commandes :

```powershell
# Set the sshd service to be started automatically
Get-Service -Name ssh-agent | Set-Service -StartupType Automatic

# Now start the sshd service
Start-Service ssh-agent
```

{% endfaire %}

L'agent fonctionne différemment sous windows que sous un système unix. Mais normalement, il devrait être reconnu, en particulier par git.

#### Création sous Linux

A priori l'agent est déjà effectif mais si ce n'est pas le cas.
Il faut lancer l'agent à la connexion de chaque shell. Via la commande :

```shell
$ eval "$(ssh-agent -s)"
```

Si vous ne voulez pas le faire dans chaque terminal, la façon la plus simple est d'ajouter la ligne précédente à la à la fin de votre `~/.profile`{.fichier} (s'il n'existe pas créez le) :

{% faire %}
Dans un terminal, tapez la commande :

```shell
$ echo 'eval "$(ssh-agent -s)"' >> $HOME/.profile
```

{% endfaire %}
{% info %}
Si vous voulez plus d'options vous pouvez aussi copier-coller le contenu de ce lien : [ajout ssh-agent](https://gist.github.com/gabetax/3756756)
{% endinfo %}

## ssh, c’est quoi ?

{% lien %}

[ssh en 10min](https://www.youtube.com/watch?v=3-MDtASgSo8)

{% endlien %}

**Secure Shell (SSH)** est à la fois un programme informatique et un protocole de communication sécurisé. Le protocole de connexion impose un échange de clés de chiffrement en début de connexion. Par la suite, tous les segments TCP sont authentifiés et chiffrés. Il devient donc impossible d'utiliser un sniffer pour voir ce que fait l'utilisateur. Il utilise [tls](../tls){.interne} pour les connexions entre ordinateurs.

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
Si vous n'êtes pas initialement connecté sur le réseau de l'école, remplacez `roucas100.etu.ec-m.fr` par `sas1.ec-m.fr` qui est l'ordinateur accessible depuis internet.
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

Si la clé de la machine change cela peut-être à cause d'une attaque de type _man in the middle_ et ssh refuse de se connecter :

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

La liste des ordinateurs connus ainsi que leur clé publique (sur lesquels on s'est déjà connecté) est stockée dans le fichier : `~/.ssh/known_hosts`{.fichier}.

```
       A                   B
     -----               -----
     |   |               |   |
     |   |-------------->|   |
     -----               -----
  known_hosts
clé de machine
```

## Identification des utilisateurs

Il est très utile de laisser ssh nous identifier sans avoir à taper de mots de passe, via notre couple de clé publique/privée.

### Générer une clé

```sh
ssh-keygen
```

{% attention %}
Comme vous allez vous servir de cette clé pour vous connecter automatiquement à des ordinateurs distant, Il **_faut_** mettre une passphrase sécurisée à votre clé.
{% endattention %}

Si vous suivez les comportement par défaut, vous aller créer deux fichier dans votre dossier `~/.ssh`{.fichier} :

- `id_ed25519` qui contient votre clé privée
- `id_ed25519.pub` qui contient votre clé publique

{% faire %}
Regardez les droits de ces deux fichiers ainsi que du dossier `~/.ssh`.
{% endfaire %}

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

```sh
the agent has no identities
```

Il faut donc récupérer votre clé ssh là où vous l'avez laissée. Rien de nouveau ici, c'est simplement une routine à prendre.

### Connexion avec agent

Pour que vous puissiez vous connecter à une machine via vos clés, il faut que votre clé publique soit disponible sur la machine distante, dans le fichier `~.ssh/authorized-keys`{.fichier}. Chaque ligne de ce fichier contient une clé publique qui est autorisée à se connecter.

Connectez vous sur `roucas100.etu.ec-m.fr` et ajoutez (ou créez) une ligne au fichier `~.ssh/authorized-keys`{.fichier} contenant votre clé publique :

```sh
cat id_rsa.pub >> ~/.ssh/authorized_keys
```

Vous pouvez ensuite vous déconnecter, puis vous reconnecter sans avoir besoin de taper un mot de passe.

```
       A                   B
     -----               -----
     |   |               |   |
     |   |-------------->|   |
     -----               -----
  known_hosts        authorized_keys
clé de machine      clé d'utilisateur
```

{% faire %}
Faire cette procédure pour vous connecter sans mot de passe.
{% endfaire %}

### Stockage des clés

Il est de coutume de stocker ses clés sur un ordinateur accessible de l'internet. Il est alors possible d'y accéder depuis de multiple ordinateurs sans avoir à dupliquer la clé.

Pour cela, il fut pouvoir se connecter sur la machine distance en _emportant l'agent avec soit_. Ceci se fait en ajoutant l'option `-A` à la connection ssh. Le principe est alors le suivant :

1. accès à l'ordinateur possédant les clés avec **notre propre** agent : `ssh -A identifiant@sas1.ec-m.fr`
2. ajout de la clé depuis cette machine : `ssh-add`
3. retour chez soit en se déconnectant de la machine : `exit`
4. connection à un autre ordinateur où notre clé est autorisée : `ssh identifiant@ovh1.ec-m.fr`

## Copie de fichiers

Pour copier un fichier vers un serveur (et inversement), on utilise donc la commande `scp`, signifiant _Secure Copy Protocol_. Cette copie utilise le protocole SSH pour assurer l'authenticité et la confidentialité du transfert. Elle s'utilise de la même manière que `cp` :

```sh
scp [option] fichier_source fichier_destination
```

Pour l'essayer, créez un index.html sur votre machine et copiez-le vers `ovh1.ec-m.fr` dans le dossier www/.

Depuis votre machine (sans être déjà connecté à `ovh1.ec-m.fr`), ça donne :

```sh
scp chemin/index.html mon_herbe@aioli.ec-m.fr:static/index.html
```

Si vous allez vérifier sur `aioli.ec-m.fr`, votre fichier a bien remplacé l'ancien index.html.

## Exercices

{% aller %}
[exercices](exercices-connexion){.interne}
{% endaller %}
