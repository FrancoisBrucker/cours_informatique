---
layout: layout/post.njk

title: openssl

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- TBD

- ajouter sub-keys avec acron2.
`❯ echo "coucou" | openssl base64 | openssl base64 -d`

- signature avec openssl <https://www.zimuel.it/blog/sign-and-verify-a-file-using-openssl>
 -->

Nous allons faire les meme étapes que le protocole openPGP avec la suite d'outils de chiffrement donné par [openSSL](https://www.openssl.org/) pour bien séparer les différentes étapes. Si vous voulez utiliser pleinement le protocole openPGP, utilisez cependant plutôt un outil dédié gomme [Gnupg](https://www.gnupg.org/), ci-après.

Placez vous dans un dossier où vous pourrez placer tous les fichiers nécessaires

> TBD <https://www.scottbrady.io/openssl/creating-rsa-keys-using-openssl>

## Installation

{% lien %}
<https://www.openssl.org/>
{% endlien %}

On utilise la version 3 d'openssl :

```shell
❯ openssl --version
OpenSSL 3.6.0 1 Oct 2025 (Library: OpenSSL 3.6.0 1 Oct 2025)
```

### Linux

```shell
❯ sudo apt install openssl
```

### Macos

```shell
❯ brew install openssl
```

### Windows

On utilise [winget](https://learn.microsoft.com/fr-fr/windows/package-manager/winget/), le gestionnaire de paquet de Windows 11.

1. recherche de openssl dans la liste des paquets disponibles : <https://winget.run/>
2. on utilise le paquet [`OpenSSL.Light`](https://winget.run/pkg/ShiningLight/OpenSSL.Light)

Une fois le parquet installé, il faut encore ajouter le chemin d'exécution. Pour cela :

1. commencez par trouver l'endroit où est installé openssl (qui moi c'est`C:\Program Files\OpenSSL-Win64\bin\`{.fichier})
2. utilisez [ce tutoriel](https://lecrabeinfo.net/tutoriels/modifier-le-path-de-windows-ajouter-un-dossier-au-path/) pour l'ajouter aux chemins d'exécution

## Clés du chiffrement asymétrique

{% lien %}
[RSA openSSL](https://en.wikibooks.org/wiki/Cryptography/Generate_a_keypair_using_OpenSSL)
{% endlien %}

```sh
openssl genpkey -help
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

## Clé du chiffrement symétrique

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

## Chiffrement symétrique

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

> TBD faire avec K et IV sans -p

## Chiffrement asymétrique de la clé symétrique

> TBD faire avec sign then encrypt. Comme ça on cache l'expéditeur
> puis zip les trois fichiers à envoyer.

### Signature

On signe un hash. OpenSSL propose plein de fonction de hash différente :

```sh
 openssl dgst -list
```

On va utiliser sha256 pour signer le message chiffré avec notre clé privée :

```sh
openssl dgst -sha256 -sign private_key.pem -out msg.txt.zip.encrypted.sign.sha256 msg.txt.zip.encrypted
```

### Chiffrement de la clé

Chiffrons la clé symétrique avec la clé publique de notre interlocuteur :

```sh
openssl pkeyutl -encrypt -in symmetric_key -pubin -inkey public_key.pem -out symmetric_key.encrypted
```

## Envoi du message

Il faut envoyer :

1. le message chiffré : `msg.txt.zip.encrypted`{.fichier}
2. la signature du message chiffré : `msg.txt.zip.encrypted.sign.sha256`{.fichier}
3. la clé symétrique chiffrée avec la clé publique de l'interlocuteur : `symmetric_key.encrypted`{.fichier}

## Déchiffrement

Vous devez avoir :

1. la clé publique de l'envoyeur
2. votre clé privée

### Vérification de la signature

```sh
openssl dgst -verify public_key.pem -signature msg.txt.zip.encrypted.sign.sha256 msg.txt.zip.encrypted    
```

Si tout s'est bien passé vous devriez voir `Verified OK` comme réponse (sinons vous auriez eu `Verification failure` comme réponse).

### Déchiffrement de la clé symétrique

```sh
openssl pkeyutl -decrypt -inkey private_key.pem -in symmetric_key.encrypted -out symmetric_key
```

### Déchiffrement du message

```sh
openssl enc -d -p -chacha20 -in msg.txt.zip.encrypted -kfile symmetric_key -pbkdf2 -out msg.txt.zip
```

### Dézippage du message

```sh
unzip msg.txt.zip
```

Et normalement, vous devriez avoir le fichier initial !
