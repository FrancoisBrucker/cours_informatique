---
layout: layout/post.njk

title: OpenPGP

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



<!-- TBD

- subkeys : <https://wiki.debian.org/Subkeys>
- list commandes : <https://rgoulter.com/blog/posts/programming/2022-06-10-a-visual-explanation-of-gpg-subkeys.html>
- tuto complet avec sub keys et tout : <https://www.youtube.com/watch?v=6i8vPJLAPRs&list=PLPj3KCksGbSZkVpgAZjAFfFp4D0SHLnFw>
- revoke key : <https://superuser.com/questions/1526283/how-to-revoke-a-gpg-key-and-upload-in-gpg-server>
- gpg config : <https://www.git-tower.com/blog/setting-up-gpg-windows>
- <https://une-tasse-de.cafe/blog/yubikey/>

 -->

{% lien %}

- [GnuPG](https://www.gnupg.org/)
- [tuto gpg](https://smarttech101.com/how-to-encrypt-and-sign-your-files-using-gpg/)
- [autre tuto](https://rgoulter.com/blog/posts/programming/2022-06-10-a-visual-explanation-of-gpg-subkeys.html)

{% endlien %}

Le logiciel gnuPG permet de sécuriser ses fichiers et ses communications.rendre plus pratique les diverses opérations faites précédemment. Il permet également un partage de clés publique via un réseau de confiance. Une clé publique va être signée par d'autres personnes, ce qui permet de la *valider* : si une clé est signée par une personne que vous connaissez, vous aurez confiance en sa véracité.

{% info %}
Ne signez les clés publique que des personnes que vous connaissez.
{% endinfo %}

## Installation

{% lien %}
<https://www.gnupg.org/>
{% endlien %}

On utilise la version 2.4 :

```sh
❯ gpg --version
gpg (GnuPG) 2.4.8
libgcrypt 1.11.2
Copyright (C) 2025 g10 Code GmbH
License GNU GPL-3.0-or-later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Home: /Users/fbrucker/.gnupg
Supported algorithms:
Pubkey: RSA, ELG, DSA, ECDH, ECDSA, EDDSA
Cipher: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH,
        CAMELLIA128, CAMELLIA192, CAMELLIA256
Hash: SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
Compression: Uncompressed, ZIP, ZLIB, BZIP2

```

On voit que chacha20 n'est pas pas pris en compte comme algorithme de chiffrage, ce qui est dommage. Nous utiliserons donc les algorithmes par défaut, qui sont :

1. `ECDSA` comme gestionnaire de clés asymétrique
2. `AES256` comme algorithme de chiffrement
3. `SHA512`comme algorithme de hash

### Linux

```sh
❯ sudo apt install openssl
```

### Macos

```sh
❯ brew install openssl
```

### Windows

On utilise [winget](https://learn.microsoft.com/fr-fr/windows/package-manager/winget/), le gestionnaire de paquet de Windows 11.

1. recherche de openssl dans la liste des paquets disponibles : <https://winget.run/>
2. on utilise le paquet [`GnuPG.GnuPG`](https://winget.run/pkg/GnuPG/GnuPG)

Une fois le parquet installé, il devrait être disponible dans une **nouvelle** fenêtre de powershell.

### Dossier de configuration/clés

{% lien %}
[Fichiers de configurations](https://www.gnupg.org/documentation/manuals/gnupg/GPG-Configuration.html)
{% endlien %}

Ce fichier va contenir et la configuration et les clés.

- `~/.gnupg`{.fichier} sous linux/macos
- `C:\Users\<nom utilisateur>\AppData\Roaming\gnupg`{.fichier} sous windows

## Chiffrer et déchiffrer des fichiers

{% lien %}
[Chiffrer/déchiffrer des fichiers avec GPG](https://www.youtube.com/watch?v=4z1LSbFHtQA)
{% endlien %}

> TBD comme chiffrement/déchiffrement  avec passphrase.
> tui puis en ligne de commande.

## Création de clés

{% lien %}
<https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key>
{% endlien %}

```sh
❯ gpg --full-generate-key
```

{% details "sortie" %}

```sh
gpg (GnuPG) 2.4.8; Copyright (C) 2025 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

gpg: directory '/Users/fbrucker/.gnupg' created
Please select what kind of key you want:
   (1) RSA and RSA
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
   (9) ECC (sign and encrypt) *default*
  (10) ECC (sign only)
  (14) Existing key from card
Your selection? 9
Please select which elliptic curve you want:
   (1) Curve 25519 *default*
   (4) NIST P-384
   (6) Brainpool P-256
Your selection? 1
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 7
Key expires at Sun Oct 26 17:42:59 2025 CET
Is this correct? (y/N) y

GnuPG needs to construct a user ID to identify your key.

Real name: François Brucker
Email address: francois.brucker@centrale-med.fr
Comment: Je suis professeur d'informatique
You are using the 'utf-8' character set.
You selected this USER-ID:
    "François Brucker (Je suis professeur d'informatique) <francois.brucker@univ-amu.fr>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: /Users/fbrucker/.gnupg/trustdb.gpg: trustdb created
gpg: directory '/Users/fbrucker/.gnupg/openpgp-revocs.d' created
gpg: revocation certificate stored as '/Users/fbrucker/.gnupg/openpgp-revocs.d/1746B97A12A97C32CB74C6157D305414B27F8E59.rev'
public and secret key created and signed.

pub   ed25519 2025-10-19 [SC] [expires: 2025-10-26]
      1746B97A12A97C32CB74C6157D305414B27F8E59
uid                      François Brucker (Je suis professeur d'informatique) <francois.brucker@univ-amu.fr>
sub   cv25519 2025-10-19 [E] [expires: 2025-10-26]


```

{% enddetails %}

1. `ECC (sign and encrypt)` (_Elliptic Curve Cryptography_): pour le chiffrement de la clé symétrique et la signature
2. `Curve 25519` : la courbe utilisée
3. Expire d'ici 7 jours.
4. Mettez vos identifiant
5. tapez une passphrase qui protège votre clé. **Ne l'oubliez pas**

{% note "**Bon usage**" %}

Il est recommandé de mettre une date d'expiration à votre clé. Ceci pour plusieurs raisons :

1. On fait toujours des bêtises lors de ses premières clés
2. Si vous la perdez les mots de  passe cela ne sera pas préjudiciable. Elle s'arrêtera toute seule d'être reconnue comme valide.

Vous pourrez de toute façon modifier la date d'expiration si vous voulez conserver la clé

{% endnote %}

Les clés sont stockées dans le dossier de configuration, qui contient de nombreux fichiers/dossiers :

```sh

❯ ls -la
.rw-r-----@   12 fbrucker 19 Oct 18:40 󱁻 common.conf
drwx------@    - fbrucker 19 Oct 18:47  openpgp-revocs.d
drwx------@    - fbrucker 19 Oct 18:47  private-keys-v1.d
drwxr-x---@    - fbrucker 19 Oct 18:47  public-keys.d
srwx------@    - fbrucker 19 Oct 18:47  S.gpg-agent
srwx------@    - fbrucker 19 Oct 18:47  S.gpg-agent.browser
srwx------@    - fbrucker 19 Oct 18:47  S.gpg-agent.extra
srwx------@    - fbrucker 19 Oct 18:47  S.gpg-agent.ssh
srwx------@    - fbrucker 19 Oct 18:47  S.keyboxd
srwx------@    - fbrucker 19 Oct 18:58  S.scdaemon
.rw-------@ 1.3k fbrucker 19 Oct 18:53 󰦝 trustdb.gpg

```

En particulier un dossier `openpgp-revocs.d`{.fichier} qui contient un fichier de révocation de la clé :

```
❯ cat ./openpgp-revocs.d/1746B97A12A97C32CB74C6157D305414B27F8E59.rev
This is a revocation certificate for the OpenPGP key:

pub   ed25519 2025-10-19 [S] [expires: 2025-10-26]
      1746B97A12A97C32CB74C6157D305414B27F8E59
uid          François Brucker (Je suis professeur d'informatique) <francois.brucker@centrale-med.fr>

A revocation certificate is a kind of "kill switch" to publicly
declare that a key shall not anymore be used.  It is not possible
to retract such a revocation certificate once it has been published.

Use it to revoke this key in case of a compromise or loss of
the secret key.  However, if the secret key is still accessible,
it is better to generate a new revocation certificate and give
a reason for the revocation.  For details see the description of
of the gpg command "--generate-revocation" in the GnuPG manual.

To avoid an accidental use of this file, a colon has been inserted
before the 5 dashes below.  Remove this colon with a text editor
before importing and publishing this revocation certificate.

:-----BEGIN PGP PUBLIC KEY BLOCK-----
Comment: This is a revocation certificate

iHgEIBYKACAWIQQXRrl6Eql8Mst0xhV9MFQUsn+OWQUCaPUWLAIdAAAKCRB9MFQU
sn+OWXHkAP9t7qt97FO6kuSHrY8Hz+drPWmtHJjzFFK7SM9XMlSxuQEAmLMFLW/H
4Lxkgb/vpQC4VUINWaeZT0dkvz/GB1louwY=
=0z0V
-----END PGP PUBLIC KEY BLOCK-----
```

{% note "**Bon usage**" %}
Placez le fichier de révocation de votre clé dans un endroit séparé. Si vous vous faites voler votre clé, vous pourrez ainsi la révoquer et éviter que des inconnus se fassent passer pour vous.
{% endnote %}

### Lister ses clés

Vous pouvez voir vos clés :

```sh
❯ gpg --list-keys
gpg: checking the trustdb
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
gpg: next trustdb check due at 2025-10-26
[keyboxd]
---------
pub   ed25519 2025-10-19 [SC] [expires: 2025-10-26]
      1746B97A12A97C32CB74C6157D305414B27F8E59
uid           [ultimate] François Brucker <francois.brucker@centrale-med.fr>
sub   cv25519 2025-10-19 [E] [expires: 2025-10-26]

```

On voit deux clés de créées :

- la clé public principale servant à Signer et à Certifier (`[SC]`)
- une clé secondaire servant à chiffrer/déchiffrer (`[E]` pour _Encrypt_)

{% info %}
On verra plus tard l'utilisation des sous-clés. Pour l'instant, prenons ça comme une unique clé séparé en responsabilités : une pour le chiffrement, l'autre pour l'authentification.
{% endinfo %}

Vous pouvez aussi voir les clés privées en votre possession :

```sh

❯ gpg --list-secret-keys
[keyboxd]
---------
sec   ed25519 2025-10-19 [SC] [expires: 2025-10-26]
      1746B97A12A97C32CB74C6157D305414B27F8E59
uid           [ultimate] François Brucker <francois.brucker@centrale-med.fr>
ssb   cv25519 2025-10-19 [E] [expires: 2025-10-26]


```

Pour l'instant, ce sont les pendant privés de la clé principale et secondaire. Lorsque vous ajouterez des clés publiques pour communiquer ces deux listes vont différer.

### Exporter ses clés

Votre clé publique est :

```sh
❯ gpg --armor --export <key id>
```

Pour la clé crée juste avant :

```sh
❯ gpg --armor --export 1746B97A12A97C32CB74C6157D305414B27F8E59
-----BEGIN PGP PUBLIC KEY BLOCK-----

mDMEaPUWEhYJKwYBBAHaRw8BAQdANlrHTZ04G9fbWXz7E1iWSN2VBOBN9VLR16cP
6tGnD1u0VEZyYW7Dp29pcyBCcnVja2VyIChKZSBzdWlzIHByb2Zlc3NldXIgZCdp
bmZvcm1hdGlxdWUpIDxmcmFuY29pcy5icnVja2VyQHVuaXYtYW11LmZyPoiZBBMW
CgBBFiEEF0a5ehKpfDLLdMYVfTBUFLJ/jlkFAmj1FhICGwMFCQAJOoAFCwkIBwIC
IgIGFQoJCAsCBBYCAwECHgcCF4AACgkQfTBUFLJ/jlnpEQEA5kGQqmYZtsaYEl+j
+kHaLcXpFwPkexvT0xfz4DKmGYgA/3PgZ8lPTz9Vf8gu3tQkM/98xECbC6dL1hSZ
ofRYi1gJuDgEaPUWEhIKKwYBBAGXVQEFAQEHQJUylKHhjp4PRAHy5/dHAdjtZqax
3QmmcusEVDT4Hq9bAwEIB4h+BBgWCgAmFiEEF0a5ehKpfDLLdMYVfTBUFLJ/jlkF
Amj1FhICGwwFCQAJOoAACgkQfTBUFLJ/jlmQyQEAoZImWol4mEad+K5xRxLuFLF9
AAfCXxreu+uWC78Tn9ABAOuc1Zf2X/8aFe0K8/qcEro1s/IEJbKWlsmOvlriaY0A
=UCdl
-----END PGP PUBLIC KEY BLOCK-----

```

L'option `--armor` exporte la clé sous [la forme base64](https://fr.wikipedia.org/wiki/Base64) qui est affichable et facilement échangeable.

```shell
❯ gpg --export 1746B97A12A97C32CB74C6157D305414B27F8E59 | base64
mDMEaPUWEhYJKwYBBAHaRw8BAQdANlrHTZ04G9fbWXz7E1iWSN2VBOBN9VLR16cP6tGnD1u0NEZyYW7Dp29pcyBCcnVja2VyIDxmcmFuY29pcy5icnVja2VyQGNlbnRyYWxlLW1lZC5mcj6ImQQTFgoAQRYhBBdGuXoSqXwyy3TGFX0wVBSyf45ZBQJo9ScdAhsDBQkACTqABQsJCAcCAiICBhUKCQgLAgQWAgMBAh4HAheAAAoJEH0wVBSyf45Z3F8BAOrcosVh1tVRoONNkD3UzjyU6mXEkXXIJa9e6rjXMKaVAP48r4FOfIioLb+Yjo6YlgTRB0YMumk6xl3M4aqQxpEcBrg4BGj1FhISCisGAQQBl1UBBQEBB0CVMpSh4Y6eD0QB8uf3RwHY7Wamsd0JpnLrBFQ0+B6vWwMBCAeIfgQYFgoAJhYhBBdGuXoSqXwyy3TGFX0wVBSyf45ZBQJo9RYSAhsMBQkACTqAAAoJEH0wVBSyf45ZkMkBAKGSJlqJeJhGnfiucUcS7hSxfQAHwl8a3rvrlgu/E5/QAQDrnNWX9l//GhXtCvP6nBK6NbPyBCWylpbJjr5a4mmNAA==
```

Par défaut, le format est binaire :

```shell
❯ gpg --export 1746B97A12A97C32CB74C6157D305414B27F8E59 | xxd
00000000: 9833 0468 f516 1216 092b 0601 0401 da47  .3.h.....+.....G
00000010: 0f01 0107 4036 5ac7 4d9d 381b d7db 597c  ....@6Z.M.8...Y|
00000020: fb13 5896 48dd 9504 e04d f552 d1d7 a70f  ..X.H....M.R....
00000030: ead1 a70f 5bb4 3446 7261 6ec3 a76f 6973  ....[.4Fran..ois
00000040: 2042 7275 636b 6572 203c 6672 616e 636f   Brucker <franco
00000050: 6973 2e62 7275 636b 6572 4063 656e 7472  is.brucker@centr
00000060: 616c 652d 6d65 642e 6672 3e88 9904 1316  ale-med.fr>.....
00000070: 0a00 4116 2104 1746 b97a 12a9 7c32 cb74  ..A.!..F.z..|2.t
00000080: c615 7d30 5414 b27f 8e59 0502 68f5 271d  ..}0T....Y..h.'.
00000090: 021b 0305 0900 093a 8005 0b09 0807 0202  .......:........
000000a0: 2202 0615 0a09 080b 0204 1602 0301 021e  "...............
000000b0: 0702 1780 000a 0910 7d30 5414 b27f 8e59  ........}0T....Y
000000c0: dc5f 0100 eadc a2c5 61d6 d551 a0e3 4d90  ._......a..Q..M.
000000d0: 3dd4 ce3c 94ea 65c4 9175 c825 af5e eab8  =..<..e..u.%.^..
000000e0: d730 a695 00fe 3caf 814e 7c88 a82d bf98  .0....<..N|..-..
000000f0: 8e8e 9896 04d1 0746 0cba 693a c65d cce1  .......F..i:.]..
00000100: aa90 c691 1c06 b838 0468 f516 1212 0a2b  .......8.h.....+
00000110: 0601 0401 9755 0105 0101 0740 9532 94a1  .....U.....@.2..
00000120: e18e 9e0f 4401 f2e7 f747 01d8 ed66 a6b1  ....D....G...f..
00000130: dd09 a672 eb04 5434 f81e af5b 0301 0807  ...r..T4...[....
00000140: 887e 0418 160a 0026 1621 0417 46b9 7a12  .~.....&.!..F.z.
00000150: a97c 32cb 74c6 157d 3054 14b2 7f8e 5905  .|2.t..}0T....Y.
00000160: 0268 f516 1202 1b0c 0509 0009 3a80 000a  .h..........:...
00000170: 0910 7d30 5414 b27f 8e59 90c9 0100 a192  ..}0T....Y......
00000180: 265a 8978 9846 9df8 ae71 4712 ee14 b17d  &Z.x.F...qG....}
00000190: 0007 c25f 1ade bbeb 960b bf13 9fd0 0100  ..._............
000001a0: eb9c d597 f65f ff1a 15ed 0af3 fa9c 12ba  ....._..........
000001b0: 35b3 f204 25b2 9696 c98e be5a e269 8d00  5...%......Z.i..
```

Et si vous voulez la sauver dans un fichier `pub.gpg`{.fichier} :

```sh
gpg --armor --output pub.gpg --export <id clé>
```

### Importer des clés

Pour pouvoir envoyer des messages à quelqu'un, il vous faut avoir sa clé publique.

{% faire %}
Envoyez votre clé publique à votre correspondant soit sous la forme d'un fichier binaire, soit le texte avec l'option `--armor`, et récupérez la sienne.
{% endfaire %}

```sh
gpg --import public-key.pgp
```

Vous pouvez ensuite voir que la clé a bien été ajoutée à votre trousseau de clés :

```sh
gpg --list-keys        
```

{% details "exemple" %}

Par exemple :

```shell

❯ gpg --import francois.brucker_at_gmail.com.pub
gpg: key 4F81085218CD36A1: public key "François Brucker <francois.brucker@gmail.com>" imported
gpg: Total number processed: 1
gpg:               imported: 1
❯ gpg --list-keys
[keyboxd]
---------
pub   ed25519 2025-10-19 [SC] [expires: 2025-10-26]
      1746B97A12A97C32CB74C6157D305414B27F8E59
uid           [ultimate] François Brucker <francois.brucker@centrale-med.fr>
sub   cv25519 2025-10-19 [E] [expires: 2025-10-26]

pub   ed25519 2025-10-19 [SC] [expires: 2025-10-29]
      794258F0679471E0E09D24454F81085218CD36A1
uid           [ unknown] François Brucker <francois.brucker@gmail.com>
sub   cv25519 2025-10-19 [E] [expires: 2025-10-29]

```

{% enddetails %}

Vous pouvez, si vous le désirez, signer sa clé :

```sh
gpg> sign

```

{% details "exemple suite" %}

```shell
❯ gpg --edit-key 4F81085218CD36A1
gpg (GnuPG) 2.4.8; Copyright (C) 2025 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.


pub  ed25519/4F81085218CD36A1
     created: 2025-10-19  expires: 2025-10-29  usage: SC
     trust: unknown       validity: unknown
sub  cv25519/AF00F1C7150468B2
     created: 2025-10-19  expires: 2025-10-29  usage: E
[ unknown] (1). François Brucker <francois.brucker@gmail.com>

gpg> sign

pub  ed25519/4F81085218CD36A1
     created: 2025-10-19  expires: 2025-10-29  usage: SC
     trust: unknown       validity: unknown
 Primary key fingerprint: 7942 58F0 6794 71E0 E09D  2445 4F81 0852 18CD 36A1

     François Brucker <francois.brucker@gmail.com>

This key is due to expire on 2025-10-29.
Are you sure that you want to sign this key with your
key "François Brucker <francois.brucker@centrale-med.fr>" (7D305414B27F8E59)

Really sign? (y/N) y

gpg> save
```

{% enddetails %}

## Utilisation

{% lien %}
[comfy guide to gpg](https://www.youtube.com/watch?v=eLKOIjNFwVs)
{% endlien %}

### Chiffrement/déchiffrement

Chiffrement. `<recipient mail>` doit être le mail associé à la clé que vous avez ajouté. :

```sh
gpg --output msg.txt.gpg --encrypt --recipient <recipient mail> msg.txt
```

Chiffrement **et** signature du message :

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

{% faire %}
Envoyez un message chiffré à votre correspondant.
{% endfaire %}

### Signature

```sh
❯ echo "un message à signer" | gpg --clearsign
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

un message à signer
-----BEGIN PGP SIGNATURE-----

iHUEARYKAB0WIQQXRrl6Eql8Mst0xhV9MFQUsn+OWQUCaPUzPAAKCRB9MFQUsn+O
WW/aAQCM01hJ6NdFZGMQHSseYBymKsikdYXYu0w1hz3kHVq2mQEA2rD67KoILa/2
aO+GUXAvAcholh7pN4J3CjCmkOzTtQg=
=zw81
-----END PGP SIGNATURE-----
```

Les deux ensembles :

```sh
❯ echo "un message à signer" | gpg --clearsign
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

un message à signer
-----BEGIN PGP SIGNATURE-----

iHUEARYKAB0WIQQXRrl6Eql8Mst0xhV9MFQUsn+OWQUCaPUzPAAKCRB9MFQUsn+O
WW/aAQCM01hJ6NdFZGMQHSseYBymKsikdYXYu0w1hz3kHVq2mQEA2rD67KoILa/2
aO+GUXAvAcholh7pN4J3CjCmkOzTtQg=
=zw81
-----END PGP SIGNATURE-----
```

Juste la signature :

```shell
❯ echo "un message à signer" | gpg --detach-sign --armor
-----BEGIN PGP SIGNATURE-----

iHUEABYKAB0WIQQXRrl6Eql8Mst0xhV9MFQUsn+OWQUCaPUzvAAKCRB9MFQUsn+O
WTnTAP0UDntHHjJWL90aJIJdc5j5xEZJluc6lZKLxPMCFhE+IgEA6U4EKwjLDTrp
zlJYun0nDYelMc26nXClw+ZDn8LpjQg=
=mdY5
-----END PGP SIGNATURE-----

```

{% faire %}

1. Envoyez un message en clair avec votre signature à votre correspondant
2. envoyez un fichier pdf d'un de vos rapport avec un second fichier contenant le rapport signé de votre part

{% endfaire %}

### Vérification

```shell
❯ echo "un message à signer" | gpg --sign | gpg --verify
gpg: Signature made Sun Oct 19 20:55:32 2025 CEST
gpg:                using EDDSA key 1746B97A12A97C32CB74C6157D305414B27F8E59
gpg: Good signature from "François Brucker <francois.brucker@centrale-med.fr>" [ultimate]
```

{% faire %}
Vérifiez le message que vous a envoyé votre correspondant.
{% endfaire %}

## utilitaire

{% lien %}
[GPG TUI](https://github.com/orhun/gpg-tui)
{% endlien %}

## Gestion des clés

### Modifier sa clé

```sh
❯ gpg --edit-key <key id>
```

On entre dans un mode d'édition (utilisez la commande `help`). Par exemple pour changer d'utilisateur :

1. on ajoute un utilisateur (_uid_)
2. on sélectionne le précédent utilisateur (`uid 1`)
3. on le supprime
4. on sauve

```sh
❯ gpg --edit-key 1746B97A12A97C32CB74C6157D305414B27F8E59
gpg (GnuPG) 2.4.8; Copyright (C) 2025 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Secret key is available.

sec  ed25519/7D305414B27F8E59
     created: 2025-10-19  expires: 2025-10-26  usage: SC
     trust: ultimate      validity: ultimate
ssb  cv25519/8305F422F269AACB
     created: 2025-10-19  expires: 2025-10-26  usage: E
[ultimate] (1). François Brucker (Je suis professeur d'informatique) <francois.brucker@univ-amu.fr>

gpg> adduid
Real name: François Brucker
Email address: francois.brucker@centrale-med.fr
Comment:
You are using the 'utf-8' character set.
You selected this USER-ID:
    "François Brucker <francois.brucker@centrale-med.fr>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o

sec  ed25519/7D305414B27F8E59
     created: 2025-10-19  expires: 2025-10-26  usage: SC
     trust: ultimate      validity: ultimate
ssb  cv25519/8305F422F269AACB
     created: 2025-10-19  expires: 2025-10-26  usage: E
[ultimate] (1)  François Brucker (Je suis professeur d'informatique) <francois.brucker@univ-amu.fr>
[ unknown] (2). François Brucker <francois.brucker@centrale-med.fr>

gpg> uid 1

sec  ed25519/7D305414B27F8E59
     created: 2025-10-19  expires: 2025-10-26  usage: SC
     trust: ultimate      validity: ultimate
ssb  cv25519/8305F422F269AACB
     created: 2025-10-19  expires: 2025-10-26  usage: E
[ultimate] (1)* François Brucker (Je suis professeur d'informatique) <francois.brucker@univ-amu.fr>
[ unknown] (2). François Brucker <francois.brucker@centrale-med.fr>

gpg> deluid
Really remove this user ID? (y/N) y

sec  ed25519/7D305414B27F8E59
     created: 2025-10-19  expires: 2025-10-26  usage: SC
     trust: ultimate      validity: ultimate
ssb  cv25519/8305F422F269AACB
     created: 2025-10-19  expires: 2025-10-26  usage: E
[ unknown] (1). François Brucker <francois.brucker@centrale-med.fr>

gpg> save

```

{% attention %}
N'oubliez pas de sauver vos modifications !
{% endattention %}

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

### Gestion des clés GPG

{% lien %}

- [clés et sous clés GPG](https://wiki.debian.org/fr/Subkeys)
- [sous clés GPG](https://mikeross.xyz/create-gpg-key-pair-with-subkeys/)

{% endlien %}

> TBD : <https://rgoulter.com/blog/posts/programming/2022-06-10-a-visual-explanation-of-gpg-subkeys.html>

### Serveur de clés

{% lien %}

<https://keyserver.ubuntu.com/>

{% endlien %}

> TBD Permet d'utiliser des clés stockées dans un serveur de clé
> <https://www.gnupg.org/gph/en/manual.html#AEN464>
>
> 1. le faire.
> 2. se signer mutuellement les clés.
