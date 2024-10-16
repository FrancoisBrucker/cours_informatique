---
layout: layout/post.njk

title: OpenPGP

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[OpenPGP](https://fr.wikipedia.org/wiki/OpenPGP)
{% endlien %}

RSA peut encrypter un nombre plus petit que $n$. On pourrait décomposer un message plus gros en paquets de $T$ bits avec $2^T < n$ mais ce n'est quasi-jamais fait car le codage/décodage est algorithmiquement long.

On utilise alors une technique mixte, issue de [PGP](https://fr.wikipedia.org/wiki/Pretty_Good_Privacy), pour cela.

Supposons qu'Alice veut envoyer un message $m$ à Bob. Il faut de :

1. l'authentification : Alice chiffre le hash de $m$ avec sa clé privée
2. la confidentialité :
   1. une clé $k$ est générée puis chiffrée avec la clé publique de Bob
   2. le message $m$ est compressé puis chiffré  avec la clé $k$ (avec un chiffre symétrique)

Alice envoie à Bob :

1. la signature électronique de son message (le hash de $m$ chiffré avec sa clé privée)
2. la clé $k$ chiffrée avec la clé publique de Bob
3. le message compressé puis chiffré avec la clé $k$

Bob peut alors :

1. retrouver la clé de chiffrement $k$ en utilisant sa clé privée
2. déchiffrer le message avec la clé $k$, puis le décompresser
3. vérifier que le message vient bien d'Alice en comparant :
   - le hash du message
   - le déchiffrement de la signature avec la clé publique d'Alice.

## Avec openSSL

Nous allons faire les meme étapes que le protocole openPGP avec la suite d'outils de chiffrement donné par [openSSL](https://www.openssl.org/) pour bien séparer les différentes étapes. Si vous voulez utiliser pleinement le protocole openPGP, utilisez cependant plutôt un outil dédié gomme [Gnupg](https://www.gnupg.org/), ci-après.

Placez vous dans un dossier où vous pourrez placer tous les fichiers nécessaires

On utilise la version 3 d'openSSL :

```sh
openssl version
```

### Clés du chiffrement asymétrique

{% lien %}
[RAS openSSL](https://en.wikibooks.org/wiki/Cryptography/Generate_a_keypair_using_OpenSSL)
{% endlien %}

```sh
openssl genkpey -help
```

On commence par [générer un couple de clés publique/privée](https://www.openssl.org/docs/man3.0/man1/openssl-genpkey.html) avec RSA :

```sh
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
```

Cette commande va produire un fichier `private_key.pem`{.fichier} au format [PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail). Ce fichier va faire office de clé privée mais **il contient bien le couple des clés publique et privée** :

```sh
openssl rsa -in private_key.pem -text
```

Extrayons la clé publique du fichier `private_key.pem`{.fichier} et stockons là dans le fichier `public_key.pem`{.fichier} :

```sh
openssl rsa -pubout -in private_key.pem -out public_key.pem
```

La taille du fichier `public_key.pem`{.fichier} ne contient **que la clé publique** (il est bien plus petit que le fichier `private_key.pem`{.fichier})

```sh
openssl rsa -pubin -in public_key.pem -text
```

{% exercice %}
Pour bien faire, changez les droits du fichier `private_key.pem`{.fichier} pour qu'il ne soit lisible que par vous.
{% endexercice %}
{% details "solution" %}

```sh
chmod go-r private_key.pem 
```

{% enddetails %}

On peut distribuer notre clé publique pour pouvoir recevoir des messages privés.

{% faire %}
Envoyez par mail votre clé **publique** à la personne avec laquelle vous voulez échanger un message privé. Vous devrez chacun avoir la clé publique de l'autres :

- vous devrez avoir la clé publique de l'autre personne pour chiffrer la clé symétrique
- l'autre personne devra avoir votre clé publique pour vérifier la signature du message chiffré
{% endfaire %}

### Clé du chiffrement symétrique

Créons une clé de 32B = 256b pour être utilisée par chacha20.

```sh
openssl rand -hex -out symmetric_key 32
```

Le fichier `symmetric_key.pem`{.fichier} contient la clé.

{% exercice %}
Vérifiez que la taille du fichier `symmetric_key.pem`{.fichier} est bien compatible avec une clé de 256b.
{% endexercice %}
{% details "solution" %}

```sh
wc -c symmetric_key
```

Donne 65. C'est cohérent :

- 1 caractère pour le retour à la ligne final
- un byte est codée sur 2 digit hexadécimaux. Il y a donc $(65-1) / 2 = 32B$
- un Byte vaut 8b, on a bien $32 \cdot 8 = 256b$

{% enddetails %}

### Chiffrement symétrique

On écrit un petit message à envoyer :

```sh
echo "Un coucou chiffré." > msg.txt
```

On commence par compresser ce fichier (on utilise ici zip, mais vous pouvez utiliser ce que vous voulez) :

```sh
zip -u msg.txt.zip msg.txt
```

OpenSSL permet le chiffrement symétrique avec plein d'algorithmes différents :

```sh
openssl enc -ciphers
```

Chiffrons avec chacha20 :

```sh
openssl enc -p -chacha20 -in msg.txt.zip -out msg.txt.zip.encrypted -kfile symmetric_key -pbkdf2
```

{% info %}
On utilise ici un passphrase qui va dériver les paramètres de chacha : une clé de chiffrement et un IV.
On a utilisé ici des clés explicites. On peut aussi passer *via* des passphrases dont sont dérivées les clés et IV :

```sh
openssl enc -p -chacha20 -in msg.txt.zip -out msg.txt.zip.encrypted -K $(openssl rand -hex -out symmetric_key 32) -iv $(openssl rand -hex 16)
```

{% endinfo %}

> TBD faire avec K et IV

### Chiffrement asymétrique de la clé symétrique

> TBD faire avec sign then encrypt. COmme ça on cache l'expéditeur
> puis zip les trois fichiers à envoyer.

#### Signature

On signe un hash. OpenSSL propose plein de fonction de hash différente :

```sh
 openssl dgst -list
```

On va utiliser sha256 pour signer le message chiffré avec notre clé privée :

```sh
openssl dgst -sha256 -sign private_key.pem -out msg.txt.zip.encrypted.sign.sha256 msg.txt.zip.encrypted
```

#### Chiffrement de la clé

Chiffrons la clé symétrique avec la clé publique de notre interlocuteur :

```sh
openssl pkeyutl -encrypt -in symmetric_key -pubin -inkey public_key.pem -out symmetric_key.encrypted
```

### Envoi du message

Il faut envoyer :

1. le message chiffré : `msg.txt.zip.encrypted`{.fichier}
2. la signature du message chiffré : `msg.txt.zip.encrypted.sign.sha256`{.fichier}
3. la clé symétrique chiffrée avec la clé publique de l'interlocuteur : `symmetric_key.encrypted`{.fichier}

### Déchiffrement

Vous devez avoir :

1. la clé publique de l'envoyeur
2. votre clé privée

#### Vérification de la signature

```sh
openssl dgst -verify public_key.pem -signature msg.txt.zip.encrypted.sign.sha256 msg.txt.zip.encrypted    
```

Si tout s'est bien passé vous devriez voir `Verified OK` comme réponse (sinons vous auriez eu `Verification failure` comme réponse).

#### Déchiffrement de la clé symétrique

```sh
openssl pkeyutl -decrypt -inkey private_key.pem -in symmetric_key.encrypted -out symmetric_key
```

#### Déchiffrement du message

```sh
openssl enc -d -p -chacha20 -in msg.txt.zip.encrypted -kfile symmetric_key -pbkdf2 -out msg.txt.zip
```

#### Dézippage du message

```sh
unzip msg.txt.zip
```

Et normalement, vous devriez avoir le fichier initial !

## Avec gnupg

{% lien %}

- [GnuPG](https://www.gnupg.org/)
- [tuto gpg](https://smarttech101.com/how-to-encrypt-and-sign-your-files-using-gpg/)

{% endlien %}

Le logiciel gnuPG permet de rendre plus pratique les diverses opérations faites précédemment. Il permet également un partage de clés publique via un réseau de confiance. Une clé publique va être signée par d'autres personnes, ce qui permet de la *valider* : si une clé est signée par une personne que vous connaissez, vous aurez confiance en sa véracité.

{% info %}
Ne signez les clés publique que des personnes que vous connaissez.
{% endinfo %}

On utilise la version 2.4.3 de GnuPG :

```sh
$ gpg --version
gpg (GnuPG) 2.4.3
libgcrypt 1.10.2
Copyright (C) 2023 g10 Code GmbH
License GNU GPL-3.0-or-later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Home: /Users/fbrucker/.gnupg
Algorithmes pris en charge :
Clef publique : RSA, ELG, DSA, ECDH, ECDSA, EDDSA
Chiffrement : IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256,
              TWOFISH, CAMELLIA128, CAMELLIA192, CAMELLIA256
Hachage : SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
Compression : Non compressé, ZIP, ZLIB, BZIP2
```

On voit que chacha20 n'est pas pas pris en compte comme algorithme de chiffrage, ce qui est dommage. Nous utiliserons donc les algorithmes par défaut, qui sont :

1. `RSA` comme gestionnaire de clés asymétrique
2. `AES256` comme algorithme de chiffrement
3. `SHA512`comme algorithme de hash

### Création de clés

```sh
gpg --full-generate-key
```

1. `RSA and RSA` : pour le chiffrement de la clé symétrique et la signature
2. taille de clé 3072
3. expire d'ici 10 jours.
4. tapez une passphrase qui protège votre clé. Ne l'oubliez pas

Vous pouvez voir votre clé :

```sh
gpg --list-keys  
```

Nous allons tout de suite créer un fichier de révocation de la clé, au cas où vous perdriez votre passphrase ou que clé privée soit compromise.

```sh
gpg --output revoke-gpg.asc --gen-revoke <id clé>
```

Où `<id clé>` est un des composant de votre clé qui l'identifie de façon unique parmi vos clés. Le nom de l'adresse mail mail par exemple.

Votre clé publique est :

```sh
gpg --armor --export <id clé>
```

Et si vous voulez la sauver dans un fichier `pub.gpg`{.fichier} :

```sh
gpg --armor --output pub.gpg --export <id clé>
```

### Préférences de clés

```sh
gpg --edit-key <id clé>
```

Vous vous retrouvez devant un prompt. Vous pouvez taper `help` pour l'aide. Tapez `setpref` et regardez vos préférences. Vous devriez y voir les différents algorithmes utilisés :

```sh
gpg> setpref
Définir la liste de préférences en :
     Chiffrement : AES256, AES192, AES, 3DES
     AEAD: OCB
     Hachage : SHA512, SHA384, SHA256, SHA224, SHA1
     Compression : ZLIB, BZIP2, ZIP, Non compressé
     Fonctionnalités : MDC, AEAD, Serveur de clefs sans modification
Faut-il vraiment mettre à jour les préférences ? (o/N) n
```

Vous pouvez ensuite taper `quit` pour quitter l'interface.

```sh
gpg> quit
```

### Gestion des clés

Pour pouvoir envoyer des messages à quelqu'un, il vous faut avoir sa clé publique.

{% faire %}
Envoyez votre clé publique à votre correspondant, et récupérez la sienne.
{% endfaire %}

```sh
gpg --import public-key.pgp
```

Vous pouvez ensuite voir que la clé a bien été ajoutée à votre trousseau de clés :

```sh
gpg --list-keys        
```

Vous pouvez, si vous le désirez, signer sa clé :

```sh
gpg> sign

```

### Utilisation

Chiffrement :

```sh
gpg --output msg.txt.gpg --encrypt --recipient <recipient id> msg.txt
```

Chiffrement et signature du message :

```sh
gpg --output msg.txt.gpg --encrypt --sign --recipient <recipient id> msg.txt
```

Uniquement signature d'un message en clair

```sh
gpg --output msg.txt.sign --clearsign msg.txt
```

Déchiffrement :

```sh
gpg --output msg.txt --decrypt msg.txt.gpg
```

{% info %}
> TBD <https://unix.stackexchange.com/questions/60213/gpg-asks-for-password-even-with-passphrase>
{% endinfo %}

### Gestion des clés GPG

> TBD : faire mieux et plus clair.

{% lien %}

- [clés et sous clés GPG](https://wiki.debian.org/fr/Subkeys)
- [sous clés GPG](https://mikeross.xyz/create-gpg-key-pair-with-subkeys/)

{% endlien %}

#### utilitaire

{% lien %}
[GPG TUI](https://github.com/orhun/gpg-tui)
{% endlien %}

#### serveur de clés

> TBD Permet d'utiliser des clés stockées dans un serveur de clé
> <https://www.gnupg.org/gph/en/manual.html#AEN464>
>
> 1. le faire.
> 2. se signer mutuellement les clés.

### Fichiers de configurations

{% lien %}
[Fichiers de configurations](https://www.gnupg.org/documentation/manuals/gnupg/GPG-Configuration.html)
{% endlien %}

Dans le dossier `~/.gnupg`.
