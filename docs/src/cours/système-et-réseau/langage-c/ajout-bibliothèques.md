---
layout: layout/post.njk

title: Ajout de bibliothèques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Un programme `C` peut utiliser de nombreuses bibliothèques, dont la plupart ne sont pas intégrées par défaut lors de l'édition de lien.

## Installation de la bibliothèque

Pour pouvoir être inclues dans notre programme, il faut que la bibliothèque soit installée :

- sur notre système :
  - la bibliothèque elle même est installée dans `/usr/lib`{.fichier} si on peut utiliser cette bibliothèque de façon dynamique
  - les fichiers d'entêtes `.h`{.fichier} sont eux dans le dossier `/usr/include`{.fichier}
- dans un dossier connu si on veut l'inclure de façon statique dans notre code.

Nous allons utiliser la bibliothèque [openssl](https://www.openssl.org/) qui permet le cryptage/décryptage de données. Cette bibliothèque est souvent installée par défaut sur un système car elle est utilisée par de nombreux programmes, mais il manque souvent les fichiers de headers qui ne sont utiles que si on peut programmer avec. C'est pourquoi il y a deux paquets à installer :

- `sudo apt install libssl` qui installe la bibliothèque openssl (devrait déjà être sur votre système).
- `sudo apt install libssl-dev` qui installe les fichiers `.h`{.language-}

{% info %}
Si vous êtes sous mac, tout est installé avec la commande `brew install openssl`.
{% endinfo %}

## Code

Nous allons utiliser les fonctions [EVP](https://www.openssl.org/docs/man3.1/man7/evp.html) pour encoder et décoder une chaîne de caractères au format [base64](https://fr.wikipedia.org/wiki/Base64)

Fichier `base64.c`{.fichier} :

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/evp.h>

int main() {

  char *entree = "longtemps je me suis couché de bonne heure.";

  // 3 bytes sont encodées en 4 bytes et un `\0` est ajouté à la fin
  size_t taille = 4 * (strlen((const char *)entree) / 3 + 1) + 1;

  unsigned char *code = malloc(taille);

  int code_sortie = 0;
  code_sortie = EVP_EncodeBlock(code, (unsigned char *)entree, strlen((const char *)entree));
  if (code_sortie < 0) {
      perror("Erreur d'encodage");
      return EXIT_FAILURE;
  }

  unsigned char *decode = malloc(taille);

  code_sortie = EVP_DecodeBlock(decode, code, strlen((const char *)code));
  if (code_sortie < 0) {
      perror("Erreur de décodage");
      return EXIT_FAILURE;
  }

  printf("'%s'\n", entree);
  printf("'%s'\n", code);
  printf("'%s'\n", decode);

  return EXIT_SUCCESS;
}

```

## Compilateur

Plusieurs options de `clang` contrôlent l'inclusion de celles-ci :

- [`-I`](https://clang.llvm.org/docs/ClangCommandLineReference.html#cmdoption-clang-I-dir) chemin vers les fichiers d'entêtes
- [`-L`](https://clang.llvm.org/docs/ClangCommandLineReference.html#cmdoption-clang-L-dir) chemin vers la bibliothèque à inclure
- [`-l`](https://clang.llvm.org/docs/ClangCommandLineReference.html#cmdoption-clang-l-arg) nom de la bibliothèque à inclure

Sous Linux/Ubuntu où les headers et les bibliothèques sont toutes installées dans le même dossier système, il suffit de renseigner la bibliothèque où sont définies les fonctions utilisées, ici c'est crypto :

```
 clang base64.c -lcrypto

 ```

La bibliothèque ajoutée est la bibliothèque cryto qui est contenu dans le fichier `libcrypto.so` (dans le dossier système `/usr/lib/aarch64-linux-gnu/` chez moi) On ne donne pas le fichier en entier, on ne donne que son nom (un fichier de  bibliothèque dynamique s'écrira toujours `libnom.so`{.fichier}).

Le fichier d'entête est dans le dossier système des entêtes : `/usr/include/`{.fichier}.

{% info %}
Sous mac, si vous avez installé la bibliothèque avec brew et avec un mac arm, la ligne de commande sera plus importante car il faudra renseigner tous les champs :

```
clang base64.c -I/opt/homebrew/include/ -L/opt/homebrew/lib -lcrypto
```

- `-I` pour trouver le fichier `/opt/homebrew/include/openssl/evp.h`{.fichier}
- `-L` pour trouver la bibliothèque `/opt/homebrew/lib/libcrypto.dylib`{.fichier}

{% endinfo %}

Il se peut que les bibliothèques ajoutée ne soient pas trouvées par le système à l'exécution. Ceci arrive lorsqu'elles ne sont pas dans des endroits système reconnu. VOus pouvez ajouter des dossiers de recherche vec la variable d'environnement [`LD_LIBRARY_PATH`](https://linuxhint.com/what-is-ld-library-path/).

## Makefile

Si vous compilez vos programme via la commande `make`, on a coutume de placer les options `-L` et `-l` dans une variable nommée `LDFLAGS` et utilisée uniquement lors de règle faisant l'édition de lien.

N'oubliez pas également d'ajouter l'option `-I` si nécessaire dans la variable `CFLAGS`.

## Bibliothèque statique

Si vous préférez lier une bibliothèque spécifique de façon statique à votre projet, il faut ruser. En effet :

- si vous utiliser l'option `-static` le compilateur va rendre statique toutes les bibliothèques dont la `libc` ce qui est inutile.
- le compilateur va préférer la version dynamique à la version statique s'il trouve les deux dans le même dossier.

Faite un lien de votre bibliothèque statique dans un dossier temporaire et ajouter ce dossier à l'option `-L` lors de l'édition de lien. Le compilateur ne devrait voir que la bibliothèque statique (et non sa version dynamique qui est dans un autre dossier) et l'inclure dans votre dossier.
