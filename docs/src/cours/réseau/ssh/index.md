---
layout: layout/post.njk

title: ssh

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

1. [ssh en 5 parties](https://www.youtube.com/watch?v=QGixbJ9prEc&list=PLQqbP89HgbbYIarPqOU8DdC2jC3P3L7a6)
2. [ssh crash course](https://www.youtube.com/watch?v=hQWRp-FdTpc)
3. [deep dive](https://tusharf5.com/posts/ssh-deep-dive/)

{% endlien %}

Le nom [ssh](https://fr.wikipedia.org/wiki/Secure_Shell) (_Secure SHell_) permet de faire de la communication sécurisée et regroupe deux usages :

- communication entre deux ordinateurs via une socket chiffrée
- identification par paire de clés.

Nous allons voir dans cette introduction comment utiliser et comprendre ces deux aspects.

{% info %}
On supposera pour les exercices et les exemples que vous êtes étudiants de l'ecm et que vous avez accès aux salles unix de l'école via un login et un mot de passe.
{% endinfo %}

<!-- TBD 

voir comment les connexion ne peuvent pas se faire via un docker ou [un compte aws](https://www.youtube.com/watch?v=u2-2c_nY6lk) 

-->

> TBD refaire avec ici juste ssh login et scp. Pour se connecter et copier
> TBD montrer comment ça marche avec vscode et -J
>
> 1. création de la clé
> 2. accéder à ses clés publiques et privées dans le dossier caché .ssh
> 3. sert d'identification à github ou de connexion à une machine distante
> 4. nécessité d'un agent
> 5. un sas et l'option -J

## Transmission sécurisée

### Connexion

La client ssh est une commande nommée  `ssh` accessible via le terminal. Par exemple la commande suivante :

```shell
$> ssh <login>@<machine>
```

Va initier une connexion sur la machine de nom `<machine>`. Pour que la connexion fonctionne, il faut qu'un serveur ssh écoute sur cette machine sur le port 22.

{% faire %}
Depuis un terminal, connectez-vous sur la machine `sas1.ec-m.fr`.

1. Lorsque l'on vous demandera (en anglais) si vous voulez continuer à vous connecter, répondez `yes`.
2. puis tapez votre mot de passe. Il est **normal** que rien ne s'affiche, les touches sont prisent en compte mais ne sont pas affichées pour des raisons de sécurité
{% endfaire %}
{% details "exemple", "open" %}

En tant que prof, je me connecte à `sas2.ec-m.fr` et pas à sas1 qui est réservé aux étudiants :

```shell
$> ssh sas2.ec-m.fr
The authenticity of host 'sas2.ec-m.fr (2001:660:5404:191::22)' can't be established.
ED25519 key fingerprint is SHA256:A3Bj05ACdCqcuQ34PFfk0TcHlBJ1HtTQKT0nUtaXEnk.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'sas2.ec-m.fr' (ED25519) to the list of known hosts.
(fbrucker@sas2.ec-m.fr) Password for fbrucker@sas2.ec-m.fr:
Last login: Fri Dec 26 10:54:22 2025 from 2a01:cb1c:886:d700:a06a:309c:8628:fd9c
FreeBSD 14.3-RELEASE-p5 GENERIC

Welcome to FreeBSD!

Release Notes, Errata: https://www.FreeBSD.org/releases/
Security Advisories:   https://www.FreeBSD.org/security/
FreeBSD Handbook:      https://www.FreeBSD.org/handbook/
FreeBSD FAQ:           https://www.FreeBSD.org/faq/
Questions List:        https://www.FreeBSD.org/lists/questions/
FreeBSD Forums:        https://forums.FreeBSD.org/

Documents installed with the system are in the /usr/local/share/doc/freebsd/
directory, or can be installed later with:  pkg install en-freebsd-doc
For other languages, replace "en" with a language code like de or fr.

Show the version of FreeBSD installed:  freebsd-version ; uname -a
Please include that output and any error messages when posting questions.
Introduction to manual pages:  man man
FreeBSD directory layout:      man hier

To change this login announcement, see motd(5).
```

{% enddetails %}

La première fois que l'on se connecte sur une machine sa clé publique nous est présentée pour vérification. Nous y reviendrons, contentons nous pour l'instant d'accepter.

Une fois connecté, on peut vérifier le nom de la machine sur laquelle on est :

```shell
$ uname -n
sas1.ec-m.fr

```

### Copie

> TBD ici. Dire que c'est par rapport au home de la destination.
> exemple avec un fichier texte
> faire dans les deux sens

Pour copier un fichier vers un serveur (et inversement), on utilise donc la commande `scp`, signifiant _Secure Copy Protocol_. Elle s'utilise de la même manière que `cp` :

```shell
scp  <fichier source> <fichier destination>
```

Le `<fichier source>` ou `<fichier destination>` être :

- un chemin vers un fichier local
- `login@destination:chemin` où :
  - `login@destination` est la connexion ssh
  - le `chemin` est un chemin absolu ou relatif (à partir de la maison) sur l'ordinateur distant

Par exemple :

```sh
scp index.html fbrucker@sas1.ec-m.fr:html/index.html
```

Va copier le fichier `index.html`{.fichier} du dossier courant du terminal vers le fichier `~/html/index.html`{.fichier} sur la machine distante.

{% exercice %}
Depuis votre machine, récupérez le fichier `/etc/passwd` sur la machine distante et copiez le dans votre maison.
{% endexercice %}
{% details "corrigé" %}

```sh
scp login@sas1.ec-m.fr:/etc/passwd ~
```

Comme `~`{.fichier} est un dossier, le fichier est copié dans ce repertoire.
{% enddetails %}

## Identification

{% lien %}
<https://fr.wikipedia.org/wiki/Signature_num%C3%A9rique>
{% endlien %}

L'authentification d'une personne ou d'une machine s'effectue via l'interaction d'une paire de clé :

- une clé publique `pub` qui est distribuée
- une clé privée `priv` qui est gardé secrète

Et d'une méthode de chiffrement `C(clé, message)` prenant en paramètres une clé et un message et rendant un message chiffré possédant les propriétés suivantes :

- il est _impossible_ (_ie._ trop long) de trouver le message originel à partir de son chiffrement
- Si `C(pub, M) = M'` alors `C(priv, M') = M`
- Si `C(priv, M) = M'` alors `C(pub, M') = M`


> TBD ajout un hash genre sha pour associer une signature à un texte, même long.
> ceci permet de vérifier que l'on connaît le texte sans le transmettre
{% info %}
N'hésitez pas à aller jeter un coup d'œil au cours [de sécurité](/cours/sécurité){.interne} pour avoir tous les détails.
{% endinfo %}

### Processus d'identification

{% lien %}

- [Diffie-Hellman](https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman)
- <https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process>
{% endlien %}

> TBD :
>
> - clé privé / public et principe
> - dire que c'est ce qu'il s'est passé lorsque l'on s'est connecté à la machine
> - dire que fingerprint la clé publique (en vrai un hash).
> - voir le fichier dans /ssh/known_host
> - création d'une paire de clé
> - connexion sur

### Machine distante

> TBD identification de la machine.

Si c'est la première fois que je me connecte à cette machine, `ssh` me montre la clé publique de la machine `roucas100` et me demande de l'identifier :

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







> TBD port 22 de la machine
> ssh login@machine
> scp <chemin relatif local> login@machine:<chemin relatif distant> (ou le contraire)

> TBD chiffrement symétrique rapide
> TBD est-on certain de la machine sur laquelle on se connecte ?

> TBD d'une machine à l'autre dans une salle : `$ uname -n`
> TBD d'une machine au sas : `$ uname -n`
> TBD schéma entrée via le sas : seul port ouvert est le 22 celui de ssh.

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

## Identification des utilisateurs

Il est très utile de laisser ssh nous identifier sans avoir à taper de mots de passe, via notre couple de clé publique/privée.

On utilise ssh pour garantir de l'authenticité et des ordinateurs sur lesquels on se connecte et des utilisateur qui s'y connecte. Il y aura ainsi essentiellement 2 jeux de clés asymétriques :

1. la paire de clé identifiant l'ordinateur sur lequel un utilisateur veut se connecter
2. la paire de clé identifiant l'utilisateur


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


## Exercices

{% aller %}
[exercices](exercices-connexion){.interne}
{% endaller %}
